"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4751 import AbstractAssemblyCompoundModalAnalysis
    from ._4752 import AbstractShaftCompoundModalAnalysis
    from ._4753 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4754 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4755 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4756 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4757 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4758 import AssemblyCompoundModalAnalysis
    from ._4759 import BearingCompoundModalAnalysis
    from ._4760 import BeltConnectionCompoundModalAnalysis
    from ._4761 import BeltDriveCompoundModalAnalysis
    from ._4762 import BevelDifferentialGearCompoundModalAnalysis
    from ._4763 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4764 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4765 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4766 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4767 import BevelGearCompoundModalAnalysis
    from ._4768 import BevelGearMeshCompoundModalAnalysis
    from ._4769 import BevelGearSetCompoundModalAnalysis
    from ._4770 import BoltCompoundModalAnalysis
    from ._4771 import BoltedJointCompoundModalAnalysis
    from ._4772 import ClutchCompoundModalAnalysis
    from ._4773 import ClutchConnectionCompoundModalAnalysis
    from ._4774 import ClutchHalfCompoundModalAnalysis
    from ._4775 import CoaxialConnectionCompoundModalAnalysis
    from ._4776 import ComponentCompoundModalAnalysis
    from ._4777 import ConceptCouplingCompoundModalAnalysis
    from ._4778 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4779 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4780 import ConceptGearCompoundModalAnalysis
    from ._4781 import ConceptGearMeshCompoundModalAnalysis
    from ._4782 import ConceptGearSetCompoundModalAnalysis
    from ._4783 import ConicalGearCompoundModalAnalysis
    from ._4784 import ConicalGearMeshCompoundModalAnalysis
    from ._4785 import ConicalGearSetCompoundModalAnalysis
    from ._4786 import ConnectionCompoundModalAnalysis
    from ._4787 import ConnectorCompoundModalAnalysis
    from ._4788 import CouplingCompoundModalAnalysis
    from ._4789 import CouplingConnectionCompoundModalAnalysis
    from ._4790 import CouplingHalfCompoundModalAnalysis
    from ._4791 import CVTBeltConnectionCompoundModalAnalysis
    from ._4792 import CVTCompoundModalAnalysis
    from ._4793 import CVTPulleyCompoundModalAnalysis
    from ._4794 import CycloidalAssemblyCompoundModalAnalysis
    from ._4795 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4796 import CycloidalDiscCompoundModalAnalysis
    from ._4797 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4798 import CylindricalGearCompoundModalAnalysis
    from ._4799 import CylindricalGearMeshCompoundModalAnalysis
    from ._4800 import CylindricalGearSetCompoundModalAnalysis
    from ._4801 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4802 import DatumCompoundModalAnalysis
    from ._4803 import ExternalCADModelCompoundModalAnalysis
    from ._4804 import FaceGearCompoundModalAnalysis
    from ._4805 import FaceGearMeshCompoundModalAnalysis
    from ._4806 import FaceGearSetCompoundModalAnalysis
    from ._4807 import FEPartCompoundModalAnalysis
    from ._4808 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4809 import GearCompoundModalAnalysis
    from ._4810 import GearMeshCompoundModalAnalysis
    from ._4811 import GearSetCompoundModalAnalysis
    from ._4812 import GuideDxfModelCompoundModalAnalysis
    from ._4813 import HypoidGearCompoundModalAnalysis
    from ._4814 import HypoidGearMeshCompoundModalAnalysis
    from ._4815 import HypoidGearSetCompoundModalAnalysis
    from ._4816 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4817 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4818 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4819 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4820 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4821 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4822 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4823 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4824 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4825 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4826 import MassDiscCompoundModalAnalysis
    from ._4827 import MeasurementComponentCompoundModalAnalysis
    from ._4828 import MountableComponentCompoundModalAnalysis
    from ._4829 import OilSealCompoundModalAnalysis
    from ._4830 import PartCompoundModalAnalysis
    from ._4831 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4832 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4833 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4834 import PlanetaryConnectionCompoundModalAnalysis
    from ._4835 import PlanetaryGearSetCompoundModalAnalysis
    from ._4836 import PlanetCarrierCompoundModalAnalysis
    from ._4837 import PointLoadCompoundModalAnalysis
    from ._4838 import PowerLoadCompoundModalAnalysis
    from ._4839 import PulleyCompoundModalAnalysis
    from ._4840 import RingPinsCompoundModalAnalysis
    from ._4841 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4842 import RollingRingAssemblyCompoundModalAnalysis
    from ._4843 import RollingRingCompoundModalAnalysis
    from ._4844 import RollingRingConnectionCompoundModalAnalysis
    from ._4845 import RootAssemblyCompoundModalAnalysis
    from ._4846 import ShaftCompoundModalAnalysis
    from ._4847 import ShaftHubConnectionCompoundModalAnalysis
    from ._4848 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4849 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4850 import SpiralBevelGearCompoundModalAnalysis
    from ._4851 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4852 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4853 import SpringDamperCompoundModalAnalysis
    from ._4854 import SpringDamperConnectionCompoundModalAnalysis
    from ._4855 import SpringDamperHalfCompoundModalAnalysis
    from ._4856 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4857 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4858 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4859 import StraightBevelGearCompoundModalAnalysis
    from ._4860 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4861 import StraightBevelGearSetCompoundModalAnalysis
    from ._4862 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4863 import StraightBevelSunGearCompoundModalAnalysis
    from ._4864 import SynchroniserCompoundModalAnalysis
    from ._4865 import SynchroniserHalfCompoundModalAnalysis
    from ._4866 import SynchroniserPartCompoundModalAnalysis
    from ._4867 import SynchroniserSleeveCompoundModalAnalysis
    from ._4868 import TorqueConverterCompoundModalAnalysis
    from ._4869 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4870 import TorqueConverterPumpCompoundModalAnalysis
    from ._4871 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4872 import UnbalancedMassCompoundModalAnalysis
    from ._4873 import VirtualComponentCompoundModalAnalysis
    from ._4874 import WormGearCompoundModalAnalysis
    from ._4875 import WormGearMeshCompoundModalAnalysis
    from ._4876 import WormGearSetCompoundModalAnalysis
    from ._4877 import ZerolBevelGearCompoundModalAnalysis
    from ._4878 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4879 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4751": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4752": ["AbstractShaftCompoundModalAnalysis"],
        "_4753": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4754": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4755": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4756": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4757": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4758": ["AssemblyCompoundModalAnalysis"],
        "_4759": ["BearingCompoundModalAnalysis"],
        "_4760": ["BeltConnectionCompoundModalAnalysis"],
        "_4761": ["BeltDriveCompoundModalAnalysis"],
        "_4762": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4763": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4764": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4765": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4766": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4767": ["BevelGearCompoundModalAnalysis"],
        "_4768": ["BevelGearMeshCompoundModalAnalysis"],
        "_4769": ["BevelGearSetCompoundModalAnalysis"],
        "_4770": ["BoltCompoundModalAnalysis"],
        "_4771": ["BoltedJointCompoundModalAnalysis"],
        "_4772": ["ClutchCompoundModalAnalysis"],
        "_4773": ["ClutchConnectionCompoundModalAnalysis"],
        "_4774": ["ClutchHalfCompoundModalAnalysis"],
        "_4775": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4776": ["ComponentCompoundModalAnalysis"],
        "_4777": ["ConceptCouplingCompoundModalAnalysis"],
        "_4778": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4779": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4780": ["ConceptGearCompoundModalAnalysis"],
        "_4781": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4782": ["ConceptGearSetCompoundModalAnalysis"],
        "_4783": ["ConicalGearCompoundModalAnalysis"],
        "_4784": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4785": ["ConicalGearSetCompoundModalAnalysis"],
        "_4786": ["ConnectionCompoundModalAnalysis"],
        "_4787": ["ConnectorCompoundModalAnalysis"],
        "_4788": ["CouplingCompoundModalAnalysis"],
        "_4789": ["CouplingConnectionCompoundModalAnalysis"],
        "_4790": ["CouplingHalfCompoundModalAnalysis"],
        "_4791": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4792": ["CVTCompoundModalAnalysis"],
        "_4793": ["CVTPulleyCompoundModalAnalysis"],
        "_4794": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4795": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4796": ["CycloidalDiscCompoundModalAnalysis"],
        "_4797": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4798": ["CylindricalGearCompoundModalAnalysis"],
        "_4799": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4800": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4801": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4802": ["DatumCompoundModalAnalysis"],
        "_4803": ["ExternalCADModelCompoundModalAnalysis"],
        "_4804": ["FaceGearCompoundModalAnalysis"],
        "_4805": ["FaceGearMeshCompoundModalAnalysis"],
        "_4806": ["FaceGearSetCompoundModalAnalysis"],
        "_4807": ["FEPartCompoundModalAnalysis"],
        "_4808": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4809": ["GearCompoundModalAnalysis"],
        "_4810": ["GearMeshCompoundModalAnalysis"],
        "_4811": ["GearSetCompoundModalAnalysis"],
        "_4812": ["GuideDxfModelCompoundModalAnalysis"],
        "_4813": ["HypoidGearCompoundModalAnalysis"],
        "_4814": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4815": ["HypoidGearSetCompoundModalAnalysis"],
        "_4816": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4817": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4818": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4819": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4820": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4821": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4822": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4823": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4824": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4825": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4826": ["MassDiscCompoundModalAnalysis"],
        "_4827": ["MeasurementComponentCompoundModalAnalysis"],
        "_4828": ["MountableComponentCompoundModalAnalysis"],
        "_4829": ["OilSealCompoundModalAnalysis"],
        "_4830": ["PartCompoundModalAnalysis"],
        "_4831": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4832": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4833": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4834": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4835": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4836": ["PlanetCarrierCompoundModalAnalysis"],
        "_4837": ["PointLoadCompoundModalAnalysis"],
        "_4838": ["PowerLoadCompoundModalAnalysis"],
        "_4839": ["PulleyCompoundModalAnalysis"],
        "_4840": ["RingPinsCompoundModalAnalysis"],
        "_4841": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4842": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4843": ["RollingRingCompoundModalAnalysis"],
        "_4844": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4845": ["RootAssemblyCompoundModalAnalysis"],
        "_4846": ["ShaftCompoundModalAnalysis"],
        "_4847": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4848": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4849": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4850": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4851": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4852": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4853": ["SpringDamperCompoundModalAnalysis"],
        "_4854": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4855": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4856": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4857": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4858": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4859": ["StraightBevelGearCompoundModalAnalysis"],
        "_4860": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4861": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4862": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4863": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4864": ["SynchroniserCompoundModalAnalysis"],
        "_4865": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4866": ["SynchroniserPartCompoundModalAnalysis"],
        "_4867": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4868": ["TorqueConverterCompoundModalAnalysis"],
        "_4869": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4870": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4871": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4872": ["UnbalancedMassCompoundModalAnalysis"],
        "_4873": ["VirtualComponentCompoundModalAnalysis"],
        "_4874": ["WormGearCompoundModalAnalysis"],
        "_4875": ["WormGearMeshCompoundModalAnalysis"],
        "_4876": ["WormGearSetCompoundModalAnalysis"],
        "_4877": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4878": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4879": ["ZerolBevelGearSetCompoundModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysis",
    "AbstractShaftCompoundModalAnalysis",
    "AbstractShaftOrHousingCompoundModalAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
    "AssemblyCompoundModalAnalysis",
    "BearingCompoundModalAnalysis",
    "BeltConnectionCompoundModalAnalysis",
    "BeltDriveCompoundModalAnalysis",
    "BevelDifferentialGearCompoundModalAnalysis",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
    "BevelDifferentialGearSetCompoundModalAnalysis",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
    "BevelDifferentialSunGearCompoundModalAnalysis",
    "BevelGearCompoundModalAnalysis",
    "BevelGearMeshCompoundModalAnalysis",
    "BevelGearSetCompoundModalAnalysis",
    "BoltCompoundModalAnalysis",
    "BoltedJointCompoundModalAnalysis",
    "ClutchCompoundModalAnalysis",
    "ClutchConnectionCompoundModalAnalysis",
    "ClutchHalfCompoundModalAnalysis",
    "CoaxialConnectionCompoundModalAnalysis",
    "ComponentCompoundModalAnalysis",
    "ConceptCouplingCompoundModalAnalysis",
    "ConceptCouplingConnectionCompoundModalAnalysis",
    "ConceptCouplingHalfCompoundModalAnalysis",
    "ConceptGearCompoundModalAnalysis",
    "ConceptGearMeshCompoundModalAnalysis",
    "ConceptGearSetCompoundModalAnalysis",
    "ConicalGearCompoundModalAnalysis",
    "ConicalGearMeshCompoundModalAnalysis",
    "ConicalGearSetCompoundModalAnalysis",
    "ConnectionCompoundModalAnalysis",
    "ConnectorCompoundModalAnalysis",
    "CouplingCompoundModalAnalysis",
    "CouplingConnectionCompoundModalAnalysis",
    "CouplingHalfCompoundModalAnalysis",
    "CVTBeltConnectionCompoundModalAnalysis",
    "CVTCompoundModalAnalysis",
    "CVTPulleyCompoundModalAnalysis",
    "CycloidalAssemblyCompoundModalAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    "CycloidalDiscCompoundModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    "CylindricalGearCompoundModalAnalysis",
    "CylindricalGearMeshCompoundModalAnalysis",
    "CylindricalGearSetCompoundModalAnalysis",
    "CylindricalPlanetGearCompoundModalAnalysis",
    "DatumCompoundModalAnalysis",
    "ExternalCADModelCompoundModalAnalysis",
    "FaceGearCompoundModalAnalysis",
    "FaceGearMeshCompoundModalAnalysis",
    "FaceGearSetCompoundModalAnalysis",
    "FEPartCompoundModalAnalysis",
    "FlexiblePinAssemblyCompoundModalAnalysis",
    "GearCompoundModalAnalysis",
    "GearMeshCompoundModalAnalysis",
    "GearSetCompoundModalAnalysis",
    "GuideDxfModelCompoundModalAnalysis",
    "HypoidGearCompoundModalAnalysis",
    "HypoidGearMeshCompoundModalAnalysis",
    "HypoidGearSetCompoundModalAnalysis",
    "InterMountableComponentConnectionCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    "MassDiscCompoundModalAnalysis",
    "MeasurementComponentCompoundModalAnalysis",
    "MountableComponentCompoundModalAnalysis",
    "OilSealCompoundModalAnalysis",
    "PartCompoundModalAnalysis",
    "PartToPartShearCouplingCompoundModalAnalysis",
    "PartToPartShearCouplingConnectionCompoundModalAnalysis",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
    "PlanetaryConnectionCompoundModalAnalysis",
    "PlanetaryGearSetCompoundModalAnalysis",
    "PlanetCarrierCompoundModalAnalysis",
    "PointLoadCompoundModalAnalysis",
    "PowerLoadCompoundModalAnalysis",
    "PulleyCompoundModalAnalysis",
    "RingPinsCompoundModalAnalysis",
    "RingPinsToDiscConnectionCompoundModalAnalysis",
    "RollingRingAssemblyCompoundModalAnalysis",
    "RollingRingCompoundModalAnalysis",
    "RollingRingConnectionCompoundModalAnalysis",
    "RootAssemblyCompoundModalAnalysis",
    "ShaftCompoundModalAnalysis",
    "ShaftHubConnectionCompoundModalAnalysis",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
    "SpecialisedAssemblyCompoundModalAnalysis",
    "SpiralBevelGearCompoundModalAnalysis",
    "SpiralBevelGearMeshCompoundModalAnalysis",
    "SpiralBevelGearSetCompoundModalAnalysis",
    "SpringDamperCompoundModalAnalysis",
    "SpringDamperConnectionCompoundModalAnalysis",
    "SpringDamperHalfCompoundModalAnalysis",
    "StraightBevelDiffGearCompoundModalAnalysis",
    "StraightBevelDiffGearMeshCompoundModalAnalysis",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
    "StraightBevelGearCompoundModalAnalysis",
    "StraightBevelGearMeshCompoundModalAnalysis",
    "StraightBevelGearSetCompoundModalAnalysis",
    "StraightBevelPlanetGearCompoundModalAnalysis",
    "StraightBevelSunGearCompoundModalAnalysis",
    "SynchroniserCompoundModalAnalysis",
    "SynchroniserHalfCompoundModalAnalysis",
    "SynchroniserPartCompoundModalAnalysis",
    "SynchroniserSleeveCompoundModalAnalysis",
    "TorqueConverterCompoundModalAnalysis",
    "TorqueConverterConnectionCompoundModalAnalysis",
    "TorqueConverterPumpCompoundModalAnalysis",
    "TorqueConverterTurbineCompoundModalAnalysis",
    "UnbalancedMassCompoundModalAnalysis",
    "VirtualComponentCompoundModalAnalysis",
    "WormGearCompoundModalAnalysis",
    "WormGearMeshCompoundModalAnalysis",
    "WormGearSetCompoundModalAnalysis",
    "ZerolBevelGearCompoundModalAnalysis",
    "ZerolBevelGearMeshCompoundModalAnalysis",
    "ZerolBevelGearSetCompoundModalAnalysis",
)
