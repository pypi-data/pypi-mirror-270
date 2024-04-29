import contextlib

from mindspore.communication.management import init, create_group, GlobalComm, destroy_group
from mindspore.communication._comm_helper import (_is_available, _is_initialized, _is_hccl_available,
                                                  _is_nccl_available, _is_mpi_available, _get_group_ranks)

import mindspore as ms
from mindspore.ops._primitive_cache import _get_cache_prim

from mindtorch.torch.common.dtype import int8, int32, float16, float32, bfloat16, all_complex_type
from mindtorch.utils import unsupported_attr, graph_mode_condition, is_under_ascend_context, \
    is_under_gpu_context
from mindtorch.torch.logging import warning
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor, Tensor
from mindtorch.torch.distributed._distributed_c10d import ( # pylint: disable=W0611
    AllreduceCoalescedOptions,
    AllreduceOptions,
    AllToAllOptions,
    # _DistributedBackendOptions,
    BarrierOptions,
    BroadcastOptions,
    GatherOptions,
    # PrefixStore,
    ProcessGroup,
    ReduceOp,
    ReduceOptions,
    ReduceScatterOptions,
    ScatterOptions,
    # Store,
    # DebugLevel,
    # get_debug_level,
    Work,
    _get_str_from_reduceop,
    _pg_map,
    _pg_names,
    _group_count
)

_ascend_support_dtype = (int8, int32, float16, float32, bfloat16)

_ascend_dtype_convert_map = {
    'bool': int8,
    'int64': int32,
    'float64': float32,
}

# should use after cast_to_ms_tensor
def _check_and_convert_dtype_on_ascend(input_ms):
    def _convert(tensor):
        _origin_dtype = tensor.dtype
        if _origin_dtype in all_complex_type:
            raise TypeError("Not support communication of complex tensor yet.")
        if _origin_dtype not in _ascend_support_dtype:
            tensor = tensor.astype(
                _ascend_dtype_convert_map[str(_origin_dtype).split('.')[-1]]
            )
        else:
            _origin_dtype = None
        return tensor, _origin_dtype

    if isinstance(input_ms, Tensor):
        return _convert(input_ms)
    elif isinstance(input_ms, tuple):
        input_ms = list(input_ms)
    elif not isinstance(input_ms, list):
        raise TypeError("input_ms must be type of Tensor, tuple or list")

    _origin_dtype_list = []
    for i, tensor in enumerate(input_ms):
        converted_tensor, origin_dtype = _convert(tensor)
        input_ms[i] = converted_tensor
        _origin_dtype_list.append(origin_dtype)

    return input_ms, _origin_dtype_list

# should use before cast_to_adapter_tensor
def _recorver_dtype_on_ascend(output_ms, _origin_dtype):
    def _recover(tensor, origin_dtype):
        if origin_dtype is not None:
            tensor = tensor.astype(origin_dtype)
        return tensor

    if isinstance(output_ms, Tensor):
        return _recover(output_ms, _origin_dtype)
    elif isinstance(output_ms, tuple):
        output_ms = list(output_ms)
    elif not isinstance(output_ms, list):
        raise TypeError(f"output_ms must be type of Tensor, tuple or list, but got {type(output_ms)}.")

    if not isinstance(_origin_dtype, list):
        raise TypeError(f"_origin_dtype must be type of list, but got {type(_origin_dtype)}.")
    if len(output_ms) != len(_origin_dtype):
        raise ValueError("length of output_ms not equal to _origin_dtype")

    for i, (output, dtype) in enumerate(zip(output_ms, _origin_dtype)):
        if dtype is not None:
            output_ms[i] = _recover(output, dtype)

    return output_ms


BACKEND_DEVICE_TARGET_DICT = {
    'mccl': 'CPU',
    'nccl': 'GPU',
    'hccl': 'Ascend',
}

DEVICE_TARGET_BACKEND_DICT = {
    'CPU': 'mccl',
    'GPU': 'nccl',
    'Ascend': 'hccl',
}

def _make_nccl_premul_sum(factor):
    raise NotImplementedError('distributed._make_nccl_premul_sum not support yet.'
                              'Please manually scale the tensor before reduce.')

_stub_work = Work()

