import numpy as np
import mindtorch.torch as mt_torch
import torch
from typing import Union
from mindtorch.torch import Tensor as mtTensor
from torch import Tensor as ptTensor
from ...utils import set_mode_by_env_config, param_compare, enable_backward

set_mode_by_env_config()

def run_backward(tensor: Union[mtTensor, ptTensor], grad_input=None):
    if grad_input is None:
        assert tensor.shape == ()
        tensor.backward()

    else:
        assert tensor.shape == grad_input.shape
        tensor.backward(grad_input)


def run_simple_op(a: Union[mtTensor, ptTensor], b: Union[mtTensor, ptTensor], op: str):
    if op == '+':
        return a + b
    if op == '-':
        return a + b
    if op == '*':
        return a + b
    if op == '/':
        return a + b
    if op == '@':
        return a @ b
    raise ValueError(f'not support {op} yet')


def test_simple_op_backward_test():
    with enable_backward():
        a = np.random.randn(3, 3).astype(np.float32)
        b = np.random.randn(3, 3).astype(np.float32)

        pt_a, pt_b = torch.tensor(a, requires_grad=True), torch.tensor(b, requires_grad=True)
        mt_a, mt_b = mt_torch.tensor(a, requires_grad=True), mt_torch.tensor(b, requires_grad=True)

        op_list = ['+', '-', '*', '/', '@']

        for op in op_list:
            pt_out = run_simple_op(pt_a, pt_b, op)
            mt_out = run_simple_op(mt_a, mt_b, op)
            assert mt_out.requires_grad == pt_out.requires_grad
            assert np.allclose(pt_out.detach().numpy(), mt_out.detach().numpy(), 1e-4, 1e-4)

            run_backward(pt_out, torch.tensor(np.ones((3, 3), np.float32)))
            run_backward(mt_out, mt_torch.tensor(np.ones((3, 3), np.float32)))

            # assert has grad
            assert mt_a.grad is not None and mt_b.grad is not None
            # allclose
            param_compare(pt_a.grad.detach(), mt_a.grad.detach(), 1e-4, 1e-4)
            param_compare(pt_b.grad.detach(), mt_b.grad.detach(), 1e-4, 1e-4)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_simple_op_backward_test()
