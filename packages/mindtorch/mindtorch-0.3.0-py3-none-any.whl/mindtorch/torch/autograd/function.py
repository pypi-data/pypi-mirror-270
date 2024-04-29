#!/usr/bin/env python
# -*- coding: utf-8 -*-
from types import FunctionType, MethodType

from mindtorch.utils import unsupported_attr
from mindtorch.torch.nn import Module
from mindtorch.torch.tensor import Tensor, cast_to_adapter_tensor, cast_to_ms_tensor
from mindtorch.torch.logging import warning


class FunctionCtx:
    def save_for_backward(self, *tensors):
        self.to_save = tensors

    def save_for_forward(self, *tensors):
        for tensor in tensors:
            if not isinstance(tensor, Tensor) or tensor is None:
                raise TypeError(
                    "save_for_forward expects all arguments to be tensors; you should "
                    "save non-tensors as attributes on ctx."
                )

        self.saved_for_forward = tensors

    def mark_dirty(self, *args):
        warning("ctx.mark_dirty do not actually take effect now.")
        self.dirty_tensors = args

    def mark_non_differentiable(self, *args):
        raise NotImplementedError("ctx.mark_non_differentiable not support yet.")

    def set_materialize_grads(self, value):
        if not value:
            warning("ctx.set_materialize_grads(false) not actually take effect now.")
        self.materialize_grads = value

    @property
    def saved_tensors(self):
        return self.to_save


class Function(Module):
    """Base class to create custom `autograd.Function`

    Examples::

        >>> class Exp(Function):
        >>>     def __init__(self):
        >>>         super(Exp, self).__init__()
        >>>
        >>>     def forward(self, i):
        >>>         result = i.exp()
        >>>         return result
        >>>
        >>>     def bprop(self, i, out, grad_output):
        >>>         return grad_output * out
        >>>
        >>> # Use non-static forward method:
        >>> output = Exp()(input)
    """
    def __init__(self, *args, **kwargs):
        unsupported_attr(args)
        unsupported_attr(kwargs)
        super(Function, self).__init__()
        self.ctx = FunctionCtx()
        def compile_bprop(num_input):
            input_args = ""
            for i in range(num_input):
                if i < num_input - 1:
                    input_args += f"input{i},"
                else:
                    input_args += f"input{i}"
            input_args += ",out,dout"
            input_args_with_self = "self," + input_args
            code = f"""def bprop({input_args_with_self}): return self._backward_wrapper({input_args})"""
            code = compile(code, "<string>", "exec")
            func = FunctionType(code.co_consts[0], globals(), "bprop")
            return func

        if not hasattr(self, 'bprop'):
            # num_input should remove ctx input, so minus 1.
            num_input = self.forward.__code__.co_argcount - 1
            self.bprop = MethodType(compile_bprop(num_input), self)

    @staticmethod
    def forward(ctx, *args, **kwargs):
        raise NotImplementedError("You must implement the forward function for custom"
                                  " autograd.Function.")

    @classmethod
    def apply(cls, *args, **kwargs):
        obj = cls()
        return obj(*args, **kwargs)

    def construct(self, *args, **kwargs):
        return self.forward(self.ctx, *args, **kwargs)

    def _run_construct(self, cast_inputs, kwargs):
        return self.forward(self.ctx, *cast_inputs, **kwargs)

    @staticmethod
    def backward(ctx, *grad_outputs):
        raise NotImplementedError("You must implement either the backward method for "
                                  "your custom autograd.Function to use it with backward "
                                  "mode AD.")

    def _backward_wrapper(self, *args, **kwargs):
        unsupported_attr(kwargs)
        # Prev node may be a mindspore bprop node, and type of grad_outputs may be MindSpore Tensor.
        # But in backward, the computation will treat it as a MindTorch Tensor.
        # So add "cast_to_adapter_tensor" to ensure self.backward get a MindTorch Tensor.
        grad_outputs = cast_to_adapter_tensor(args[-1])
        if isinstance(grad_outputs, (list, tuple)):
            res = self.backward(self.ctx, *grad_outputs)
        else:
            res = self.backward(self.ctx, grad_outputs)

        # Next Node may be a MindSpore bprop node, so need to "cast_to_ms_tensor"
        # to ensure next node get a MindSpore Tensor
        if res is None:
            res = 0
        elif isinstance(res, (list, tuple)):
            res = tuple(0 if x is None else cast_to_ms_tensor(x) for x in res)
        else:
            res = cast_to_ms_tensor(res)
        return res
