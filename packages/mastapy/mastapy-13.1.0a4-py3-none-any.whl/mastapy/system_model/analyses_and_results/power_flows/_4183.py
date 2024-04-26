"""VirtualComponentPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "VirtualComponentPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4133,
        _4134,
        _4144,
        _4147,
        _4182,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentPowerFlow",)


Self = TypeVar("Self", bound="VirtualComponentPowerFlow")


class VirtualComponentPowerFlow(_4135.MountableComponentPowerFlow):
    """VirtualComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentPowerFlow")

    class _Cast_VirtualComponentPowerFlow:
        """Special nested class for casting VirtualComponentPowerFlow to subclasses."""

        def __init__(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
            parent: "VirtualComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4133.MassDiscPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4134.MeasurementComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.MeasurementComponentPowerFlow)

        @property
        def point_load_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4144.PointLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.PointLoadPowerFlow)

        @property
        def power_load_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4147.PowerLoadPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.PowerLoadPowerFlow)

        @property
        def unbalanced_mass_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "_4182.UnbalancedMassPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4182

            return self._parent._cast(_4182.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow",
        ) -> "VirtualComponentPowerFlow":
            return self._parent

        def __getattr__(
            self: "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentPowerFlow.TYPE"):
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
    def component_design(self: Self) -> "_2497.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow":
        return self._Cast_VirtualComponentPowerFlow(self)
