import numpy as np
import torch

from mindspore import context
import mindspore as ms

import mindtorch.torch as ms_torch
from mindtorch.torch.nn import Parameter

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, enable_backward, is_test_under_pynative_context
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_parameter_data1():
    input = np.array([[[1.2, 2.1], [2.2, 3.2], [2.0, 3.0]]]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_parameter = torch.nn.parameter.Parameter(data=torch_tensor)
    torch_parameter.data.fill_(0)

    ms_tensor = ms_torch.tensor(input)
    ms_parameter = Parameter(data=ms_tensor)
    ms_parameter.data.fill_(0)
    assert np.allclose(torch_parameter.data.numpy(), ms_parameter.data.numpy())
    return

def test_parameter_data2():
    input = np.array([[[1.2, 2.1], [2.2, 3.2], [2.0, 3.0]]]).astype(np.float32)

    torch_tensor = torch.tensor(input)
    torch_parameter = torch.nn.parameter.Parameter(data=torch_tensor, requires_grad=False)
    torch_parameter = -torch_parameter
    ms_tensor = ms_torch.tensor(input)
    ms_parameter = Parameter(data=ms_tensor, requires_grad=False)
    ms_parameter = -ms_parameter
    assert np.allclose(torch_parameter.numpy(), ms_parameter.numpy())
    return

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_parameter_no_grad():
    input = np.array([[[1.2, 2.1], [2.2, 3.2], [2.0, 3.0]]]).astype(np.float32)

    torch_tensor = torch.tensor(input)
    torch_parameter = torch.nn.parameter.Parameter(data=torch_tensor, requires_grad=False)
    torch_parameter.fill_(0)
    ms_tensor = ms_torch.tensor(input)
    ms_parameter = Parameter(data=ms_tensor, requires_grad=False)
    ms_parameter.fill_(0)
    assert np.allclose(torch_parameter.numpy(), ms_parameter.numpy())
    return


def test_requires_grad_():
    input_init = np.random.randn(1, 3, 16).astype(float)
    weight_init = np.random.randn(64, 3, 3).astype(float)
    weight_init_t = weight_init
    bias_init = np.random.randn(64).astype(float)

    class Conv1dPadModel(torch.nn.Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv1dPadModel, self).__init__()
            self.conv = torch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, stride=stride,
                                        padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = torch.nn.Parameter(torch.tensor(weight_init, dtype=torch.float32))
            self.conv.bias = torch.nn.Parameter(torch.tensor(bias_init, dtype=torch.float32))
            self.conv.bias.requires_grad_(False)

        def forward(self, inputs):
            x = self.conv(inputs)
            return torch.sum(x)

    class Conv1dPadModelMs(ms_torch.nn.Module):
        def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
            super(Conv1dPadModelMs, self).__init__()
            self.conv = ms_torch.nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, stride=stride,
                                        padding=padding, dilation=dilation, padding_mode=padding_mode)
            self.conv.weight = Parameter(ms_torch.tensor(weight_init_t, ms_torch.float32))
            self.conv.bias = Parameter(ms_torch.tensor(bias_init, ms_torch.float32))
            self.conv.bias.requires_grad_(False)

        def forward(self, inputs):
            x = self.conv(inputs)
            return ms_torch.sum(x)

    with enable_backward():
        torch_net = Conv1dPadModel()
        py_input = torch.tensor(input_init, dtype=torch.float32)
        torch_out = torch_net(py_input)

        ms_net = Conv1dPadModelMs()
        ms_input = ms_torch.tensor(input_init, ms_torch.float32)
        ms_out = ms_net(ms_input)

        if ms.get_context('device_target') == 'Ascend':
            assert np.allclose(ms_out.numpy(), torch_out.detach().numpy(), rtol=1e-3, atol=1e-2)
        else:
            assert np.allclose(ms_out.numpy(), torch_out.detach().numpy())

        torch_out.backward()
        grad_out = torch_net.conv.weight.grad

        # Automatic differentiation method 1
        ms_grad = ms.grad(ms_net, grad_position=None, weights=ms_net.trainable_params())(ms_input)

        # Automatic differentiation method 2
        if is_test_under_pynative_context():
            ms_out.backward()
            ms_grad_out = ms_net.conv.weight.grad

            assert len(ms_grad) == 1
            ms_grad = ms.ops.squeeze(ms_grad[0])
            if ms.get_context('device_target') == 'Ascend':
                assert np.allclose(grad_out.numpy(), ms_grad.numpy(), rtol=1e-3, atol=1e-3)
                assert np.allclose(grad_out.numpy(), ms_grad_out.numpy(), rtol=1e-3, atol=1e-3)
            else:
                assert np.allclose(grad_out.numpy(), ms_grad.numpy())
                assert np.allclose(grad_out.numpy(), ms_grad_out.numpy())


