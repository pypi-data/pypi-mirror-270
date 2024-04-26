"""KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2792
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.static_loads import _6944
    from mastapy.gears.rating.klingelnberg_hypoid import _417
    from mastapy.system_model.analyses_and_results.power_flows import _4129
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2796,
        _2794,
        _2748,
        _2783,
        _2829,
        _2708,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetSystemDeflection")


class KlingelnbergCycloPalloidHypoidGearSetSystemDeflection(
    _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def conical_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2783.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(_2783.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection.TYPE",
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
    def power_flow_results(
        self: Self,
    ) -> "_4129.KlingelnbergCycloPalloidHypoidGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_conical_gears_system_deflection(
        self: Self,
    ) -> "List[_2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_system_deflection(
        self: Self,
    ) -> "List[_2796.KlingelnbergCycloPalloidHypoidGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_conical_meshes_system_deflection(
        self: Self,
    ) -> "List[_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidConicalMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_system_deflection(
        self: Self,
    ) -> "List[_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetSystemDeflection(self)
