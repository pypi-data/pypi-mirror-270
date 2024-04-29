#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_cov1():
    np_1 = np.random.randn(8).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cov(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cov(torch_tensor)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cov2():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cov(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cov(torch_tensor)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cov3():
    np_1 = np.random.randint(0, 10, 5).astype(np.int32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cov(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cov(torch_tensor)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cov4():
    np_1 = np.random.randint(0, 10, (3, 4)).astype(np.int32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.cov(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.cov(torch_tensor)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cov5():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    fw = np.random.randint(1, 10, (4,))
    aw = np.random.rand(4).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_fw = ms_torch.tensor(fw)
    ms_aw = ms_torch.tensor(aw)
    ms_result = ms_torch.cov(ms_tensor, fweights=ms_fw, aweights=ms_aw)
    torch_tensor = torch.tensor(np_1)
    torch_fw = torch.tensor(fw)
    torch_aw = torch.tensor(aw)
    torch_result = torch.cov(torch_tensor, fweights=torch_fw, aweights=torch_aw)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


if __name__ == "__main__":
    set_mode_by_env_config()
    test_cov1()
    test_cov2()
    test_cov3()
    test_cov4()
    test_cov5()
