"""KlingelnbergCycloPalloidConicalGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4088
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4128,
        _4131,
        _4117,
        _4135,
        _4080,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearPowerFlow")


class KlingelnbergCycloPalloidConicalGearPowerFlow(_4088.ConicalGearPowerFlow):
    """KlingelnbergCycloPalloidConicalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4088.ConicalGearPowerFlow":
            return self._parent._cast(_4088.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4117.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4135.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4080.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4080

            return self._parent._cast(_4080.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "_4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(
                _4131.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearPowerFlow(self)