class Backend:
    UNDEFINED = "undefined"
    HCCL = "hccl"
    NCCL = "nccl"
    MCCL = "mccl"

    backend_list = [UNDEFINED, HCCL, NCCL, MCCL]

    @staticmethod
    def __new__(cls, name):
        """Create instance object of Backend."""
        if not isinstance(name, str):
            raise TypeError("For 'Backend', the class variable 'name' must be a string, "
                            "but got the type : {}".format(type(name)))
        value = getattr(Backend, name.upper(), Backend.UNDEFINED)
        if value not in (Backend.HCCL, Backend.NCCL, Backend.MCCL):
            value = name.lower()
        return value

    @classmethod
    def register_backend(cls, name, func, extended_api=False):
        raise NotImplementedError("For distributed.Backend, register_backend has not been supported yet. "
                                  "For now, only 'hccl', 'nccl', 'mccl' are supported.")

_backend = Backend.UNDEFINED
dist_backend = Backend

# jit_class for _World to support graph mode
@ms.jit_class
class _World:
    def __init__(self):
        self._default_pg = None

    @property
    def default_pg(self):
        return self._default_pg

    @default_pg.setter
    def default_pg(self, value):
        self._default_pg = value

    @property
    def pg_map(self):
        return _pg_map

    @property
    def pg_names(self):
        return _pg_names

    @property
    def group_count(self):
        return _group_count

    @group_count.setter
    def group_count(self, value):
        global _group_count
        _group_count = value


_world = _World()

class _WorldMeta(type):
    @property
    def WORLD(cls):
        return _world.default_pg

    @WORLD.setter
    def WORLD(cls, pg):
        _world.default_pg = pg


class group(metaclass=_WorldMeta):
    pass

class GroupMember(metaclass=_WorldMeta):
    NON_GROUP_MEMBER = "non_group_member"

NON_GROUP_MEMBER = "non_group_member"

def _get_default_group():
    if not is_initialized():
        raise RuntimeError(
            "Default process group has not been initialized, "
            "please make sure to call init_process_group."
        )
    return _world.default_pg

def _update_default_pg(pg):
    _world.default_pg = pg

def _rank_not_in_group(group):
    if group is None:
        return False
    return group == NON_GROUP_MEMBER

def _warn_not_in_group(op_name):
    global_rank = -1 if group.WORLD is None else get_rank()
    warning(
        f"Running {op_name} on global rank {global_rank} which does not "
        "belong to the given group."
    )

def get_backend(group=None):
    if _rank_not_in_group(group):
        raise RuntimeError("Invalid process group specified")
    if group is None:
        pg = _get_default_group()
    else:
        pg = group
    pg_store = _world.pg_map.get(pg, None)
    return pg_store[0]

def _check_single_tensor(param, param_name):
    if not isinstance(param, Tensor):
        raise RuntimeError(
            "Invalid function argument. Expected parameter `{}` "
            "to be of type Tensor.".format(param_name)
        )


def _check_tensor_list(param, param_name):
    if not isinstance(param, list) or not all(
        isinstance(p, Tensor) for p in param
    ):
        raise RuntimeError(
            "Invalid function argument. Expected parameter `{}` "
            "to be of type List[Tensor].".format(param_name)
        )

def _validate_output_list_for_rank(my_rank, dst, gather_list):
    if dst == my_rank:
        if not gather_list:
            raise ValueError(
                "Argument ``gather_list`` must be specified on destination rank."
            )
    elif gather_list:
        raise ValueError(
            "Argument ``gather_list`` must NOT be specified "
            "on non-destination ranks."
        )

