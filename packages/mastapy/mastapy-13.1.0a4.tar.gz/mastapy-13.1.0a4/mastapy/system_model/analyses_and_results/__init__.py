"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2642 import CompoundAnalysis
    from ._2643 import SingleAnalysis
    from ._2644 import AdvancedSystemDeflectionAnalysis
    from ._2645 import AdvancedSystemDeflectionSubAnalysis
    from ._2646 import AdvancedTimeSteppingAnalysisForModulation
    from ._2647 import CompoundParametricStudyToolAnalysis
    from ._2648 import CriticalSpeedAnalysis
    from ._2649 import DynamicAnalysis
    from ._2650 import DynamicModelAtAStiffnessAnalysis
    from ._2651 import DynamicModelForHarmonicAnalysis
    from ._2652 import DynamicModelForModalAnalysis
    from ._2653 import DynamicModelForStabilityAnalysis
    from ._2654 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2655 import HarmonicAnalysis
    from ._2656 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2657 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2658 import ModalAnalysis
    from ._2659 import ModalAnalysisAtASpeed
    from ._2660 import ModalAnalysisAtAStiffness
    from ._2661 import ModalAnalysisForHarmonicAnalysis
    from ._2662 import MultibodyDynamicsAnalysis
    from ._2663 import ParametricStudyToolAnalysis
    from ._2664 import PowerFlowAnalysis
    from ._2665 import StabilityAnalysis
    from ._2666 import SteadyStateSynchronousResponseAnalysis
    from ._2667 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2668 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2669 import SystemDeflectionAnalysis
    from ._2670 import TorsionalSystemDeflectionAnalysis
    from ._2671 import AnalysisCaseVariable
    from ._2672 import ConnectionAnalysis
    from ._2673 import Context
    from ._2674 import DesignEntityAnalysis
    from ._2675 import DesignEntityGroupAnalysis
    from ._2676 import DesignEntitySingleContextAnalysis
    from ._2680 import PartAnalysis
    from ._2681 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2682 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2683 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2684 import CompoundCriticalSpeedAnalysis
    from ._2685 import CompoundDynamicAnalysis
    from ._2686 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2687 import CompoundDynamicModelForHarmonicAnalysis
    from ._2688 import CompoundDynamicModelForModalAnalysis
    from ._2689 import CompoundDynamicModelForStabilityAnalysis
    from ._2690 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2691 import CompoundHarmonicAnalysis
    from ._2692 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._2693 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2694 import CompoundModalAnalysis
    from ._2695 import CompoundModalAnalysisAtASpeed
    from ._2696 import CompoundModalAnalysisAtAStiffness
    from ._2697 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2698 import CompoundMultibodyDynamicsAnalysis
    from ._2699 import CompoundPowerFlowAnalysis
    from ._2700 import CompoundStabilityAnalysis
    from ._2701 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2702 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2703 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2704 import CompoundSystemDeflectionAnalysis
    from ._2705 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2706 import TESetUpForDynamicAnalysisOptions
    from ._2707 import TimeOptions
