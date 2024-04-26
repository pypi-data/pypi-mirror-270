"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3398 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3399 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3400 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3401 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3402 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3403 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3404 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3405 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3408 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3409 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3410 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3411 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3412 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3413 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3414 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3417 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3418 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3419 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3420 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3422 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3423 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3424 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3426 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3428 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3430 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3434 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3438 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3439 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3440 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3441 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3442 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3443 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3444 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3445 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3446 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3447 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3448 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3449 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3450 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3451 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3452 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3453 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3454 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3455 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3456 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3457 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3458 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3460 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3462 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3463 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3464 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3465 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3466 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3467 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3468 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3469 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3470 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3471 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3472 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3473 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3474 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3475 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3476 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3477 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3478 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3479 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3480 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3481 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3482 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3483 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3484 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3485 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3486 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3487 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3488 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3489 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3490 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3491 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3492 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3493 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3494 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3495 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3496 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3497 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3498 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3499 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3500 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3501 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3502 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3503 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3504 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3505 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3506 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3507 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3508 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3509 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3510 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3511 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3512 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3513 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3514 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3515 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3516 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3517 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3518 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3519 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3520 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3521 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3522 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3523 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3524 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3525 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3526 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        "_3398": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3399": ["AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3400": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3401": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3402": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3403": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3404": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3405": ["AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3406": ["BearingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3407": ["BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3408": ["BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3409": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3410": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3411": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3412": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3413": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3414": ["BevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3415": ["BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3416": ["BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3417": ["BoltCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3418": ["BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3419": ["ClutchCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3420": ["ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3421": ["ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3422": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3423": ["ComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3424": ["ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3425": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3426": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3427": ["ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3428": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3429": ["ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3430": ["ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3431": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3432": ["ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3433": ["ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3434": ["ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3435": ["CouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3436": ["CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3437": ["CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3438": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3439": ["CVTCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3440": ["CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3441": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3442": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3443": ["CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3444": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3445": ["CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3446": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3447": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3448": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3449": ["DatumCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3450": ["ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3451": ["FaceGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3452": ["FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3453": ["FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3454": ["FEPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3455": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3456": ["GearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3457": ["GearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3458": ["GearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3459": ["GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3460": ["HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3461": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3462": ["HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3463": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3464": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3465": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3466": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3467": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3468": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3469": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3470": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3471": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3472": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3473": ["MassDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3474": ["MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3475": ["MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3476": ["OilSealCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3477": ["PartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3478": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3479": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3480": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3481": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3482": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3483": ["PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3484": ["PointLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3485": ["PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3486": ["PulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3487": ["RingPinsCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3488": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3489": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3490": ["RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3491": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3492": ["RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3493": ["ShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3494": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3495": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3496": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3497": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3498": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3499": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3500": ["SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3501": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3502": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3503": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3504": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3505": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3506": ["StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3507": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3508": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3509": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3510": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3511": ["SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3512": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3513": ["SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3514": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3515": ["TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3516": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3517": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3518": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3519": ["UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3520": ["VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3521": ["WormGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3522": ["WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3523": ["WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3524": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3525": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3526": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "BearingCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "FEPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "MassDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "OilSealCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft",
    "PointLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft",
    "VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)
