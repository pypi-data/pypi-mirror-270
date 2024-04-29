#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import numpy as np
import mindtorch.torch as torch
import mindtorch.torch.nn as nn
import mindtorch.torch.nn.utils.parametrize as parametrize
import mindspore as ms
from itertools import product
from testing.ut.utils import set_mode_by_env_config, param_compare, SKIP_ENV_GPU, SKIP_ENV_CPU, SKIP_ENV_GRAPH_MODE, \
    enable_backward
set_mode_by_env_config()


@SKIP_ENV_GPU(reason="Unsupported op [MatrixExp] on GPU.")
@SKIP_ENV_CPU(reason="Unsupported op [MatrixExp] on CPU.")
@SKIP_ENV_GRAPH_MODE(reason="orthogonal is not supported in GRAPH_MODE")
def test_orthogonal_parametrization():
    def assert_is_orthogonal(X):
        n, k = X.size(-2), X.size(-1)
        if n < k:
            X = X.mT
            n, k = k, n
        Id = torch.eye(k, dtype=X.dtype, device=X.device).expand(*(X.size()[:-2]), k, k)
        param_compare(X.mH @ X, Id, atol=1e-3, rtol=1e-3)

    def assert_weight_allclose_Q(weight, W):
        # Test that weight is equal to the Q part of the QR decomposition of W
        # (or of its transpose if the matrix is wide)
        wide_matrix = W.size(-2) < W.size(-1)
        if wide_matrix:
            W = W.mT
        Q, R = torch.linalg.qr(W)
        Q *= R.diagonal(dim1=-2, dim2=-1).sgn().unsqueeze(-2)
        if wide_matrix:
            Q = Q.mT
        param_compare(Q, weight, atol=1e-3, rtol=1e-3)

    with enable_backward():
        for shape, dtype, use_linear in product(((4, 4), (5, 3), (3, 5)),  # square/ tall / wide
                                                (torch.float32,),
                                                (True, False)):
            # Conv2d does not support complex yet
            if not use_linear:
                continue

            if use_linear:
                input = torch.randn(3, shape[0], dtype=dtype)
            else:
                input = torch.randn(2, 2, shape[0] + 2, shape[1] + 1, dtype=dtype)

            for parametrization, use_trivialization in product(("matrix_exp", "cayley", "householder"),
                                                               (False, True)):
                can_initialize = use_trivialization or parametrization == "householder"

                if use_linear:
                    m = nn.Linear(*shape, dtype=dtype)
                else:
                    m = nn.Conv2d(2, 3, shape, dtype=dtype)

                w_init = m.weight.clone()
                if parametrization == "householder" and m.weight.is_complex():
                    msg = "householder parametrization does not support complex tensors"
                    with pytest.raises(ValueError, match=msg):
                        torch.nn.utils.parametrizations.orthogonal(m,
                                                                   "weight",
                                                                   parametrization,
                                                                   use_trivialization=use_trivialization)
                    continue

                wide_matrix = w_init.size(-2) < w_init.size(-1)
                torch.nn.utils.parametrizations.orthogonal(m,
                                                           "weight",
                                                           parametrization,
                                                           use_trivialization=use_trivialization)
                # Forwards works as expected
                assert w_init.shape == m.weight.shape
                assert_is_orthogonal(m.weight)
                if can_initialize:
                    assert_weight_allclose_Q(m.weight, w_init)

                # Intializing with a given orthogonal matrix works
                X = torch.randn_like(m.weight)
                if wide_matrix:
                    X = X.mT
                w_new = torch.linalg.qr(X).Q
                if wide_matrix:
                    w_new = w_new.mT
                if can_initialize:
                    m.weight = w_new
                    param_compare(w_new, m.weight, atol=1e-3, rtol=1e-3)
                else:
                    msg = "assign to the matrix exponential or the Cayley parametrization"
                    with pytest.raises(NotImplementedError, match=msg):
                        m.weight = w_new

                # Intializing with a non-orthogonal matrix makes m.weight be the Q part of the given matrix
                w_new = torch.randn_like(m.weight)
                if can_initialize:
                    m.weight = w_new
                    assert_weight_allclose_Q(m.weight, w_new)
                else:
                    msg = "assign to the matrix exponential or the Cayley parametrization"
                    with pytest.raises(NotImplementedError, match=msg):
                        m.weight = w_new

                opt = torch.optim.SGD(m.parameters(), lr=0.1)

                # TODO: cayley:`solve`, which implement through the numpy API, can not backward currently.
                #  householder: Orgqr's bprop not defined.
                if parametrization in ("cayley", "householder"):
                    continue

                for _ in range(2):
                    opt.zero_grad()
                    m(input).norm().backward()
                    grad = m.parametrizations.weight.original.grad
                    assert grad is not None
                    if grad.size(-2) >= grad.size(-1):
                        zeros_grad = grad.triu(1)
                    else:
                        zeros_grad = grad.tril(-1)
                    param_compare(zeros_grad, torch.zeros_like(zeros_grad))
                    diag_grad = grad.diagonal(dim1=-2, dim2=-1)
                    if grad.is_complex():
                        diag_grad = diag_grad.real
                    param_compare(diag_grad, torch.zeros_like(diag_grad))
                    opt.step()
                    assert_is_orthogonal(m.weight)


