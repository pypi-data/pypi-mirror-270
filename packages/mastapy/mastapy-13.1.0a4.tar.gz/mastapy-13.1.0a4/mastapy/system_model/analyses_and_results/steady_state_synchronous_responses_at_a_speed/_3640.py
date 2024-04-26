"""StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3635,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3545,
        _3533,
        _3561,
        _3587,
        _3604,
        _3552,
        _3606,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"
)


class StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed(
    _3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3561.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3587.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(_3587.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
