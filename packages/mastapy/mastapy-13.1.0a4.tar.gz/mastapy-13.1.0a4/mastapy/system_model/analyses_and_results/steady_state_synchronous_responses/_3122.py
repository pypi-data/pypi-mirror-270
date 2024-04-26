"""StraightBevelSunGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3117,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "StraightBevelSunGearSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
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
__all__ = ("StraightBevelSunGearSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="StraightBevelSunGearSteadyStateSynchronousResponse")


class StraightBevelSunGearSteadyStateSynchronousResponse(
    _3117.StraightBevelDiffGearSteadyStateSynchronousResponse
):
    """StraightBevelSunGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearSteadyStateSynchronousResponse"
    )

    class _Cast_StraightBevelSunGearSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelSunGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
            parent: "StraightBevelSunGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3117.StraightBevelDiffGearSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3117.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3024.BevelGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(_3024.BevelGearSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3012,
            )

            return self._parent._cast(
                _3012.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3040.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3067.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3067,
            )

            return self._parent._cast(_3067.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3084.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3031.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(_3031.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
        ) -> "StraightBevelSunGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelSunGearSteadyStateSynchronousResponse.TYPE",
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
    ) -> "StraightBevelSunGearSteadyStateSynchronousResponse._Cast_StraightBevelSunGearSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelSunGearSteadyStateSynchronousResponse(self)
