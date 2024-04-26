"""TorqueConverterTurbineSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2753
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TorqueConverterTurbineSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2633
    from mastapy.system_model.analyses_and_results.static_loads import _7002
    from mastapy.system_model.analyses_and_results.power_flows import _4181
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2805,
        _2738,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterTurbineSystemDeflection")


class TorqueConverterTurbineSystemDeflection(_2753.CouplingHalfSystemDeflection):
    """TorqueConverterTurbineSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineSystemDeflection"
    )

    class _Cast_TorqueConverterTurbineSystemDeflection:
        """Special nested class for casting TorqueConverterTurbineSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
            parent: "TorqueConverterTurbineSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2753.CouplingHalfSystemDeflection":
            return self._parent._cast(_2753.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "TorqueConverterTurbineSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "TorqueConverterTurbineSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2633.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7002.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4181.TorqueConverterTurbinePowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection":
        return self._Cast_TorqueConverterTurbineSystemDeflection(self)
