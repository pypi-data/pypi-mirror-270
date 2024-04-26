"""CouplingHalfSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3345,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "CouplingHalfSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3290,
        _3295,
        _3309,
        _3349,
        _3356,
        _3361,
        _3371,
        _3382,
        _3383,
        _3384,
        _3387,
        _3389,
        _3293,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="CouplingHalfSteadyStateSynchronousResponseOnAShaft")


class CouplingHalfSteadyStateSynchronousResponseOnAShaft(
    _3345.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """CouplingHalfSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CouplingHalfSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
            parent: "CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3345.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3293.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3290.ClutchHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3290,
            )

            return self._parent._cast(
                _3290.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3295.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(
                _3295.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3309.CVTPulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3349.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3356.PulleySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3361.RollingRingSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3371.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3382.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3382,
            )

            return self._parent._cast(
                _3382.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3383.SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3383,
            )

            return self._parent._cast(
                _3383.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3384.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3384,
            )

            return self._parent._cast(
                _3384.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3387.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3387,
            )

            return self._parent._cast(
                _3387.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3389.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3389,
            )

            return self._parent._cast(
                _3389.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
        ) -> "CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CouplingHalfSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfSteadyStateSynchronousResponseOnAShaft._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_CouplingHalfSteadyStateSynchronousResponseOnAShaft(self)
