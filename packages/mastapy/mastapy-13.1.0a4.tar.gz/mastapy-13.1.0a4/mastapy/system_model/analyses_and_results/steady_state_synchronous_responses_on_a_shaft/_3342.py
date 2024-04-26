"""KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3336,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.static_loads import _6945
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3302,
        _3328,
        _3345,
        _3293,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
)


class KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft(
    _3336.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
):
    """KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3336.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3336.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3302.ConicalGearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3328.GearSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3328,
            )

            return self._parent._cast(_3328.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft(
            self
        )
