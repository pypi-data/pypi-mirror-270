"""CouplingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3105,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CouplingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3029,
        _3034,
        _3089,
        _3111,
        _3129,
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CouplingSteadyStateSynchronousResponse")


class CouplingSteadyStateSynchronousResponse(
    _3105.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """CouplingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingSteadyStateSynchronousResponse"
    )

    class _Cast_CouplingSteadyStateSynchronousResponse:
        """Special nested class for casting CouplingSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
            parent: "CouplingSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3029.ClutchSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.ClutchSteadyStateSynchronousResponse)

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3034.ConceptCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(
                _3034.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3089.PartToPartShearCouplingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3089,
            )

            return self._parent._cast(
                _3089.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3111.SpringDamperSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(_3111.SpringDamperSteadyStateSynchronousResponse)

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "_3129.TorqueConverterSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3129,
            )

            return self._parent._cast(
                _3129.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def coupling_steady_state_synchronous_response(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
        ) -> "CouplingSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CouplingSteadyStateSynchronousResponse.TYPE"
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
    ) -> "CouplingSteadyStateSynchronousResponse._Cast_CouplingSteadyStateSynchronousResponse":
        return self._Cast_CouplingSteadyStateSynchronousResponse(self)
