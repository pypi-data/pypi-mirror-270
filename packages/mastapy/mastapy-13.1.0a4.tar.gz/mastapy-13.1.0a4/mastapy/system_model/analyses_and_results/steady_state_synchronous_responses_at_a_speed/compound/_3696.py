"""CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3734,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3565,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3680,
        _3685,
        _3699,
        _3739,
        _3745,
        _3749,
        _3761,
        _3771,
        _3772,
        _3773,
        _3776,
        _3777,
        _3682,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
)


class CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
    _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3734.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3680.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3685.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3699.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3739.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3739,
            )

            return self._parent._cast(
                _3739.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3745.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3749.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3749,
            )

            return self._parent._cast(
                _3749.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3761.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3771.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3771,
            )

            return self._parent._cast(
                _3771.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3772.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3772,
            )

            return self._parent._cast(
                _3772.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3773.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3773,
            )

            return self._parent._cast(
                _3773.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3776.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3776,
            )

            return self._parent._cast(
                _3776.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3777.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3777,
            )

            return self._parent._cast(
                _3777.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.CouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