def init_process_group(
        backend=None,
        init_method=None,
        timeout=None,
        world_size=-1,
        rank=-1,
        store=None,
        group_name="",
        pg_options=None,
):
    if group_name != "":
        raise NotImplementedError("distributed.init_process_group: `group_name` not support yet.")

    if init_method not in ("env://", None):
        raise NotImplementedError("distributed.init_process_group: `init_method` not support yet.")

    if store is not None:
        raise NotImplementedError("distributed.init_process_group: `store` not support yet.")

    if timeout is not None:
        warning("distributed.init_process_group: `timeout` not support yet.")

    if pg_options is not None:
        raise NotImplementedError("distributed.init_process_group: `pg_options` not support yet.")

    global _world

    if _world.default_pg is not None:
        raise RuntimeError("trying to initialize the default process group " "twice!")

    #TODO: To support `backend` other than in BACKEND_DEVICE_TARGET_DICT/None/UNDEFINED
    if backend is None:
        backend = Backend('undefined')
        init()
    else:
        backend = Backend(backend)
        # Help user automatically shift between Ascend and GPU backend without changing user code.
        if backend == 'nccl' and is_under_ascend_context():
            backend = 'hccl'
        elif backend == 'hccl' and is_under_gpu_context():
            backend = 'nccl'
        init(backend)

    name = GlobalComm.WORLD_COMM_GROUP
    # ProcessGroup not support graph mode
    pg = ProcessGroup(name=name)
    _world.pg_map[pg] = (backend,)
    _world.pg_names[pg] = name  # not support group_name now.
    _world.group_count += 1
    _update_default_pg(pg)

    _real_world_size = get_world_size()
    if world_size not in (-1, _real_world_size):
        raise ValueError('The world_size:{} is not equal to the actual world_size:{}.'
                         .format(world_size, _real_world_size))

    _real_rank = get_rank()
    if rank not in (-1, _real_rank):
        raise ValueError('The rank:{} is not equal to the actual rank:{}.'.format(rank, _real_rank))

def _get_group_name():
    global _world
    name = 'group_{}'.format(_world.group_count)
    # Regardless of whether 'name' is used later in the code,
    # add `group_count` to maintain group_name consistency across different processes.
    _world.group_count += 1
    return name

def new_group(ranks=None,
              timeout=None,
              backend=None,
              pg_options=None):
    unsupported_attr(backend)
    global _world

    if timeout is not None:
        warning("distributed.new_group: `timeout` is not supported yet.")

    if pg_options is not None:
        raise NotImplementedError("distributed.new_group: `pg_options` is not supported.")

    global_world_size = get_world_size()

    if ranks is not None:
        ranks = sorted(ranks)
        group_world_size = len(ranks)
        if group_world_size > global_world_size:
            raise RuntimeError(
                "the new group's world size should be less or "
                "equal to the world size set by "
                "init_process_group"
            )
        for rank in ranks:
            if rank < 0 or rank >= global_world_size:
                raise RuntimeError(
                    "The new group's rank should be within the "
                    "the world_size set by init_process_group"
                )
    else:
        ranks = list(range(global_world_size))

    rank = get_rank()
    name = _get_group_name()

    if rank not in ranks:
        # if this process not in `ranks`, means it do not need create_group.
        pg = NON_GROUP_MEMBER
    else:
        pg = ProcessGroup(name=name)
        create_group(name, ranks)

    # TODO: after support `backend` arg, use 'backend' rather than 'get_backend()'.
    backend = get_backend()
    _world.pg_names[pg] = name
    _world.pg_map[pg] = (backend,)

    return pg

def get_rank(group=None):
    if _rank_not_in_group(group):
        return -1
    if group is None:
        group = _get_default_group()
    group_name = _get_pg_name(group)
    return ms.communication.get_rank(group_name)

def get_world_size(group=None):
    if _rank_not_in_group(group):
        return -1
    return _get_group_size(group)

def _get_group_size(group):
    _group_name = None
    if group is None:
        group = _get_default_group()
    _group_name = _get_pg_name(group)
    return ms.communication.get_group_size(_group_name)

def destroy_process_group(group=None):
    global _world

    if group == NON_GROUP_MEMBER:
        return

    if group is None:
        pg = GroupMember.WORLD
    else:
        pg = group

    if group is None or group == GroupMember.WORLD: # pylint: disable=W0143
        del_pg_list = list()
        for pg in _world.pg_map:
            if pg == NON_GROUP_MEMBER:
                del_pg_list.append(pg)
                continue
            name = _get_pg_name(group)
            if name != GlobalComm.WORLD_COMM_GROUP:
                destroy_group(name)
                del_pg_list.append(pg)
        for pg in del_pg_list:
            del _world.pg_map[pg]
            del _world.pg_names[pg]
        _world.group_count = 1
    else:
        if group in _world.pg_map:
            name = _get_pg_name(group)
            if name != GlobalComm.WORLD_COMM_GROUP:
                destroy_group(name)
                del _world.pg_map[group]
                del _world.pg_names[group]
                # should not use the code below. To guarantee always create a unique new group.
                # because some process's rank may not in the group's ranks,
                # and this process did not create pg in _world.pg_map, and will not enter this branch.
                # _world.group_count -= 1

