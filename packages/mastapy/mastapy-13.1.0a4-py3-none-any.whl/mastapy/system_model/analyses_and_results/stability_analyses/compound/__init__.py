"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3920 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3921 import AbstractShaftCompoundStabilityAnalysis
    from ._3922 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3923 import (
        AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis,
    )
    from ._3924 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3925 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3926 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3927 import AssemblyCompoundStabilityAnalysis
    from ._3928 import BearingCompoundStabilityAnalysis
    from ._3929 import BeltConnectionCompoundStabilityAnalysis
    from ._3930 import BeltDriveCompoundStabilityAnalysis
    from ._3931 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3932 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3933 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3934 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3935 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3936 import BevelGearCompoundStabilityAnalysis
    from ._3937 import BevelGearMeshCompoundStabilityAnalysis
    from ._3938 import BevelGearSetCompoundStabilityAnalysis
    from ._3939 import BoltCompoundStabilityAnalysis
    from ._3940 import BoltedJointCompoundStabilityAnalysis
    from ._3941 import ClutchCompoundStabilityAnalysis
    from ._3942 import ClutchConnectionCompoundStabilityAnalysis
    from ._3943 import ClutchHalfCompoundStabilityAnalysis
    from ._3944 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3945 import ComponentCompoundStabilityAnalysis
    from ._3946 import ConceptCouplingCompoundStabilityAnalysis
    from ._3947 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3948 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3949 import ConceptGearCompoundStabilityAnalysis
    from ._3950 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3951 import ConceptGearSetCompoundStabilityAnalysis
    from ._3952 import ConicalGearCompoundStabilityAnalysis
    from ._3953 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3954 import ConicalGearSetCompoundStabilityAnalysis
    from ._3955 import ConnectionCompoundStabilityAnalysis
    from ._3956 import ConnectorCompoundStabilityAnalysis
    from ._3957 import CouplingCompoundStabilityAnalysis
    from ._3958 import CouplingConnectionCompoundStabilityAnalysis
    from ._3959 import CouplingHalfCompoundStabilityAnalysis
    from ._3960 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3961 import CVTCompoundStabilityAnalysis
    from ._3962 import CVTPulleyCompoundStabilityAnalysis
    from ._3963 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3964 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3965 import CycloidalDiscCompoundStabilityAnalysis
    from ._3966 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3967 import CylindricalGearCompoundStabilityAnalysis
    from ._3968 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3969 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3970 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3971 import DatumCompoundStabilityAnalysis
    from ._3972 import ExternalCADModelCompoundStabilityAnalysis
    from ._3973 import FaceGearCompoundStabilityAnalysis
    from ._3974 import FaceGearMeshCompoundStabilityAnalysis
    from ._3975 import FaceGearSetCompoundStabilityAnalysis
    from ._3976 import FEPartCompoundStabilityAnalysis
    from ._3977 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3978 import GearCompoundStabilityAnalysis
    from ._3979 import GearMeshCompoundStabilityAnalysis
    from ._3980 import GearSetCompoundStabilityAnalysis
    from ._3981 import GuideDxfModelCompoundStabilityAnalysis
    from ._3982 import HypoidGearCompoundStabilityAnalysis
    from ._3983 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3984 import HypoidGearSetCompoundStabilityAnalysis
    from ._3985 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3986 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3987 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3988 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3989 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3990 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3991 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3992 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3993 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis,
    )
    from ._3994 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis,
    )
    from ._3995 import MassDiscCompoundStabilityAnalysis
    from ._3996 import MeasurementComponentCompoundStabilityAnalysis
    from ._3997 import MountableComponentCompoundStabilityAnalysis
    from ._3998 import OilSealCompoundStabilityAnalysis
    from ._3999 import PartCompoundStabilityAnalysis
    from ._4000 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._4001 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._4002 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._4003 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._4004 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._4005 import PlanetCarrierCompoundStabilityAnalysis
    from ._4006 import PointLoadCompoundStabilityAnalysis
    from ._4007 import PowerLoadCompoundStabilityAnalysis
    from ._4008 import PulleyCompoundStabilityAnalysis
    from ._4009 import RingPinsCompoundStabilityAnalysis
    from ._4010 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._4011 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._4012 import RollingRingCompoundStabilityAnalysis
    from ._4013 import RollingRingConnectionCompoundStabilityAnalysis
    from ._4014 import RootAssemblyCompoundStabilityAnalysis
    from ._4015 import ShaftCompoundStabilityAnalysis
    from ._4016 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._4017 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._4018 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._4019 import SpiralBevelGearCompoundStabilityAnalysis
    from ._4020 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._4021 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._4022 import SpringDamperCompoundStabilityAnalysis
    from ._4023 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._4024 import SpringDamperHalfCompoundStabilityAnalysis
    from ._4025 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._4026 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._4027 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._4028 import StraightBevelGearCompoundStabilityAnalysis
    from ._4029 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._4030 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._4031 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._4032 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._4033 import SynchroniserCompoundStabilityAnalysis
    from ._4034 import SynchroniserHalfCompoundStabilityAnalysis
    from ._4035 import SynchroniserPartCompoundStabilityAnalysis
    from ._4036 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._4037 import TorqueConverterCompoundStabilityAnalysis
    from ._4038 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._4039 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._4040 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._4041 import UnbalancedMassCompoundStabilityAnalysis
    from ._4042 import VirtualComponentCompoundStabilityAnalysis
    from ._4043 import WormGearCompoundStabilityAnalysis
    from ._4044 import WormGearMeshCompoundStabilityAnalysis
    from ._4045 import WormGearSetCompoundStabilityAnalysis
    from ._4046 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4047 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4048 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        "_3920": ["AbstractAssemblyCompoundStabilityAnalysis"],
        "_3921": ["AbstractShaftCompoundStabilityAnalysis"],
        "_3922": ["AbstractShaftOrHousingCompoundStabilityAnalysis"],
        "_3923": [
            "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ],
        "_3924": ["AGMAGleasonConicalGearCompoundStabilityAnalysis"],
        "_3925": ["AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"],
        "_3926": ["AGMAGleasonConicalGearSetCompoundStabilityAnalysis"],
        "_3927": ["AssemblyCompoundStabilityAnalysis"],
        "_3928": ["BearingCompoundStabilityAnalysis"],
        "_3929": ["BeltConnectionCompoundStabilityAnalysis"],
        "_3930": ["BeltDriveCompoundStabilityAnalysis"],
        "_3931": ["BevelDifferentialGearCompoundStabilityAnalysis"],
        "_3932": ["BevelDifferentialGearMeshCompoundStabilityAnalysis"],
        "_3933": ["BevelDifferentialGearSetCompoundStabilityAnalysis"],
        "_3934": ["BevelDifferentialPlanetGearCompoundStabilityAnalysis"],
        "_3935": ["BevelDifferentialSunGearCompoundStabilityAnalysis"],
        "_3936": ["BevelGearCompoundStabilityAnalysis"],
        "_3937": ["BevelGearMeshCompoundStabilityAnalysis"],
        "_3938": ["BevelGearSetCompoundStabilityAnalysis"],
        "_3939": ["BoltCompoundStabilityAnalysis"],
        "_3940": ["BoltedJointCompoundStabilityAnalysis"],
        "_3941": ["ClutchCompoundStabilityAnalysis"],
        "_3942": ["ClutchConnectionCompoundStabilityAnalysis"],
        "_3943": ["ClutchHalfCompoundStabilityAnalysis"],
        "_3944": ["CoaxialConnectionCompoundStabilityAnalysis"],
        "_3945": ["ComponentCompoundStabilityAnalysis"],
        "_3946": ["ConceptCouplingCompoundStabilityAnalysis"],
        "_3947": ["ConceptCouplingConnectionCompoundStabilityAnalysis"],
        "_3948": ["ConceptCouplingHalfCompoundStabilityAnalysis"],
        "_3949": ["ConceptGearCompoundStabilityAnalysis"],
        "_3950": ["ConceptGearMeshCompoundStabilityAnalysis"],
        "_3951": ["ConceptGearSetCompoundStabilityAnalysis"],
        "_3952": ["ConicalGearCompoundStabilityAnalysis"],
        "_3953": ["ConicalGearMeshCompoundStabilityAnalysis"],
        "_3954": ["ConicalGearSetCompoundStabilityAnalysis"],
        "_3955": ["ConnectionCompoundStabilityAnalysis"],
        "_3956": ["ConnectorCompoundStabilityAnalysis"],
        "_3957": ["CouplingCompoundStabilityAnalysis"],
        "_3958": ["CouplingConnectionCompoundStabilityAnalysis"],
        "_3959": ["CouplingHalfCompoundStabilityAnalysis"],
        "_3960": ["CVTBeltConnectionCompoundStabilityAnalysis"],
        "_3961": ["CVTCompoundStabilityAnalysis"],
        "_3962": ["CVTPulleyCompoundStabilityAnalysis"],
        "_3963": ["CycloidalAssemblyCompoundStabilityAnalysis"],
        "_3964": ["CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"],
        "_3965": ["CycloidalDiscCompoundStabilityAnalysis"],
        "_3966": ["CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis"],
        "_3967": ["CylindricalGearCompoundStabilityAnalysis"],
        "_3968": ["CylindricalGearMeshCompoundStabilityAnalysis"],
        "_3969": ["CylindricalGearSetCompoundStabilityAnalysis"],
        "_3970": ["CylindricalPlanetGearCompoundStabilityAnalysis"],
        "_3971": ["DatumCompoundStabilityAnalysis"],
        "_3972": ["ExternalCADModelCompoundStabilityAnalysis"],
        "_3973": ["FaceGearCompoundStabilityAnalysis"],
        "_3974": ["FaceGearMeshCompoundStabilityAnalysis"],
        "_3975": ["FaceGearSetCompoundStabilityAnalysis"],
        "_3976": ["FEPartCompoundStabilityAnalysis"],
        "_3977": ["FlexiblePinAssemblyCompoundStabilityAnalysis"],
        "_3978": ["GearCompoundStabilityAnalysis"],
        "_3979": ["GearMeshCompoundStabilityAnalysis"],
        "_3980": ["GearSetCompoundStabilityAnalysis"],
        "_3981": ["GuideDxfModelCompoundStabilityAnalysis"],
        "_3982": ["HypoidGearCompoundStabilityAnalysis"],
        "_3983": ["HypoidGearMeshCompoundStabilityAnalysis"],
        "_3984": ["HypoidGearSetCompoundStabilityAnalysis"],
        "_3985": ["InterMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3986": ["KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"],
        "_3987": ["KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"],
        "_3988": ["KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"],
        "_3989": ["KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"],
        "_3990": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"],
        "_3991": ["KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"],
        "_3992": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis"],
        "_3993": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ],
        "_3994": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ],
        "_3995": ["MassDiscCompoundStabilityAnalysis"],
        "_3996": ["MeasurementComponentCompoundStabilityAnalysis"],
        "_3997": ["MountableComponentCompoundStabilityAnalysis"],
        "_3998": ["OilSealCompoundStabilityAnalysis"],
        "_3999": ["PartCompoundStabilityAnalysis"],
        "_4000": ["PartToPartShearCouplingCompoundStabilityAnalysis"],
        "_4001": ["PartToPartShearCouplingConnectionCompoundStabilityAnalysis"],
        "_4002": ["PartToPartShearCouplingHalfCompoundStabilityAnalysis"],
        "_4003": ["PlanetaryConnectionCompoundStabilityAnalysis"],
        "_4004": ["PlanetaryGearSetCompoundStabilityAnalysis"],
        "_4005": ["PlanetCarrierCompoundStabilityAnalysis"],
        "_4006": ["PointLoadCompoundStabilityAnalysis"],
        "_4007": ["PowerLoadCompoundStabilityAnalysis"],
        "_4008": ["PulleyCompoundStabilityAnalysis"],
        "_4009": ["RingPinsCompoundStabilityAnalysis"],
        "_4010": ["RingPinsToDiscConnectionCompoundStabilityAnalysis"],
        "_4011": ["RollingRingAssemblyCompoundStabilityAnalysis"],
        "_4012": ["RollingRingCompoundStabilityAnalysis"],
        "_4013": ["RollingRingConnectionCompoundStabilityAnalysis"],
        "_4014": ["RootAssemblyCompoundStabilityAnalysis"],
        "_4015": ["ShaftCompoundStabilityAnalysis"],
        "_4016": ["ShaftHubConnectionCompoundStabilityAnalysis"],
        "_4017": ["ShaftToMountableComponentConnectionCompoundStabilityAnalysis"],
        "_4018": ["SpecialisedAssemblyCompoundStabilityAnalysis"],
        "_4019": ["SpiralBevelGearCompoundStabilityAnalysis"],
        "_4020": ["SpiralBevelGearMeshCompoundStabilityAnalysis"],
        "_4021": ["SpiralBevelGearSetCompoundStabilityAnalysis"],
        "_4022": ["SpringDamperCompoundStabilityAnalysis"],
        "_4023": ["SpringDamperConnectionCompoundStabilityAnalysis"],
        "_4024": ["SpringDamperHalfCompoundStabilityAnalysis"],
        "_4025": ["StraightBevelDiffGearCompoundStabilityAnalysis"],
        "_4026": ["StraightBevelDiffGearMeshCompoundStabilityAnalysis"],
        "_4027": ["StraightBevelDiffGearSetCompoundStabilityAnalysis"],
        "_4028": ["StraightBevelGearCompoundStabilityAnalysis"],
        "_4029": ["StraightBevelGearMeshCompoundStabilityAnalysis"],
        "_4030": ["StraightBevelGearSetCompoundStabilityAnalysis"],
        "_4031": ["StraightBevelPlanetGearCompoundStabilityAnalysis"],
        "_4032": ["StraightBevelSunGearCompoundStabilityAnalysis"],
        "_4033": ["SynchroniserCompoundStabilityAnalysis"],
        "_4034": ["SynchroniserHalfCompoundStabilityAnalysis"],
        "_4035": ["SynchroniserPartCompoundStabilityAnalysis"],
        "_4036": ["SynchroniserSleeveCompoundStabilityAnalysis"],
        "_4037": ["TorqueConverterCompoundStabilityAnalysis"],
        "_4038": ["TorqueConverterConnectionCompoundStabilityAnalysis"],
        "_4039": ["TorqueConverterPumpCompoundStabilityAnalysis"],
        "_4040": ["TorqueConverterTurbineCompoundStabilityAnalysis"],
        "_4041": ["UnbalancedMassCompoundStabilityAnalysis"],
        "_4042": ["VirtualComponentCompoundStabilityAnalysis"],
        "_4043": ["WormGearCompoundStabilityAnalysis"],
        "_4044": ["WormGearMeshCompoundStabilityAnalysis"],
        "_4045": ["WormGearSetCompoundStabilityAnalysis"],
        "_4046": ["ZerolBevelGearCompoundStabilityAnalysis"],
        "_4047": ["ZerolBevelGearMeshCompoundStabilityAnalysis"],
        "_4048": ["ZerolBevelGearSetCompoundStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundStabilityAnalysis",
    "AbstractShaftCompoundStabilityAnalysis",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
    "AssemblyCompoundStabilityAnalysis",
    "BearingCompoundStabilityAnalysis",
    "BeltConnectionCompoundStabilityAnalysis",
    "BeltDriveCompoundStabilityAnalysis",
    "BevelDifferentialGearCompoundStabilityAnalysis",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
    "BevelDifferentialGearSetCompoundStabilityAnalysis",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
    "BevelGearCompoundStabilityAnalysis",
    "BevelGearMeshCompoundStabilityAnalysis",
    "BevelGearSetCompoundStabilityAnalysis",
    "BoltCompoundStabilityAnalysis",
    "BoltedJointCompoundStabilityAnalysis",
    "ClutchCompoundStabilityAnalysis",
    "ClutchConnectionCompoundStabilityAnalysis",
    "ClutchHalfCompoundStabilityAnalysis",
    "CoaxialConnectionCompoundStabilityAnalysis",
    "ComponentCompoundStabilityAnalysis",
    "ConceptCouplingCompoundStabilityAnalysis",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
    "ConceptCouplingHalfCompoundStabilityAnalysis",
    "ConceptGearCompoundStabilityAnalysis",
    "ConceptGearMeshCompoundStabilityAnalysis",
    "ConceptGearSetCompoundStabilityAnalysis",
    "ConicalGearCompoundStabilityAnalysis",
    "ConicalGearMeshCompoundStabilityAnalysis",
    "ConicalGearSetCompoundStabilityAnalysis",
    "ConnectionCompoundStabilityAnalysis",
    "ConnectorCompoundStabilityAnalysis",
    "CouplingCompoundStabilityAnalysis",
    "CouplingConnectionCompoundStabilityAnalysis",
    "CouplingHalfCompoundStabilityAnalysis",
    "CVTBeltConnectionCompoundStabilityAnalysis",
    "CVTCompoundStabilityAnalysis",
    "CVTPulleyCompoundStabilityAnalysis",
    "CycloidalAssemblyCompoundStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    "CycloidalDiscCompoundStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis",
    "CylindricalGearCompoundStabilityAnalysis",
    "CylindricalGearMeshCompoundStabilityAnalysis",
    "CylindricalGearSetCompoundStabilityAnalysis",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
    "DatumCompoundStabilityAnalysis",
    "ExternalCADModelCompoundStabilityAnalysis",
    "FaceGearCompoundStabilityAnalysis",
    "FaceGearMeshCompoundStabilityAnalysis",
    "FaceGearSetCompoundStabilityAnalysis",
    "FEPartCompoundStabilityAnalysis",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
    "GearCompoundStabilityAnalysis",
    "GearMeshCompoundStabilityAnalysis",
    "GearSetCompoundStabilityAnalysis",
    "GuideDxfModelCompoundStabilityAnalysis",
    "HypoidGearCompoundStabilityAnalysis",
    "HypoidGearMeshCompoundStabilityAnalysis",
    "HypoidGearSetCompoundStabilityAnalysis",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    "MassDiscCompoundStabilityAnalysis",
    "MeasurementComponentCompoundStabilityAnalysis",
    "MountableComponentCompoundStabilityAnalysis",
    "OilSealCompoundStabilityAnalysis",
    "PartCompoundStabilityAnalysis",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    "PartToPartShearCouplingHalfCompoundStabilityAnalysis",
    "PlanetaryConnectionCompoundStabilityAnalysis",
    "PlanetaryGearSetCompoundStabilityAnalysis",
    "PlanetCarrierCompoundStabilityAnalysis",
    "PointLoadCompoundStabilityAnalysis",
    "PowerLoadCompoundStabilityAnalysis",
    "PulleyCompoundStabilityAnalysis",
    "RingPinsCompoundStabilityAnalysis",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
    "RollingRingAssemblyCompoundStabilityAnalysis",
    "RollingRingCompoundStabilityAnalysis",
    "RollingRingConnectionCompoundStabilityAnalysis",
    "RootAssemblyCompoundStabilityAnalysis",
    "ShaftCompoundStabilityAnalysis",
    "ShaftHubConnectionCompoundStabilityAnalysis",
    "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
    "SpiralBevelGearCompoundStabilityAnalysis",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
    "SpringDamperCompoundStabilityAnalysis",
    "SpringDamperConnectionCompoundStabilityAnalysis",
    "SpringDamperHalfCompoundStabilityAnalysis",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
    "StraightBevelGearCompoundStabilityAnalysis",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
    "StraightBevelGearSetCompoundStabilityAnalysis",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
    "StraightBevelSunGearCompoundStabilityAnalysis",
    "SynchroniserCompoundStabilityAnalysis",
    "SynchroniserHalfCompoundStabilityAnalysis",
    "SynchroniserPartCompoundStabilityAnalysis",
    "SynchroniserSleeveCompoundStabilityAnalysis",
    "TorqueConverterCompoundStabilityAnalysis",
    "TorqueConverterConnectionCompoundStabilityAnalysis",
    "TorqueConverterPumpCompoundStabilityAnalysis",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
    "UnbalancedMassCompoundStabilityAnalysis",
    "VirtualComponentCompoundStabilityAnalysis",
    "WormGearCompoundStabilityAnalysis",
    "WormGearMeshCompoundStabilityAnalysis",
    "WormGearSetCompoundStabilityAnalysis",
    "ZerolBevelGearCompoundStabilityAnalysis",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
    "ZerolBevelGearSetCompoundStabilityAnalysis",
)
