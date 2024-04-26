"""PowerLoadSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PowerLoadSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2490
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.power_flows import _4147
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2856,
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
__all__ = ("PowerLoadSystemDeflection",)


Self = TypeVar("Self", bound="PowerLoadSystemDeflection")


class PowerLoadSystemDeflection(_2858.VirtualComponentSystemDeflection):
    """PowerLoadSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadSystemDeflection")

    class _Cast_PowerLoadSystemDeflection:
        """Special nested class for casting PowerLoadSystemDeflection to subclasses."""

        def __init__(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
            parent: "PowerLoadSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2858.VirtualComponentSystemDeflection":
            return self._parent._cast(_2858.VirtualComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def power_load_system_deflection(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection",
        ) -> "PowerLoadSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2490.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6966.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4147.PowerLoadPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerLoadPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def transmission_error_to_other_power_loads(
        self: Self,
    ) -> "List[_2856.TransmissionErrorResult]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TransmissionErrorResult]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorToOtherPowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PowerLoadSystemDeflection._Cast_PowerLoadSystemDeflection":
        return self._Cast_PowerLoadSystemDeflection(self)
