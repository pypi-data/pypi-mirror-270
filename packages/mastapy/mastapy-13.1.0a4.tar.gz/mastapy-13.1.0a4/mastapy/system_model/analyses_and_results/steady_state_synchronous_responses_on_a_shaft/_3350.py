"""PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3307,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3366,
        _3268,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft"
)


class PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft(
    _3307.CouplingSteadyStateSynchronousResponseOnAShaft
):
    """PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
            parent: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3307.CouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3307.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2607.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft(
            self
        )
