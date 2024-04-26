"""TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3437,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3387,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3475,
        _3423,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"
)


class TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft(
    _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
):
    """TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2631.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3387.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3387.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