def _get_pg_name(group=None):
    if group is None:
        return GlobalComm.WORLD_COMM_GROUP
    if isinstance(group, ProcessGroup):
        if group in _world.pg_map:
            return _world.pg_names[group]
        raise ValueError(f"Group {group} is not existed.")
    raise TypeError('The dtype of `group` must be `ProcessGroup`, but got {}'.format(type(group)))

def is_available():
    return _is_available()

def is_initialized():
    return _is_initialized()

def is_mpi_available():
    return _is_mpi_available()

def is_nccl_available():
    device_target = ms.get_context('device_target')
    if device_target == 'Ascend':
        warning("On Ascend, the result of is_hccl_available() is returned. " \
                "If you do not want to see this log, please use that API.")
        return _is_hccl_available()
    return _is_nccl_available()

def is_hccl_available():
    return _is_hccl_available()

def is_gloo_available():
    return False

def get_process_group_ranks(group):
    if _rank_not_in_group(group):
        _warn_not_in_group("get_process_group_ranks")
        return []
    _group_name = _get_pg_name(group)
    return _get_group_ranks(_group_name)

def get_group_rank(group, global_rank):
    if group is _world._default_pg:
        return global_rank

    # TODO: mindspore not support get group rank when the process not in group
    if _rank_not_in_group(group):
        _warn_not_in_group("get_group_rank")
        return None

    _group_name = _get_pg_name(group)
    return ms.communication.get_group_rank_from_world_rank(global_rank, _group_name)

def get_global_rank(group, group_rank):
    if group is _world._default_pg:
        return group_rank

    # TODO: mindspore not support get group rank when the process not in group
    if _rank_not_in_group(group):
        _warn_not_in_group("get_global_rank")
        return None

    _group_name = _get_pg_name(group)
    return ms.communication.get_world_rank_from_group_rank(_group_name, group_rank)

def all_reduce_not_inplace(tensor, op=ReduceOp.SUM, group=None, async_op=False):
    if async_op:
        warning("all_reduce: 'async_op' not actually supported now. Run as sync op")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("all_reduce")
        return None
    if group is None:
        group = _get_default_group()

    op = _get_str_from_reduceop(op)

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _reduce_op = _get_cache_prim(ms.ops.AllReduce)(op)
    else:
        _reduce_op = _get_cache_prim(ms.ops.AllReduce)(op, _group_name)
    result = _reduce_op(tensor)
    return cast_to_adapter_tensor(result)

def all_reduce(tensor, op=ReduceOp.SUM, group=None, async_op=False):
    if async_op:
        warning("all_reduce: 'async_op' not actually supported now. Run as sync op")
    _inplace_raise_error_graph_mode('all_reduce', 'all_reduce_not_inplace')

    _check_single_tensor(tensor, "tensor")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("all_reduce")
        return None
    if group is None:
        group = _get_default_group()

    op = _get_str_from_reduceop(op)

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _reduce_op = _get_cache_prim(ms.ops.AllReduce)(op)
    else:
        _reduce_op = _get_cache_prim(ms.ops.AllReduce)(op, _group_name)
    if get_backend(group) == "hccl":
        cast_tensor, _origin_dtype = _check_and_convert_dtype_on_ascend(tensor)
        result = _reduce_op(cast_tensor)
        result = _recorver_dtype_on_ascend(result, _origin_dtype)
    else:
        result = _reduce_op(tensor)
    tensor.data = result
    if async_op:
        return _stub_work
    else:
        return None

def broadcast(tensor, src, group=None, async_op=False):
    if async_op:
        warning("broadcast: 'async_op' not actually supported now. Run as sync op")

    _inplace_raise_error_graph_mode('broadcast', 'broadcast_not_inplace')

    _check_single_tensor(tensor, "tensor")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("broadcast")
        return None

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _bc_op = _get_cache_prim(ms.ops.Broadcast)(src)
    else:
        src = get_group_rank(group, src)
        _bc_op = _get_cache_prim(ms.ops.Broadcast)(src, _group_name)
    if get_backend(group) == "hccl":
        cast_tensor, _origin_dtype = _check_and_convert_dtype_on_ascend(tensor)
        result = _bc_op((cast_tensor,))[0]
        result = _recorver_dtype_on_ascend(result, _origin_dtype)
    else:
        result = _bc_op((tensor,))[0]
    tensor.data = result
    if async_op:
        return _stub_work
    else:
        return None

