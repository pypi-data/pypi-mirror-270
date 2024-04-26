"""KlingelnbergCycloPalloidHypoidGearSetPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4126
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.gears.rating.klingelnberg_hypoid import _417
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4128,
        _4127,
        _4089,
        _4118,
        _4158,
        _4055,
        _4137,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetPowerFlow")


class KlingelnbergCycloPalloidHypoidGearSetPowerFlow(
    _4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow
):
    """KlingelnbergCycloPalloidHypoidGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
            parent: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow":
            return self._parent._cast(
                _4126.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def conical_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_4089.ConicalGearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4089

            return self._parent._cast(_4089.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_4118.GearSetPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4118

            return self._parent._cast(_4118.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_4158.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_4055.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_4137.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_417.KlingelnbergCycloPalloidHypoidGearSetRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_417.KlingelnbergCycloPalloidHypoidGearSetRating":
        """mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_conical_gears_power_flow(
        self: Self,
    ) -> "List[_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow]

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
    def klingelnberg_cyclo_palloid_hypoid_gears_power_flow(
        self: Self,
    ) -> "List[_4128.KlingelnbergCycloPalloidHypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_power_flow(
        self: Self,
    ) -> "List[_4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]

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
    def klingelnberg_cyclo_palloid_hypoid_meshes_power_flow(
        self: Self,
    ) -> "List[_4127.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetPowerFlow(self)
