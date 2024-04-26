"""GearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "GearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7376,
        _7359,
        _7360,
        _7305,
        _7312,
        _7317,
        _7330,
        _7333,
        _7349,
        _7356,
        _7365,
        _7369,
        _7372,
        _7375,
        _7386,
        _7403,
        _7409,
        _7412,
        _7428,
        _7431,
        _7296,
        _7381,
    )
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.gears.rating import _370
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GearSetAdvancedSystemDeflection")


class GearSetAdvancedSystemDeflection(
    _7400.SpecialisedAssemblyAdvancedSystemDeflection
):
    """GearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetAdvancedSystemDeflection")

    class _Cast_GearSetAdvancedSystemDeflection:
        """Special nested class for casting GearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
            parent: "GearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7312.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(
                _7312.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7317.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.BevelGearSetAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7330.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7333.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.ConicalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7349.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7356.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.FaceGearSetAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7365.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(
                _7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(
                _7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7386.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7403.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7409.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7409,
            )

            return self._parent._cast(
                _7409.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7412.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7412,
            )

            return self._parent._cast(
                _7412.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7428.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7428,
            )

            return self._parent._cast(_7428.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "_7431.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7431,
            )

            return self._parent._cast(_7431.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
        ) -> "GearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_ltca_in_advanced_system_deflection(
        self: Self,
    ) -> "_7376.UseLtcaInAsdOption":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.UseLtcaInAsdOption"""
        temp = self.wrapped.UseLTCAInAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.advanced_system_deflections._7376",
            "UseLtcaInAsdOption",
        )(value)

    @use_ltca_in_advanced_system_deflection.setter
    @enforce_parameter_types
    def use_ltca_in_advanced_system_deflection(
        self: Self, value: "_7376.UseLtcaInAsdOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.UseLtcaInAsdOption",
        )
        self.wrapped.UseLTCAInAdvancedSystemDeflection = value

    @property
    def assembly_design(self: Self) -> "_2550.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_370.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7359.GearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7360.GearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetAdvancedSystemDeflection._Cast_GearSetAdvancedSystemDeflection":
        return self._Cast_GearSetAdvancedSystemDeflection(self)