@SKIP_ENV_GRAPH_MODE(reason="spectral_norm is not supported in GRAPH_MODE")
def test_new_spectral_norm():
    with enable_backward():
        m = nn.Linear(5, 7)
        m = torch.nn.utils.parametrizations.spectral_norm(m)
        spectral_norm_m = m.parametrizations.weight[0]

        assert spectral_norm_m._u.size() == torch.Size([m.weight.size(0)])

        # .parametrizations.weight.original should be trainable
        assert hasattr(m.parametrizations.weight, 'original')
        assert 'original' in m.parametrizations.weight._parameters

        # u should be just a reused buffer
        assert hasattr(spectral_norm_m, '_u')
        assert '_u' in spectral_norm_m._buffers
        assert '_v' in spectral_norm_m._buffers

        # weight should be a plain attribute, not counted as a buffer or a param
        assert m.weight is not None
        assert 'weight' not in m._buffers
        assert 'weight' not in m._parameters

        # it should also be sharing storage as `weight_orig`
        # self.assertEqual(m.parametrizations.weight.original.storage(), m.weight.storage())
        assert m.parametrizations.weight.original.size() == m.weight.size()
        assert m.parametrizations.weight.original.stride() == m.weight.stride()

        m = torch.nn.utils.parametrize.remove_parametrizations(m, 'weight')

        # spectral_norm is the only parametrization
        assert not hasattr(m, 'parametrizations')
        assert 'weight' in m._parameters

        # We can register spectral_norm multiple times on the same parameter
        # and on multiple parameters in the same module
        m = torch.nn.utils.parametrizations.spectral_norm(m, 'weight')
        m = torch.nn.utils.parametrizations.spectral_norm(m, 'weight')
        m = torch.nn.utils.parametrizations.spectral_norm(m, 'bias')

        # If we remove the parametrization on bias, weight is still parametrized
        # Removing a parametrization runs forward in eval mode if leave_parametrized=True
        m = torch.nn.utils.parametrize.remove_parametrizations(m, 'bias')
        assert 'bias' in m._parameters
        assert hasattr(m, 'parametrizations')
        assert 'weight' not in m._parameters

        m = torch.nn.utils.parametrize.remove_parametrizations(m, 'weight')
        # Neither weight and bias are parametrized
        assert not hasattr(m, 'parametrizations')
        assert 'weight' in m._parameters
        assert not torch.nn.utils.parametrize.is_parametrized(m)


        for requires_grad in (True, False):
            def get_modules():
                m = nn.Linear(3, 4)
                m.weight.requires_grad_(requires_grad)
                m = torch.nn.utils.parametrizations.spectral_norm(m)
                wrapped_m = m
                spectral_norm_m = m.parametrizations.weight[0]
                return m, wrapped_m, spectral_norm_m

            input = torch.randn(2, 3)

            m, wrapped_m, spectral_norm_m = get_modules()

            assert hasattr(spectral_norm_m, '_u')
            u0 = spectral_norm_m._u.clone()
            v0 = spectral_norm_m._v.clone()

            # TEST TRAINING BEHAVIOR

            # We perform GD first to modify the initial matrix
            opt = torch.optim.SGD(wrapped_m.parameters(), lr=0.1)

            opt.zero_grad()
            wrapped_m(input).sum().backward()
            opt.step()

            out = wrapped_m(input)
            if requires_grad:
                # run forward again and assert that u and v are updated
                assert not np.allclose(u0.numpy(), spectral_norm_m._u.numpy())
                assert not np.allclose(v0.numpy(), spectral_norm_m._v.numpy())

            # test backward works with multiple forwards
            # it uses training mode so we need to reset `u` and `v` vectors
            # to same value at beginning for finite difference test to pass
            saved_u = spectral_norm_m._u.clone()
            saved_v = spectral_norm_m._v.clone()

            def fn(input):
                spectral_norm_m._u.data.copy_(saved_u)
                spectral_norm_m._v.data.copy_(saved_v)
                out0 = wrapped_m(input)
                out1 = wrapped_m(input)
                return out0 + out1


            # test removing
            m, wrapped_m, _ = get_modules()
            pre_remove_out = wrapped_m(input)
            m.eval()
            m = torch.nn.utils.parametrize.remove_parametrizations(m, 'weight')
            param_compare(wrapped_m(input), pre_remove_out)

            torch.nn.utils.parametrizations.spectral_norm(m)
            for _ in range(3):
                pre_remove_out = wrapped_m(input)
            m.eval()
            m = torch.nn.utils.parametrize.remove_parametrizations(m, 'weight')
            param_compare(wrapped_m(input), pre_remove_out)

            # TEST EVAL BEHAVIOR
            m, wrapped_m, spectral_norm_m = get_modules()
            wrapped_m(input)
            last_train_out = wrapped_m(input)
            last_train_u = spectral_norm_m._u.clone()
            last_train_v = spectral_norm_m._v.clone()
            wrapped_m.zero_grad()
            wrapped_m.eval()

            eval_out0 = wrapped_m(input)
            # assert eval gives same result as last training iteration
            param_compare(eval_out0, last_train_out)
            # assert doing more iteartion in eval don't change things
            param_compare(eval_out0, wrapped_m(input))
            param_compare(last_train_u, spectral_norm_m._u)
            param_compare(last_train_v, spectral_norm_m._v)


@SKIP_ENV_GRAPH_MODE(reason="parametrize.cached is not supported in GRAPH_MODE")
def test_caching_parametrization():
    class Skew(nn.Module):
        def forward(self, X):
            X = X.tril(-1)
            return X - X.T

    class Orthogonal(nn.Module):
        def forward(self, X):
            Id = torch.eye(X.size(0), device=X.device)
            return torch.linalg.solve(Id + X, Id - X)

    model = nn.Linear(5, 5)
    parametrize.register_parametrization(model, "weight", Skew())
    parametrize.register_parametrization(model, "weight", Orthogonal())

    with parametrize.cached():
        X = model.weight
        Y = model.weight
        assert id(X) == id(Y)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_orthogonal_parametrization()
    test_new_spectral_norm()
    test_caching_parametrization()
