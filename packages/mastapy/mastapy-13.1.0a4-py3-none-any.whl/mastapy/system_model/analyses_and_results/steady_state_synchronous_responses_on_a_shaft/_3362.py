"""RootAssemblySteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3275,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "RootAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3373,
        _3268,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblySteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="RootAssemblySteadyStateSynchronousResponseOnAShaft")


class RootAssemblySteadyStateSynchronousResponseOnAShaft(
    _3275.AssemblySteadyStateSynchronousResponseOnAShaft
):
    """RootAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RootAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
            parent: "RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3275.AssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3275.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
        ) -> "RootAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "RootAssemblySteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2492.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_on_a_shaft_inputs(
        self: Self,
    ) -> "_3373.SteadyStateSynchronousResponseOnAShaft":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SteadyStateSynchronousResponseOnAShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateSynchronousResponseOnAShaftInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblySteadyStateSynchronousResponseOnAShaft._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RootAssemblySteadyStateSynchronousResponseOnAShaft(self)