def all_gather_into_tensor_not_inplace(input_tensor, group=None, async_op=False):
    if async_op:
        warning("all_gather_into_tensor: 'async_op' not actually supported now. Run as sync op")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("broadcast")
        return None

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _ag_op = _get_cache_prim(ms.ops.AllGather)()
    else:
        _ag_op = _get_cache_prim(ms.ops.AllGather)(_group_name)
    return cast_to_adapter_tensor(_ag_op(input_tensor))

def all_gather_into_tensor(output_tensor, input_tensor, group=None, async_op=False):
    _inplace_raise_error_graph_mode('all_gather_into_tensor', 'all_gather_into_tensor_not_inplace')

    if async_op:
        warning("all_gather_into_tensor: 'async_op' not actually supported now. Run as sync op")

    _check_single_tensor(input_tensor, "input_tensor")
    _check_single_tensor(output_tensor, "output_tensor")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("broadcast")
        return None

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _ag_op = _get_cache_prim(ms.ops.AllGather)()
    else:
        _ag_op = _get_cache_prim(ms.ops.AllGather)(_group_name)

    result =_ag_op(input_tensor)

    _out_tensor_prim_size = output_tensor.shape[0]
    _result_prim_size = result.shape[0]
    # for stack mode of all_gather_into_tensor
    if _out_tensor_prim_size != _result_prim_size:
        if _result_prim_size % _out_tensor_prim_size != 0:
            raise ValueError("distributed.all_gather_into_tensor: if want to use stack mode, "
                             "the primary dimension size of `output_tensor` should match the gather result,"
                             f"but got output_tensor: {_out_tensor_prim_size} and gather result: {_result_prim_size}.")
        split_size = _result_prim_size // _out_tensor_prim_size
        result = ms.ops.split(result, split_size)
        result = ms.ops.stack(result)
    output_tensor.data = result
    if async_op:
        return _stub_work
    else:
        return None

def _all_gather_base(output_tensor, input_tensor, group=None, async_op=False):
    return all_gather_into_tensor(output_tensor, input_tensor, group, async_op)

def all_gather_not_inplace(tensor, group=None, async_op=False):
    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("all_gather")
        return None
    result = all_gather_into_tensor_not_inplace(tensor, group, async_op)
    group_size = _get_group_size(group)
    _split_op = _get_cache_prim(ms.ops.Split)(0, group_size)
    return cast_to_adapter_tensor(_split_op(result))

def all_gather(tensor_list, tensor, group=None, async_op=False):
    _check_tensor_list(tensor_list, "tensor_list")
    _check_single_tensor(tensor, "tensor")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("all_gather")
        return None
    result = all_gather_not_inplace(tensor, group, async_op)
    for i, _tensor in enumerate(tensor_list):
        _tensor.data = result[i]
    if async_op:
        return _stub_work
    else:
        return None

def barrier(group=None, async_op=False, device_ids=None):
    if async_op:
        warning("barrier: 'async_op' not actually supported now. Run as sync op")

    if device_ids:
        raise NotImplementedError("distributed.barrier not support device_ids yet.")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("barrier")
        return None

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _barrier_op = _get_cache_prim(ms.ops.operations._inner_ops.Barrier)()
    else:
        _barrier_op = _get_cache_prim(ms.ops.operations._inner_ops.Barrier)(_group_name)
    _barrier_op()
    if async_op:
        return _stub_work
    else:
        return None

def all_to_all(output_tensor_list, input_tensor_list, group=None, async_op=False):
    if async_op:
        warning("all_to_all: 'async_op' not actually supported now. Run as sync op")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("all_to_all_single")
        return None

    if group is None:
        group = _get_default_group()

    _split_dim = 0
    _concat_dim = 0
    _split_count = len(input_tensor_list)

    input_tensor_list = cast_to_ms_tensor(input_tensor_list)
    _input_tensor = ms.ops.stack(input_tensor_list)

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _op = _get_cache_prim(ms.ops.AlltoAll)(_split_count, _split_dim, _concat_dim)
    else:
        _op = _get_cache_prim(ms.ops.AlltoAll)(_split_count, _split_dim, _concat_dim, _group_name)

    out = _op(_input_tensor)
    _spilit_size = out.shape[0] // _split_count
    out = ms.ops.split(out, _spilit_size)
    for i, output in enumerate(output_tensor_list):
        output.data = out[i]
    if async_op:
        return _stub_work
    else:
        return None

