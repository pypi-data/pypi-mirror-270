# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.


"""Support megatron parallel linear."""

from megatron.core.tensor_parallel.layers import ColumnParallelLinear, RowParallelLinear

from modelopt.torch.sparsity.config import SparseGPTConfig, SparseMagnitudeConfig
from modelopt.torch.sparsity.module import SparseModule, SpDMRegistry

SpDMRegistry.register(
    {
        ColumnParallelLinear: "megatron.core.tensor_parallel.layers.ColumnParallelLinear",
        RowParallelLinear: "megatron.core.tensor_parallel.layers.RowParallelLinear",
    }
)(SparseModule)


def _get_extra_rules():
    """Get the extra rules for megatron."""
    return {
        "megatron.core.tensor_parallel.layers.ColumnParallelLinear": {
            "*": {},
            "*output_layer*": None,
        },
        "megatron.core.tensor_parallel.layers.RowParallelLinear": {
            "*": {},
            "*output_layer*": None,
        },
    }


# Update the default rules
SparseMagnitudeConfig.register_default(_get_extra_rules())
SparseGPTConfig.register_default(_get_extra_rules())
