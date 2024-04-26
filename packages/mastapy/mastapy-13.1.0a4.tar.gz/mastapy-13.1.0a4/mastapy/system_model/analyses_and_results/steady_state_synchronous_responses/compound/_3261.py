"""VirtualComponentCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3216,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "VirtualComponentCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3132,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3214,
        _3215,
        _3225,
        _3226,
        _3260,
        _3164,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="VirtualComponentCompoundSteadyStateSynchronousResponse")


class VirtualComponentCompoundSteadyStateSynchronousResponse(
    _3216.MountableComponentCompoundSteadyStateSynchronousResponse
):
    """VirtualComponentCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_VirtualComponentCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting VirtualComponentCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
            parent: "VirtualComponentCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3164.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MassDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3215.MeasurementComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.PointLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3226.PowerLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3260.UnbalancedMassCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3260,
            )

            return self._parent._cast(
                _3260.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
        ) -> "VirtualComponentCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "VirtualComponentCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3132.VirtualComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.VirtualComponentSteadyStateSynchronousResponse]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3132.VirtualComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.VirtualComponentSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundSteadyStateSynchronousResponse._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse":
        return self._Cast_VirtualComponentCompoundSteadyStateSynchronousResponse(self)