def all_to_all_single(
    output,
    input,
    output_split_sizes=None,
    input_split_sizes=None,
    group=None,
    async_op=False,
):
    if async_op:
        warning("all_to_all_single: 'async_op' not actually supported now. Run as sync op")

    if output_split_sizes is not None or input_split_sizes is not None:
        raise NotImplementedError("all_to_all_single not support output_split_sizes and input_split_sizes now.")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("all_to_all_single")
        return None

    _split_count = input.shape[0]
    _split_dim = 0
    _concat_dim = 0

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _op = _get_cache_prim(ms.ops.AlltoAll)(_split_count, _split_dim, _concat_dim)
    else:
        _op = _get_cache_prim(ms.ops.AlltoAll)(_split_count, _split_dim, _concat_dim, _group_name)

    input_ms = cast_to_ms_tensor(input)
    out = _op(input_ms)
    output.data = out
    if async_op:
        return _stub_work
    else:
        return None

def reduce(tensor, dst, op=ReduceOp.SUM, group=None, async_op=False):
    if async_op:
        warning("reduce: 'async_op' not actually supported now. Run as sync op")

    _check_single_tensor(tensor, "tensor")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("reduce")
        return None

    if group is None:
        group = _get_default_group()

    op = _get_str_from_reduceop(op)

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _reduce_op = _get_cache_prim(ms.ops.operations._inner_ops.Reduce)(dst, op)
    else:
        # translate to world rank to group rank.
        group_dst_rank = get_group_rank(group, dst)
        _reduce_op = _get_cache_prim(ms.ops.operations._inner_ops.Reduce)(group_dst_rank, op, _group_name)

    out = _reduce_op(tensor)
    if dst == get_rank():
        tensor.data = out
    if async_op:
        return _stub_work
    else:
        return None

def send(tensor, dst, group=None, tag=0):
    if get_rank() == dst:
        raise ValueError(
            "Invalid destination rank: destination rank should not be the same as "
            "the rank of the current process."
        )

    _check_single_tensor(tensor, "tensor")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("send")
        return None

    if group is None:
        group = _get_default_group()

    # `dst` is global rank, but mindspore only accept local_rank
    dst = get_group_rank(group, dst)
    # TODO: ms.ops.operations._inner_ops.Send(group='hccl_world_group'), default is under Ascend.
    # So have to pass '_group_name' as arg to support both GPU and Ascend.
    _group_name = _get_pg_name(group)
    _send_op = _get_cache_prim(ms.ops.operations._inner_ops.Send)(tag, dst, _group_name, _group_name)
    out = _send_op(tensor)

    # Additionly return 'out' to ensure bprop is correctly running.
    return out

def recv(tensor, src=None, group=None, tag=0):
    _inplace_raise_error_graph_mode('recv', 'recv_not_inplace')
    _check_single_tensor(tensor, "tensor")

    if src is None:
        raise NotImplementedError("distributed.recv not support `src` is None yet, "
                                  "can only receive message from a certain process.")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("send")
        return -1

    if group is None:
        group = _get_default_group()

    # `src` is global rank, but mindspore only accept local_rank
    src = get_group_rank(group, src)
    # TODO: ms.ops.operations._inner_ops.Receive(group='hccl_world_group'), default is under Ascend.
    # So have to pass '_group_name' as arg to support both GPU and Ascend.
    _group_name = _get_pg_name(group)
    _recv_op = _get_cache_prim(ms.ops.operations._inner_ops.Receive)(tag,
                                                                     src,
                                                                     list(tensor.shape),
                                                                     tensor.dtype,
                                                                     _group_name,
                                                                     _group_name)
    # Additionly pass 'tensor' to _recv_op to ensure bprop is correctly running.
    out = _recv_op(tensor)
    tensor.data = out
    return src

def reduce_scatter(output, input_list, op=ReduceOp.SUM, group=None, async_op=False):
    if async_op:
        warning("reduce_scatter: 'async_op' not actually supported now. Run as sync op")

    _check_single_tensor(output, "output")
    _check_tensor_list(input_list, "input_list")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("reduce_scatter")
        return None

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _op = _get_cache_prim(ms.ops.ReduceScatter)(op)
    else:
        _op = _get_cache_prim(ms.ops.ReduceScatter)(op, _group_name)

    input_list = cast_to_ms_tensor(input_list)
    input_ms = ms.ops.concat(input_list)
    out = _op(input_ms)
    output.data = out
    if async_op:
        return _stub_work
    else:
        return None

