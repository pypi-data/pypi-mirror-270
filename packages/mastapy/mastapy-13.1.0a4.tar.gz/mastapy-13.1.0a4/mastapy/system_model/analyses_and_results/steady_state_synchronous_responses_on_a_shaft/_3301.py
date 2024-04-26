"""ConicalGearSetSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3327,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3302,
        _3300,
        _3273,
        _3280,
        _3285,
        _3331,
        _3335,
        _3338,
        _3341,
        _3368,
        _3375,
        _3378,
        _3396,
        _3366,
        _3268,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConicalGearSetSteadyStateSynchronousResponseOnAShaft")


class ConicalGearSetSteadyStateSynchronousResponseOnAShaft(
    _3327.GearSetSteadyStateSynchronousResponseOnAShaft
):
    """ConicalGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConicalGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.GearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3327.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3280,
            )

            return self._parent._cast(
                _3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3331.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3335.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3335,
            )

            return self._parent._cast(
                _3335.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3338.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3341.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(
                _3341.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3368.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3375.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3375,
            )

            return self._parent._cast(
                _3375.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3378.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3378,
            )

            return self._parent._cast(
                _3378.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3396.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3396,
            )

            return self._parent._cast(
                _3396.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConicalGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3302.ConicalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3302.ConicalGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3300.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3300.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConicalGearSetSteadyStateSynchronousResponseOnAShaft(self)
