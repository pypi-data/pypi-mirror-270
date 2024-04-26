"""AbstractAssemblyCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3999
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AbstractAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3786
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3926,
        _3927,
        _3930,
        _3933,
        _3938,
        _3940,
        _3941,
        _3946,
        _3951,
        _3954,
        _3957,
        _3961,
        _3963,
        _3969,
        _3975,
        _3977,
        _3980,
        _3984,
        _3988,
        _3991,
        _3994,
        _4000,
        _4004,
        _4011,
        _4014,
        _4018,
        _4021,
        _4022,
        _4027,
        _4030,
        _4033,
        _4037,
        _4045,
        _4048,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundStabilityAnalysis")


class AbstractAssemblyCompoundStabilityAnalysis(_3999.PartCompoundStabilityAnalysis):
    """AbstractAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
            parent: "AbstractAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(
                _3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3927.AssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.AssemblyCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3930.BeltDriveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3933.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3938.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3940.BoltedJointCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3941.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.ClutchCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3946.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3951.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3954.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3957.CouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.CouplingCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3961.CVTCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(_3961.CVTCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3963.CycloidalAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3969.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3975.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(_3975.FaceGearSetCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3977.FlexiblePinAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(
                _3977.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3984.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_3991.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(
                _3991.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> (
            "_3994.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4000.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4004.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(_4004.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4011.RollingRingAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(
                _4011.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def root_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4014.RootAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(_4014.RootAssemblyCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4021.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4022.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.SpringDamperCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4030.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(
                _4030.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4033.SynchroniserCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4033,
            )

            return self._parent._cast(_4033.SynchroniserCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4037.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4037,
            )

            return self._parent._cast(_4037.TorqueConverterCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4045.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4045,
            )

            return self._parent._cast(_4045.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "_4048.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4048,
            )

            return self._parent._cast(_4048.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
        ) -> "AbstractAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3786.AbstractAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractAssemblyStabilityAnalysis]

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
    ) -> "List[_3786.AbstractAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AbstractAssemblyStabilityAnalysis]

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
    ) -> "AbstractAssemblyCompoundStabilityAnalysis._Cast_AbstractAssemblyCompoundStabilityAnalysis":
        return self._Cast_AbstractAssemblyCompoundStabilityAnalysis(self)