def reduce_scatter_tensor(output, input, op=ReduceOp.SUM, group=None, async_op=False):
    if async_op:
        warning("reduce_scatter_tensor: 'async_op' not actually supported now. Run as sync op")

    _check_single_tensor(output, "output")
    _check_single_tensor(input, "input")

    if _rank_not_in_group(group):
        # Graph mode not support code below.
        # _warn_not_in_group("reduce_scatter_tensor")
        return None

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _op = _get_cache_prim(ms.ops.ReduceScatter)(op)
    else:
        _op = _get_cache_prim(ms.ops.ReduceScatter)(op, _group_name)

    input_ms = cast_to_ms_tensor(input)
    out = _op(input_ms)
    output.data = out
    if async_op:
        return _stub_work
    else:
        return None

def _reduce_scatter_base(output, input, op=ReduceOp.SUM, group=None, async_op=False):
    return reduce_scatter_tensor(output, input, op, group, async_op)

def gather(tensor, gather_list=None, dst=0, group=None, async_op=False):
    if async_op:
        warning("gather: 'async_op' not actually supported now. Run as sync op")

    _check_single_tensor(tensor, "tensor")

    if gather_list:
        _check_tensor_list(gather_list, "gather_list")
    else:
        gather_list = []

    if _rank_not_in_group(group):
        # _warn_not_in_group("gather")
        return None

    my_rank = get_rank()
    _validate_output_list_for_rank(my_rank, dst, gather_list)

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _op = _get_cache_prim(ms.ops.operations._inner_ops.CollectiveGather)(dst)
    else:
        group_dst_rank = get_group_rank(group, dst)
        _op = _get_cache_prim(ms.ops.operations._inner_ops.CollectiveGather)(group_dst_rank, _group_name)
    out = _op(tensor)

    if dst == my_rank:
        _split_count = len(gather_list)
        _spilit_size = out.shape[0] // _split_count
        out = ms.ops.split(out, _spilit_size)
        for i, output in enumerate(gather_list):
            output.data = out[i]
    if async_op:
        return _stub_work
    else:
        return None

def scatter(tensor, scatter_list=None, src=0, group=None, async_op=False):
    if async_op:
        warning("scatter: 'async_op' not actually supported now. Run as sync op")

    _check_single_tensor(tensor, "tensor")

    # Parameter ``scatter_list`` may be left unspecified on non-src ranks.
    if scatter_list:
        _check_tensor_list(scatter_list, "scatter_list")
    else:
        scatter_list = []

    if _rank_not_in_group(group):
        # _warn_not_in_group("scatter")
        return None

    if group is None:
        group = _get_default_group()

    _group_name = _get_pg_name(group)
    if _group_name == GlobalComm.WORLD_COMM_GROUP:
        _op = _get_cache_prim(ms.ops.operations._inner_ops.CollectiveScatter)(src)
    else:
        group_src_rank = get_group_rank(group, src)
        _op = _get_cache_prim(ms.ops.operations._inner_ops.CollectiveScatter)(group_src_rank, _group_name)

    my_rank = get_rank()
    if my_rank == src:
        if not scatter_list:
            raise ValueError(
                "Argument ``scatter_list`` must be specified " "on source rank."
            )
        input_list = cast_to_ms_tensor(scatter_list)
        input_ms = ms.ops.stack(input_list)
        out = _op(input_ms)[0]
    else:
        if scatter_list:
            raise ValueError(
                "Argument ``scatter_list`` must NOT be specified "
                "on non-source ranks."
            )
        group_size = _get_group_size(group)
        input_ms = ms.ops.zeros((group_size,) + tensor.shape, dtype=tensor.dtype)
        out = _op(input_ms)[0]
    tensor.data = out
    if async_op:
        return _stub_work
    else:
        return None

@contextlib.contextmanager
def _coalescing_manager(group, device, reqs):
    unsupported_attr(group)
    unsupported_attr(device)
    unsupported_attr(reqs)
    try:
        yield
    finally:
        pass

def _inplace_raise_error_graph_mode(inplace_op, not_inplace_op):
    if graph_mode_condition():
        raise ValueError(f"distributed.{inplace_op} is a inplace op and it is not supported to be used under "
                         "MindSpore static graph mode. please use "
                         f"x = distributed.{not_inplace_op}(x) instead.")
