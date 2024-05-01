# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

"""Support quantization for megatron linear layers."""


import megatron.core.tensor_parallel.layers as megatron_parallel

from ..nn import QuantModuleRegistry
from .custom import _ParallelLinear

__all__ = []


@QuantModuleRegistry.register(
    {
        megatron_parallel.ColumnParallelLinear: "megatron_ColumnParallelLinear",
        megatron_parallel.RowParallelLinear: "megatron_RowParallelLinear",
    }
)
class _MegatronParallelLinear(_ParallelLinear):
    _functionals_to_replace = [
        (megatron_parallel, "linear_with_grad_accumulation_and_async_allreduce"),
        (megatron_parallel, "linear_with_frozen_weight"),
    ]
