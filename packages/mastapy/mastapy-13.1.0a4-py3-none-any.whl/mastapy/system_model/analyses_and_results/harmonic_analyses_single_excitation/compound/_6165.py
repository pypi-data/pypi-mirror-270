"""AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6244,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6034,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6171,
        _6172,
        _6175,
        _6178,
        _6183,
        _6185,
        _6186,
        _6191,
        _6196,
        _6199,
        _6202,
        _6206,
        _6208,
        _6214,
        _6220,
        _6222,
        _6225,
        _6229,
        _6233,
        _6236,
        _6239,
        _6245,
        _6249,
        _6256,
        _6259,
        _6263,
        _6266,
        _6267,
        _6272,
        _6275,
        _6278,
        _6282,
        _6290,
        _6293,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation"
)


class AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
    _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
):
    """AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6244.PartCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6244.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6171.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6172.AssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6175.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6178.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6183.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6186.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6191.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6191,
            )

            return self._parent._cast(
                _6191.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6196.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6199.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6202.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6202,
            )

            return self._parent._cast(
                _6202.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6206.CVTCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6208.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6208,
            )

            return self._parent._cast(
                _6208.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6214.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6222.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6225.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6229.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6233.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6236.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6245.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6249.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6256.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6256,
            )

            return self._parent._cast(
                _6256.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6259.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6259,
            )

            return self._parent._cast(
                _6259.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6263.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6266.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6267.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6272.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6272,
            )

            return self._parent._cast(
                _6272.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6275.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6275,
            )

            return self._parent._cast(
                _6275.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6278.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6278,
            )

            return self._parent._cast(
                _6278.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6282.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6282,
            )

            return self._parent._cast(
                _6282.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6290.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6290,
            )

            return self._parent._cast(
                _6290.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6293.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6293,
            )

            return self._parent._cast(
                _6293.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6034.AbstractAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
