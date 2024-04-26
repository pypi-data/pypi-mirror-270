"""SpecialisedAssemblyCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7432,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7400,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7438,
        _7442,
        _7445,
        _7450,
        _7452,
        _7453,
        _7458,
        _7463,
        _7466,
        _7469,
        _7473,
        _7475,
        _7481,
        _7487,
        _7489,
        _7492,
        _7496,
        _7500,
        _7503,
        _7506,
        _7512,
        _7516,
        _7523,
        _7533,
        _7534,
        _7539,
        _7542,
        _7545,
        _7549,
        _7557,
        _7560,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundAdvancedSystemDeflection")


class SpecialisedAssemblyCompoundAdvancedSystemDeflection(
    _7432.AbstractAssemblyCompoundAdvancedSystemDeflection
):
    """SpecialisedAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7432.AbstractAssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7432.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7438.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(
                _7438.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7442.BeltDriveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(_7442.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7445.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7450.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(
                _7450.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7452.BoltedJointCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(_7452.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7453.ClutchCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(_7453.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7458.ConceptCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7458,
            )

            return self._parent._cast(
                _7458.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7463.ConceptGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(
                _7463.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7466.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7469.CouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(_7469.CouplingCompoundAdvancedSystemDeflection)

        @property
        def cvt_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7473.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(_7473.CVTCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7475.CycloidalAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7481.CylindricalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(
                _7481.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7487.FaceGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7489.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(
                _7489.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7492.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.GearSetCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7496.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7500.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(
                _7500.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7503.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7506.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7512.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7516.PlanetaryGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7523.RollingRingAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7533.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7534.SpringDamperCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7539.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7539,
            )

            return self._parent._cast(
                _7539.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7542.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7542,
            )

            return self._parent._cast(
                _7542.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7545.SynchroniserCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7545,
            )

            return self._parent._cast(
                _7545.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7549.TorqueConverterCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7549,
            )

            return self._parent._cast(
                _7549.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7557.WormGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7557,
            )

            return self._parent._cast(_7557.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7560.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7560,
            )

            return self._parent._cast(
                _7560.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7400.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "List[_7400.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection(self)
