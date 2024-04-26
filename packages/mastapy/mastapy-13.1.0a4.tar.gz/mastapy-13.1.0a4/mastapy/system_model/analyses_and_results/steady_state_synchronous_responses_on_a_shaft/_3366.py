"""SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3268,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2494
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3273,
        _3278,
        _3280,
        _3285,
        _3287,
        _3291,
        _3296,
        _3298,
        _3301,
        _3307,
        _3310,
        _3311,
        _3316,
        _3322,
        _3325,
        _3327,
        _3331,
        _3335,
        _3338,
        _3341,
        _3350,
        _3352,
        _3359,
        _3368,
        _3372,
        _3375,
        _3378,
        _3385,
        _3388,
        _3393,
        _3396,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"
)


class SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
    _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
):
    """SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3278.BeltDriveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3287.BoltedJointSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(
                _3287.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3296.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3298.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3298,
            )

            return self._parent._cast(
                _3298.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.CouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3307,
            )

            return self._parent._cast(
                _3307.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3310.CVTSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3310,
            )

            return self._parent._cast(_3310.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3311.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3311,
            )

            return self._parent._cast(
                _3311.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3316.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3322.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3325.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3325,
            )

            return self._parent._cast(
                _3325.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3335.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3338.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3341.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3350.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3352.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3359.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3368.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3372.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3375.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3375,
            )

            return self._parent._cast(
                _3375.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3378.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3378,
            )

            return self._parent._cast(
                _3378.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3385.SynchroniserSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3385,
            )

            return self._parent._cast(
                _3385.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3388.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3388,
            )

            return self._parent._cast(
                _3388.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3393.WormGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3393,
            )

            return self._parent._cast(
                _3393.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3396.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3396,
            )

            return self._parent._cast(
                _3396.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2494.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
            self
        )
