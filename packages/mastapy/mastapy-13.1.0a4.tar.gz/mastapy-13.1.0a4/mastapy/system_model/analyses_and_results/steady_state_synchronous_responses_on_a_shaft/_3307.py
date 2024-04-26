"""CouplingSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3366,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3291,
        _3296,
        _3350,
        _3372,
        _3388,
        _3268,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingSteadyStateSynchronousResponseOnAShaft")


class CouplingSteadyStateSynchronousResponseOnAShaft(
    _3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
):
    """CouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_CouplingSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3291.ClutchSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3296.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(
                _3296.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3350.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3350,
            )

            return self._parent._cast(
                _3350.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3372.SpringDamperSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3372,
            )

            return self._parent._cast(
                _3372.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3388.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3388,
            )

            return self._parent._cast(
                _3388.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2602.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

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
    ) -> "CouplingSteadyStateSynchronousResponseOnAShaft._Cast_CouplingSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingSteadyStateSynchronousResponseOnAShaft(self)
