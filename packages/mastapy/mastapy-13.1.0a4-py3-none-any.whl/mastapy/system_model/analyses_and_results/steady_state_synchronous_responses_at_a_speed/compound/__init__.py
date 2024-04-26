"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3657 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3658 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3659 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3660 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3661 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3662 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3663 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3664 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3667 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3668 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3669 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3670 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3671 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3672 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3673 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3676 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3677 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3678 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3679 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3681 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3682 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3683 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3685 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3687 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3689 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3693 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3697 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3698 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3699 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3700 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3701 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3702 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3703 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3704 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3705 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3706 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3707 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3708 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3709 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3710 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3711 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3712 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3713 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3714 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3715 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3716 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3717 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3719 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3721 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3722 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3723 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3724 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3725 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3726 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3727 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3728 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3729 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3730 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3731 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3732 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3733 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3734 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3735 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3736 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3737 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3738 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3739 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3740 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3741 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3742 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3743 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3744 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3745 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3746 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3747 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3748 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3749 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3750 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3751 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3752 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3753 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3754 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3755 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3756 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3757 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3758 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3759 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3760 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3761 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3762 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3763 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3764 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3765 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3766 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3767 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3768 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3769 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3770 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3771 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3772 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3773 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3774 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3775 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3776 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3777 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3778 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3779 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3780 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3781 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3782 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3783 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3784 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3785 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3657": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3658": ["AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3659": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3660": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3661": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3662": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3663": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3664": ["AssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3665": ["BearingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3666": ["BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3667": ["BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3668": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3669": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3670": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3671": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3672": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3673": ["BevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3674": ["BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3675": ["BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3676": ["BoltCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3677": ["BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3678": ["ClutchCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3679": ["ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3680": ["ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3681": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3682": ["ComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3683": ["ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3684": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3685": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3686": ["ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3687": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3688": ["ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3689": ["ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3690": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3691": ["ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3692": ["ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3693": ["ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3694": ["CouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3695": ["CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3696": ["CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3697": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3698": ["CVTCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3699": ["CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3700": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3701": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3702": ["CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3703": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3704": ["CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3705": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3706": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3707": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3708": ["DatumCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3709": ["ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3710": ["FaceGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3711": ["FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3712": ["FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3713": ["FEPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3714": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3715": ["GearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3716": ["GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3717": ["GearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3718": ["GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3719": ["HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3720": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3721": ["HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3722": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3723": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3724": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3725": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3726": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3727": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3728": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3729": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3730": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3731": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3732": ["MassDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3733": ["MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3734": ["MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3735": ["OilSealCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3736": ["PartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3737": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3738": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3739": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3740": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3741": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3742": ["PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3743": ["PointLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3744": ["PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3745": ["PulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3746": ["RingPinsCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3747": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3748": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3749": ["RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3750": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3751": ["RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3752": ["ShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3753": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3754": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3755": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3756": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3757": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3758": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3759": ["SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3760": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3761": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3762": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3763": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3764": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3765": ["StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3766": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3767": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3768": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3769": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3770": ["SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3771": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3772": ["SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3773": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3774": ["TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3775": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3776": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3777": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3778": ["UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3779": ["VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3780": ["WormGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3781": ["WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3782": ["WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3783": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3784": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3785": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "AssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "DatumCompoundSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "FEPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "MassDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "OilSealCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed",
    "PointLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)
