"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6569 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6570 import AbstractShaftCriticalSpeedAnalysis
    from ._6571 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6572 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6573 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6574 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6575 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6576 import AssemblyCriticalSpeedAnalysis
    from ._6577 import BearingCriticalSpeedAnalysis
    from ._6578 import BeltConnectionCriticalSpeedAnalysis
    from ._6579 import BeltDriveCriticalSpeedAnalysis
    from ._6580 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6581 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6582 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6583 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6584 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6585 import BevelGearCriticalSpeedAnalysis
    from ._6586 import BevelGearMeshCriticalSpeedAnalysis
    from ._6587 import BevelGearSetCriticalSpeedAnalysis
    from ._6588 import BoltCriticalSpeedAnalysis
    from ._6589 import BoltedJointCriticalSpeedAnalysis
    from ._6590 import ClutchConnectionCriticalSpeedAnalysis
    from ._6591 import ClutchCriticalSpeedAnalysis
    from ._6592 import ClutchHalfCriticalSpeedAnalysis
    from ._6593 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6594 import ComponentCriticalSpeedAnalysis
    from ._6595 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6596 import ConceptCouplingCriticalSpeedAnalysis
    from ._6597 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6598 import ConceptGearCriticalSpeedAnalysis
    from ._6599 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6600 import ConceptGearSetCriticalSpeedAnalysis
    from ._6601 import ConicalGearCriticalSpeedAnalysis
    from ._6602 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6603 import ConicalGearSetCriticalSpeedAnalysis
    from ._6604 import ConnectionCriticalSpeedAnalysis
    from ._6605 import ConnectorCriticalSpeedAnalysis
    from ._6606 import CouplingConnectionCriticalSpeedAnalysis
    from ._6607 import CouplingCriticalSpeedAnalysis
    from ._6608 import CouplingHalfCriticalSpeedAnalysis
    from ._6609 import CriticalSpeedAnalysis
    from ._6610 import CriticalSpeedAnalysisDrawStyle
    from ._6611 import CriticalSpeedAnalysisOptions
    from ._6612 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6613 import CVTCriticalSpeedAnalysis
    from ._6614 import CVTPulleyCriticalSpeedAnalysis
    from ._6615 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6616 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6617 import CycloidalDiscCriticalSpeedAnalysis
    from ._6618 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6619 import CylindricalGearCriticalSpeedAnalysis
    from ._6620 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6621 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6622 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6623 import DatumCriticalSpeedAnalysis
    from ._6624 import ExternalCADModelCriticalSpeedAnalysis
    from ._6625 import FaceGearCriticalSpeedAnalysis
    from ._6626 import FaceGearMeshCriticalSpeedAnalysis
    from ._6627 import FaceGearSetCriticalSpeedAnalysis
    from ._6628 import FEPartCriticalSpeedAnalysis
    from ._6629 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6630 import GearCriticalSpeedAnalysis
    from ._6631 import GearMeshCriticalSpeedAnalysis
    from ._6632 import GearSetCriticalSpeedAnalysis
    from ._6633 import GuideDxfModelCriticalSpeedAnalysis
    from ._6634 import HypoidGearCriticalSpeedAnalysis
    from ._6635 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6636 import HypoidGearSetCriticalSpeedAnalysis
    from ._6637 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6638 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6639 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6640 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6641 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6642 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6643 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6644 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6645 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6646 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6647 import MassDiscCriticalSpeedAnalysis
    from ._6648 import MeasurementComponentCriticalSpeedAnalysis
    from ._6649 import MountableComponentCriticalSpeedAnalysis
    from ._6650 import OilSealCriticalSpeedAnalysis
    from ._6651 import PartCriticalSpeedAnalysis
    from ._6652 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6653 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6654 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6655 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6656 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6657 import PlanetCarrierCriticalSpeedAnalysis
    from ._6658 import PointLoadCriticalSpeedAnalysis
    from ._6659 import PowerLoadCriticalSpeedAnalysis
    from ._6660 import PulleyCriticalSpeedAnalysis
    from ._6661 import RingPinsCriticalSpeedAnalysis
    from ._6662 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6663 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6664 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6665 import RollingRingCriticalSpeedAnalysis
    from ._6666 import RootAssemblyCriticalSpeedAnalysis
    from ._6667 import ShaftCriticalSpeedAnalysis
    from ._6668 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6669 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6670 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6671 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6672 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6673 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6674 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6675 import SpringDamperCriticalSpeedAnalysis
    from ._6676 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6677 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6678 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6679 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6680 import StraightBevelGearCriticalSpeedAnalysis
    from ._6681 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6682 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6683 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6684 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6685 import SynchroniserCriticalSpeedAnalysis
    from ._6686 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6687 import SynchroniserPartCriticalSpeedAnalysis
    from ._6688 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6689 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6690 import TorqueConverterCriticalSpeedAnalysis
    from ._6691 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6692 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6693 import UnbalancedMassCriticalSpeedAnalysis
    from ._6694 import VirtualComponentCriticalSpeedAnalysis
    from ._6695 import WormGearCriticalSpeedAnalysis
    from ._6696 import WormGearMeshCriticalSpeedAnalysis
    from ._6697 import WormGearSetCriticalSpeedAnalysis
    from ._6698 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6699 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6700 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6569": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6570": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6571": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6572": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6573": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6574": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6575": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6576": ["AssemblyCriticalSpeedAnalysis"],
        "_6577": ["BearingCriticalSpeedAnalysis"],
        "_6578": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6579": ["BeltDriveCriticalSpeedAnalysis"],
        "_6580": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6581": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6582": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6583": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6584": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6585": ["BevelGearCriticalSpeedAnalysis"],
        "_6586": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6587": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6588": ["BoltCriticalSpeedAnalysis"],
        "_6589": ["BoltedJointCriticalSpeedAnalysis"],
        "_6590": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6591": ["ClutchCriticalSpeedAnalysis"],
        "_6592": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6593": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6594": ["ComponentCriticalSpeedAnalysis"],
        "_6595": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6596": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6597": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6598": ["ConceptGearCriticalSpeedAnalysis"],
        "_6599": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6600": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6601": ["ConicalGearCriticalSpeedAnalysis"],
        "_6602": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6603": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6604": ["ConnectionCriticalSpeedAnalysis"],
        "_6605": ["ConnectorCriticalSpeedAnalysis"],
        "_6606": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6607": ["CouplingCriticalSpeedAnalysis"],
        "_6608": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6609": ["CriticalSpeedAnalysis"],
        "_6610": ["CriticalSpeedAnalysisDrawStyle"],
        "_6611": ["CriticalSpeedAnalysisOptions"],
        "_6612": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6613": ["CVTCriticalSpeedAnalysis"],
        "_6614": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6615": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6616": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6617": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6618": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6619": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6620": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6621": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6622": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6623": ["DatumCriticalSpeedAnalysis"],
        "_6624": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6625": ["FaceGearCriticalSpeedAnalysis"],
        "_6626": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6627": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6628": ["FEPartCriticalSpeedAnalysis"],
        "_6629": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6630": ["GearCriticalSpeedAnalysis"],
        "_6631": ["GearMeshCriticalSpeedAnalysis"],
        "_6632": ["GearSetCriticalSpeedAnalysis"],
        "_6633": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6634": ["HypoidGearCriticalSpeedAnalysis"],
        "_6635": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6636": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6637": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6638": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6639": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6640": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6641": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6642": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6643": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6644": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6645": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6646": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6647": ["MassDiscCriticalSpeedAnalysis"],
        "_6648": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6649": ["MountableComponentCriticalSpeedAnalysis"],
        "_6650": ["OilSealCriticalSpeedAnalysis"],
        "_6651": ["PartCriticalSpeedAnalysis"],
        "_6652": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6653": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6654": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6655": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6656": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6657": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6658": ["PointLoadCriticalSpeedAnalysis"],
        "_6659": ["PowerLoadCriticalSpeedAnalysis"],
        "_6660": ["PulleyCriticalSpeedAnalysis"],
        "_6661": ["RingPinsCriticalSpeedAnalysis"],
        "_6662": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6663": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6664": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6665": ["RollingRingCriticalSpeedAnalysis"],
        "_6666": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6667": ["ShaftCriticalSpeedAnalysis"],
        "_6668": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6669": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6670": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6671": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6672": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6673": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6674": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6675": ["SpringDamperCriticalSpeedAnalysis"],
        "_6676": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6677": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6678": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6679": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6680": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6681": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6682": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6683": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6684": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6685": ["SynchroniserCriticalSpeedAnalysis"],
        "_6686": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6687": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6688": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6689": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6690": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6691": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6692": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6693": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6694": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6695": ["WormGearCriticalSpeedAnalysis"],
        "_6696": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6697": ["WormGearSetCriticalSpeedAnalysis"],
        "_6698": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6699": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6700": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCriticalSpeedAnalysis",
    "AbstractShaftCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
    "AssemblyCriticalSpeedAnalysis",
    "BearingCriticalSpeedAnalysis",
    "BeltConnectionCriticalSpeedAnalysis",
    "BeltDriveCriticalSpeedAnalysis",
    "BevelDifferentialGearCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
    "BevelGearCriticalSpeedAnalysis",
    "BevelGearMeshCriticalSpeedAnalysis",
    "BevelGearSetCriticalSpeedAnalysis",
    "BoltCriticalSpeedAnalysis",
    "BoltedJointCriticalSpeedAnalysis",
    "ClutchConnectionCriticalSpeedAnalysis",
    "ClutchCriticalSpeedAnalysis",
    "ClutchHalfCriticalSpeedAnalysis",
    "CoaxialConnectionCriticalSpeedAnalysis",
    "ComponentCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
    "ConceptCouplingCriticalSpeedAnalysis",
    "ConceptCouplingHalfCriticalSpeedAnalysis",
    "ConceptGearCriticalSpeedAnalysis",
    "ConceptGearMeshCriticalSpeedAnalysis",
    "ConceptGearSetCriticalSpeedAnalysis",
    "ConicalGearCriticalSpeedAnalysis",
    "ConicalGearMeshCriticalSpeedAnalysis",
    "ConicalGearSetCriticalSpeedAnalysis",
    "ConnectionCriticalSpeedAnalysis",
    "ConnectorCriticalSpeedAnalysis",
    "CouplingConnectionCriticalSpeedAnalysis",
    "CouplingCriticalSpeedAnalysis",
    "CouplingHalfCriticalSpeedAnalysis",
    "CriticalSpeedAnalysis",
    "CriticalSpeedAnalysisDrawStyle",
    "CriticalSpeedAnalysisOptions",
    "CVTBeltConnectionCriticalSpeedAnalysis",
    "CVTCriticalSpeedAnalysis",
    "CVTPulleyCriticalSpeedAnalysis",
    "CycloidalAssemblyCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    "CycloidalDiscCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    "CylindricalGearCriticalSpeedAnalysis",
    "CylindricalGearMeshCriticalSpeedAnalysis",
    "CylindricalGearSetCriticalSpeedAnalysis",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
    "DatumCriticalSpeedAnalysis",
    "ExternalCADModelCriticalSpeedAnalysis",
    "FaceGearCriticalSpeedAnalysis",
    "FaceGearMeshCriticalSpeedAnalysis",
    "FaceGearSetCriticalSpeedAnalysis",
    "FEPartCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
    "GearCriticalSpeedAnalysis",
    "GearMeshCriticalSpeedAnalysis",
    "GearSetCriticalSpeedAnalysis",
    "GuideDxfModelCriticalSpeedAnalysis",
    "HypoidGearCriticalSpeedAnalysis",
    "HypoidGearMeshCriticalSpeedAnalysis",
    "HypoidGearSetCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    "MassDiscCriticalSpeedAnalysis",
    "MeasurementComponentCriticalSpeedAnalysis",
    "MountableComponentCriticalSpeedAnalysis",
    "OilSealCriticalSpeedAnalysis",
    "PartCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCriticalSpeedAnalysis",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
    "PlanetaryConnectionCriticalSpeedAnalysis",
    "PlanetaryGearSetCriticalSpeedAnalysis",
    "PlanetCarrierCriticalSpeedAnalysis",
    "PointLoadCriticalSpeedAnalysis",
    "PowerLoadCriticalSpeedAnalysis",
    "PulleyCriticalSpeedAnalysis",
    "RingPinsCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
    "RollingRingAssemblyCriticalSpeedAnalysis",
    "RollingRingConnectionCriticalSpeedAnalysis",
    "RollingRingCriticalSpeedAnalysis",
    "RootAssemblyCriticalSpeedAnalysis",
    "ShaftCriticalSpeedAnalysis",
    "ShaftHubConnectionCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
    "SpiralBevelGearCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
    "SpiralBevelGearSetCriticalSpeedAnalysis",
    "SpringDamperConnectionCriticalSpeedAnalysis",
    "SpringDamperCriticalSpeedAnalysis",
    "SpringDamperHalfCriticalSpeedAnalysis",
    "StraightBevelDiffGearCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
    "StraightBevelGearCriticalSpeedAnalysis",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
    "StraightBevelGearSetCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCriticalSpeedAnalysis",
    "StraightBevelSunGearCriticalSpeedAnalysis",
    "SynchroniserCriticalSpeedAnalysis",
    "SynchroniserHalfCriticalSpeedAnalysis",
    "SynchroniserPartCriticalSpeedAnalysis",
    "SynchroniserSleeveCriticalSpeedAnalysis",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
    "TorqueConverterCriticalSpeedAnalysis",
    "TorqueConverterPumpCriticalSpeedAnalysis",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
    "UnbalancedMassCriticalSpeedAnalysis",
    "VirtualComponentCriticalSpeedAnalysis",
    "WormGearCriticalSpeedAnalysis",
    "WormGearMeshCriticalSpeedAnalysis",
    "WormGearSetCriticalSpeedAnalysis",
    "ZerolBevelGearCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCriticalSpeedAnalysis",
    "ZerolBevelGearSetCriticalSpeedAnalysis",
)
