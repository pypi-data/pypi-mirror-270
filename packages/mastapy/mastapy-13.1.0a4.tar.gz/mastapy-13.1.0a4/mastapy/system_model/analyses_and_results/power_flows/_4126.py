"""KlingelnbergCycloPalloidConicalGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4089
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4125,
        _4124,
        _4129,
        _4132,
        _4118,
        _4158,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetPowerFlow")


class KlingelnbergCycloPalloidConicalGearSetPowerFlow(_4089.ConicalGearSetPowerFlow):
    """KlingelnbergCycloPalloidConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
            parent: "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4089.ConicalGearSetPowerFlow":
            return self._parent._cast(_4089.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4118.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4129

            return self._parent._cast(
                _4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "_4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(
                _4132.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
        ) -> "KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears_power_flow(
        self: Self,
    ) -> "List[_4125.KlingelnbergCycloPalloidConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_gears_power_flow(
        self: Self,
    ) -> "List[_4125.KlingelnbergCycloPalloidConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_power_flow(
        self: Self,
    ) -> "List[_4124.KlingelnbergCycloPalloidConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_power_flow(
        self: Self,
    ) -> "List[_4124.KlingelnbergCycloPalloidConicalGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetPowerFlow._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetPowerFlow(self)
