# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

"""Base class for quantization modules."""
import contextlib
import copy

import torch

from modelopt.torch.opt.dynamic import DynamicModule, _DMRegistryCls
from modelopt.torch.quantization.utils import is_torch_export_mode

from ...tensor_quant import QUANT_DESC_8BIT_PER_TENSOR, QuantDescriptor
from .tensor_quantizer import TensorQuantizer

__all__ = ["QuantInputBase", "QuantLinearConvBase", "QuantModuleRegistry"]

QuantModuleRegistry = _DMRegistryCls("Quant")


class QuantInputBase(DynamicModule):
    """Base class for modules where the input is quantized."""

    input_quantizer: TensorQuantizer
    output_quantizer: TensorQuantizer
    default_quant_desc_input = QUANT_DESC_8BIT_PER_TENSOR
    default_quant_desc_output = QUANT_DESC_8BIT_PER_TENSOR

    def forward(self, input, *args, **kwargs):
        """Quantize the input before calling the original forward method."""
        input = self.input_quantizer(input)
        output = super().forward(input, *args, **kwargs)
        if isinstance(output, tuple):
            return (self.output_quantizer(output[0]), *output[1:])
        return self.output_quantizer(output)

    def _setup(self):
        """Patch the module's forward method to quantize the input."""
        self._register_temp_attribute(
            "input_quantizer", TensorQuantizer(self.default_quant_desc_input)
        )
        self._register_temp_attribute(
            "output_quantizer", TensorQuantizer(self.default_quant_desc_output)
        )
        self.output_quantizer.disable()


class QuantLinearConvBase(QuantInputBase):
    """Base class for quantized linear modules.

    Quantized linear modules are modules where both the input and the weight are quantized.
    """

    weight_quantizer: TensorQuantizer
    _enable_weight_quantization: bool
    default_quant_desc_weight = QUANT_DESC_8BIT_PER_TENSOR

    @contextlib.contextmanager
    def quantize_weight(self):
        """Context in which `self.weight` is quantized."""
        self._enable_weight_quantization = True
        yield
        self._enable_weight_quantization = False

    @staticmethod
    def _get_quantized_weight(module: "QuantLinearConvBase", weight: torch.Tensor) -> torch.Tensor:
        if module._enable_weight_quantization or is_torch_export_mode():
            return module.weight_quantizer(weight)
        return weight

    def forward(self, input, *args, **kwargs):
        """Quantize the input and the weight before calling the original forward method."""
        # self.quntize_weight() setting attributes is not allowed for torch.export.
        if is_torch_export_mode():
            return super().forward(input, *args, **kwargs)
        with self.quantize_weight():
            return super().forward(input, *args, **kwargs)

    def _setup(self):
        super()._setup()
        self._register_temp_attribute(
            "weight_quantizer", TensorQuantizer(self.default_quant_desc_weight)
        )
        self._register_temp_attribute("_enable_weight_quantization", False)
        self._register_dynamic_attribute("weight", self._get_quantized_weight)


class _LegacyQuantInputBaseMixin:
    """A mixin to support legacy quantized modules which needs to have an __init__ method."""

    _quantized_cls = QuantInputBase
    default_quant_desc_input = QUANT_DESC_8BIT_PER_TENSOR
    default_quant_desc_output = QUANT_DESC_8BIT_PER_TENSOR

    def __init__(self, *args, quant_desc_input=None, **kwargs):
        """Initialize the module with its original __init__ and patch its forward."""
        self.default_quant_desc_input = quant_desc_input or self.default_quant_desc_input
        super().__init__(*args, **kwargs)
        QuantModuleRegistry.convert(self)

    @classmethod
    def set_default_quant_desc_input(cls, value):
        """Set the class default input quantization descriptor (legacy method)."""
        if not isinstance(value, QuantDescriptor):
            raise ValueError("{} is not an instance of QuantDescriptor!")
        cls.default_quant_desc_input = copy.deepcopy(value)


class _LegacyQuantLinearConvBaseMixin(_LegacyQuantInputBaseMixin):
    """A mixin to support legacy quantized modules which needs to have an __init__ method."""

    _quantized_cls = QuantLinearConvBase
    default_quant_desc_weight = QUANT_DESC_8BIT_PER_TENSOR

    def __init__(self, *args, quant_desc_input=None, quant_desc_weight=None, **kwargs):
        """Initialize the module with its original __init__ and patch its forward."""
        self.default_quant_desc_weight = quant_desc_weight or self.default_quant_desc_weight
        super().__init__(*args, quant_desc_input=quant_desc_input, **kwargs)

    @classmethod
    def set_default_quant_desc_weight(cls, value):
        """Set the class default weight quantization descriptor (legacy method)."""
        if not isinstance(value, QuantDescriptor):
            raise ValueError("{} is not an instance of QuantDescriptor!")
        cls.default_quant_desc_weight = copy.deepcopy(value)
