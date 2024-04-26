"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4466 import AbstractAssemblyCompoundParametricStudyTool
    from ._4467 import AbstractShaftCompoundParametricStudyTool
    from ._4468 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4469 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4470 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4471 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4472 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4473 import AssemblyCompoundParametricStudyTool
    from ._4474 import BearingCompoundParametricStudyTool
    from ._4475 import BeltConnectionCompoundParametricStudyTool
    from ._4476 import BeltDriveCompoundParametricStudyTool
    from ._4477 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4478 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4479 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4480 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4481 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4482 import BevelGearCompoundParametricStudyTool
    from ._4483 import BevelGearMeshCompoundParametricStudyTool
    from ._4484 import BevelGearSetCompoundParametricStudyTool
    from ._4485 import BoltCompoundParametricStudyTool
    from ._4486 import BoltedJointCompoundParametricStudyTool
    from ._4487 import ClutchCompoundParametricStudyTool
    from ._4488 import ClutchConnectionCompoundParametricStudyTool
    from ._4489 import ClutchHalfCompoundParametricStudyTool
    from ._4490 import CoaxialConnectionCompoundParametricStudyTool
    from ._4491 import ComponentCompoundParametricStudyTool
    from ._4492 import ConceptCouplingCompoundParametricStudyTool
    from ._4493 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4494 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4495 import ConceptGearCompoundParametricStudyTool
    from ._4496 import ConceptGearMeshCompoundParametricStudyTool
    from ._4497 import ConceptGearSetCompoundParametricStudyTool
    from ._4498 import ConicalGearCompoundParametricStudyTool
    from ._4499 import ConicalGearMeshCompoundParametricStudyTool
    from ._4500 import ConicalGearSetCompoundParametricStudyTool
    from ._4501 import ConnectionCompoundParametricStudyTool
    from ._4502 import ConnectorCompoundParametricStudyTool
    from ._4503 import CouplingCompoundParametricStudyTool
    from ._4504 import CouplingConnectionCompoundParametricStudyTool
    from ._4505 import CouplingHalfCompoundParametricStudyTool
    from ._4506 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4507 import CVTCompoundParametricStudyTool
    from ._4508 import CVTPulleyCompoundParametricStudyTool
    from ._4509 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4510 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4511 import CycloidalDiscCompoundParametricStudyTool
    from ._4512 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4513 import CylindricalGearCompoundParametricStudyTool
    from ._4514 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4515 import CylindricalGearSetCompoundParametricStudyTool
    from ._4516 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4517 import DatumCompoundParametricStudyTool
    from ._4518 import ExternalCADModelCompoundParametricStudyTool
    from ._4519 import FaceGearCompoundParametricStudyTool
    from ._4520 import FaceGearMeshCompoundParametricStudyTool
    from ._4521 import FaceGearSetCompoundParametricStudyTool
    from ._4522 import FEPartCompoundParametricStudyTool
    from ._4523 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4524 import GearCompoundParametricStudyTool
    from ._4525 import GearMeshCompoundParametricStudyTool
    from ._4526 import GearSetCompoundParametricStudyTool
    from ._4527 import GuideDxfModelCompoundParametricStudyTool
    from ._4528 import HypoidGearCompoundParametricStudyTool
    from ._4529 import HypoidGearMeshCompoundParametricStudyTool
    from ._4530 import HypoidGearSetCompoundParametricStudyTool
    from ._4531 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4532 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4533 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4534 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4535 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4536 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4537 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4538 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4539 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4540 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4541 import MassDiscCompoundParametricStudyTool
    from ._4542 import MeasurementComponentCompoundParametricStudyTool
    from ._4543 import MountableComponentCompoundParametricStudyTool
    from ._4544 import OilSealCompoundParametricStudyTool
    from ._4545 import PartCompoundParametricStudyTool
    from ._4546 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4547 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4548 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4549 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4550 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4551 import PlanetCarrierCompoundParametricStudyTool
    from ._4552 import PointLoadCompoundParametricStudyTool
    from ._4553 import PowerLoadCompoundParametricStudyTool
    from ._4554 import PulleyCompoundParametricStudyTool
    from ._4555 import RingPinsCompoundParametricStudyTool
    from ._4556 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4557 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4558 import RollingRingCompoundParametricStudyTool
    from ._4559 import RollingRingConnectionCompoundParametricStudyTool
    from ._4560 import RootAssemblyCompoundParametricStudyTool
    from ._4561 import ShaftCompoundParametricStudyTool
    from ._4562 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4563 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4564 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4565 import SpiralBevelGearCompoundParametricStudyTool
    from ._4566 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4567 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4568 import SpringDamperCompoundParametricStudyTool
    from ._4569 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4570 import SpringDamperHalfCompoundParametricStudyTool
    from ._4571 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4572 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4573 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4574 import StraightBevelGearCompoundParametricStudyTool
    from ._4575 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4576 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4577 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4578 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4579 import SynchroniserCompoundParametricStudyTool
    from ._4580 import SynchroniserHalfCompoundParametricStudyTool
    from ._4581 import SynchroniserPartCompoundParametricStudyTool
    from ._4582 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4583 import TorqueConverterCompoundParametricStudyTool
    from ._4584 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4585 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4586 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4587 import UnbalancedMassCompoundParametricStudyTool
    from ._4588 import VirtualComponentCompoundParametricStudyTool
    from ._4589 import WormGearCompoundParametricStudyTool
    from ._4590 import WormGearMeshCompoundParametricStudyTool
    from ._4591 import WormGearSetCompoundParametricStudyTool
    from ._4592 import ZerolBevelGearCompoundParametricStudyTool
    from ._4593 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4594 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4466": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4467": ["AbstractShaftCompoundParametricStudyTool"],
        "_4468": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4469": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4470": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4471": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4472": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4473": ["AssemblyCompoundParametricStudyTool"],
        "_4474": ["BearingCompoundParametricStudyTool"],
        "_4475": ["BeltConnectionCompoundParametricStudyTool"],
        "_4476": ["BeltDriveCompoundParametricStudyTool"],
        "_4477": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4478": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4479": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4480": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4481": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4482": ["BevelGearCompoundParametricStudyTool"],
        "_4483": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4484": ["BevelGearSetCompoundParametricStudyTool"],
        "_4485": ["BoltCompoundParametricStudyTool"],
        "_4486": ["BoltedJointCompoundParametricStudyTool"],
        "_4487": ["ClutchCompoundParametricStudyTool"],
        "_4488": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4489": ["ClutchHalfCompoundParametricStudyTool"],
        "_4490": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4491": ["ComponentCompoundParametricStudyTool"],
        "_4492": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4493": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4494": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4495": ["ConceptGearCompoundParametricStudyTool"],
        "_4496": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4497": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4498": ["ConicalGearCompoundParametricStudyTool"],
        "_4499": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4500": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4501": ["ConnectionCompoundParametricStudyTool"],
        "_4502": ["ConnectorCompoundParametricStudyTool"],
        "_4503": ["CouplingCompoundParametricStudyTool"],
        "_4504": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4505": ["CouplingHalfCompoundParametricStudyTool"],
        "_4506": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4507": ["CVTCompoundParametricStudyTool"],
        "_4508": ["CVTPulleyCompoundParametricStudyTool"],
        "_4509": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4510": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4511": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4512": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4513": ["CylindricalGearCompoundParametricStudyTool"],
        "_4514": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4515": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4516": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4517": ["DatumCompoundParametricStudyTool"],
        "_4518": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4519": ["FaceGearCompoundParametricStudyTool"],
        "_4520": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4521": ["FaceGearSetCompoundParametricStudyTool"],
        "_4522": ["FEPartCompoundParametricStudyTool"],
        "_4523": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4524": ["GearCompoundParametricStudyTool"],
        "_4525": ["GearMeshCompoundParametricStudyTool"],
        "_4526": ["GearSetCompoundParametricStudyTool"],
        "_4527": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4528": ["HypoidGearCompoundParametricStudyTool"],
        "_4529": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4530": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4531": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4532": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4533": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4534": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4535": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4536": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4537": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4538": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4539": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4540": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4541": ["MassDiscCompoundParametricStudyTool"],
        "_4542": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4543": ["MountableComponentCompoundParametricStudyTool"],
        "_4544": ["OilSealCompoundParametricStudyTool"],
        "_4545": ["PartCompoundParametricStudyTool"],
        "_4546": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4547": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4548": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4549": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4550": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4551": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4552": ["PointLoadCompoundParametricStudyTool"],
        "_4553": ["PowerLoadCompoundParametricStudyTool"],
        "_4554": ["PulleyCompoundParametricStudyTool"],
        "_4555": ["RingPinsCompoundParametricStudyTool"],
        "_4556": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4557": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4558": ["RollingRingCompoundParametricStudyTool"],
        "_4559": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4560": ["RootAssemblyCompoundParametricStudyTool"],
        "_4561": ["ShaftCompoundParametricStudyTool"],
        "_4562": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4563": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4564": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4565": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4566": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4567": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4568": ["SpringDamperCompoundParametricStudyTool"],
        "_4569": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4570": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4571": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4572": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4573": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4574": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4575": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4576": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4577": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4578": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4579": ["SynchroniserCompoundParametricStudyTool"],
        "_4580": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4581": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4582": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4583": ["TorqueConverterCompoundParametricStudyTool"],
        "_4584": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4585": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4586": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4587": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4588": ["VirtualComponentCompoundParametricStudyTool"],
        "_4589": ["WormGearCompoundParametricStudyTool"],
        "_4590": ["WormGearMeshCompoundParametricStudyTool"],
        "_4591": ["WormGearSetCompoundParametricStudyTool"],
        "_4592": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4593": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4594": ["ZerolBevelGearSetCompoundParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundParametricStudyTool",
    "AbstractShaftCompoundParametricStudyTool",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    "AssemblyCompoundParametricStudyTool",
    "BearingCompoundParametricStudyTool",
    "BeltConnectionCompoundParametricStudyTool",
    "BeltDriveCompoundParametricStudyTool",
    "BevelDifferentialGearCompoundParametricStudyTool",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
    "BevelDifferentialGearSetCompoundParametricStudyTool",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
    "BevelDifferentialSunGearCompoundParametricStudyTool",
    "BevelGearCompoundParametricStudyTool",
    "BevelGearMeshCompoundParametricStudyTool",
    "BevelGearSetCompoundParametricStudyTool",
    "BoltCompoundParametricStudyTool",
    "BoltedJointCompoundParametricStudyTool",
    "ClutchCompoundParametricStudyTool",
    "ClutchConnectionCompoundParametricStudyTool",
    "ClutchHalfCompoundParametricStudyTool",
    "CoaxialConnectionCompoundParametricStudyTool",
    "ComponentCompoundParametricStudyTool",
    "ConceptCouplingCompoundParametricStudyTool",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
    "ConceptCouplingHalfCompoundParametricStudyTool",
    "ConceptGearCompoundParametricStudyTool",
    "ConceptGearMeshCompoundParametricStudyTool",
    "ConceptGearSetCompoundParametricStudyTool",
    "ConicalGearCompoundParametricStudyTool",
    "ConicalGearMeshCompoundParametricStudyTool",
    "ConicalGearSetCompoundParametricStudyTool",
    "ConnectionCompoundParametricStudyTool",
    "ConnectorCompoundParametricStudyTool",
    "CouplingCompoundParametricStudyTool",
    "CouplingConnectionCompoundParametricStudyTool",
    "CouplingHalfCompoundParametricStudyTool",
    "CVTBeltConnectionCompoundParametricStudyTool",
    "CVTCompoundParametricStudyTool",
    "CVTPulleyCompoundParametricStudyTool",
    "CycloidalAssemblyCompoundParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    "CycloidalDiscCompoundParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool",
    "CylindricalGearCompoundParametricStudyTool",
    "CylindricalGearMeshCompoundParametricStudyTool",
    "CylindricalGearSetCompoundParametricStudyTool",
    "CylindricalPlanetGearCompoundParametricStudyTool",
    "DatumCompoundParametricStudyTool",
    "ExternalCADModelCompoundParametricStudyTool",
    "FaceGearCompoundParametricStudyTool",
    "FaceGearMeshCompoundParametricStudyTool",
    "FaceGearSetCompoundParametricStudyTool",
    "FEPartCompoundParametricStudyTool",
    "FlexiblePinAssemblyCompoundParametricStudyTool",
    "GearCompoundParametricStudyTool",
    "GearMeshCompoundParametricStudyTool",
    "GearSetCompoundParametricStudyTool",
    "GuideDxfModelCompoundParametricStudyTool",
    "HypoidGearCompoundParametricStudyTool",
    "HypoidGearMeshCompoundParametricStudyTool",
    "HypoidGearSetCompoundParametricStudyTool",
    "InterMountableComponentConnectionCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool",
    "MassDiscCompoundParametricStudyTool",
    "MeasurementComponentCompoundParametricStudyTool",
    "MountableComponentCompoundParametricStudyTool",
    "OilSealCompoundParametricStudyTool",
    "PartCompoundParametricStudyTool",
    "PartToPartShearCouplingCompoundParametricStudyTool",
    "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
    "PlanetaryConnectionCompoundParametricStudyTool",
    "PlanetaryGearSetCompoundParametricStudyTool",
    "PlanetCarrierCompoundParametricStudyTool",
    "PointLoadCompoundParametricStudyTool",
    "PowerLoadCompoundParametricStudyTool",
    "PulleyCompoundParametricStudyTool",
    "RingPinsCompoundParametricStudyTool",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
    "RollingRingAssemblyCompoundParametricStudyTool",
    "RollingRingCompoundParametricStudyTool",
    "RollingRingConnectionCompoundParametricStudyTool",
    "RootAssemblyCompoundParametricStudyTool",
    "ShaftCompoundParametricStudyTool",
    "ShaftHubConnectionCompoundParametricStudyTool",
    "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "SpecialisedAssemblyCompoundParametricStudyTool",
    "SpiralBevelGearCompoundParametricStudyTool",
    "SpiralBevelGearMeshCompoundParametricStudyTool",
    "SpiralBevelGearSetCompoundParametricStudyTool",
    "SpringDamperCompoundParametricStudyTool",
    "SpringDamperConnectionCompoundParametricStudyTool",
    "SpringDamperHalfCompoundParametricStudyTool",
    "StraightBevelDiffGearCompoundParametricStudyTool",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
    "StraightBevelDiffGearSetCompoundParametricStudyTool",
    "StraightBevelGearCompoundParametricStudyTool",
    "StraightBevelGearMeshCompoundParametricStudyTool",
    "StraightBevelGearSetCompoundParametricStudyTool",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
    "StraightBevelSunGearCompoundParametricStudyTool",
    "SynchroniserCompoundParametricStudyTool",
    "SynchroniserHalfCompoundParametricStudyTool",
    "SynchroniserPartCompoundParametricStudyTool",
    "SynchroniserSleeveCompoundParametricStudyTool",
    "TorqueConverterCompoundParametricStudyTool",
    "TorqueConverterConnectionCompoundParametricStudyTool",
    "TorqueConverterPumpCompoundParametricStudyTool",
    "TorqueConverterTurbineCompoundParametricStudyTool",
    "UnbalancedMassCompoundParametricStudyTool",
    "VirtualComponentCompoundParametricStudyTool",
    "WormGearCompoundParametricStudyTool",
    "WormGearMeshCompoundParametricStudyTool",
    "WormGearSetCompoundParametricStudyTool",
    "ZerolBevelGearCompoundParametricStudyTool",
    "ZerolBevelGearMeshCompoundParametricStudyTool",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)
