"""StraightBevelGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2566
    from mastapy.system_model.analyses_and_results.static_loads import _6991
    from mastapy.gears.rating.straight_bevel import _404
    from mastapy.system_model.analyses_and_results.system_deflections import _2840
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7410,
        _7411,
        _7305,
        _7333,
        _7361,
        _7400,
        _7296,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelGearSetAdvancedSystemDeflection")


class StraightBevelGearSetAdvancedSystemDeflection(
    _7317.BevelGearSetAdvancedSystemDeflection
):
    """StraightBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
            parent: "StraightBevelGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7317.BevelGearSetAdvancedSystemDeflection":
            return self._parent._cast(_7317.BevelGearSetAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7333.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7361.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
        ) -> "StraightBevelGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelGearSetAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2566.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6991.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_404.StraightBevelGearSetRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_404.StraightBevelGearSetRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearSetRating

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
    ) -> "List[_2840.StraightBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection]

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
    def bevel_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7410.StraightBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7410.StraightBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7411.StraightBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7411.StraightBevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.StraightBevelGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetAdvancedSystemDeflection._Cast_StraightBevelGearSetAdvancedSystemDeflection":
        return self._Cast_StraightBevelGearSetAdvancedSystemDeflection(self)
