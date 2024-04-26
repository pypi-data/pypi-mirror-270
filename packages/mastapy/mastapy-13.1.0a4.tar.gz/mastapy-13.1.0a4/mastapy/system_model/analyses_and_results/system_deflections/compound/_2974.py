"""SpecialisedAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SpecialisedAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2829
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2880,
        _2884,
        _2887,
        _2892,
        _2894,
        _2895,
        _2900,
        _2905,
        _2908,
        _2911,
        _2915,
        _2917,
        _2923,
        _2930,
        _2932,
        _2935,
        _2939,
        _2943,
        _2946,
        _2949,
        _2955,
        _2959,
        _2966,
        _2977,
        _2978,
        _2983,
        _2986,
        _2989,
        _2993,
        _3001,
        _3004,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundSystemDeflection")


class SpecialisedAssemblyCompoundSystemDeflection(
    _2874.AbstractAssemblyCompoundSystemDeflection
):
    """SpecialisedAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyCompoundSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
            parent: "SpecialisedAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2880.AGMAGleasonConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(
                _2880.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def belt_drive_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2884.BeltDriveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2887.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(
                _2887.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2892.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2894.BoltedJointCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2895.ClutchCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2900.ConceptCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2905.ConceptGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2908.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2911.CouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2915.CVTCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2917.CycloidalAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(_2917.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2923.CylindricalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(_2923.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2930.FaceGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(_2930.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2932.FlexiblePinAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2935.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.GearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2939.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2943.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(
                _2943.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2946.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(
                _2946.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2949.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(
                _2949.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2955.PartToPartShearCouplingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(
                _2955.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2959.PlanetaryGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2966.RollingRingAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(_2966.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2977.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2978.SpringDamperCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2983.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(
                _2983.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2986.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(
                _2986.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2989.SynchroniserCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2989,
            )

            return self._parent._cast(_2989.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_2993.TorqueConverterCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2993,
            )

            return self._parent._cast(_2993.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_3001.WormGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3001,
            )

            return self._parent._cast(_3001.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "_3004.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3004,
            )

            return self._parent._cast(_3004.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
        ) -> "SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2829.SpecialisedAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2829.SpecialisedAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection":
        return self._Cast_SpecialisedAssemblyCompoundSystemDeflection(self)
