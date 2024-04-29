import os
import pytest
import numpy as np
import torch
import mindtorch.torch as pytorch
from ...utils import  set_mode_by_env_config, param_compare, SKIP_ENV_CPU, SKIP_ENV_GPU, SKIP_ENV_ASCEND

set_mode_by_env_config()

@pytest.fixture(scope='function')
def test_save_load_1():
    state_dict_torch ={}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64,64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_1_torch.pth")
    pytorch.save(state_dict_mindtorch, "test_save_load_1_mindtorch.pth")

    state_dict_torch = torch.load("test_save_load_1_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_1_mindtorch.pth")
    os.remove("test_save_load_1_torch.pth")
    os.remove("test_save_load_1_mindtorch.pth")
    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_2():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_2_torch.pth", _use_new_zipfile_serialization=False)
    pytorch.save(state_dict_mindtorch, "test_save_load_2_mindtorch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_2_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_2_mindtorch.pth")
    os.remove("test_save_load_2_torch.pth")
    os.remove("test_save_load_2_mindtorch.pth")
    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_3():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_3_torch.pth")

    state_dict_torch = torch.load("test_save_load_3_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_3_torch.pth")
    os.remove("test_save_load_3_torch.pth")

    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_4():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_4_torch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_4_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_4_torch.pth")
    os.remove("test_save_load_4_torch.pth")

    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_bf16_1():
    state_dict_mindtorch = {}
    a = pytorch.tensor(800000, dtype=pytorch.bfloat16)
    b = pytorch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=pytorch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    pytorch.save(state_dict_mindtorch, "test_save_load_bf16_1.pth", _use_new_zipfile_serialization=False)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_1.pth")
    os.remove("test_save_load_bf16_1.pth")
    assert a.dtype == state_dict_mindtorch["a"].dtype
    assert b.dtype == state_dict_mindtorch["b"].dtype
    param_compare(a.to(pytorch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(pytorch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_bf16_2():
    state_dict_mindtorch = {}
    a = pytorch.tensor(800000, dtype=pytorch.bfloat16)
    b = pytorch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=pytorch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    pytorch.save(state_dict_mindtorch, "test_save_load_bf16_2.pth", _use_new_zipfile_serialization=True)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_2.pth")
    os.remove("test_save_load_bf16_2.pth")
    assert a.dtype == state_dict_mindtorch["a"].dtype
    assert b.dtype == state_dict_mindtorch["b"].dtype
    param_compare(a.to(pytorch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(pytorch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_bf16_3():
    state_dict_mindtorch = {}
    a = torch.tensor(800000, dtype=torch.bfloat16)
    b = torch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=torch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_mindtorch, "test_save_load_bf16_3.pth", _use_new_zipfile_serialization=False)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_3.pth")
    os.remove("test_save_load_bf16_3.pth")
    param_compare(a.to(torch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(torch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_bf16_4():
    state_dict_mindtorch = {}
    a = torch.tensor(800000, dtype=torch.bfloat16)
    b = torch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=torch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_mindtorch, "test_save_load_bf16_4.pth", _use_new_zipfile_serialization=True)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_4.pth")
    os.remove("test_save_load_bf16_4.pth")
    param_compare(a.to(torch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(torch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_parameter_1():
    state_dict_torch ={}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64,64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_1_torch.pth")
    pytorch.save(state_dict_mindtorch, "test_save_load_parameter_1_mindtorch.pth")

    state_dict_torch = torch.load("test_save_load_parameter_1_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_1_mindtorch.pth")
    os.remove("test_save_load_parameter_1_torch.pth")
    os.remove("test_save_load_parameter_1_mindtorch.pth")
    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_parameter_2():
    state_dict_torch ={}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64,64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_2_torch.pth", _use_new_zipfile_serialization=False)
    pytorch.save(state_dict_mindtorch, "test_save_load_parameter_2_mindtorch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_parameter_2_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_2_mindtorch.pth")
    os.remove("test_save_load_parameter_2_torch.pth")
    os.remove("test_save_load_parameter_2_mindtorch.pth")
    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]


@pytest.fixture(scope='function')
def test_save_load_parameter_3():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_3_torch.pth")

    state_dict_torch = torch.load("test_save_load_parameter_3_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_3_torch.pth")
    os.remove("test_save_load_parameter_3_torch.pth")

    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_parameter_4():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_4_torch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_parameter_4_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_4_torch.pth")
    os.remove("test_save_load_parameter_4_torch.pth")

    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

@pytest.fixture(scope='function')
def test_save_load_net():
    import torch
    import torch.nn as nn
    class Net(nn.Module):
        def __init__(self, num_classes: int = 10) -> None:
            super(Net, self).__init__()

            self.features = nn.Sequential(
                nn.Conv2d(3, 64, (11, 11), (4, 4), (2, 2), bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(),
                nn.MaxPool2d((3, 3), (2, 2)),
            )

            self.avgpool = nn.AdaptiveAvgPool2d((6, 6))

            self.classifier = nn.Sequential(
                nn.Dropout(0.5),
                nn.Linear(256 * 6 * 6, 4096),
            )

    net = Net()
    state_dict = {
        'net': net.state_dict(),
    }

    torch.save(state_dict, 'torch_module.pt', _use_new_zipfile_serialization=True)

    torch.save(state_dict, 'torch_module_oldfile.pt', _use_new_zipfile_serialization=False)

    import mindtorch.torch as pytorch
    import mindtorch.torch.nn as nn
    class Net(nn.Module):
        def __init__(self, num_classes: int = 10) -> None:
            super(Net, self).__init__()

            self.features = nn.Sequential(
                nn.Conv2d(3, 64, (11, 11), (4, 4), (2, 2), bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(),
                nn.MaxPool2d((3, 3), (2, 2)),
            )

            self.avgpool = nn.AdaptiveAvgPool2d((6, 6))

            self.classifier = nn.Sequential(
                nn.Dropout(0.5),
                nn.Linear(256 * 6 * 6, 4096),
            )

    net = Net()
    state = pytorch.load("torch_module.pt")
    net.load_state_dict(state['net'])
    os.remove("torch_module.pt")
    state_dict = {
        'net': net.state_dict(),
    }
    pytorch.save(state_dict, 'mindtorch_module.pt', _use_new_zipfile_serialization=True)
    os.remove("mindtorch_module.pt")

    state = pytorch.load("torch_module_oldfile.pt")
    net.load_state_dict(state['net'])
    os.remove("torch_module_oldfile.pt")
    state_dict = {
        'net': net.state_dict(),
    }
    pytorch.save(state_dict, 'mindtorch_module_oldfile.pt', _use_new_zipfile_serialization=False)
    os.remove('mindtorch_module_oldfile.pt')


@pytest.fixture(scope='function')
@SKIP_ENV_ASCEND(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_GPU(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_CPU(reason="This function need torch version >= 2.1.0")
def test_save_load_5():
    a = torch.tensor(2.)
    a.kkk = 3
    torch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a, tensor)


@pytest.fixture(scope='function')
def test_save_load_6():
    a = pytorch.tensor(2.)
    a.kkk = 3
    pytorch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a, tensor)


@pytest.fixture(scope='function')
@SKIP_ENV_ASCEND(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_GPU(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_CPU(reason="This function need torch version >= 2.1.0")
def test_save_load_7():
    a = torch.nn.Parameter(torch.tensor(2.))
    a.kkk = 3
    torch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a.detach(), tensor)


@pytest.fixture(scope='function')
def test_save_load_8():
    a = pytorch.nn.Parameter(pytorch.tensor(2.))
    a.kkk = 3
    pytorch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a, tensor)

if __name__ == '__main__':
    test_save_load_1()
    test_save_load_2()
    test_save_load_3()
    test_save_load_4()
    test_save_load_bf16_1()
    test_save_load_bf16_2()
    test_save_load_bf16_3()
    test_save_load_bf16_4()
    test_save_load_parameter_1()
    test_save_load_parameter_2()
    test_save_load_parameter_3()
    test_save_load_parameter_4()
    test_save_load_net()
    test_save_load_5()
    test_save_load_6()
