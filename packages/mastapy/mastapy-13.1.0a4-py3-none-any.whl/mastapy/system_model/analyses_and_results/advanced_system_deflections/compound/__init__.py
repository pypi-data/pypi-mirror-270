"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7432 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7433 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7434 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7435 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7436 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7437 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7438 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7439 import AssemblyCompoundAdvancedSystemDeflection
    from ._7440 import BearingCompoundAdvancedSystemDeflection
    from ._7441 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7442 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7443 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7444 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7445 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7446 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7447 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7448 import BevelGearCompoundAdvancedSystemDeflection
    from ._7449 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7450 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7451 import BoltCompoundAdvancedSystemDeflection
    from ._7452 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7453 import ClutchCompoundAdvancedSystemDeflection
    from ._7454 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7455 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7456 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7457 import ComponentCompoundAdvancedSystemDeflection
    from ._7458 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7459 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7460 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7461 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7462 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7463 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7464 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7465 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7466 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7467 import ConnectionCompoundAdvancedSystemDeflection
    from ._7468 import ConnectorCompoundAdvancedSystemDeflection
    from ._7469 import CouplingCompoundAdvancedSystemDeflection
    from ._7470 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7471 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7472 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7473 import CVTCompoundAdvancedSystemDeflection
    from ._7474 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7475 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7476 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7477 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7478 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7479 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7480 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7481 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7482 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7483 import DatumCompoundAdvancedSystemDeflection
    from ._7484 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7485 import FaceGearCompoundAdvancedSystemDeflection
    from ._7486 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7487 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7488 import FEPartCompoundAdvancedSystemDeflection
    from ._7489 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7490 import GearCompoundAdvancedSystemDeflection
    from ._7491 import GearMeshCompoundAdvancedSystemDeflection
    from ._7492 import GearSetCompoundAdvancedSystemDeflection
    from ._7493 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7494 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7495 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7496 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7497 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7498 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7499 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7500 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7501 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7502 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7503 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7504 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7505 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7506 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7507 import MassDiscCompoundAdvancedSystemDeflection
    from ._7508 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7509 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7510 import OilSealCompoundAdvancedSystemDeflection
    from ._7511 import PartCompoundAdvancedSystemDeflection
    from ._7512 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7513 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7514 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7515 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7516 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7517 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7518 import PointLoadCompoundAdvancedSystemDeflection
    from ._7519 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7520 import PulleyCompoundAdvancedSystemDeflection
    from ._7521 import RingPinsCompoundAdvancedSystemDeflection
    from ._7522 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7523 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7524 import RollingRingCompoundAdvancedSystemDeflection
    from ._7525 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7526 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7527 import ShaftCompoundAdvancedSystemDeflection
    from ._7528 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7529 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7530 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7531 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7532 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7533 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7534 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7535 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7536 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7537 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7538 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7539 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7540 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7541 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7542 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7543 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7544 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7545 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7546 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7547 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7548 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7549 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7550 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7551 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7552 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7553 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7554 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7555 import WormGearCompoundAdvancedSystemDeflection
    from ._7556 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7557 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7558 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7559 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7560 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7432": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7433": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7434": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7435": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7436": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7437": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7438": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7439": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7440": ["BearingCompoundAdvancedSystemDeflection"],
        "_7441": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7442": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7443": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7444": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7445": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7446": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7447": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7448": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7449": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7450": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7451": ["BoltCompoundAdvancedSystemDeflection"],
        "_7452": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7453": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7454": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7455": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7456": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7457": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7458": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7459": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7460": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7461": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7462": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7463": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7464": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7465": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7466": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7467": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7468": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7469": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7470": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7471": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7472": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7473": ["CVTCompoundAdvancedSystemDeflection"],
        "_7474": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7475": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7476": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7477": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7478": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7479": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7480": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7481": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7482": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7483": ["DatumCompoundAdvancedSystemDeflection"],
        "_7484": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7485": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7486": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7487": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7488": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7489": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7490": ["GearCompoundAdvancedSystemDeflection"],
        "_7491": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7492": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7493": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7494": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7495": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7496": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7497": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7498": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7499": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7500": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7501": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7502": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7503": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7504": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7505": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7506": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7507": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7508": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7509": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7510": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7511": ["PartCompoundAdvancedSystemDeflection"],
        "_7512": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7513": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7514": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7515": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7516": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7517": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7518": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7519": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7520": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7521": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7522": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7523": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7524": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7525": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7526": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7527": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7528": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7529": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7530": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7531": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7532": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7533": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7534": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7535": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7536": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7537": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7538": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7539": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7540": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7541": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7542": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7543": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7544": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7545": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7546": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7547": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7548": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7549": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7550": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7551": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7552": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7553": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7554": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7555": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7556": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7557": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7558": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7559": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7560": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedSystemDeflection",
    "AbstractShaftCompoundAdvancedSystemDeflection",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    "AssemblyCompoundAdvancedSystemDeflection",
    "BearingCompoundAdvancedSystemDeflection",
    "BeltConnectionCompoundAdvancedSystemDeflection",
    "BeltDriveCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    "BevelGearCompoundAdvancedSystemDeflection",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
    "BevelGearSetCompoundAdvancedSystemDeflection",
    "BoltCompoundAdvancedSystemDeflection",
    "BoltedJointCompoundAdvancedSystemDeflection",
    "ClutchCompoundAdvancedSystemDeflection",
    "ClutchConnectionCompoundAdvancedSystemDeflection",
    "ClutchHalfCompoundAdvancedSystemDeflection",
    "CoaxialConnectionCompoundAdvancedSystemDeflection",
    "ComponentCompoundAdvancedSystemDeflection",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
    "ConceptGearCompoundAdvancedSystemDeflection",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
    "ConicalGearCompoundAdvancedSystemDeflection",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
    "ConnectionCompoundAdvancedSystemDeflection",
    "ConnectorCompoundAdvancedSystemDeflection",
    "CouplingCompoundAdvancedSystemDeflection",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
    "CouplingHalfCompoundAdvancedSystemDeflection",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
    "CVTCompoundAdvancedSystemDeflection",
    "CVTPulleyCompoundAdvancedSystemDeflection",
    "CycloidalAssemblyCompoundAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    "CylindricalGearCompoundAdvancedSystemDeflection",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
    "CylindricalGearSetCompoundAdvancedSystemDeflection",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    "DatumCompoundAdvancedSystemDeflection",
    "ExternalCADModelCompoundAdvancedSystemDeflection",
    "FaceGearCompoundAdvancedSystemDeflection",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
    "FaceGearSetCompoundAdvancedSystemDeflection",
    "FEPartCompoundAdvancedSystemDeflection",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
    "GearCompoundAdvancedSystemDeflection",
    "GearMeshCompoundAdvancedSystemDeflection",
    "GearSetCompoundAdvancedSystemDeflection",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
    "HypoidGearCompoundAdvancedSystemDeflection",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "MassDiscCompoundAdvancedSystemDeflection",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
    "MountableComponentCompoundAdvancedSystemDeflection",
    "OilSealCompoundAdvancedSystemDeflection",
    "PartCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection",
    "PlanetaryConnectionCompoundAdvancedSystemDeflection",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
    "PlanetCarrierCompoundAdvancedSystemDeflection",
    "PointLoadCompoundAdvancedSystemDeflection",
    "PowerLoadCompoundAdvancedSystemDeflection",
    "PulleyCompoundAdvancedSystemDeflection",
    "RingPinsCompoundAdvancedSystemDeflection",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
    "RollingRingCompoundAdvancedSystemDeflection",
    "RollingRingConnectionCompoundAdvancedSystemDeflection",
    "RootAssemblyCompoundAdvancedSystemDeflection",
    "ShaftCompoundAdvancedSystemDeflection",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "SpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "SpringDamperCompoundAdvancedSystemDeflection",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelGearCompoundAdvancedSystemDeflection",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
    "SynchroniserCompoundAdvancedSystemDeflection",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
    "SynchroniserPartCompoundAdvancedSystemDeflection",
    "SynchroniserSleeveCompoundAdvancedSystemDeflection",
    "TorqueConverterCompoundAdvancedSystemDeflection",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    "TorqueConverterPumpCompoundAdvancedSystemDeflection",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
    "VirtualComponentCompoundAdvancedSystemDeflection",
    "WormGearCompoundAdvancedSystemDeflection",
    "WormGearMeshCompoundAdvancedSystemDeflection",
    "WormGearSetCompoundAdvancedSystemDeflection",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)
