"""AbstractAssemblyCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5399
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5561,
        _5562,
        _5565,
        _5568,
        _5573,
        _5575,
        _5576,
        _5581,
        _5586,
        _5589,
        _5592,
        _5596,
        _5598,
        _5604,
        _5610,
        _5612,
        _5615,
        _5619,
        _5623,
        _5626,
        _5629,
        _5635,
        _5639,
        _5646,
        _5649,
        _5653,
        _5656,
        _5657,
        _5662,
        _5665,
        _5668,
        _5672,
        _5680,
        _5683,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundMultibodyDynamicsAnalysis")


class AbstractAssemblyCompoundMultibodyDynamicsAnalysis(
    _5634.PartCompoundMultibodyDynamicsAnalysis
):
    """AbstractAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5561.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.AssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(_5562.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5565.BeltDriveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(_5565.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5568.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5573.BevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(
                _5573.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5575.BoltedJointCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5576.ClutchCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(_5576.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5581.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5586.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5589.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(
                _5589.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5592.CouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(_5592.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.CVTCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(_5596.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5598.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5604.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(
                _5604.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.FaceGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5612.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(
                _5612.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.GearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5619.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5623.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5626.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5629.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5635.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5639.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5646.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5649.RootAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5656.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5657.SpringDamperCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5662.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5662,
            )

            return self._parent._cast(
                _5662.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5665.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5665,
            )

            return self._parent._cast(
                _5665.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5668.SynchroniserCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5668,
            )

            return self._parent._cast(
                _5668.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5672.TorqueConverterCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5672,
            )

            return self._parent._cast(
                _5672.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5680.WormGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5680,
            )

            return self._parent._cast(
                _5680.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5683.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5683,
            )

            return self._parent._cast(
                _5683.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5399.AbstractAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5399.AbstractAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "AbstractAssemblyCompoundMultibodyDynamicsAnalysis._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractAssemblyCompoundMultibodyDynamicsAnalysis(self)
