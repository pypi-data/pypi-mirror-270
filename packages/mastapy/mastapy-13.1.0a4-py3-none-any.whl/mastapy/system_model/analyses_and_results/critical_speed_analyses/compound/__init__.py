"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6701 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6702 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6703 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6704 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6705 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6706 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6707 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6708 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6709 import BearingCompoundCriticalSpeedAnalysis
    from ._6710 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6711 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6712 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6713 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6714 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6715 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6716 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6717 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6718 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6719 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6720 import BoltCompoundCriticalSpeedAnalysis
    from ._6721 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6722 import ClutchCompoundCriticalSpeedAnalysis
    from ._6723 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6724 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6725 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6726 import ComponentCompoundCriticalSpeedAnalysis
    from ._6727 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6728 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6729 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6730 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6731 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6732 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6733 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6734 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6735 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6736 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6737 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6738 import CouplingCompoundCriticalSpeedAnalysis
    from ._6739 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6740 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6741 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6742 import CVTCompoundCriticalSpeedAnalysis
    from ._6743 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6744 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6745 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6746 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6747 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6748 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6749 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6750 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6751 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6752 import DatumCompoundCriticalSpeedAnalysis
    from ._6753 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6754 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6755 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6756 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6757 import FEPartCompoundCriticalSpeedAnalysis
    from ._6758 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6759 import GearCompoundCriticalSpeedAnalysis
    from ._6760 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6761 import GearSetCompoundCriticalSpeedAnalysis
    from ._6762 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6763 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6764 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6765 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6766 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6767 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6768 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6769 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6770 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6771 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6772 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6773 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6774 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6775 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6776 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6777 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6778 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6779 import OilSealCompoundCriticalSpeedAnalysis
    from ._6780 import PartCompoundCriticalSpeedAnalysis
    from ._6781 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6782 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6783 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6784 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6785 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6786 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6787 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6788 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6789 import PulleyCompoundCriticalSpeedAnalysis
    from ._6790 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6791 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6792 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6793 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6794 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6795 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6796 import ShaftCompoundCriticalSpeedAnalysis
    from ._6797 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6798 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6799 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6800 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6801 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6802 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6803 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6804 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6805 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6806 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6807 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6808 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6809 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6810 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6811 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6812 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6813 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6814 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6815 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6816 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6817 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6818 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6819 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6820 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6821 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6822 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6823 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6824 import WormGearCompoundCriticalSpeedAnalysis
    from ._6825 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6826 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6827 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6828 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6829 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6701": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6702": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6703": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6704": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6705": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6706": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6707": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6708": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6709": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6710": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6711": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6712": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6713": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6714": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6715": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6716": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6717": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6718": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6719": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6720": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6721": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6722": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6723": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6724": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6725": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6726": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6727": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6728": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6729": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6730": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6731": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6732": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6733": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6734": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6735": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6736": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6737": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6738": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6739": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6740": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6741": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6742": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6743": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6744": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6745": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6746": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6747": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6748": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6749": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6750": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6751": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6752": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6753": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6754": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6755": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6756": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6757": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6758": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6759": ["GearCompoundCriticalSpeedAnalysis"],
        "_6760": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6761": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6762": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6763": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6764": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6765": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6766": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6767": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6768": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6769": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6770": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6771": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6772": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6773": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6774": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6775": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6776": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6777": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6778": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6779": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6780": ["PartCompoundCriticalSpeedAnalysis"],
        "_6781": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6782": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6783": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6784": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6785": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6786": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6787": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6788": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6789": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6790": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6791": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6792": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6793": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6794": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6795": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6796": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6797": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6798": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6799": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6800": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6801": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6802": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6803": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6804": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6805": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6806": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6807": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6808": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6809": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6810": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6811": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6812": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6813": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6814": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6815": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6816": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6817": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6818": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6819": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6820": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6821": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6822": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6823": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6824": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6825": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6826": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6827": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6828": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6829": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    "AssemblyCompoundCriticalSpeedAnalysis",
    "BearingCompoundCriticalSpeedAnalysis",
    "BeltConnectionCompoundCriticalSpeedAnalysis",
    "BeltDriveCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCompoundCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
    "BevelGearCompoundCriticalSpeedAnalysis",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
    "BoltCompoundCriticalSpeedAnalysis",
    "BoltedJointCompoundCriticalSpeedAnalysis",
    "ClutchCompoundCriticalSpeedAnalysis",
    "ClutchConnectionCompoundCriticalSpeedAnalysis",
    "ClutchHalfCompoundCriticalSpeedAnalysis",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
    "ComponentCompoundCriticalSpeedAnalysis",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
    "ConceptGearCompoundCriticalSpeedAnalysis",
    "ConceptGearMeshCompoundCriticalSpeedAnalysis",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
    "ConicalGearCompoundCriticalSpeedAnalysis",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
    "ConnectionCompoundCriticalSpeedAnalysis",
    "ConnectorCompoundCriticalSpeedAnalysis",
    "CouplingCompoundCriticalSpeedAnalysis",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
    "CVTCompoundCriticalSpeedAnalysis",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
    "CycloidalAssemblyCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis",
    "CylindricalGearCompoundCriticalSpeedAnalysis",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
    "CylindricalGearSetCompoundCriticalSpeedAnalysis",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
    "DatumCompoundCriticalSpeedAnalysis",
    "ExternalCADModelCompoundCriticalSpeedAnalysis",
    "FaceGearCompoundCriticalSpeedAnalysis",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
    "FEPartCompoundCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
    "GearCompoundCriticalSpeedAnalysis",
    "GearMeshCompoundCriticalSpeedAnalysis",
    "GearSetCompoundCriticalSpeedAnalysis",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
    "HypoidGearCompoundCriticalSpeedAnalysis",
    "HypoidGearMeshCompoundCriticalSpeedAnalysis",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "MassDiscCompoundCriticalSpeedAnalysis",
    "MeasurementComponentCompoundCriticalSpeedAnalysis",
    "MountableComponentCompoundCriticalSpeedAnalysis",
    "OilSealCompoundCriticalSpeedAnalysis",
    "PartCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    "PlanetaryConnectionCompoundCriticalSpeedAnalysis",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
    "PointLoadCompoundCriticalSpeedAnalysis",
    "PowerLoadCompoundCriticalSpeedAnalysis",
    "PulleyCompoundCriticalSpeedAnalysis",
    "RingPinsCompoundCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
    "RollingRingAssemblyCompoundCriticalSpeedAnalysis",
    "RollingRingCompoundCriticalSpeedAnalysis",
    "RollingRingConnectionCompoundCriticalSpeedAnalysis",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
    "ShaftCompoundCriticalSpeedAnalysis",
    "ShaftHubConnectionCompoundCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "SpringDamperCompoundCriticalSpeedAnalysis",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelGearCompoundCriticalSpeedAnalysis",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
    "SynchroniserCompoundCriticalSpeedAnalysis",
    "SynchroniserHalfCompoundCriticalSpeedAnalysis",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
    "TorqueConverterConnectionCompoundCriticalSpeedAnalysis",
    "TorqueConverterPumpCompoundCriticalSpeedAnalysis",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
    "WormGearCompoundCriticalSpeedAnalysis",
    "WormGearMeshCompoundCriticalSpeedAnalysis",
    "WormGearSetCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)
