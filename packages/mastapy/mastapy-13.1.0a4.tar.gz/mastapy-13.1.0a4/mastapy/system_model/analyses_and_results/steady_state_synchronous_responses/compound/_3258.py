"""TorqueConverterPumpCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3178,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2631
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3128,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3216,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="TorqueConverterPumpCompoundSteadyStateSynchronousResponse"
)


class TorqueConverterPumpCompoundSteadyStateSynchronousResponse(
    _3178.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """TorqueConverterPumpCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting TorqueConverterPumpCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
            parent: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.CouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3178.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
        ) -> "TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "TorqueConverterPumpCompoundSteadyStateSynchronousResponse.TYPE",
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
    ) -> "List[_3128.TorqueConverterPumpSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterPumpSteadyStateSynchronousResponse]

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
    ) -> "List[_3128.TorqueConverterPumpSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.TorqueConverterPumpSteadyStateSynchronousResponse]

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
    ) -> "TorqueConverterPumpCompoundSteadyStateSynchronousResponse._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
        return self._Cast_TorqueConverterPumpCompoundSteadyStateSynchronousResponse(
            self
        )
