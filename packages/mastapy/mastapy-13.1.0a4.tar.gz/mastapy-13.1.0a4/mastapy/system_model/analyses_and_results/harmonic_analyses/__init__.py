"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5704 import AbstractAssemblyHarmonicAnalysis
    from ._5705 import AbstractPeriodicExcitationDetail
    from ._5706 import AbstractShaftHarmonicAnalysis
    from ._5707 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5708 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5709 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5710 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5711 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5712 import AssemblyHarmonicAnalysis
    from ._5713 import BearingHarmonicAnalysis
    from ._5714 import BeltConnectionHarmonicAnalysis
    from ._5715 import BeltDriveHarmonicAnalysis
    from ._5716 import BevelDifferentialGearHarmonicAnalysis
    from ._5717 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5718 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5719 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5720 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5721 import BevelGearHarmonicAnalysis
    from ._5722 import BevelGearMeshHarmonicAnalysis
    from ._5723 import BevelGearSetHarmonicAnalysis
    from ._5724 import BoltedJointHarmonicAnalysis
    from ._5725 import BoltHarmonicAnalysis
    from ._5726 import ClutchConnectionHarmonicAnalysis
    from ._5727 import ClutchHalfHarmonicAnalysis
    from ._5728 import ClutchHarmonicAnalysis
    from ._5729 import CoaxialConnectionHarmonicAnalysis
    from ._5730 import ComplianceAndForceData
    from ._5731 import ComponentHarmonicAnalysis
    from ._5732 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5733 import ConceptCouplingHalfHarmonicAnalysis
    from ._5734 import ConceptCouplingHarmonicAnalysis
    from ._5735 import ConceptGearHarmonicAnalysis
    from ._5736 import ConceptGearMeshHarmonicAnalysis
    from ._5737 import ConceptGearSetHarmonicAnalysis
    from ._5738 import ConicalGearHarmonicAnalysis
    from ._5739 import ConicalGearMeshHarmonicAnalysis
    from ._5740 import ConicalGearSetHarmonicAnalysis
    from ._5741 import ConnectionHarmonicAnalysis
    from ._5742 import ConnectorHarmonicAnalysis
    from ._5743 import CouplingConnectionHarmonicAnalysis
    from ._5744 import CouplingHalfHarmonicAnalysis
    from ._5745 import CouplingHarmonicAnalysis
    from ._5746 import CVTBeltConnectionHarmonicAnalysis
    from ._5747 import CVTHarmonicAnalysis
    from ._5748 import CVTPulleyHarmonicAnalysis
    from ._5749 import CycloidalAssemblyHarmonicAnalysis
    from ._5750 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5751 import CycloidalDiscHarmonicAnalysis
    from ._5752 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5753 import CylindricalGearHarmonicAnalysis
    from ._5754 import CylindricalGearMeshHarmonicAnalysis
    from ._5755 import CylindricalGearSetHarmonicAnalysis
    from ._5756 import CylindricalPlanetGearHarmonicAnalysis
    from ._5757 import DatumHarmonicAnalysis
    from ._5758 import DynamicModelForHarmonicAnalysis
    from ._5759 import ElectricMachinePeriodicExcitationDetail
    from ._5760 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5761 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5762 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5763 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5764 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5765 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5766 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5767 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5768 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5769 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5770 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5771 import ExportOutputType
    from ._5772 import ExternalCADModelHarmonicAnalysis
    from ._5773 import FaceGearHarmonicAnalysis
    from ._5774 import FaceGearMeshHarmonicAnalysis
    from ._5775 import FaceGearSetHarmonicAnalysis
    from ._5776 import FEPartHarmonicAnalysis
    from ._5777 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5778 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5779 import GearHarmonicAnalysis
    from ._5780 import GearMeshExcitationDetail
    from ._5781 import GearMeshHarmonicAnalysis
    from ._5782 import GearMeshMisalignmentExcitationDetail
    from ._5783 import GearMeshTEExcitationDetail
    from ._5784 import GearSetHarmonicAnalysis
    from ._5785 import GeneralPeriodicExcitationDetail
    from ._5786 import GuideDxfModelHarmonicAnalysis
    from ._5787 import HarmonicAnalysis
    from ._5788 import HarmonicAnalysisDrawStyle
    from ._5789 import HarmonicAnalysisExportOptions
    from ._5790 import HarmonicAnalysisFEExportOptions
    from ._5791 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5792 import HarmonicAnalysisOptions
    from ._5793 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5794 import HarmonicAnalysisShaftExportOptions
    from ._5795 import HarmonicAnalysisTorqueInputType
    from ._5796 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5797 import HypoidGearHarmonicAnalysis
    from ._5798 import HypoidGearMeshHarmonicAnalysis
    from ._5799 import HypoidGearSetHarmonicAnalysis
    from ._5800 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5801 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5802 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5803 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5804 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5805 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5806 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5807 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5808 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5809 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5810 import MassDiscHarmonicAnalysis
    from ._5811 import MeasurementComponentHarmonicAnalysis
    from ._5812 import MountableComponentHarmonicAnalysis
    from ._5813 import OilSealHarmonicAnalysis
    from ._5814 import PartHarmonicAnalysis
    from ._5815 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5816 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5817 import PartToPartShearCouplingHarmonicAnalysis
    from ._5818 import PeriodicExcitationWithReferenceShaft
    from ._5819 import PlanetaryConnectionHarmonicAnalysis
    from ._5820 import PlanetaryGearSetHarmonicAnalysis
    from ._5821 import PlanetCarrierHarmonicAnalysis
    from ._5822 import PointLoadHarmonicAnalysis
    from ._5823 import PowerLoadHarmonicAnalysis
    from ._5824 import PulleyHarmonicAnalysis
    from ._5825 import ResponseCacheLevel
    from ._5826 import RingPinsHarmonicAnalysis
    from ._5827 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5828 import RollingRingAssemblyHarmonicAnalysis
    from ._5829 import RollingRingConnectionHarmonicAnalysis
    from ._5830 import RollingRingHarmonicAnalysis
    from ._5831 import RootAssemblyHarmonicAnalysis
    from ._5832 import ShaftHarmonicAnalysis
    from ._5833 import ShaftHubConnectionHarmonicAnalysis
    from ._5834 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5835 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5836 import SpecialisedAssemblyHarmonicAnalysis
    from ._5837 import SpeedOptionsForHarmonicAnalysisResults
    from ._5838 import SpiralBevelGearHarmonicAnalysis
    from ._5839 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5840 import SpiralBevelGearSetHarmonicAnalysis
    from ._5841 import SpringDamperConnectionHarmonicAnalysis
    from ._5842 import SpringDamperHalfHarmonicAnalysis
    from ._5843 import SpringDamperHarmonicAnalysis
    from ._5844 import StiffnessOptionsForHarmonicAnalysis
    from ._5845 import StraightBevelDiffGearHarmonicAnalysis
    from ._5846 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5847 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5848 import StraightBevelGearHarmonicAnalysis
    from ._5849 import StraightBevelGearMeshHarmonicAnalysis
    from ._5850 import StraightBevelGearSetHarmonicAnalysis
    from ._5851 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5852 import StraightBevelSunGearHarmonicAnalysis
    from ._5853 import SynchroniserHalfHarmonicAnalysis
    from ._5854 import SynchroniserHarmonicAnalysis
    from ._5855 import SynchroniserPartHarmonicAnalysis
    from ._5856 import SynchroniserSleeveHarmonicAnalysis
    from ._5857 import TorqueConverterConnectionHarmonicAnalysis
    from ._5858 import TorqueConverterHarmonicAnalysis
    from ._5859 import TorqueConverterPumpHarmonicAnalysis
    from ._5860 import TorqueConverterTurbineHarmonicAnalysis
    from ._5861 import UnbalancedMassExcitationDetail
    from ._5862 import UnbalancedMassHarmonicAnalysis
    from ._5863 import VirtualComponentHarmonicAnalysis
    from ._5864 import WormGearHarmonicAnalysis
    from ._5865 import WormGearMeshHarmonicAnalysis
    from ._5866 import WormGearSetHarmonicAnalysis
    from ._5867 import ZerolBevelGearHarmonicAnalysis
    from ._5868 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5869 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5704": ["AbstractAssemblyHarmonicAnalysis"],
        "_5705": ["AbstractPeriodicExcitationDetail"],
        "_5706": ["AbstractShaftHarmonicAnalysis"],
        "_5707": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5708": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5709": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5710": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5711": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5712": ["AssemblyHarmonicAnalysis"],
        "_5713": ["BearingHarmonicAnalysis"],
        "_5714": ["BeltConnectionHarmonicAnalysis"],
        "_5715": ["BeltDriveHarmonicAnalysis"],
        "_5716": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5717": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5718": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5719": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5720": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5721": ["BevelGearHarmonicAnalysis"],
        "_5722": ["BevelGearMeshHarmonicAnalysis"],
        "_5723": ["BevelGearSetHarmonicAnalysis"],
        "_5724": ["BoltedJointHarmonicAnalysis"],
        "_5725": ["BoltHarmonicAnalysis"],
        "_5726": ["ClutchConnectionHarmonicAnalysis"],
        "_5727": ["ClutchHalfHarmonicAnalysis"],
        "_5728": ["ClutchHarmonicAnalysis"],
        "_5729": ["CoaxialConnectionHarmonicAnalysis"],
        "_5730": ["ComplianceAndForceData"],
        "_5731": ["ComponentHarmonicAnalysis"],
        "_5732": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5733": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5734": ["ConceptCouplingHarmonicAnalysis"],
        "_5735": ["ConceptGearHarmonicAnalysis"],
        "_5736": ["ConceptGearMeshHarmonicAnalysis"],
        "_5737": ["ConceptGearSetHarmonicAnalysis"],
        "_5738": ["ConicalGearHarmonicAnalysis"],
        "_5739": ["ConicalGearMeshHarmonicAnalysis"],
        "_5740": ["ConicalGearSetHarmonicAnalysis"],
        "_5741": ["ConnectionHarmonicAnalysis"],
        "_5742": ["ConnectorHarmonicAnalysis"],
        "_5743": ["CouplingConnectionHarmonicAnalysis"],
        "_5744": ["CouplingHalfHarmonicAnalysis"],
        "_5745": ["CouplingHarmonicAnalysis"],
        "_5746": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5747": ["CVTHarmonicAnalysis"],
        "_5748": ["CVTPulleyHarmonicAnalysis"],
        "_5749": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5750": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5751": ["CycloidalDiscHarmonicAnalysis"],
        "_5752": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5753": ["CylindricalGearHarmonicAnalysis"],
        "_5754": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5755": ["CylindricalGearSetHarmonicAnalysis"],
        "_5756": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5757": ["DatumHarmonicAnalysis"],
        "_5758": ["DynamicModelForHarmonicAnalysis"],
        "_5759": ["ElectricMachinePeriodicExcitationDetail"],
        "_5760": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5761": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5762": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5763": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5764": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5765": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5766": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5767": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5768": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5769": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5770": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5771": ["ExportOutputType"],
        "_5772": ["ExternalCADModelHarmonicAnalysis"],
        "_5773": ["FaceGearHarmonicAnalysis"],
        "_5774": ["FaceGearMeshHarmonicAnalysis"],
        "_5775": ["FaceGearSetHarmonicAnalysis"],
        "_5776": ["FEPartHarmonicAnalysis"],
        "_5777": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5778": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5779": ["GearHarmonicAnalysis"],
        "_5780": ["GearMeshExcitationDetail"],
        "_5781": ["GearMeshHarmonicAnalysis"],
        "_5782": ["GearMeshMisalignmentExcitationDetail"],
        "_5783": ["GearMeshTEExcitationDetail"],
        "_5784": ["GearSetHarmonicAnalysis"],
        "_5785": ["GeneralPeriodicExcitationDetail"],
        "_5786": ["GuideDxfModelHarmonicAnalysis"],
        "_5787": ["HarmonicAnalysis"],
        "_5788": ["HarmonicAnalysisDrawStyle"],
        "_5789": ["HarmonicAnalysisExportOptions"],
        "_5790": ["HarmonicAnalysisFEExportOptions"],
        "_5791": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5792": ["HarmonicAnalysisOptions"],
        "_5793": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5794": ["HarmonicAnalysisShaftExportOptions"],
        "_5795": ["HarmonicAnalysisTorqueInputType"],
        "_5796": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5797": ["HypoidGearHarmonicAnalysis"],
        "_5798": ["HypoidGearMeshHarmonicAnalysis"],
        "_5799": ["HypoidGearSetHarmonicAnalysis"],
        "_5800": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5801": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5802": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5803": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5804": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5805": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5806": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5807": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5808": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5809": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5810": ["MassDiscHarmonicAnalysis"],
        "_5811": ["MeasurementComponentHarmonicAnalysis"],
        "_5812": ["MountableComponentHarmonicAnalysis"],
        "_5813": ["OilSealHarmonicAnalysis"],
        "_5814": ["PartHarmonicAnalysis"],
        "_5815": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5816": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5817": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5818": ["PeriodicExcitationWithReferenceShaft"],
        "_5819": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5820": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5821": ["PlanetCarrierHarmonicAnalysis"],
        "_5822": ["PointLoadHarmonicAnalysis"],
        "_5823": ["PowerLoadHarmonicAnalysis"],
        "_5824": ["PulleyHarmonicAnalysis"],
        "_5825": ["ResponseCacheLevel"],
        "_5826": ["RingPinsHarmonicAnalysis"],
        "_5827": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5828": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5829": ["RollingRingConnectionHarmonicAnalysis"],
        "_5830": ["RollingRingHarmonicAnalysis"],
        "_5831": ["RootAssemblyHarmonicAnalysis"],
        "_5832": ["ShaftHarmonicAnalysis"],
        "_5833": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5834": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5835": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5836": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5837": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5838": ["SpiralBevelGearHarmonicAnalysis"],
        "_5839": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5840": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5841": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5842": ["SpringDamperHalfHarmonicAnalysis"],
        "_5843": ["SpringDamperHarmonicAnalysis"],
        "_5844": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5845": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5846": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5847": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5848": ["StraightBevelGearHarmonicAnalysis"],
        "_5849": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5850": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5851": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5852": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5853": ["SynchroniserHalfHarmonicAnalysis"],
        "_5854": ["SynchroniserHarmonicAnalysis"],
        "_5855": ["SynchroniserPartHarmonicAnalysis"],
        "_5856": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5857": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5858": ["TorqueConverterHarmonicAnalysis"],
        "_5859": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5860": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5861": ["UnbalancedMassExcitationDetail"],
        "_5862": ["UnbalancedMassHarmonicAnalysis"],
        "_5863": ["VirtualComponentHarmonicAnalysis"],
        "_5864": ["WormGearHarmonicAnalysis"],
        "_5865": ["WormGearMeshHarmonicAnalysis"],
        "_5866": ["WormGearSetHarmonicAnalysis"],
        "_5867": ["ZerolBevelGearHarmonicAnalysis"],
        "_5868": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5869": ["ZerolBevelGearSetHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyHarmonicAnalysis",
    "AbstractPeriodicExcitationDetail",
    "AbstractShaftHarmonicAnalysis",
    "AbstractShaftOrHousingHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    "AGMAGleasonConicalGearHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
    "AssemblyHarmonicAnalysis",
    "BearingHarmonicAnalysis",
    "BeltConnectionHarmonicAnalysis",
    "BeltDriveHarmonicAnalysis",
    "BevelDifferentialGearHarmonicAnalysis",
    "BevelDifferentialGearMeshHarmonicAnalysis",
    "BevelDifferentialGearSetHarmonicAnalysis",
    "BevelDifferentialPlanetGearHarmonicAnalysis",
    "BevelDifferentialSunGearHarmonicAnalysis",
    "BevelGearHarmonicAnalysis",
    "BevelGearMeshHarmonicAnalysis",
    "BevelGearSetHarmonicAnalysis",
    "BoltedJointHarmonicAnalysis",
    "BoltHarmonicAnalysis",
    "ClutchConnectionHarmonicAnalysis",
    "ClutchHalfHarmonicAnalysis",
    "ClutchHarmonicAnalysis",
    "CoaxialConnectionHarmonicAnalysis",
    "ComplianceAndForceData",
    "ComponentHarmonicAnalysis",
    "ConceptCouplingConnectionHarmonicAnalysis",
    "ConceptCouplingHalfHarmonicAnalysis",
    "ConceptCouplingHarmonicAnalysis",
    "ConceptGearHarmonicAnalysis",
    "ConceptGearMeshHarmonicAnalysis",
    "ConceptGearSetHarmonicAnalysis",
    "ConicalGearHarmonicAnalysis",
    "ConicalGearMeshHarmonicAnalysis",
    "ConicalGearSetHarmonicAnalysis",
    "ConnectionHarmonicAnalysis",
    "ConnectorHarmonicAnalysis",
    "CouplingConnectionHarmonicAnalysis",
    "CouplingHalfHarmonicAnalysis",
    "CouplingHarmonicAnalysis",
    "CVTBeltConnectionHarmonicAnalysis",
    "CVTHarmonicAnalysis",
    "CVTPulleyHarmonicAnalysis",
    "CycloidalAssemblyHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
    "CycloidalDiscHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    "CylindricalGearHarmonicAnalysis",
    "CylindricalGearMeshHarmonicAnalysis",
    "CylindricalGearSetHarmonicAnalysis",
    "CylindricalPlanetGearHarmonicAnalysis",
    "DatumHarmonicAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "ElectricMachinePeriodicExcitationDetail",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
    "ElectricMachineRotorXMomentPeriodicExcitationDetail",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
    "ElectricMachineStatorToothLoadsExcitationDetail",
    "ElectricMachineStatorToothMomentsExcitationDetail",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
    "ExportOutputType",
    "ExternalCADModelHarmonicAnalysis",
    "FaceGearHarmonicAnalysis",
    "FaceGearMeshHarmonicAnalysis",
    "FaceGearSetHarmonicAnalysis",
    "FEPartHarmonicAnalysis",
    "FlexiblePinAssemblyHarmonicAnalysis",
    "FrequencyOptionsForHarmonicAnalysisResults",
    "GearHarmonicAnalysis",
    "GearMeshExcitationDetail",
    "GearMeshHarmonicAnalysis",
    "GearMeshMisalignmentExcitationDetail",
    "GearMeshTEExcitationDetail",
    "GearSetHarmonicAnalysis",
    "GeneralPeriodicExcitationDetail",
    "GuideDxfModelHarmonicAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisDrawStyle",
    "HarmonicAnalysisExportOptions",
    "HarmonicAnalysisFEExportOptions",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptions",
    "HarmonicAnalysisRootAssemblyExportOptions",
    "HarmonicAnalysisShaftExportOptions",
    "HarmonicAnalysisTorqueInputType",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
    "HypoidGearHarmonicAnalysis",
    "HypoidGearMeshHarmonicAnalysis",
    "HypoidGearSetHarmonicAnalysis",
    "InterMountableComponentConnectionHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    "MassDiscHarmonicAnalysis",
    "MeasurementComponentHarmonicAnalysis",
    "MountableComponentHarmonicAnalysis",
    "OilSealHarmonicAnalysis",
    "PartHarmonicAnalysis",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
    "PartToPartShearCouplingHarmonicAnalysis",
    "PeriodicExcitationWithReferenceShaft",
    "PlanetaryConnectionHarmonicAnalysis",
    "PlanetaryGearSetHarmonicAnalysis",
    "PlanetCarrierHarmonicAnalysis",
    "PointLoadHarmonicAnalysis",
    "PowerLoadHarmonicAnalysis",
    "PulleyHarmonicAnalysis",
    "ResponseCacheLevel",
    "RingPinsHarmonicAnalysis",
    "RingPinsToDiscConnectionHarmonicAnalysis",
    "RollingRingAssemblyHarmonicAnalysis",
    "RollingRingConnectionHarmonicAnalysis",
    "RollingRingHarmonicAnalysis",
    "RootAssemblyHarmonicAnalysis",
    "ShaftHarmonicAnalysis",
    "ShaftHubConnectionHarmonicAnalysis",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
    "SingleNodePeriodicExcitationWithReferenceShaft",
    "SpecialisedAssemblyHarmonicAnalysis",
    "SpeedOptionsForHarmonicAnalysisResults",
    "SpiralBevelGearHarmonicAnalysis",
    "SpiralBevelGearMeshHarmonicAnalysis",
    "SpiralBevelGearSetHarmonicAnalysis",
    "SpringDamperConnectionHarmonicAnalysis",
    "SpringDamperHalfHarmonicAnalysis",
    "SpringDamperHarmonicAnalysis",
    "StiffnessOptionsForHarmonicAnalysis",
    "StraightBevelDiffGearHarmonicAnalysis",
    "StraightBevelDiffGearMeshHarmonicAnalysis",
    "StraightBevelDiffGearSetHarmonicAnalysis",
    "StraightBevelGearHarmonicAnalysis",
    "StraightBevelGearMeshHarmonicAnalysis",
    "StraightBevelGearSetHarmonicAnalysis",
    "StraightBevelPlanetGearHarmonicAnalysis",
    "StraightBevelSunGearHarmonicAnalysis",
    "SynchroniserHalfHarmonicAnalysis",
    "SynchroniserHarmonicAnalysis",
    "SynchroniserPartHarmonicAnalysis",
    "SynchroniserSleeveHarmonicAnalysis",
    "TorqueConverterConnectionHarmonicAnalysis",
    "TorqueConverterHarmonicAnalysis",
    "TorqueConverterPumpHarmonicAnalysis",
    "TorqueConverterTurbineHarmonicAnalysis",
    "UnbalancedMassExcitationDetail",
    "UnbalancedMassHarmonicAnalysis",
    "VirtualComponentHarmonicAnalysis",
    "WormGearHarmonicAnalysis",
    "WormGearMeshHarmonicAnalysis",
    "WormGearSetHarmonicAnalysis",
    "ZerolBevelGearHarmonicAnalysis",
    "ZerolBevelGearMeshHarmonicAnalysis",
    "ZerolBevelGearSetHarmonicAnalysis",
)
