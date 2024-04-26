"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3527 import AbstractAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3528 import AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
    from ._3529 import AbstractShaftSteadyStateSynchronousResponseAtASpeed
    from ._3530 import (
        AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3531 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3532 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3533 import AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3534 import AssemblySteadyStateSynchronousResponseAtASpeed
    from ._3535 import BearingSteadyStateSynchronousResponseAtASpeed
    from ._3536 import BeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3537 import BeltDriveSteadyStateSynchronousResponseAtASpeed
    from ._3538 import BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3539 import BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3540 import BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
    from ._3541 import BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3542 import BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3543 import BevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3544 import BevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3545 import BevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3546 import BoltedJointSteadyStateSynchronousResponseAtASpeed
    from ._3547 import BoltSteadyStateSynchronousResponseAtASpeed
    from ._3548 import ClutchConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3549 import ClutchHalfSteadyStateSynchronousResponseAtASpeed
    from ._3550 import ClutchSteadyStateSynchronousResponseAtASpeed
    from ._3551 import CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3552 import ComponentSteadyStateSynchronousResponseAtASpeed
    from ._3553 import ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3554 import ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3555 import ConceptCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3556 import ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3557 import ConceptGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3558 import ConceptGearSteadyStateSynchronousResponseAtASpeed
    from ._3559 import ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3560 import ConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3561 import ConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3562 import ConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3563 import ConnectorSteadyStateSynchronousResponseAtASpeed
    from ._3564 import CouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3565 import CouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3566 import CouplingSteadyStateSynchronousResponseAtASpeed
    from ._3567 import CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3568 import CVTPulleySteadyStateSynchronousResponseAtASpeed
    from ._3569 import CVTSteadyStateSynchronousResponseAtASpeed
    from ._3570 import CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3571 import (
        CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3572 import (
        CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3573 import CycloidalDiscSteadyStateSynchronousResponseAtASpeed
    from ._3574 import CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3575 import CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3576 import CylindricalGearSteadyStateSynchronousResponseAtASpeed
    from ._3577 import CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3578 import DatumSteadyStateSynchronousResponseAtASpeed
    from ._3579 import ExternalCADModelSteadyStateSynchronousResponseAtASpeed
    from ._3580 import FaceGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3581 import FaceGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3582 import FaceGearSteadyStateSynchronousResponseAtASpeed
    from ._3583 import FEPartSteadyStateSynchronousResponseAtASpeed
    from ._3584 import FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3585 import GearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3586 import GearSetSteadyStateSynchronousResponseAtASpeed
    from ._3587 import GearSteadyStateSynchronousResponseAtASpeed
    from ._3588 import GuideDxfModelSteadyStateSynchronousResponseAtASpeed
    from ._3589 import HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3590 import HypoidGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3591 import HypoidGearSteadyStateSynchronousResponseAtASpeed
    from ._3592 import (
        InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3593 import (
        KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3594 import (
        KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3595 import (
        KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3596 import (
        KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3597 import (
        KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3598 import (
        KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3599 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3600 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3601 import (
        KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3602 import MassDiscSteadyStateSynchronousResponseAtASpeed
    from ._3603 import MeasurementComponentSteadyStateSynchronousResponseAtASpeed
    from ._3604 import MountableComponentSteadyStateSynchronousResponseAtASpeed
    from ._3605 import OilSealSteadyStateSynchronousResponseAtASpeed
    from ._3606 import PartSteadyStateSynchronousResponseAtASpeed
    from ._3607 import (
        PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3608 import PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3609 import PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3610 import PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3611 import PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3612 import PlanetCarrierSteadyStateSynchronousResponseAtASpeed
    from ._3613 import PointLoadSteadyStateSynchronousResponseAtASpeed
    from ._3614 import PowerLoadSteadyStateSynchronousResponseAtASpeed
    from ._3615 import PulleySteadyStateSynchronousResponseAtASpeed
    from ._3616 import RingPinsSteadyStateSynchronousResponseAtASpeed
    from ._3617 import RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3618 import RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3619 import RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3620 import RollingRingSteadyStateSynchronousResponseAtASpeed
    from ._3621 import RootAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3622 import ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3623 import ShaftSteadyStateSynchronousResponseAtASpeed
    from ._3624 import (
        ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3625 import SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3626 import SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3627 import SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3628 import SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3629 import SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3630 import SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
    from ._3631 import SpringDamperSteadyStateSynchronousResponseAtASpeed
    from ._3632 import SteadyStateSynchronousResponseAtASpeed
    from ._3633 import StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3634 import StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3635 import StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
    from ._3636 import StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3637 import StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3638 import StraightBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3639 import StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3640 import StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3641 import SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
    from ._3642 import SynchroniserPartSteadyStateSynchronousResponseAtASpeed
    from ._3643 import SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
    from ._3644 import SynchroniserSteadyStateSynchronousResponseAtASpeed
    from ._3645 import TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3646 import TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
    from ._3647 import TorqueConverterSteadyStateSynchronousResponseAtASpeed
    from ._3648 import TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
    from ._3649 import UnbalancedMassSteadyStateSynchronousResponseAtASpeed
    from ._3650 import VirtualComponentSteadyStateSynchronousResponseAtASpeed
    from ._3651 import WormGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3652 import WormGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3653 import WormGearSteadyStateSynchronousResponseAtASpeed
    from ._3654 import ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3655 import ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3656 import ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3527": ["AbstractAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3528": ["AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed"],
        "_3529": ["AbstractShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3530": [
            "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3531": ["AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3532": ["AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3533": ["AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3534": ["AssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3535": ["BearingSteadyStateSynchronousResponseAtASpeed"],
        "_3536": ["BeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3537": ["BeltDriveSteadyStateSynchronousResponseAtASpeed"],
        "_3538": ["BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3539": ["BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3540": ["BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed"],
        "_3541": ["BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3542": ["BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3543": ["BevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3544": ["BevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3545": ["BevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3546": ["BoltedJointSteadyStateSynchronousResponseAtASpeed"],
        "_3547": ["BoltSteadyStateSynchronousResponseAtASpeed"],
        "_3548": ["ClutchConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3549": ["ClutchHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3550": ["ClutchSteadyStateSynchronousResponseAtASpeed"],
        "_3551": ["CoaxialConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3552": ["ComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3553": ["ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3554": ["ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3555": ["ConceptCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3556": ["ConceptGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3557": ["ConceptGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3558": ["ConceptGearSteadyStateSynchronousResponseAtASpeed"],
        "_3559": ["ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3560": ["ConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3561": ["ConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3562": ["ConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3563": ["ConnectorSteadyStateSynchronousResponseAtASpeed"],
        "_3564": ["CouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3565": ["CouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3566": ["CouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3567": ["CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3568": ["CVTPulleySteadyStateSynchronousResponseAtASpeed"],
        "_3569": ["CVTSteadyStateSynchronousResponseAtASpeed"],
        "_3570": ["CycloidalAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3571": [
            "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3572": [
            "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3573": ["CycloidalDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3574": ["CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3575": ["CylindricalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3576": ["CylindricalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3577": ["CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3578": ["DatumSteadyStateSynchronousResponseAtASpeed"],
        "_3579": ["ExternalCADModelSteadyStateSynchronousResponseAtASpeed"],
        "_3580": ["FaceGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3581": ["FaceGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3582": ["FaceGearSteadyStateSynchronousResponseAtASpeed"],
        "_3583": ["FEPartSteadyStateSynchronousResponseAtASpeed"],
        "_3584": ["FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3585": ["GearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3586": ["GearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3587": ["GearSteadyStateSynchronousResponseAtASpeed"],
        "_3588": ["GuideDxfModelSteadyStateSynchronousResponseAtASpeed"],
        "_3589": ["HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3590": ["HypoidGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3591": ["HypoidGearSteadyStateSynchronousResponseAtASpeed"],
        "_3592": [
            "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3593": [
            "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3594": [
            "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3595": [
            "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3596": [
            "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3597": [
            "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3598": [
            "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3599": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3600": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3601": [
            "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3602": ["MassDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3603": ["MeasurementComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3604": ["MountableComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3605": ["OilSealSteadyStateSynchronousResponseAtASpeed"],
        "_3606": ["PartSteadyStateSynchronousResponseAtASpeed"],
        "_3607": [
            "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3608": ["PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3609": ["PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3610": ["PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3611": ["PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3612": ["PlanetCarrierSteadyStateSynchronousResponseAtASpeed"],
        "_3613": ["PointLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3614": ["PowerLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3615": ["PulleySteadyStateSynchronousResponseAtASpeed"],
        "_3616": ["RingPinsSteadyStateSynchronousResponseAtASpeed"],
        "_3617": ["RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3618": ["RollingRingAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3619": ["RollingRingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3620": ["RollingRingSteadyStateSynchronousResponseAtASpeed"],
        "_3621": ["RootAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3622": ["ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3623": ["ShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3624": [
            "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3625": ["SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3626": ["SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3627": ["SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3628": ["SpiralBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3629": ["SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3630": ["SpringDamperHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3631": ["SpringDamperSteadyStateSynchronousResponseAtASpeed"],
        "_3632": ["SteadyStateSynchronousResponseAtASpeed"],
        "_3633": ["StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3634": ["StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3635": ["StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed"],
        "_3636": ["StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3637": ["StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3638": ["StraightBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3639": ["StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3640": ["StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3641": ["SynchroniserHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3642": ["SynchroniserPartSteadyStateSynchronousResponseAtASpeed"],
        "_3643": ["SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed"],
        "_3644": ["SynchroniserSteadyStateSynchronousResponseAtASpeed"],
        "_3645": ["TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3646": ["TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed"],
        "_3647": ["TorqueConverterSteadyStateSynchronousResponseAtASpeed"],
        "_3648": ["TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed"],
        "_3649": ["UnbalancedMassSteadyStateSynchronousResponseAtASpeed"],
        "_3650": ["VirtualComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3651": ["WormGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3652": ["WormGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3653": ["WormGearSteadyStateSynchronousResponseAtASpeed"],
        "_3654": ["ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3655": ["ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3656": ["ZerolBevelGearSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
    "AssemblySteadyStateSynchronousResponseAtASpeed",
    "BearingSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointSteadyStateSynchronousResponseAtASpeed",
    "BoltSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfSteadyStateSynchronousResponseAtASpeed",
    "ClutchSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
    "ComponentSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSteadyStateSynchronousResponseAtASpeed",
    "ConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConnectorSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "CouplingSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleySteadyStateSynchronousResponseAtASpeed",
    "CVTSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "DatumSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSteadyStateSynchronousResponseAtASpeed",
    "FEPartSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed",
    "GearMeshSteadyStateSynchronousResponseAtASpeed",
    "GearSetSteadyStateSynchronousResponseAtASpeed",
    "GearSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "MassDiscSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentSteadyStateSynchronousResponseAtASpeed",
    "OilSealSteadyStateSynchronousResponseAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
    "PointLoadSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadSteadyStateSynchronousResponseAtASpeed",
    "PulleySteadyStateSynchronousResponseAtASpeed",
    "RingPinsSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblySteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblySteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed",
    "ShaftSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperSteadyStateSynchronousResponseAtASpeed",
    "SteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetSteadyStateSynchronousResponseAtASpeed",
    "WormGearSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
)
