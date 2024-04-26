"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2708 import AbstractAssemblySystemDeflection
    from ._2709 import AbstractShaftOrHousingSystemDeflection
    from ._2710 import AbstractShaftSystemDeflection
    from ._2711 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2712 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2713 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2714 import AGMAGleasonConicalGearSystemDeflection
    from ._2715 import AssemblySystemDeflection
    from ._2716 import BearingDynamicElementContactPropertyWrapper
    from ._2717 import BearingDynamicElementPropertyWrapper
    from ._2718 import BearingDynamicPostAnalysisResultWrapper
    from ._2719 import BearingDynamicResultsPropertyWrapper
    from ._2720 import BearingDynamicResultsUIWrapper
    from ._2721 import BearingSystemDeflection
    from ._2722 import BeltConnectionSystemDeflection
    from ._2723 import BeltDriveSystemDeflection
    from ._2724 import BevelDifferentialGearMeshSystemDeflection
    from ._2725 import BevelDifferentialGearSetSystemDeflection
    from ._2726 import BevelDifferentialGearSystemDeflection
    from ._2727 import BevelDifferentialPlanetGearSystemDeflection
    from ._2728 import BevelDifferentialSunGearSystemDeflection
    from ._2729 import BevelGearMeshSystemDeflection
    from ._2730 import BevelGearSetSystemDeflection
    from ._2731 import BevelGearSystemDeflection
    from ._2732 import BoltedJointSystemDeflection
    from ._2733 import BoltSystemDeflection
    from ._2734 import ClutchConnectionSystemDeflection
    from ._2735 import ClutchHalfSystemDeflection
    from ._2736 import ClutchSystemDeflection
    from ._2737 import CoaxialConnectionSystemDeflection
    from ._2738 import ComponentSystemDeflection
    from ._2739 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2740 import ConceptCouplingConnectionSystemDeflection
    from ._2741 import ConceptCouplingHalfSystemDeflection
    from ._2742 import ConceptCouplingSystemDeflection
    from ._2743 import ConceptGearMeshSystemDeflection
    from ._2744 import ConceptGearSetSystemDeflection
    from ._2745 import ConceptGearSystemDeflection
    from ._2746 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2747 import ConicalGearMeshSystemDeflection
    from ._2748 import ConicalGearSetSystemDeflection
    from ._2749 import ConicalGearSystemDeflection
    from ._2750 import ConnectionSystemDeflection
    from ._2751 import ConnectorSystemDeflection
    from ._2752 import CouplingConnectionSystemDeflection
    from ._2753 import CouplingHalfSystemDeflection
    from ._2754 import CouplingSystemDeflection
    from ._2755 import CVTBeltConnectionSystemDeflection
    from ._2756 import CVTPulleySystemDeflection
    from ._2757 import CVTSystemDeflection
    from ._2758 import CycloidalAssemblySystemDeflection
    from ._2759 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2760 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2761 import CycloidalDiscSystemDeflection
    from ._2762 import CylindricalGearMeshSystemDeflection
    from ._2763 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2764 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2765 import CylindricalGearSetSystemDeflection
    from ._2766 import CylindricalGearSetSystemDeflectionTimestep
    from ._2767 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2768 import CylindricalGearSystemDeflection
    from ._2769 import CylindricalGearSystemDeflectionTimestep
    from ._2770 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2771 import CylindricalMeshedGearFlankSystemDeflection
    from ._2772 import CylindricalMeshedGearSystemDeflection
    from ._2773 import CylindricalPlanetGearSystemDeflection
    from ._2774 import DatumSystemDeflection
    from ._2775 import ExternalCADModelSystemDeflection
    from ._2776 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2777 import FaceGearMeshSystemDeflection
    from ._2778 import FaceGearSetSystemDeflection
    from ._2779 import FaceGearSystemDeflection
    from ._2780 import FEPartSystemDeflection
    from ._2781 import FlexiblePinAssemblySystemDeflection
    from ._2782 import GearMeshSystemDeflection
    from ._2783 import GearSetSystemDeflection
    from ._2784 import GearSystemDeflection
    from ._2785 import GuideDxfModelSystemDeflection
    from ._2786 import HypoidGearMeshSystemDeflection
    from ._2787 import HypoidGearSetSystemDeflection
    from ._2788 import HypoidGearSystemDeflection
    from ._2789 import InformationForContactAtPointAlongFaceWidth
    from ._2790 import InterMountableComponentConnectionSystemDeflection
    from ._2791 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2792 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2793 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2794 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2795 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2796 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2797 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2798 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2799 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2800 import LoadCaseOverallEfficiencyResult
    from ._2801 import LoadSharingFactorReporter
    from ._2802 import MassDiscSystemDeflection
    from ._2803 import MeasurementComponentSystemDeflection
    from ._2804 import MeshSeparationsAtFaceWidth
    from ._2805 import MountableComponentSystemDeflection
    from ._2806 import ObservedPinStiffnessReporter
    from ._2807 import OilSealSystemDeflection
    from ._2808 import PartSystemDeflection
    from ._2809 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2810 import PartToPartShearCouplingHalfSystemDeflection
    from ._2811 import PartToPartShearCouplingSystemDeflection
    from ._2812 import PlanetaryConnectionSystemDeflection
    from ._2813 import PlanetCarrierSystemDeflection
    from ._2814 import PointLoadSystemDeflection
    from ._2815 import PowerLoadSystemDeflection
    from ._2816 import PulleySystemDeflection
    from ._2817 import RingPinsSystemDeflection
    from ._2818 import RingPinsToDiscConnectionSystemDeflection
    from ._2819 import RingPinToDiscContactReporting
    from ._2820 import RollingRingAssemblySystemDeflection
    from ._2821 import RollingRingConnectionSystemDeflection
    from ._2822 import RollingRingSystemDeflection
    from ._2823 import RootAssemblySystemDeflection
    from ._2824 import ShaftHubConnectionSystemDeflection
    from ._2825 import ShaftSectionEndResultsSystemDeflection
    from ._2826 import ShaftSectionSystemDeflection
    from ._2827 import ShaftSystemDeflection
    from ._2828 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2829 import SpecialisedAssemblySystemDeflection
    from ._2830 import SpiralBevelGearMeshSystemDeflection
    from ._2831 import SpiralBevelGearSetSystemDeflection
    from ._2832 import SpiralBevelGearSystemDeflection
    from ._2833 import SpringDamperConnectionSystemDeflection
    from ._2834 import SpringDamperHalfSystemDeflection
    from ._2835 import SpringDamperSystemDeflection
    from ._2836 import StraightBevelDiffGearMeshSystemDeflection
    from ._2837 import StraightBevelDiffGearSetSystemDeflection
    from ._2838 import StraightBevelDiffGearSystemDeflection
    from ._2839 import StraightBevelGearMeshSystemDeflection
    from ._2840 import StraightBevelGearSetSystemDeflection
    from ._2841 import StraightBevelGearSystemDeflection
    from ._2842 import StraightBevelPlanetGearSystemDeflection
    from ._2843 import StraightBevelSunGearSystemDeflection
    from ._2844 import SynchroniserHalfSystemDeflection
    from ._2845 import SynchroniserPartSystemDeflection
    from ._2846 import SynchroniserSleeveSystemDeflection
    from ._2847 import SynchroniserSystemDeflection
    from ._2848 import SystemDeflection
    from ._2849 import SystemDeflectionDrawStyle
    from ._2850 import SystemDeflectionOptions
    from ._2851 import TorqueConverterConnectionSystemDeflection
    from ._2852 import TorqueConverterPumpSystemDeflection
    from ._2853 import TorqueConverterSystemDeflection
    from ._2854 import TorqueConverterTurbineSystemDeflection
    from ._2855 import TorsionalSystemDeflection
    from ._2856 import TransmissionErrorResult
    from ._2857 import UnbalancedMassSystemDeflection
    from ._2858 import VirtualComponentSystemDeflection
    from ._2859 import WormGearMeshSystemDeflection
    from ._2860 import WormGearSetSystemDeflection
    from ._2861 import WormGearSystemDeflection
    from ._2862 import ZerolBevelGearMeshSystemDeflection
    from ._2863 import ZerolBevelGearSetSystemDeflection
    from ._2864 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        "_2708": ["AbstractAssemblySystemDeflection"],
        "_2709": ["AbstractShaftOrHousingSystemDeflection"],
        "_2710": ["AbstractShaftSystemDeflection"],
        "_2711": ["AbstractShaftToMountableComponentConnectionSystemDeflection"],
        "_2712": ["AGMAGleasonConicalGearMeshSystemDeflection"],
        "_2713": ["AGMAGleasonConicalGearSetSystemDeflection"],
        "_2714": ["AGMAGleasonConicalGearSystemDeflection"],
        "_2715": ["AssemblySystemDeflection"],
        "_2716": ["BearingDynamicElementContactPropertyWrapper"],
        "_2717": ["BearingDynamicElementPropertyWrapper"],
        "_2718": ["BearingDynamicPostAnalysisResultWrapper"],
        "_2719": ["BearingDynamicResultsPropertyWrapper"],
        "_2720": ["BearingDynamicResultsUIWrapper"],
        "_2721": ["BearingSystemDeflection"],
        "_2722": ["BeltConnectionSystemDeflection"],
        "_2723": ["BeltDriveSystemDeflection"],
        "_2724": ["BevelDifferentialGearMeshSystemDeflection"],
        "_2725": ["BevelDifferentialGearSetSystemDeflection"],
        "_2726": ["BevelDifferentialGearSystemDeflection"],
        "_2727": ["BevelDifferentialPlanetGearSystemDeflection"],
        "_2728": ["BevelDifferentialSunGearSystemDeflection"],
        "_2729": ["BevelGearMeshSystemDeflection"],
        "_2730": ["BevelGearSetSystemDeflection"],
        "_2731": ["BevelGearSystemDeflection"],
        "_2732": ["BoltedJointSystemDeflection"],
        "_2733": ["BoltSystemDeflection"],
        "_2734": ["ClutchConnectionSystemDeflection"],
        "_2735": ["ClutchHalfSystemDeflection"],
        "_2736": ["ClutchSystemDeflection"],
        "_2737": ["CoaxialConnectionSystemDeflection"],
        "_2738": ["ComponentSystemDeflection"],
        "_2739": ["ConcentricPartGroupCombinationSystemDeflectionResults"],
        "_2740": ["ConceptCouplingConnectionSystemDeflection"],
        "_2741": ["ConceptCouplingHalfSystemDeflection"],
        "_2742": ["ConceptCouplingSystemDeflection"],
        "_2743": ["ConceptGearMeshSystemDeflection"],
        "_2744": ["ConceptGearSetSystemDeflection"],
        "_2745": ["ConceptGearSystemDeflection"],
        "_2746": ["ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2747": ["ConicalGearMeshSystemDeflection"],
        "_2748": ["ConicalGearSetSystemDeflection"],
        "_2749": ["ConicalGearSystemDeflection"],
        "_2750": ["ConnectionSystemDeflection"],
        "_2751": ["ConnectorSystemDeflection"],
        "_2752": ["CouplingConnectionSystemDeflection"],
        "_2753": ["CouplingHalfSystemDeflection"],
        "_2754": ["CouplingSystemDeflection"],
        "_2755": ["CVTBeltConnectionSystemDeflection"],
        "_2756": ["CVTPulleySystemDeflection"],
        "_2757": ["CVTSystemDeflection"],
        "_2758": ["CycloidalAssemblySystemDeflection"],
        "_2759": ["CycloidalDiscCentralBearingConnectionSystemDeflection"],
        "_2760": ["CycloidalDiscPlanetaryBearingConnectionSystemDeflection"],
        "_2761": ["CycloidalDiscSystemDeflection"],
        "_2762": ["CylindricalGearMeshSystemDeflection"],
        "_2763": ["CylindricalGearMeshSystemDeflectionTimestep"],
        "_2764": ["CylindricalGearMeshSystemDeflectionWithLTCAResults"],
        "_2765": ["CylindricalGearSetSystemDeflection"],
        "_2766": ["CylindricalGearSetSystemDeflectionTimestep"],
        "_2767": ["CylindricalGearSetSystemDeflectionWithLTCAResults"],
        "_2768": ["CylindricalGearSystemDeflection"],
        "_2769": ["CylindricalGearSystemDeflectionTimestep"],
        "_2770": ["CylindricalGearSystemDeflectionWithLTCAResults"],
        "_2771": ["CylindricalMeshedGearFlankSystemDeflection"],
        "_2772": ["CylindricalMeshedGearSystemDeflection"],
        "_2773": ["CylindricalPlanetGearSystemDeflection"],
        "_2774": ["DatumSystemDeflection"],
        "_2775": ["ExternalCADModelSystemDeflection"],
        "_2776": ["FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2777": ["FaceGearMeshSystemDeflection"],
        "_2778": ["FaceGearSetSystemDeflection"],
        "_2779": ["FaceGearSystemDeflection"],
        "_2780": ["FEPartSystemDeflection"],
        "_2781": ["FlexiblePinAssemblySystemDeflection"],
        "_2782": ["GearMeshSystemDeflection"],
        "_2783": ["GearSetSystemDeflection"],
        "_2784": ["GearSystemDeflection"],
        "_2785": ["GuideDxfModelSystemDeflection"],
        "_2786": ["HypoidGearMeshSystemDeflection"],
        "_2787": ["HypoidGearSetSystemDeflection"],
        "_2788": ["HypoidGearSystemDeflection"],
        "_2789": ["InformationForContactAtPointAlongFaceWidth"],
        "_2790": ["InterMountableComponentConnectionSystemDeflection"],
        "_2791": ["KlingelnbergCycloPalloidConicalGearMeshSystemDeflection"],
        "_2792": ["KlingelnbergCycloPalloidConicalGearSetSystemDeflection"],
        "_2793": ["KlingelnbergCycloPalloidConicalGearSystemDeflection"],
        "_2794": ["KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection"],
        "_2795": ["KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"],
        "_2796": ["KlingelnbergCycloPalloidHypoidGearSystemDeflection"],
        "_2797": ["KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"],
        "_2798": ["KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection"],
        "_2799": ["KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"],
        "_2800": ["LoadCaseOverallEfficiencyResult"],
        "_2801": ["LoadSharingFactorReporter"],
        "_2802": ["MassDiscSystemDeflection"],
        "_2803": ["MeasurementComponentSystemDeflection"],
        "_2804": ["MeshSeparationsAtFaceWidth"],
        "_2805": ["MountableComponentSystemDeflection"],
        "_2806": ["ObservedPinStiffnessReporter"],
        "_2807": ["OilSealSystemDeflection"],
        "_2808": ["PartSystemDeflection"],
        "_2809": ["PartToPartShearCouplingConnectionSystemDeflection"],
        "_2810": ["PartToPartShearCouplingHalfSystemDeflection"],
        "_2811": ["PartToPartShearCouplingSystemDeflection"],
        "_2812": ["PlanetaryConnectionSystemDeflection"],
        "_2813": ["PlanetCarrierSystemDeflection"],
        "_2814": ["PointLoadSystemDeflection"],
        "_2815": ["PowerLoadSystemDeflection"],
        "_2816": ["PulleySystemDeflection"],
        "_2817": ["RingPinsSystemDeflection"],
        "_2818": ["RingPinsToDiscConnectionSystemDeflection"],
        "_2819": ["RingPinToDiscContactReporting"],
        "_2820": ["RollingRingAssemblySystemDeflection"],
        "_2821": ["RollingRingConnectionSystemDeflection"],
        "_2822": ["RollingRingSystemDeflection"],
        "_2823": ["RootAssemblySystemDeflection"],
        "_2824": ["ShaftHubConnectionSystemDeflection"],
        "_2825": ["ShaftSectionEndResultsSystemDeflection"],
        "_2826": ["ShaftSectionSystemDeflection"],
        "_2827": ["ShaftSystemDeflection"],
        "_2828": ["ShaftToMountableComponentConnectionSystemDeflection"],
        "_2829": ["SpecialisedAssemblySystemDeflection"],
        "_2830": ["SpiralBevelGearMeshSystemDeflection"],
        "_2831": ["SpiralBevelGearSetSystemDeflection"],
        "_2832": ["SpiralBevelGearSystemDeflection"],
        "_2833": ["SpringDamperConnectionSystemDeflection"],
        "_2834": ["SpringDamperHalfSystemDeflection"],
        "_2835": ["SpringDamperSystemDeflection"],
        "_2836": ["StraightBevelDiffGearMeshSystemDeflection"],
        "_2837": ["StraightBevelDiffGearSetSystemDeflection"],
        "_2838": ["StraightBevelDiffGearSystemDeflection"],
        "_2839": ["StraightBevelGearMeshSystemDeflection"],
        "_2840": ["StraightBevelGearSetSystemDeflection"],
        "_2841": ["StraightBevelGearSystemDeflection"],
        "_2842": ["StraightBevelPlanetGearSystemDeflection"],
        "_2843": ["StraightBevelSunGearSystemDeflection"],
        "_2844": ["SynchroniserHalfSystemDeflection"],
        "_2845": ["SynchroniserPartSystemDeflection"],
        "_2846": ["SynchroniserSleeveSystemDeflection"],
        "_2847": ["SynchroniserSystemDeflection"],
        "_2848": ["SystemDeflection"],
        "_2849": ["SystemDeflectionDrawStyle"],
        "_2850": ["SystemDeflectionOptions"],
        "_2851": ["TorqueConverterConnectionSystemDeflection"],
        "_2852": ["TorqueConverterPumpSystemDeflection"],
        "_2853": ["TorqueConverterSystemDeflection"],
        "_2854": ["TorqueConverterTurbineSystemDeflection"],
        "_2855": ["TorsionalSystemDeflection"],
        "_2856": ["TransmissionErrorResult"],
        "_2857": ["UnbalancedMassSystemDeflection"],
        "_2858": ["VirtualComponentSystemDeflection"],
        "_2859": ["WormGearMeshSystemDeflection"],
        "_2860": ["WormGearSetSystemDeflection"],
        "_2861": ["WormGearSystemDeflection"],
        "_2862": ["ZerolBevelGearMeshSystemDeflection"],
        "_2863": ["ZerolBevelGearSetSystemDeflection"],
        "_2864": ["ZerolBevelGearSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySystemDeflection",
    "AbstractShaftOrHousingSystemDeflection",
    "AbstractShaftSystemDeflection",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
    "AGMAGleasonConicalGearMeshSystemDeflection",
    "AGMAGleasonConicalGearSetSystemDeflection",
    "AGMAGleasonConicalGearSystemDeflection",
    "AssemblySystemDeflection",
    "BearingDynamicElementContactPropertyWrapper",
    "BearingDynamicElementPropertyWrapper",
    "BearingDynamicPostAnalysisResultWrapper",
    "BearingDynamicResultsPropertyWrapper",
    "BearingDynamicResultsUIWrapper",
    "BearingSystemDeflection",
    "BeltConnectionSystemDeflection",
    "BeltDriveSystemDeflection",
    "BevelDifferentialGearMeshSystemDeflection",
    "BevelDifferentialGearSetSystemDeflection",
    "BevelDifferentialGearSystemDeflection",
    "BevelDifferentialPlanetGearSystemDeflection",
    "BevelDifferentialSunGearSystemDeflection",
    "BevelGearMeshSystemDeflection",
    "BevelGearSetSystemDeflection",
    "BevelGearSystemDeflection",
    "BoltedJointSystemDeflection",
    "BoltSystemDeflection",
    "ClutchConnectionSystemDeflection",
    "ClutchHalfSystemDeflection",
    "ClutchSystemDeflection",
    "CoaxialConnectionSystemDeflection",
    "ComponentSystemDeflection",
    "ConcentricPartGroupCombinationSystemDeflectionResults",
    "ConceptCouplingConnectionSystemDeflection",
    "ConceptCouplingHalfSystemDeflection",
    "ConceptCouplingSystemDeflection",
    "ConceptGearMeshSystemDeflection",
    "ConceptGearSetSystemDeflection",
    "ConceptGearSystemDeflection",
    "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "ConicalGearMeshSystemDeflection",
    "ConicalGearSetSystemDeflection",
    "ConicalGearSystemDeflection",
    "ConnectionSystemDeflection",
    "ConnectorSystemDeflection",
    "CouplingConnectionSystemDeflection",
    "CouplingHalfSystemDeflection",
    "CouplingSystemDeflection",
    "CVTBeltConnectionSystemDeflection",
    "CVTPulleySystemDeflection",
    "CVTSystemDeflection",
    "CycloidalAssemblySystemDeflection",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    "CycloidalDiscSystemDeflection",
    "CylindricalGearMeshSystemDeflection",
    "CylindricalGearMeshSystemDeflectionTimestep",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
    "CylindricalGearSetSystemDeflection",
    "CylindricalGearSetSystemDeflectionTimestep",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
    "CylindricalGearSystemDeflection",
    "CylindricalGearSystemDeflectionTimestep",
    "CylindricalGearSystemDeflectionWithLTCAResults",
    "CylindricalMeshedGearFlankSystemDeflection",
    "CylindricalMeshedGearSystemDeflection",
    "CylindricalPlanetGearSystemDeflection",
    "DatumSystemDeflection",
    "ExternalCADModelSystemDeflection",
    "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "FaceGearMeshSystemDeflection",
    "FaceGearSetSystemDeflection",
    "FaceGearSystemDeflection",
    "FEPartSystemDeflection",
    "FlexiblePinAssemblySystemDeflection",
    "GearMeshSystemDeflection",
    "GearSetSystemDeflection",
    "GearSystemDeflection",
    "GuideDxfModelSystemDeflection",
    "HypoidGearMeshSystemDeflection",
    "HypoidGearSetSystemDeflection",
    "HypoidGearSystemDeflection",
    "InformationForContactAtPointAlongFaceWidth",
    "InterMountableComponentConnectionSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    "LoadCaseOverallEfficiencyResult",
    "LoadSharingFactorReporter",
    "MassDiscSystemDeflection",
    "MeasurementComponentSystemDeflection",
    "MeshSeparationsAtFaceWidth",
    "MountableComponentSystemDeflection",
    "ObservedPinStiffnessReporter",
    "OilSealSystemDeflection",
    "PartSystemDeflection",
    "PartToPartShearCouplingConnectionSystemDeflection",
    "PartToPartShearCouplingHalfSystemDeflection",
    "PartToPartShearCouplingSystemDeflection",
    "PlanetaryConnectionSystemDeflection",
    "PlanetCarrierSystemDeflection",
    "PointLoadSystemDeflection",
    "PowerLoadSystemDeflection",
    "PulleySystemDeflection",
    "RingPinsSystemDeflection",
    "RingPinsToDiscConnectionSystemDeflection",
    "RingPinToDiscContactReporting",
    "RollingRingAssemblySystemDeflection",
    "RollingRingConnectionSystemDeflection",
    "RollingRingSystemDeflection",
    "RootAssemblySystemDeflection",
    "ShaftHubConnectionSystemDeflection",
    "ShaftSectionEndResultsSystemDeflection",
    "ShaftSectionSystemDeflection",
    "ShaftSystemDeflection",
    "ShaftToMountableComponentConnectionSystemDeflection",
    "SpecialisedAssemblySystemDeflection",
    "SpiralBevelGearMeshSystemDeflection",
    "SpiralBevelGearSetSystemDeflection",
    "SpiralBevelGearSystemDeflection",
    "SpringDamperConnectionSystemDeflection",
    "SpringDamperHalfSystemDeflection",
    "SpringDamperSystemDeflection",
    "StraightBevelDiffGearMeshSystemDeflection",
    "StraightBevelDiffGearSetSystemDeflection",
    "StraightBevelDiffGearSystemDeflection",
    "StraightBevelGearMeshSystemDeflection",
    "StraightBevelGearSetSystemDeflection",
    "StraightBevelGearSystemDeflection",
    "StraightBevelPlanetGearSystemDeflection",
    "StraightBevelSunGearSystemDeflection",
    "SynchroniserHalfSystemDeflection",
    "SynchroniserPartSystemDeflection",
    "SynchroniserSleeveSystemDeflection",
    "SynchroniserSystemDeflection",
    "SystemDeflection",
    "SystemDeflectionDrawStyle",
    "SystemDeflectionOptions",
    "TorqueConverterConnectionSystemDeflection",
    "TorqueConverterPumpSystemDeflection",
    "TorqueConverterSystemDeflection",
    "TorqueConverterTurbineSystemDeflection",
    "TorsionalSystemDeflection",
    "TransmissionErrorResult",
    "UnbalancedMassSystemDeflection",
    "VirtualComponentSystemDeflection",
    "WormGearMeshSystemDeflection",
    "WormGearSetSystemDeflection",
    "WormGearSystemDeflection",
    "ZerolBevelGearMeshSystemDeflection",
    "ZerolBevelGearSetSystemDeflection",
    "ZerolBevelGearSystemDeflection",
)
