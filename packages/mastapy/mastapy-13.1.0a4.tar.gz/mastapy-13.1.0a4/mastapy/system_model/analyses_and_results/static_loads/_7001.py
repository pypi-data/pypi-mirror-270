"""TorqueConverterPumpLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6879
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterPumpLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpLoadCase",)


Self = TypeVar("Self", bound="TorqueConverterPumpLoadCase")


class TorqueConverterPumpLoadCase(_6879.CouplingHalfLoadCase):
    """TorqueConverterPumpLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpLoadCase")

    class _Cast_TorqueConverterPumpLoadCase:
        """Special nested class for casting TorqueConverterPumpLoadCase to subclasses."""

        def __init__(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
            parent: "TorqueConverterPumpLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_6879.CouplingHalfLoadCase":
            return self._parent._cast(_6879.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_pump_load_case(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
        ) -> "TorqueConverterPumpLoadCase":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPumpLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2631.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpLoadCase._Cast_TorqueConverterPumpLoadCase":
        return self._Cast_TorqueConverterPumpLoadCase(self)