else:
    import_structure = {
        "_2642": ["CompoundAnalysis"],
        "_2643": ["SingleAnalysis"],
        "_2644": ["AdvancedSystemDeflectionAnalysis"],
        "_2645": ["AdvancedSystemDeflectionSubAnalysis"],
        "_2646": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_2647": ["CompoundParametricStudyToolAnalysis"],
        "_2648": ["CriticalSpeedAnalysis"],
        "_2649": ["DynamicAnalysis"],
        "_2650": ["DynamicModelAtAStiffnessAnalysis"],
        "_2651": ["DynamicModelForHarmonicAnalysis"],
        "_2652": ["DynamicModelForModalAnalysis"],
        "_2653": ["DynamicModelForStabilityAnalysis"],
        "_2654": ["DynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2655": ["HarmonicAnalysis"],
        "_2656": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_2657": ["HarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2658": ["ModalAnalysis"],
        "_2659": ["ModalAnalysisAtASpeed"],
        "_2660": ["ModalAnalysisAtAStiffness"],
        "_2661": ["ModalAnalysisForHarmonicAnalysis"],
        "_2662": ["MultibodyDynamicsAnalysis"],
        "_2663": ["ParametricStudyToolAnalysis"],
        "_2664": ["PowerFlowAnalysis"],
        "_2665": ["StabilityAnalysis"],
        "_2666": ["SteadyStateSynchronousResponseAnalysis"],
        "_2667": ["SteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2668": ["SteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2669": ["SystemDeflectionAnalysis"],
        "_2670": ["TorsionalSystemDeflectionAnalysis"],
        "_2671": ["AnalysisCaseVariable"],
        "_2672": ["ConnectionAnalysis"],
        "_2673": ["Context"],
        "_2674": ["DesignEntityAnalysis"],
        "_2675": ["DesignEntityGroupAnalysis"],
        "_2676": ["DesignEntitySingleContextAnalysis"],
        "_2680": ["PartAnalysis"],
        "_2681": ["CompoundAdvancedSystemDeflectionAnalysis"],
        "_2682": ["CompoundAdvancedSystemDeflectionSubAnalysis"],
        "_2683": ["CompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_2684": ["CompoundCriticalSpeedAnalysis"],
        "_2685": ["CompoundDynamicAnalysis"],
        "_2686": ["CompoundDynamicModelAtAStiffnessAnalysis"],
        "_2687": ["CompoundDynamicModelForHarmonicAnalysis"],
        "_2688": ["CompoundDynamicModelForModalAnalysis"],
        "_2689": ["CompoundDynamicModelForStabilityAnalysis"],
        "_2690": ["CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2691": ["CompoundHarmonicAnalysis"],
        "_2692": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_2693": ["CompoundHarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2694": ["CompoundModalAnalysis"],
        "_2695": ["CompoundModalAnalysisAtASpeed"],
        "_2696": ["CompoundModalAnalysisAtAStiffness"],
        "_2697": ["CompoundModalAnalysisForHarmonicAnalysis"],
        "_2698": ["CompoundMultibodyDynamicsAnalysis"],
        "_2699": ["CompoundPowerFlowAnalysis"],
        "_2700": ["CompoundStabilityAnalysis"],
        "_2701": ["CompoundSteadyStateSynchronousResponseAnalysis"],
        "_2702": ["CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2703": ["CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2704": ["CompoundSystemDeflectionAnalysis"],
        "_2705": ["CompoundTorsionalSystemDeflectionAnalysis"],
        "_2706": ["TESetUpForDynamicAnalysisOptions"],
        "_2707": ["TimeOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "SingleAnalysis",
    "AdvancedSystemDeflectionAnalysis",
    "AdvancedSystemDeflectionSubAnalysis",
    "AdvancedTimeSteppingAnalysisForModulation",
    "CompoundParametricStudyToolAnalysis",
    "CriticalSpeedAnalysis",
    "DynamicAnalysis",
    "DynamicModelAtAStiffnessAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicModelForStabilityAnalysis",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOfSingleExcitationAnalysis",
    "ModalAnalysis",
    "ModalAnalysisAtASpeed",
    "ModalAnalysisAtAStiffness",
    "ModalAnalysisForHarmonicAnalysis",
    "MultibodyDynamicsAnalysis",
    "ParametricStudyToolAnalysis",
    "PowerFlowAnalysis",
    "StabilityAnalysis",
    "SteadyStateSynchronousResponseAnalysis",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
    "SystemDeflectionAnalysis",
    "TorsionalSystemDeflectionAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflectionAnalysis",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffnessAnalysis",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlowAnalysis",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponseAnalysis",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    "CompoundSystemDeflectionAnalysis",
    "CompoundTorsionalSystemDeflectionAnalysis",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
