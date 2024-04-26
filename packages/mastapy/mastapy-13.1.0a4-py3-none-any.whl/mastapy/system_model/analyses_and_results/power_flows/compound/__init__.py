"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4190 import AbstractAssemblyCompoundPowerFlow
    from ._4191 import AbstractShaftCompoundPowerFlow
    from ._4192 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4193 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4194 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4195 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4196 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4197 import AssemblyCompoundPowerFlow
    from ._4198 import BearingCompoundPowerFlow
    from ._4199 import BeltConnectionCompoundPowerFlow
    from ._4200 import BeltDriveCompoundPowerFlow
    from ._4201 import BevelDifferentialGearCompoundPowerFlow
    from ._4202 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4203 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4204 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4205 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4206 import BevelGearCompoundPowerFlow
    from ._4207 import BevelGearMeshCompoundPowerFlow
    from ._4208 import BevelGearSetCompoundPowerFlow
    from ._4209 import BoltCompoundPowerFlow
    from ._4210 import BoltedJointCompoundPowerFlow
    from ._4211 import ClutchCompoundPowerFlow
    from ._4212 import ClutchConnectionCompoundPowerFlow
    from ._4213 import ClutchHalfCompoundPowerFlow
    from ._4214 import CoaxialConnectionCompoundPowerFlow
    from ._4215 import ComponentCompoundPowerFlow
    from ._4216 import ConceptCouplingCompoundPowerFlow
    from ._4217 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4218 import ConceptCouplingHalfCompoundPowerFlow
    from ._4219 import ConceptGearCompoundPowerFlow
    from ._4220 import ConceptGearMeshCompoundPowerFlow
    from ._4221 import ConceptGearSetCompoundPowerFlow
    from ._4222 import ConicalGearCompoundPowerFlow
    from ._4223 import ConicalGearMeshCompoundPowerFlow
    from ._4224 import ConicalGearSetCompoundPowerFlow
    from ._4225 import ConnectionCompoundPowerFlow
    from ._4226 import ConnectorCompoundPowerFlow
    from ._4227 import CouplingCompoundPowerFlow
    from ._4228 import CouplingConnectionCompoundPowerFlow
    from ._4229 import CouplingHalfCompoundPowerFlow
    from ._4230 import CVTBeltConnectionCompoundPowerFlow
    from ._4231 import CVTCompoundPowerFlow
    from ._4232 import CVTPulleyCompoundPowerFlow
    from ._4233 import CycloidalAssemblyCompoundPowerFlow
    from ._4234 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4235 import CycloidalDiscCompoundPowerFlow
    from ._4236 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4237 import CylindricalGearCompoundPowerFlow
    from ._4238 import CylindricalGearMeshCompoundPowerFlow
    from ._4239 import CylindricalGearSetCompoundPowerFlow
    from ._4240 import CylindricalPlanetGearCompoundPowerFlow
    from ._4241 import DatumCompoundPowerFlow
    from ._4242 import ExternalCADModelCompoundPowerFlow
    from ._4243 import FaceGearCompoundPowerFlow
    from ._4244 import FaceGearMeshCompoundPowerFlow
    from ._4245 import FaceGearSetCompoundPowerFlow
    from ._4246 import FEPartCompoundPowerFlow
    from ._4247 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4248 import GearCompoundPowerFlow
    from ._4249 import GearMeshCompoundPowerFlow
    from ._4250 import GearSetCompoundPowerFlow
    from ._4251 import GuideDxfModelCompoundPowerFlow
    from ._4252 import HypoidGearCompoundPowerFlow
    from ._4253 import HypoidGearMeshCompoundPowerFlow
    from ._4254 import HypoidGearSetCompoundPowerFlow
    from ._4255 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4256 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4257 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4258 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4259 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4260 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4261 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4262 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4263 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4264 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4265 import MassDiscCompoundPowerFlow
    from ._4266 import MeasurementComponentCompoundPowerFlow
    from ._4267 import MountableComponentCompoundPowerFlow
    from ._4268 import OilSealCompoundPowerFlow
    from ._4269 import PartCompoundPowerFlow
    from ._4270 import PartToPartShearCouplingCompoundPowerFlow
    from ._4271 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4272 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4273 import PlanetaryConnectionCompoundPowerFlow
    from ._4274 import PlanetaryGearSetCompoundPowerFlow
    from ._4275 import PlanetCarrierCompoundPowerFlow
    from ._4276 import PointLoadCompoundPowerFlow
    from ._4277 import PowerLoadCompoundPowerFlow
    from ._4278 import PulleyCompoundPowerFlow
    from ._4279 import RingPinsCompoundPowerFlow
    from ._4280 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4281 import RollingRingAssemblyCompoundPowerFlow
    from ._4282 import RollingRingCompoundPowerFlow
    from ._4283 import RollingRingConnectionCompoundPowerFlow
    from ._4284 import RootAssemblyCompoundPowerFlow
    from ._4285 import ShaftCompoundPowerFlow
    from ._4286 import ShaftHubConnectionCompoundPowerFlow
    from ._4287 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4288 import SpecialisedAssemblyCompoundPowerFlow
    from ._4289 import SpiralBevelGearCompoundPowerFlow
    from ._4290 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4291 import SpiralBevelGearSetCompoundPowerFlow
    from ._4292 import SpringDamperCompoundPowerFlow
    from ._4293 import SpringDamperConnectionCompoundPowerFlow
    from ._4294 import SpringDamperHalfCompoundPowerFlow
    from ._4295 import StraightBevelDiffGearCompoundPowerFlow
    from ._4296 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4297 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4298 import StraightBevelGearCompoundPowerFlow
    from ._4299 import StraightBevelGearMeshCompoundPowerFlow
    from ._4300 import StraightBevelGearSetCompoundPowerFlow
    from ._4301 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4302 import StraightBevelSunGearCompoundPowerFlow
    from ._4303 import SynchroniserCompoundPowerFlow
    from ._4304 import SynchroniserHalfCompoundPowerFlow
    from ._4305 import SynchroniserPartCompoundPowerFlow
    from ._4306 import SynchroniserSleeveCompoundPowerFlow
    from ._4307 import TorqueConverterCompoundPowerFlow
    from ._4308 import TorqueConverterConnectionCompoundPowerFlow
    from ._4309 import TorqueConverterPumpCompoundPowerFlow
    from ._4310 import TorqueConverterTurbineCompoundPowerFlow
    from ._4311 import UnbalancedMassCompoundPowerFlow
    from ._4312 import VirtualComponentCompoundPowerFlow
    from ._4313 import WormGearCompoundPowerFlow
    from ._4314 import WormGearMeshCompoundPowerFlow
    from ._4315 import WormGearSetCompoundPowerFlow
    from ._4316 import ZerolBevelGearCompoundPowerFlow
    from ._4317 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4318 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4190": ["AbstractAssemblyCompoundPowerFlow"],
        "_4191": ["AbstractShaftCompoundPowerFlow"],
        "_4192": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4193": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4194": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4195": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4196": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4197": ["AssemblyCompoundPowerFlow"],
        "_4198": ["BearingCompoundPowerFlow"],
        "_4199": ["BeltConnectionCompoundPowerFlow"],
        "_4200": ["BeltDriveCompoundPowerFlow"],
        "_4201": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4202": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4203": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4204": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4205": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4206": ["BevelGearCompoundPowerFlow"],
        "_4207": ["BevelGearMeshCompoundPowerFlow"],
        "_4208": ["BevelGearSetCompoundPowerFlow"],
        "_4209": ["BoltCompoundPowerFlow"],
        "_4210": ["BoltedJointCompoundPowerFlow"],
        "_4211": ["ClutchCompoundPowerFlow"],
        "_4212": ["ClutchConnectionCompoundPowerFlow"],
        "_4213": ["ClutchHalfCompoundPowerFlow"],
        "_4214": ["CoaxialConnectionCompoundPowerFlow"],
        "_4215": ["ComponentCompoundPowerFlow"],
        "_4216": ["ConceptCouplingCompoundPowerFlow"],
        "_4217": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4218": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4219": ["ConceptGearCompoundPowerFlow"],
        "_4220": ["ConceptGearMeshCompoundPowerFlow"],
        "_4221": ["ConceptGearSetCompoundPowerFlow"],
        "_4222": ["ConicalGearCompoundPowerFlow"],
        "_4223": ["ConicalGearMeshCompoundPowerFlow"],
        "_4224": ["ConicalGearSetCompoundPowerFlow"],
        "_4225": ["ConnectionCompoundPowerFlow"],
        "_4226": ["ConnectorCompoundPowerFlow"],
        "_4227": ["CouplingCompoundPowerFlow"],
        "_4228": ["CouplingConnectionCompoundPowerFlow"],
        "_4229": ["CouplingHalfCompoundPowerFlow"],
        "_4230": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4231": ["CVTCompoundPowerFlow"],
        "_4232": ["CVTPulleyCompoundPowerFlow"],
        "_4233": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4234": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4235": ["CycloidalDiscCompoundPowerFlow"],
        "_4236": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4237": ["CylindricalGearCompoundPowerFlow"],
        "_4238": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4239": ["CylindricalGearSetCompoundPowerFlow"],
        "_4240": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4241": ["DatumCompoundPowerFlow"],
        "_4242": ["ExternalCADModelCompoundPowerFlow"],
        "_4243": ["FaceGearCompoundPowerFlow"],
        "_4244": ["FaceGearMeshCompoundPowerFlow"],
        "_4245": ["FaceGearSetCompoundPowerFlow"],
        "_4246": ["FEPartCompoundPowerFlow"],
        "_4247": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4248": ["GearCompoundPowerFlow"],
        "_4249": ["GearMeshCompoundPowerFlow"],
        "_4250": ["GearSetCompoundPowerFlow"],
        "_4251": ["GuideDxfModelCompoundPowerFlow"],
        "_4252": ["HypoidGearCompoundPowerFlow"],
        "_4253": ["HypoidGearMeshCompoundPowerFlow"],
        "_4254": ["HypoidGearSetCompoundPowerFlow"],
        "_4255": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4256": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4257": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4258": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4259": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4260": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4261": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4262": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4263": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4264": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4265": ["MassDiscCompoundPowerFlow"],
        "_4266": ["MeasurementComponentCompoundPowerFlow"],
        "_4267": ["MountableComponentCompoundPowerFlow"],
        "_4268": ["OilSealCompoundPowerFlow"],
        "_4269": ["PartCompoundPowerFlow"],
        "_4270": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4271": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4272": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4273": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4274": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4275": ["PlanetCarrierCompoundPowerFlow"],
        "_4276": ["PointLoadCompoundPowerFlow"],
        "_4277": ["PowerLoadCompoundPowerFlow"],
        "_4278": ["PulleyCompoundPowerFlow"],
        "_4279": ["RingPinsCompoundPowerFlow"],
        "_4280": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4281": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4282": ["RollingRingCompoundPowerFlow"],
        "_4283": ["RollingRingConnectionCompoundPowerFlow"],
        "_4284": ["RootAssemblyCompoundPowerFlow"],
        "_4285": ["ShaftCompoundPowerFlow"],
        "_4286": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4287": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4288": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4289": ["SpiralBevelGearCompoundPowerFlow"],
        "_4290": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4291": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4292": ["SpringDamperCompoundPowerFlow"],
        "_4293": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4294": ["SpringDamperHalfCompoundPowerFlow"],
        "_4295": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4296": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4297": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4298": ["StraightBevelGearCompoundPowerFlow"],
        "_4299": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4300": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4301": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4302": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4303": ["SynchroniserCompoundPowerFlow"],
        "_4304": ["SynchroniserHalfCompoundPowerFlow"],
        "_4305": ["SynchroniserPartCompoundPowerFlow"],
        "_4306": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4307": ["TorqueConverterCompoundPowerFlow"],
        "_4308": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4309": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4310": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4311": ["UnbalancedMassCompoundPowerFlow"],
        "_4312": ["VirtualComponentCompoundPowerFlow"],
        "_4313": ["WormGearCompoundPowerFlow"],
        "_4314": ["WormGearMeshCompoundPowerFlow"],
        "_4315": ["WormGearSetCompoundPowerFlow"],
        "_4316": ["ZerolBevelGearCompoundPowerFlow"],
        "_4317": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4318": ["ZerolBevelGearSetCompoundPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundPowerFlow",
    "AbstractShaftCompoundPowerFlow",
    "AbstractShaftOrHousingCompoundPowerFlow",
    "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    "AGMAGleasonConicalGearCompoundPowerFlow",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
    "AssemblyCompoundPowerFlow",
    "BearingCompoundPowerFlow",
    "BeltConnectionCompoundPowerFlow",
    "BeltDriveCompoundPowerFlow",
    "BevelDifferentialGearCompoundPowerFlow",
    "BevelDifferentialGearMeshCompoundPowerFlow",
    "BevelDifferentialGearSetCompoundPowerFlow",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
    "BevelDifferentialSunGearCompoundPowerFlow",
    "BevelGearCompoundPowerFlow",
    "BevelGearMeshCompoundPowerFlow",
    "BevelGearSetCompoundPowerFlow",
    "BoltCompoundPowerFlow",
    "BoltedJointCompoundPowerFlow",
    "ClutchCompoundPowerFlow",
    "ClutchConnectionCompoundPowerFlow",
    "ClutchHalfCompoundPowerFlow",
    "CoaxialConnectionCompoundPowerFlow",
    "ComponentCompoundPowerFlow",
    "ConceptCouplingCompoundPowerFlow",
    "ConceptCouplingConnectionCompoundPowerFlow",
    "ConceptCouplingHalfCompoundPowerFlow",
    "ConceptGearCompoundPowerFlow",
    "ConceptGearMeshCompoundPowerFlow",
    "ConceptGearSetCompoundPowerFlow",
    "ConicalGearCompoundPowerFlow",
    "ConicalGearMeshCompoundPowerFlow",
    "ConicalGearSetCompoundPowerFlow",
    "ConnectionCompoundPowerFlow",
    "ConnectorCompoundPowerFlow",
    "CouplingCompoundPowerFlow",
    "CouplingConnectionCompoundPowerFlow",
    "CouplingHalfCompoundPowerFlow",
    "CVTBeltConnectionCompoundPowerFlow",
    "CVTCompoundPowerFlow",
    "CVTPulleyCompoundPowerFlow",
    "CycloidalAssemblyCompoundPowerFlow",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    "CycloidalDiscCompoundPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow",
    "CylindricalGearCompoundPowerFlow",
    "CylindricalGearMeshCompoundPowerFlow",
    "CylindricalGearSetCompoundPowerFlow",
    "CylindricalPlanetGearCompoundPowerFlow",
    "DatumCompoundPowerFlow",
    "ExternalCADModelCompoundPowerFlow",
    "FaceGearCompoundPowerFlow",
    "FaceGearMeshCompoundPowerFlow",
    "FaceGearSetCompoundPowerFlow",
    "FEPartCompoundPowerFlow",
    "FlexiblePinAssemblyCompoundPowerFlow",
    "GearCompoundPowerFlow",
    "GearMeshCompoundPowerFlow",
    "GearSetCompoundPowerFlow",
    "GuideDxfModelCompoundPowerFlow",
    "HypoidGearCompoundPowerFlow",
    "HypoidGearMeshCompoundPowerFlow",
    "HypoidGearSetCompoundPowerFlow",
    "InterMountableComponentConnectionCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    "MassDiscCompoundPowerFlow",
    "MeasurementComponentCompoundPowerFlow",
    "MountableComponentCompoundPowerFlow",
    "OilSealCompoundPowerFlow",
    "PartCompoundPowerFlow",
    "PartToPartShearCouplingCompoundPowerFlow",
    "PartToPartShearCouplingConnectionCompoundPowerFlow",
    "PartToPartShearCouplingHalfCompoundPowerFlow",
    "PlanetaryConnectionCompoundPowerFlow",
    "PlanetaryGearSetCompoundPowerFlow",
    "PlanetCarrierCompoundPowerFlow",
    "PointLoadCompoundPowerFlow",
    "PowerLoadCompoundPowerFlow",
    "PulleyCompoundPowerFlow",
    "RingPinsCompoundPowerFlow",
    "RingPinsToDiscConnectionCompoundPowerFlow",
    "RollingRingAssemblyCompoundPowerFlow",
    "RollingRingCompoundPowerFlow",
    "RollingRingConnectionCompoundPowerFlow",
    "RootAssemblyCompoundPowerFlow",
    "ShaftCompoundPowerFlow",
    "ShaftHubConnectionCompoundPowerFlow",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
    "SpecialisedAssemblyCompoundPowerFlow",
    "SpiralBevelGearCompoundPowerFlow",
    "SpiralBevelGearMeshCompoundPowerFlow",
    "SpiralBevelGearSetCompoundPowerFlow",
    "SpringDamperCompoundPowerFlow",
    "SpringDamperConnectionCompoundPowerFlow",
    "SpringDamperHalfCompoundPowerFlow",
    "StraightBevelDiffGearCompoundPowerFlow",
    "StraightBevelDiffGearMeshCompoundPowerFlow",
    "StraightBevelDiffGearSetCompoundPowerFlow",
    "StraightBevelGearCompoundPowerFlow",
    "StraightBevelGearMeshCompoundPowerFlow",
    "StraightBevelGearSetCompoundPowerFlow",
    "StraightBevelPlanetGearCompoundPowerFlow",
    "StraightBevelSunGearCompoundPowerFlow",
    "SynchroniserCompoundPowerFlow",
    "SynchroniserHalfCompoundPowerFlow",
    "SynchroniserPartCompoundPowerFlow",
    "SynchroniserSleeveCompoundPowerFlow",
    "TorqueConverterCompoundPowerFlow",
    "TorqueConverterConnectionCompoundPowerFlow",
    "TorqueConverterPumpCompoundPowerFlow",
    "TorqueConverterTurbineCompoundPowerFlow",
    "UnbalancedMassCompoundPowerFlow",
    "VirtualComponentCompoundPowerFlow",
    "WormGearCompoundPowerFlow",
    "WormGearMeshCompoundPowerFlow",
    "WormGearSetCompoundPowerFlow",
    "ZerolBevelGearCompoundPowerFlow",
    "ZerolBevelGearMeshCompoundPowerFlow",
    "ZerolBevelGearSetCompoundPowerFlow",
)
