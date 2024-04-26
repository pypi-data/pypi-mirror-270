"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4055 import AbstractAssemblyPowerFlow
    from ._4056 import AbstractShaftOrHousingPowerFlow
    from ._4057 import AbstractShaftPowerFlow
    from ._4058 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4059 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4060 import AGMAGleasonConicalGearPowerFlow
    from ._4061 import AGMAGleasonConicalGearSetPowerFlow
    from ._4062 import AssemblyPowerFlow
    from ._4063 import BearingPowerFlow
    from ._4064 import BeltConnectionPowerFlow
    from ._4065 import BeltDrivePowerFlow
    from ._4066 import BevelDifferentialGearMeshPowerFlow
    from ._4067 import BevelDifferentialGearPowerFlow
    from ._4068 import BevelDifferentialGearSetPowerFlow
    from ._4069 import BevelDifferentialPlanetGearPowerFlow
    from ._4070 import BevelDifferentialSunGearPowerFlow
    from ._4071 import BevelGearMeshPowerFlow
    from ._4072 import BevelGearPowerFlow
    from ._4073 import BevelGearSetPowerFlow
    from ._4074 import BoltedJointPowerFlow
    from ._4075 import BoltPowerFlow
    from ._4076 import ClutchConnectionPowerFlow
    from ._4077 import ClutchHalfPowerFlow
    from ._4078 import ClutchPowerFlow
    from ._4079 import CoaxialConnectionPowerFlow
    from ._4080 import ComponentPowerFlow
    from ._4081 import ConceptCouplingConnectionPowerFlow
    from ._4082 import ConceptCouplingHalfPowerFlow
    from ._4083 import ConceptCouplingPowerFlow
    from ._4084 import ConceptGearMeshPowerFlow
    from ._4085 import ConceptGearPowerFlow
    from ._4086 import ConceptGearSetPowerFlow
    from ._4087 import ConicalGearMeshPowerFlow
    from ._4088 import ConicalGearPowerFlow
    from ._4089 import ConicalGearSetPowerFlow
    from ._4090 import ConnectionPowerFlow
    from ._4091 import ConnectorPowerFlow
    from ._4092 import CouplingConnectionPowerFlow
    from ._4093 import CouplingHalfPowerFlow
    from ._4094 import CouplingPowerFlow
    from ._4095 import CVTBeltConnectionPowerFlow
    from ._4096 import CVTPowerFlow
    from ._4097 import CVTPulleyPowerFlow
    from ._4098 import CycloidalAssemblyPowerFlow
    from ._4099 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4100 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4101 import CycloidalDiscPowerFlow
    from ._4102 import CylindricalGearGeometricEntityDrawStyle
    from ._4103 import CylindricalGearMeshPowerFlow
    from ._4104 import CylindricalGearPowerFlow
    from ._4105 import CylindricalGearSetPowerFlow
    from ._4106 import CylindricalPlanetGearPowerFlow
    from ._4107 import DatumPowerFlow
    from ._4108 import ExternalCADModelPowerFlow
    from ._4109 import FaceGearMeshPowerFlow
    from ._4110 import FaceGearPowerFlow
    from ._4111 import FaceGearSetPowerFlow
    from ._4112 import FastPowerFlow
    from ._4113 import FastPowerFlowSolution
    from ._4114 import FEPartPowerFlow
    from ._4115 import FlexiblePinAssemblyPowerFlow
    from ._4116 import GearMeshPowerFlow
    from ._4117 import GearPowerFlow
    from ._4118 import GearSetPowerFlow
    from ._4119 import GuideDxfModelPowerFlow
    from ._4120 import HypoidGearMeshPowerFlow
    from ._4121 import HypoidGearPowerFlow
    from ._4122 import HypoidGearSetPowerFlow
    from ._4123 import InterMountableComponentConnectionPowerFlow
    from ._4124 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4125 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4126 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4127 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4128 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4129 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4130 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4131 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4132 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4133 import MassDiscPowerFlow
    from ._4134 import MeasurementComponentPowerFlow
    from ._4135 import MountableComponentPowerFlow
    from ._4136 import OilSealPowerFlow
    from ._4137 import PartPowerFlow
    from ._4138 import PartToPartShearCouplingConnectionPowerFlow
    from ._4139 import PartToPartShearCouplingHalfPowerFlow
    from ._4140 import PartToPartShearCouplingPowerFlow
    from ._4141 import PlanetaryConnectionPowerFlow
    from ._4142 import PlanetaryGearSetPowerFlow
    from ._4143 import PlanetCarrierPowerFlow
    from ._4144 import PointLoadPowerFlow
    from ._4145 import PowerFlow
    from ._4146 import PowerFlowDrawStyle
    from ._4147 import PowerLoadPowerFlow
    from ._4148 import PulleyPowerFlow
    from ._4149 import RingPinsPowerFlow
    from ._4150 import RingPinsToDiscConnectionPowerFlow
    from ._4151 import RollingRingAssemblyPowerFlow
    from ._4152 import RollingRingConnectionPowerFlow
    from ._4153 import RollingRingPowerFlow
    from ._4154 import RootAssemblyPowerFlow
    from ._4155 import ShaftHubConnectionPowerFlow
    from ._4156 import ShaftPowerFlow
    from ._4157 import ShaftToMountableComponentConnectionPowerFlow
    from ._4158 import SpecialisedAssemblyPowerFlow
    from ._4159 import SpiralBevelGearMeshPowerFlow
    from ._4160 import SpiralBevelGearPowerFlow
    from ._4161 import SpiralBevelGearSetPowerFlow
    from ._4162 import SpringDamperConnectionPowerFlow
    from ._4163 import SpringDamperHalfPowerFlow
    from ._4164 import SpringDamperPowerFlow
    from ._4165 import StraightBevelDiffGearMeshPowerFlow
    from ._4166 import StraightBevelDiffGearPowerFlow
    from ._4167 import StraightBevelDiffGearSetPowerFlow
    from ._4168 import StraightBevelGearMeshPowerFlow
    from ._4169 import StraightBevelGearPowerFlow
    from ._4170 import StraightBevelGearSetPowerFlow
    from ._4171 import StraightBevelPlanetGearPowerFlow
    from ._4172 import StraightBevelSunGearPowerFlow
    from ._4173 import SynchroniserHalfPowerFlow
    from ._4174 import SynchroniserPartPowerFlow
    from ._4175 import SynchroniserPowerFlow
    from ._4176 import SynchroniserSleevePowerFlow
    from ._4177 import ToothPassingHarmonic
    from ._4178 import TorqueConverterConnectionPowerFlow
    from ._4179 import TorqueConverterPowerFlow
    from ._4180 import TorqueConverterPumpPowerFlow
    from ._4181 import TorqueConverterTurbinePowerFlow
    from ._4182 import UnbalancedMassPowerFlow
    from ._4183 import VirtualComponentPowerFlow
    from ._4184 import WormGearMeshPowerFlow
    from ._4185 import WormGearPowerFlow
    from ._4186 import WormGearSetPowerFlow
    from ._4187 import ZerolBevelGearMeshPowerFlow
    from ._4188 import ZerolBevelGearPowerFlow
    from ._4189 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        "_4055": ["AbstractAssemblyPowerFlow"],
        "_4056": ["AbstractShaftOrHousingPowerFlow"],
        "_4057": ["AbstractShaftPowerFlow"],
        "_4058": ["AbstractShaftToMountableComponentConnectionPowerFlow"],
        "_4059": ["AGMAGleasonConicalGearMeshPowerFlow"],
        "_4060": ["AGMAGleasonConicalGearPowerFlow"],
        "_4061": ["AGMAGleasonConicalGearSetPowerFlow"],
        "_4062": ["AssemblyPowerFlow"],
        "_4063": ["BearingPowerFlow"],
        "_4064": ["BeltConnectionPowerFlow"],
        "_4065": ["BeltDrivePowerFlow"],
        "_4066": ["BevelDifferentialGearMeshPowerFlow"],
        "_4067": ["BevelDifferentialGearPowerFlow"],
        "_4068": ["BevelDifferentialGearSetPowerFlow"],
        "_4069": ["BevelDifferentialPlanetGearPowerFlow"],
        "_4070": ["BevelDifferentialSunGearPowerFlow"],
        "_4071": ["BevelGearMeshPowerFlow"],
        "_4072": ["BevelGearPowerFlow"],
        "_4073": ["BevelGearSetPowerFlow"],
        "_4074": ["BoltedJointPowerFlow"],
        "_4075": ["BoltPowerFlow"],
        "_4076": ["ClutchConnectionPowerFlow"],
        "_4077": ["ClutchHalfPowerFlow"],
        "_4078": ["ClutchPowerFlow"],
        "_4079": ["CoaxialConnectionPowerFlow"],
        "_4080": ["ComponentPowerFlow"],
        "_4081": ["ConceptCouplingConnectionPowerFlow"],
        "_4082": ["ConceptCouplingHalfPowerFlow"],
        "_4083": ["ConceptCouplingPowerFlow"],
        "_4084": ["ConceptGearMeshPowerFlow"],
        "_4085": ["ConceptGearPowerFlow"],
        "_4086": ["ConceptGearSetPowerFlow"],
        "_4087": ["ConicalGearMeshPowerFlow"],
        "_4088": ["ConicalGearPowerFlow"],
        "_4089": ["ConicalGearSetPowerFlow"],
        "_4090": ["ConnectionPowerFlow"],
        "_4091": ["ConnectorPowerFlow"],
        "_4092": ["CouplingConnectionPowerFlow"],
        "_4093": ["CouplingHalfPowerFlow"],
        "_4094": ["CouplingPowerFlow"],
        "_4095": ["CVTBeltConnectionPowerFlow"],
        "_4096": ["CVTPowerFlow"],
        "_4097": ["CVTPulleyPowerFlow"],
        "_4098": ["CycloidalAssemblyPowerFlow"],
        "_4099": ["CycloidalDiscCentralBearingConnectionPowerFlow"],
        "_4100": ["CycloidalDiscPlanetaryBearingConnectionPowerFlow"],
        "_4101": ["CycloidalDiscPowerFlow"],
        "_4102": ["CylindricalGearGeometricEntityDrawStyle"],
        "_4103": ["CylindricalGearMeshPowerFlow"],
        "_4104": ["CylindricalGearPowerFlow"],
        "_4105": ["CylindricalGearSetPowerFlow"],
        "_4106": ["CylindricalPlanetGearPowerFlow"],
        "_4107": ["DatumPowerFlow"],
        "_4108": ["ExternalCADModelPowerFlow"],
        "_4109": ["FaceGearMeshPowerFlow"],
        "_4110": ["FaceGearPowerFlow"],
        "_4111": ["FaceGearSetPowerFlow"],
        "_4112": ["FastPowerFlow"],
        "_4113": ["FastPowerFlowSolution"],
        "_4114": ["FEPartPowerFlow"],
        "_4115": ["FlexiblePinAssemblyPowerFlow"],
        "_4116": ["GearMeshPowerFlow"],
        "_4117": ["GearPowerFlow"],
        "_4118": ["GearSetPowerFlow"],
        "_4119": ["GuideDxfModelPowerFlow"],
        "_4120": ["HypoidGearMeshPowerFlow"],
        "_4121": ["HypoidGearPowerFlow"],
        "_4122": ["HypoidGearSetPowerFlow"],
        "_4123": ["InterMountableComponentConnectionPowerFlow"],
        "_4124": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4125": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4126": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4127": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4128": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4129": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4130": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4131": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4132": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4133": ["MassDiscPowerFlow"],
        "_4134": ["MeasurementComponentPowerFlow"],
        "_4135": ["MountableComponentPowerFlow"],
        "_4136": ["OilSealPowerFlow"],
        "_4137": ["PartPowerFlow"],
        "_4138": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4139": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4140": ["PartToPartShearCouplingPowerFlow"],
        "_4141": ["PlanetaryConnectionPowerFlow"],
        "_4142": ["PlanetaryGearSetPowerFlow"],
        "_4143": ["PlanetCarrierPowerFlow"],
        "_4144": ["PointLoadPowerFlow"],
        "_4145": ["PowerFlow"],
        "_4146": ["PowerFlowDrawStyle"],
        "_4147": ["PowerLoadPowerFlow"],
        "_4148": ["PulleyPowerFlow"],
        "_4149": ["RingPinsPowerFlow"],
        "_4150": ["RingPinsToDiscConnectionPowerFlow"],
        "_4151": ["RollingRingAssemblyPowerFlow"],
        "_4152": ["RollingRingConnectionPowerFlow"],
        "_4153": ["RollingRingPowerFlow"],
        "_4154": ["RootAssemblyPowerFlow"],
        "_4155": ["ShaftHubConnectionPowerFlow"],
        "_4156": ["ShaftPowerFlow"],
        "_4157": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4158": ["SpecialisedAssemblyPowerFlow"],
        "_4159": ["SpiralBevelGearMeshPowerFlow"],
        "_4160": ["SpiralBevelGearPowerFlow"],
        "_4161": ["SpiralBevelGearSetPowerFlow"],
        "_4162": ["SpringDamperConnectionPowerFlow"],
        "_4163": ["SpringDamperHalfPowerFlow"],
        "_4164": ["SpringDamperPowerFlow"],
        "_4165": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4166": ["StraightBevelDiffGearPowerFlow"],
        "_4167": ["StraightBevelDiffGearSetPowerFlow"],
        "_4168": ["StraightBevelGearMeshPowerFlow"],
        "_4169": ["StraightBevelGearPowerFlow"],
        "_4170": ["StraightBevelGearSetPowerFlow"],
        "_4171": ["StraightBevelPlanetGearPowerFlow"],
        "_4172": ["StraightBevelSunGearPowerFlow"],
        "_4173": ["SynchroniserHalfPowerFlow"],
        "_4174": ["SynchroniserPartPowerFlow"],
        "_4175": ["SynchroniserPowerFlow"],
        "_4176": ["SynchroniserSleevePowerFlow"],
        "_4177": ["ToothPassingHarmonic"],
        "_4178": ["TorqueConverterConnectionPowerFlow"],
        "_4179": ["TorqueConverterPowerFlow"],
        "_4180": ["TorqueConverterPumpPowerFlow"],
        "_4181": ["TorqueConverterTurbinePowerFlow"],
        "_4182": ["UnbalancedMassPowerFlow"],
        "_4183": ["VirtualComponentPowerFlow"],
        "_4184": ["WormGearMeshPowerFlow"],
        "_4185": ["WormGearPowerFlow"],
        "_4186": ["WormGearSetPowerFlow"],
        "_4187": ["ZerolBevelGearMeshPowerFlow"],
        "_4188": ["ZerolBevelGearPowerFlow"],
        "_4189": ["ZerolBevelGearSetPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyPowerFlow",
    "AbstractShaftOrHousingPowerFlow",
    "AbstractShaftPowerFlow",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
    "AGMAGleasonConicalGearMeshPowerFlow",
    "AGMAGleasonConicalGearPowerFlow",
    "AGMAGleasonConicalGearSetPowerFlow",
    "AssemblyPowerFlow",
    "BearingPowerFlow",
    "BeltConnectionPowerFlow",
    "BeltDrivePowerFlow",
    "BevelDifferentialGearMeshPowerFlow",
    "BevelDifferentialGearPowerFlow",
    "BevelDifferentialGearSetPowerFlow",
    "BevelDifferentialPlanetGearPowerFlow",
    "BevelDifferentialSunGearPowerFlow",
    "BevelGearMeshPowerFlow",
    "BevelGearPowerFlow",
    "BevelGearSetPowerFlow",
    "BoltedJointPowerFlow",
    "BoltPowerFlow",
    "ClutchConnectionPowerFlow",
    "ClutchHalfPowerFlow",
    "ClutchPowerFlow",
    "CoaxialConnectionPowerFlow",
    "ComponentPowerFlow",
    "ConceptCouplingConnectionPowerFlow",
    "ConceptCouplingHalfPowerFlow",
    "ConceptCouplingPowerFlow",
    "ConceptGearMeshPowerFlow",
    "ConceptGearPowerFlow",
    "ConceptGearSetPowerFlow",
    "ConicalGearMeshPowerFlow",
    "ConicalGearPowerFlow",
    "ConicalGearSetPowerFlow",
    "ConnectionPowerFlow",
    "ConnectorPowerFlow",
    "CouplingConnectionPowerFlow",
    "CouplingHalfPowerFlow",
    "CouplingPowerFlow",
    "CVTBeltConnectionPowerFlow",
    "CVTPowerFlow",
    "CVTPulleyPowerFlow",
    "CycloidalAssemblyPowerFlow",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
    "CycloidalDiscPowerFlow",
    "CylindricalGearGeometricEntityDrawStyle",
    "CylindricalGearMeshPowerFlow",
    "CylindricalGearPowerFlow",
    "CylindricalGearSetPowerFlow",
    "CylindricalPlanetGearPowerFlow",
    "DatumPowerFlow",
    "ExternalCADModelPowerFlow",
    "FaceGearMeshPowerFlow",
    "FaceGearPowerFlow",
    "FaceGearSetPowerFlow",
    "FastPowerFlow",
    "FastPowerFlowSolution",
    "FEPartPowerFlow",
    "FlexiblePinAssemblyPowerFlow",
    "GearMeshPowerFlow",
    "GearPowerFlow",
    "GearSetPowerFlow",
    "GuideDxfModelPowerFlow",
    "HypoidGearMeshPowerFlow",
    "HypoidGearPowerFlow",
    "HypoidGearSetPowerFlow",
    "InterMountableComponentConnectionPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
    "MassDiscPowerFlow",
    "MeasurementComponentPowerFlow",
    "MountableComponentPowerFlow",
    "OilSealPowerFlow",
    "PartPowerFlow",
    "PartToPartShearCouplingConnectionPowerFlow",
    "PartToPartShearCouplingHalfPowerFlow",
    "PartToPartShearCouplingPowerFlow",
    "PlanetaryConnectionPowerFlow",
    "PlanetaryGearSetPowerFlow",
    "PlanetCarrierPowerFlow",
    "PointLoadPowerFlow",
    "PowerFlow",
    "PowerFlowDrawStyle",
    "PowerLoadPowerFlow",
    "PulleyPowerFlow",
    "RingPinsPowerFlow",
    "RingPinsToDiscConnectionPowerFlow",
    "RollingRingAssemblyPowerFlow",
    "RollingRingConnectionPowerFlow",
    "RollingRingPowerFlow",
    "RootAssemblyPowerFlow",
    "ShaftHubConnectionPowerFlow",
    "ShaftPowerFlow",
    "ShaftToMountableComponentConnectionPowerFlow",
    "SpecialisedAssemblyPowerFlow",
    "SpiralBevelGearMeshPowerFlow",
    "SpiralBevelGearPowerFlow",
    "SpiralBevelGearSetPowerFlow",
    "SpringDamperConnectionPowerFlow",
    "SpringDamperHalfPowerFlow",
    "SpringDamperPowerFlow",
    "StraightBevelDiffGearMeshPowerFlow",
    "StraightBevelDiffGearPowerFlow",
    "StraightBevelDiffGearSetPowerFlow",
    "StraightBevelGearMeshPowerFlow",
    "StraightBevelGearPowerFlow",
    "StraightBevelGearSetPowerFlow",
    "StraightBevelPlanetGearPowerFlow",
    "StraightBevelSunGearPowerFlow",
    "SynchroniserHalfPowerFlow",
    "SynchroniserPartPowerFlow",
    "SynchroniserPowerFlow",
    "SynchroniserSleevePowerFlow",
    "ToothPassingHarmonic",
    "TorqueConverterConnectionPowerFlow",
    "TorqueConverterPowerFlow",
    "TorqueConverterPumpPowerFlow",
    "TorqueConverterTurbinePowerFlow",
    "UnbalancedMassPowerFlow",
    "VirtualComponentPowerFlow",
    "WormGearMeshPowerFlow",
    "WormGearPowerFlow",
    "WormGearSetPowerFlow",
    "ZerolBevelGearMeshPowerFlow",
    "ZerolBevelGearPowerFlow",
    "ZerolBevelGearSetPowerFlow",
)
