"""ZerolBevelGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3545,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _7012
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
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
__all__ = ("ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ZerolBevelGearSteadyStateSynchronousResponseAtASpeed")


class ZerolBevelGearSteadyStateSynchronousResponseAtASpeed(
    _3545.BevelGearSteadyStateSynchronousResponseAtASpeed
):
    """ZerolBevelGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ZerolBevelGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
            parent: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.BevelGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3545.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3561.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3587.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(_3587.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3552.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3606,
            )

            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7012.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ZerolBevelGearSteadyStateSynchronousResponseAtASpeed(self)
