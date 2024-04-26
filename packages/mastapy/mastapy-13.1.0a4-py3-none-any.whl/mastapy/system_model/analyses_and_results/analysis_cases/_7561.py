"""AnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2673
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "AnalysisCase"
)

if TYPE_CHECKING:
    from mastapy.utility import _1591
    from mastapy.system_model import _2221
    from mastapy.system_model.analyses_and_results import _2674
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2848,
        _2855,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3058,
        _3112,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3373,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3632,
    )
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3839,
        _3893,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4145
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4411
    from mastapy.system_model.analyses_and_results.modal_analyses import _4648, _4677
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4932,
        _4958,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5217,
    )
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5489
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5758,
        _5787,
        _5791,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6096,
        _6112,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6609
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7036,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7300,
        _7302,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7563,
        _7570,
        _7576,
        _7577,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AnalysisCase",)


Self = TypeVar("Self", bound="AnalysisCase")


class AnalysisCase(_2673.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AnalysisCase")

    class _Cast_AnalysisCase:
        """Special nested class for casting AnalysisCase to subclasses."""

        def __init__(self: "AnalysisCase._Cast_AnalysisCase", parent: "AnalysisCase"):
            self._parent = parent

        @property
        def context(self: "AnalysisCase._Cast_AnalysisCase") -> "_2673.Context":
            return self._parent._cast(_2673.Context)

        @property
        def system_deflection(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_2848.SystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2848,
            )

            return self._parent._cast(_2848.SystemDeflection)

        @property
        def torsional_system_deflection(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_2855.TorsionalSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2855,
            )

            return self._parent._cast(_2855.TorsionalSystemDeflection)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3058.DynamicModelForSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.DynamicModelForSteadyStateSynchronousResponse
            )

        @property
        def steady_state_synchronous_response(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3112.SteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(_3112.SteadyStateSynchronousResponse)

        @property
        def steady_state_synchronous_response_on_a_shaft(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3373.SteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(_3373.SteadyStateSynchronousResponseOnAShaft)

        @property
        def steady_state_synchronous_response_at_a_speed(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3632.SteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(_3632.SteadyStateSynchronousResponseAtASpeed)

        @property
        def dynamic_model_for_stability_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3839.DynamicModelForStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(_3839.DynamicModelForStabilityAnalysis)

        @property
        def stability_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_3893.StabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.StabilityAnalysis)

        @property
        def power_flow(self: "AnalysisCase._Cast_AnalysisCase") -> "_4145.PowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.PowerFlow)

        @property
        def parametric_study_tool(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4411.ParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.ParametricStudyTool)

        @property
        def dynamic_model_for_modal_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4648.DynamicModelForModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(_4648.DynamicModelForModalAnalysis)

        @property
        def modal_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4677.ModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.ModalAnalysis)

        @property
        def dynamic_model_at_a_stiffness(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4932.DynamicModelAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.DynamicModelAtAStiffness)

        @property
        def modal_analysis_at_a_stiffness(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_4958.ModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(_4958.ModalAnalysisAtAStiffness)

        @property
        def modal_analysis_at_a_speed(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5217.ModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5217,
            )

            return self._parent._cast(_5217.ModalAnalysisAtASpeed)

        @property
        def multibody_dynamics_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5489.MultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(_5489.MultibodyDynamicsAnalysis)

        @property
        def dynamic_model_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5758.DynamicModelForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.DynamicModelForHarmonicAnalysis)

        @property
        def harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5787.HarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.HarmonicAnalysis)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_5791.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(
                _5791.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def harmonic_analysis_of_single_excitation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6096.HarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(_6096.HarmonicAnalysisOfSingleExcitation)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6112.ModalAnalysisForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6112,
            )

            return self._parent._cast(_6112.ModalAnalysisForHarmonicAnalysis)

        @property
        def dynamic_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6355.DynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.DynamicAnalysis)

        @property
        def critical_speed_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_6609.CriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6609,
            )

            return self._parent._cast(_6609.CriticalSpeedAnalysis)

        @property
        def advanced_time_stepping_analysis_for_modulation(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7036.AdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(_7036.AdvancedTimeSteppingAnalysisForModulation)

        @property
        def advanced_system_deflection(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7300.AdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.AdvancedSystemDeflection)

        @property
        def advanced_system_deflection_sub_analysis(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7302.AdvancedSystemDeflectionSubAnalysis":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.AdvancedSystemDeflectionSubAnalysis)

        @property
        def compound_analysis_case(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7563.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.CompoundAnalysisCase)

        @property
        def fe_analysis(self: "AnalysisCase._Cast_AnalysisCase") -> "_7570.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7576.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7576

            return self._parent._cast(_7576.StaticLoadAnalysisCase)

        @property
        def time_series_load_analysis_case(
            self: "AnalysisCase._Cast_AnalysisCase",
        ) -> "_7577.TimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7577

            return self._parent._cast(_7577.TimeSeriesLoadAnalysisCase)

        @property
        def analysis_case(self: "AnalysisCase._Cast_AnalysisCase") -> "AnalysisCase":
            return self._parent

        def __getattr__(self: "AnalysisCase._Cast_AnalysisCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSetupTime

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ""

        return temp

    @property
    def analysis_run_information(self: Self) -> "_1591.AnalysisRunInformation":
        """mastapy.utility.AnalysisRunInformation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisRunInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsReady

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def results_for(
        self: Self, design_entity: "_2221.DesignEntity"
    ) -> "_2674.DesignEntityAnalysis":
        """mastapy.system_model.analyses_and_results.DesignEntityAnalysis

        Args:
            design_entity (mastapy.system_model.DesignEntity)
        """
        method_result = self.wrapped.ResultsFor(
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def perform_analysis(self: Self):
        """Method does not return."""
        self.wrapped.PerformAnalysis()

    @property
    def cast_to(self: Self) -> "AnalysisCase._Cast_AnalysisCase":
        return self._Cast_AnalysisCase(self)