def test_parameter_data_setter():
    data = np.array([1, 2])
    a = ms_torch.nn.Parameter(ms_torch.Tensor(data))
    _id_temp = id(a)
    a.data = a.data + 1
    assert np.allclose(a.detach().numpy(), data + 1)
    assert id(a) == _id_temp

def test_reduce_ex():
    _ignore_arg = 1
    a = Parameter(ms_torch.tensor(1))
    a.name = 'aaa'
    a.requires_grad = True
    args = a.__reduce_ex__(_ignore_arg)
    func = args[0]
    input = args[1]
    func(*input)


def test_parameter_tensor_method():
    data = np.array([1, 2])
    a = ms_torch.nn.Parameter(ms_torch.Tensor(data))
    assert isinstance(a, ms_torch.nn.Parameter) == True
    assert isinstance(a, ms_torch.Tensor) == True
    assert a.size(0) == 2

    out = a * 2
    assert type(out) is ms_torch.Tensor


def test_parameter_ininstance():
    class Net(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.param = ms_torch.nn.Parameter(ms_torch.arange(0, 32))

        def forward(self, input):
            out1 = isinstance(input, ms_torch.nn.Parameter)
            out2 = isinstance(self.param, ms_torch.nn.Parameter)
            return out1, out2

    net = Net()
    input1 = ms_torch.tensor([1.0, 2.0])
    output1_1, output1_2 = net(input1)
    assert output1_1 is False
    assert output1_2 is True

    input2 = ms_torch.nn.Parameter(input1)
    output2_1, output2_2 = net(input2)
    assert output2_1 is True
    assert output2_2 is True


def test_parameter_grad():
    class Net(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.param = ms_torch.nn.Parameter(ms_torch.arange(0, 4))

        def forward(self, input):
            out = ms_torch.mul(self.param, input)
            return out.sum()

    net = Net()
    input = ms_torch.tensor([1.0, 2.0, 3.0, 4.0])
    _, grad = ms.value_and_grad(net, grad_position=None, weights=net.param)(input)
    assert np.allclose(grad.numpy(), input.numpy())


def test_parameter_const_output():
    data = np.array([1, 2])
    adapter_para = ms_torch.nn.Parameter(ms_torch.Tensor(data))
    torch_para = torch.nn.Parameter(torch.Tensor(data))
    assert isinstance(adapter_para, ms_torch.nn.Parameter) == True
    assert isinstance(adapter_para, ms_torch.Tensor) == True
    assert adapter_para.numel() == torch_para.numel()
    assert adapter_para.nelement() == torch_para.nelement()
    assert adapter_para.stride() == torch_para.stride()
    assert adapter_para.is_signed() == torch_para.is_signed()
    assert adapter_para.is_complex() == torch_para.is_complex()
    assert adapter_para.is_floating_point() == torch_para.is_floating_point()


def test_parameter_item():
    data = np.array([2])
    adapter_para = ms_torch.nn.Parameter(ms_torch.Tensor(data))
    torch_para = torch.nn.Parameter(torch.Tensor(data))
    assert adapter_para.item() == torch_para.item()


def test_parameter_equal():
    data = np.array([2, 3])
    adapter_tensor = ms_torch.Tensor(data)
    adapter_para = ms_torch.nn.Parameter(adapter_tensor)
    is_adapter_equal = adapter_para.equal(adapter_tensor)

    torch_tensor = torch.Tensor(data)
    torch_para = torch.nn.Parameter(torch_tensor)
    is_torch_equal = torch_para.equal(torch_tensor)
    assert is_adapter_equal == is_torch_equal

def test_parameters_data_different_shape():
    data = np.array([2, 3])
    adapter_tensor = ms_torch.Tensor(data)
    new_data = np.random.randn(2, 3)
    new_tensor = ms_torch.Tensor(new_data)
    b = ms_torch.nn.Parameter(new_tensor)

    a = ms_torch.nn.Parameter(adapter_tensor)
    a.data = b
    np.allclose(a.asnumpy(), new_data)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_parameter_data1()
    test_parameter_data2()
    test_parameter_no_grad()
    test_requires_grad_()
    test_parameter_data_setter()
    test_reduce_ex()
    test_parameter_tensor_method()
    test_parameter_ininstance()
    test_parameter_const_output()
    test_parameter_item()
    test_parameter_equal()
    test_parameters_data_different_shape()