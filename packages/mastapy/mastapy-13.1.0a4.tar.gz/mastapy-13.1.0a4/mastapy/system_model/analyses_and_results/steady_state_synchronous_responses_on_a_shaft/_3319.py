"""DatumSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3293,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "DatumSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.static_loads import _6896
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("DatumSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="DatumSteadyStateSynchronousResponseOnAShaft")


class DatumSteadyStateSynchronousResponseOnAShaft(
    _3293.ComponentSteadyStateSynchronousResponseOnAShaft
):
    """DatumSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _DATUM_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DatumSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_DatumSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting DatumSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
            parent: "DatumSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.ComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3293.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
        ) -> "DatumSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft",
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
        self: Self, instance_to_wrap: "DatumSteadyStateSynchronousResponseOnAShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6896.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

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
    ) -> "DatumSteadyStateSynchronousResponseOnAShaft._Cast_DatumSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_DatumSteadyStateSynchronousResponseOnAShaft(self)
