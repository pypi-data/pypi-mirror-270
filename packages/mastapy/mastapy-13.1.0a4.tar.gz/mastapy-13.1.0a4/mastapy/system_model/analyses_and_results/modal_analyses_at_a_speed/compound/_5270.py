"""AbstractAssemblyCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5349,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5140,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5276,
        _5277,
        _5280,
        _5283,
        _5288,
        _5290,
        _5291,
        _5296,
        _5301,
        _5304,
        _5307,
        _5311,
        _5313,
        _5319,
        _5325,
        _5327,
        _5330,
        _5334,
        _5338,
        _5341,
        _5344,
        _5350,
        _5354,
        _5361,
        _5364,
        _5368,
        _5371,
        _5372,
        _5377,
        _5380,
        _5383,
        _5387,
        _5395,
        _5398,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundModalAnalysisAtASpeed")


class AbstractAssemblyCompoundModalAnalysisAtASpeed(
    _5349.PartCompoundModalAnalysisAtASpeed
):
    """AbstractAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
            parent: "AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5276.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(
                _5276.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5277.AssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(_5277.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5280.BeltDriveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5283.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(
                _5283.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5288.BevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5290.BoltedJointCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5291.ClutchCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(_5291.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5296.ConceptCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(
                _5296.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5301.ConceptGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5304.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5307.CouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5311.CVTCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5313.CycloidalAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(
                _5313.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5319.CylindricalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(
                _5319.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5325.FaceGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5327.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5330.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5334.HypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> (
            "_5338.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(
                _5338.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5341.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(
                _5341.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5344.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5350.PartToPartShearCouplingCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5354.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5361.RollingRingAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5364.RootAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(_5364.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5371.SpiralBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5372.SpringDamperCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(_5372.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5377.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5377,
            )

            return self._parent._cast(
                _5377.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5380.StraightBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5380,
            )

            return self._parent._cast(
                _5380.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5383.SynchroniserCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5383,
            )

            return self._parent._cast(_5383.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5387.TorqueConverterCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5387,
            )

            return self._parent._cast(
                _5387.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5395.WormGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5395,
            )

            return self._parent._cast(_5395.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "_5398.ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5398,
            )

            return self._parent._cast(
                _5398.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "AbstractAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5140.AbstractAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5140.AbstractAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractAssemblyModalAnalysisAtASpeed]

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
    ) -> "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed(self)
