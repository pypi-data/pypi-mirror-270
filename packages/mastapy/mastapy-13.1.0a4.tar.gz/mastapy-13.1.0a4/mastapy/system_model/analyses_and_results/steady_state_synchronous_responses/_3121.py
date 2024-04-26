"""StraightBevelPlanetGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3117,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelPlanetGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3024,
        _3012,
        _3040,
        _3067,
        _3084,
        _3031,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearSteadyStateSynchronousResponse")


class StraightBevelPlanetGearSteadyStateSynchronousResponse(
    _3117.StraightBevelDiffGearSteadyStateSynchronousResponse
):
    """StraightBevelPlanetGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse"
    )

    class _Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelPlanetGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
            parent: "StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3117.StraightBevelDiffGearSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3117.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3024.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(_3024.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3040.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3067.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
        ) -> "StraightBevelPlanetGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelPlanetGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearSteadyStateSynchronousResponse._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelPlanetGearSteadyStateSynchronousResponse(self)
