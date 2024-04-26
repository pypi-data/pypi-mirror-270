"""HypoidGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "HypoidGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.static_loads import _6934
    from mastapy.gears.rating.hypoid import _447
    from mastapy.system_model.analyses_and_results.system_deflections import _2787
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7363,
        _7364,
        _7333,
        _7361,
        _7400,
        _7296,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearSetAdvancedSystemDeflection")


class HypoidGearSetAdvancedSystemDeflection(
    _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
):
    """HypoidGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetAdvancedSystemDeflection"
    )

    class _Cast_HypoidGearSetAdvancedSystemDeflection:
        """Special nested class for casting HypoidGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
            parent: "HypoidGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            return self._parent._cast(
                _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7333.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7361.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
        ) -> "HypoidGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "HypoidGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6934.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_447.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_447.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2787.HypoidGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7363.HypoidGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7363.HypoidGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7364.HypoidGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7364.HypoidGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetAdvancedSystemDeflection._Cast_HypoidGearSetAdvancedSystemDeflection":
        return self._Cast_HypoidGearSetAdvancedSystemDeflection(self)
