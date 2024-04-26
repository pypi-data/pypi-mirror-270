"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4319 import AbstractAssemblyParametricStudyTool
    from ._4320 import AbstractShaftOrHousingParametricStudyTool
    from ._4321 import AbstractShaftParametricStudyTool
    from ._4322 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4323 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4324 import AGMAGleasonConicalGearParametricStudyTool
    from ._4325 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4326 import AssemblyParametricStudyTool
    from ._4327 import BearingParametricStudyTool
    from ._4328 import BeltConnectionParametricStudyTool
    from ._4329 import BeltDriveParametricStudyTool
    from ._4330 import BevelDifferentialGearMeshParametricStudyTool
    from ._4331 import BevelDifferentialGearParametricStudyTool
    from ._4332 import BevelDifferentialGearSetParametricStudyTool
    from ._4333 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4334 import BevelDifferentialSunGearParametricStudyTool
    from ._4335 import BevelGearMeshParametricStudyTool
    from ._4336 import BevelGearParametricStudyTool
    from ._4337 import BevelGearSetParametricStudyTool
    from ._4338 import BoltedJointParametricStudyTool
    from ._4339 import BoltParametricStudyTool
    from ._4340 import ClutchConnectionParametricStudyTool
    from ._4341 import ClutchHalfParametricStudyTool
    from ._4342 import ClutchParametricStudyTool
    from ._4343 import CoaxialConnectionParametricStudyTool
    from ._4344 import ComponentParametricStudyTool
    from ._4345 import ConceptCouplingConnectionParametricStudyTool
    from ._4346 import ConceptCouplingHalfParametricStudyTool
    from ._4347 import ConceptCouplingParametricStudyTool
    from ._4348 import ConceptGearMeshParametricStudyTool
    from ._4349 import ConceptGearParametricStudyTool
    from ._4350 import ConceptGearSetParametricStudyTool
    from ._4351 import ConicalGearMeshParametricStudyTool
    from ._4352 import ConicalGearParametricStudyTool
    from ._4353 import ConicalGearSetParametricStudyTool
    from ._4354 import ConnectionParametricStudyTool
    from ._4355 import ConnectorParametricStudyTool
    from ._4356 import CouplingConnectionParametricStudyTool
    from ._4357 import CouplingHalfParametricStudyTool
    from ._4358 import CouplingParametricStudyTool
    from ._4359 import CVTBeltConnectionParametricStudyTool
    from ._4360 import CVTParametricStudyTool
    from ._4361 import CVTPulleyParametricStudyTool
    from ._4362 import CycloidalAssemblyParametricStudyTool
    from ._4363 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4364 import CycloidalDiscParametricStudyTool
    from ._4365 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4366 import CylindricalGearMeshParametricStudyTool
    from ._4367 import CylindricalGearParametricStudyTool
    from ._4368 import CylindricalGearSetParametricStudyTool
    from ._4369 import CylindricalPlanetGearParametricStudyTool
    from ._4370 import DatumParametricStudyTool
    from ._4371 import DesignOfExperimentsVariableSetter
    from ._4372 import DoeValueSpecificationOption
    from ._4373 import DutyCycleResultsForAllComponents
    from ._4374 import DutyCycleResultsForAllGearSets
    from ._4375 import DutyCycleResultsForRootAssembly
    from ._4376 import DutyCycleResultsForSingleBearing
    from ._4377 import DutyCycleResultsForSingleShaft
    from ._4378 import ExternalCADModelParametricStudyTool
    from ._4379 import FaceGearMeshParametricStudyTool
    from ._4380 import FaceGearParametricStudyTool
    from ._4381 import FaceGearSetParametricStudyTool
    from ._4382 import FEPartParametricStudyTool
    from ._4383 import FlexiblePinAssemblyParametricStudyTool
    from ._4384 import GearMeshParametricStudyTool
    from ._4385 import GearParametricStudyTool
    from ._4386 import GearSetParametricStudyTool
    from ._4387 import GuideDxfModelParametricStudyTool
    from ._4388 import HypoidGearMeshParametricStudyTool
    from ._4389 import HypoidGearParametricStudyTool
    from ._4390 import HypoidGearSetParametricStudyTool
    from ._4391 import InterMountableComponentConnectionParametricStudyTool
    from ._4392 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4393 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4394 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4395 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4396 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4397 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4398 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4399 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4400 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4401 import MassDiscParametricStudyTool
    from ._4402 import MeasurementComponentParametricStudyTool
    from ._4403 import MonteCarloDistribution
    from ._4404 import MountableComponentParametricStudyTool
    from ._4405 import OilSealParametricStudyTool
    from ._4406 import ParametricStudyDimension
    from ._4407 import ParametricStudyDOEResultVariable
    from ._4408 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4409 import ParametricStudyHistogram
    from ._4410 import ParametricStudyStaticLoad
    from ._4411 import ParametricStudyTool
    from ._4412 import ParametricStudyToolOptions
    from ._4413 import ParametricStudyToolResultsForReporting
    from ._4414 import ParametricStudyToolStepResult
    from ._4415 import ParametricStudyVariable
    from ._4416 import PartParametricStudyTool
    from ._4417 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4418 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4419 import PartToPartShearCouplingParametricStudyTool
    from ._4420 import PlanetaryConnectionParametricStudyTool
    from ._4421 import PlanetaryGearSetParametricStudyTool
    from ._4422 import PlanetCarrierParametricStudyTool
    from ._4423 import PointLoadParametricStudyTool
    from ._4424 import PowerLoadParametricStudyTool
    from ._4425 import PulleyParametricStudyTool
    from ._4426 import RingPinsParametricStudyTool
    from ._4427 import RingPinsToDiscConnectionParametricStudyTool
    from ._4428 import RollingRingAssemblyParametricStudyTool
    from ._4429 import RollingRingConnectionParametricStudyTool
    from ._4430 import RollingRingParametricStudyTool
    from ._4431 import RootAssemblyParametricStudyTool
    from ._4432 import ShaftHubConnectionParametricStudyTool
    from ._4433 import ShaftParametricStudyTool
    from ._4434 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4435 import SpecialisedAssemblyParametricStudyTool
    from ._4436 import SpiralBevelGearMeshParametricStudyTool
    from ._4437 import SpiralBevelGearParametricStudyTool
    from ._4438 import SpiralBevelGearSetParametricStudyTool
    from ._4439 import SpringDamperConnectionParametricStudyTool
    from ._4440 import SpringDamperHalfParametricStudyTool
    from ._4441 import SpringDamperParametricStudyTool
    from ._4442 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4443 import StraightBevelDiffGearParametricStudyTool
    from ._4444 import StraightBevelDiffGearSetParametricStudyTool
    from ._4445 import StraightBevelGearMeshParametricStudyTool
    from ._4446 import StraightBevelGearParametricStudyTool
    from ._4447 import StraightBevelGearSetParametricStudyTool
    from ._4448 import StraightBevelPlanetGearParametricStudyTool
    from ._4449 import StraightBevelSunGearParametricStudyTool
    from ._4450 import SynchroniserHalfParametricStudyTool
    from ._4451 import SynchroniserParametricStudyTool
    from ._4452 import SynchroniserPartParametricStudyTool
    from ._4453 import SynchroniserSleeveParametricStudyTool
    from ._4454 import TorqueConverterConnectionParametricStudyTool
    from ._4455 import TorqueConverterParametricStudyTool
    from ._4456 import TorqueConverterPumpParametricStudyTool
    from ._4457 import TorqueConverterTurbineParametricStudyTool
    from ._4458 import UnbalancedMassParametricStudyTool
    from ._4459 import VirtualComponentParametricStudyTool
    from ._4460 import WormGearMeshParametricStudyTool
    from ._4461 import WormGearParametricStudyTool
    from ._4462 import WormGearSetParametricStudyTool
    from ._4463 import ZerolBevelGearMeshParametricStudyTool
    from ._4464 import ZerolBevelGearParametricStudyTool
    from ._4465 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4319": ["AbstractAssemblyParametricStudyTool"],
        "_4320": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4321": ["AbstractShaftParametricStudyTool"],
        "_4322": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4323": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4324": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4325": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4326": ["AssemblyParametricStudyTool"],
        "_4327": ["BearingParametricStudyTool"],
        "_4328": ["BeltConnectionParametricStudyTool"],
        "_4329": ["BeltDriveParametricStudyTool"],
        "_4330": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4331": ["BevelDifferentialGearParametricStudyTool"],
        "_4332": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4333": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4334": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4335": ["BevelGearMeshParametricStudyTool"],
        "_4336": ["BevelGearParametricStudyTool"],
        "_4337": ["BevelGearSetParametricStudyTool"],
        "_4338": ["BoltedJointParametricStudyTool"],
        "_4339": ["BoltParametricStudyTool"],
        "_4340": ["ClutchConnectionParametricStudyTool"],
        "_4341": ["ClutchHalfParametricStudyTool"],
        "_4342": ["ClutchParametricStudyTool"],
        "_4343": ["CoaxialConnectionParametricStudyTool"],
        "_4344": ["ComponentParametricStudyTool"],
        "_4345": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4346": ["ConceptCouplingHalfParametricStudyTool"],
        "_4347": ["ConceptCouplingParametricStudyTool"],
        "_4348": ["ConceptGearMeshParametricStudyTool"],
        "_4349": ["ConceptGearParametricStudyTool"],
        "_4350": ["ConceptGearSetParametricStudyTool"],
        "_4351": ["ConicalGearMeshParametricStudyTool"],
        "_4352": ["ConicalGearParametricStudyTool"],
        "_4353": ["ConicalGearSetParametricStudyTool"],
        "_4354": ["ConnectionParametricStudyTool"],
        "_4355": ["ConnectorParametricStudyTool"],
        "_4356": ["CouplingConnectionParametricStudyTool"],
        "_4357": ["CouplingHalfParametricStudyTool"],
        "_4358": ["CouplingParametricStudyTool"],
        "_4359": ["CVTBeltConnectionParametricStudyTool"],
        "_4360": ["CVTParametricStudyTool"],
        "_4361": ["CVTPulleyParametricStudyTool"],
        "_4362": ["CycloidalAssemblyParametricStudyTool"],
        "_4363": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4364": ["CycloidalDiscParametricStudyTool"],
        "_4365": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4366": ["CylindricalGearMeshParametricStudyTool"],
        "_4367": ["CylindricalGearParametricStudyTool"],
        "_4368": ["CylindricalGearSetParametricStudyTool"],
        "_4369": ["CylindricalPlanetGearParametricStudyTool"],
        "_4370": ["DatumParametricStudyTool"],
        "_4371": ["DesignOfExperimentsVariableSetter"],
        "_4372": ["DoeValueSpecificationOption"],
        "_4373": ["DutyCycleResultsForAllComponents"],
        "_4374": ["DutyCycleResultsForAllGearSets"],
        "_4375": ["DutyCycleResultsForRootAssembly"],
        "_4376": ["DutyCycleResultsForSingleBearing"],
        "_4377": ["DutyCycleResultsForSingleShaft"],
        "_4378": ["ExternalCADModelParametricStudyTool"],
        "_4379": ["FaceGearMeshParametricStudyTool"],
        "_4380": ["FaceGearParametricStudyTool"],
        "_4381": ["FaceGearSetParametricStudyTool"],
        "_4382": ["FEPartParametricStudyTool"],
        "_4383": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4384": ["GearMeshParametricStudyTool"],
        "_4385": ["GearParametricStudyTool"],
        "_4386": ["GearSetParametricStudyTool"],
        "_4387": ["GuideDxfModelParametricStudyTool"],
        "_4388": ["HypoidGearMeshParametricStudyTool"],
        "_4389": ["HypoidGearParametricStudyTool"],
        "_4390": ["HypoidGearSetParametricStudyTool"],
        "_4391": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4392": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4393": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4394": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4395": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4396": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4397": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4398": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4399": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4400": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4401": ["MassDiscParametricStudyTool"],
        "_4402": ["MeasurementComponentParametricStudyTool"],
        "_4403": ["MonteCarloDistribution"],
        "_4404": ["MountableComponentParametricStudyTool"],
        "_4405": ["OilSealParametricStudyTool"],
        "_4406": ["ParametricStudyDimension"],
        "_4407": ["ParametricStudyDOEResultVariable"],
        "_4408": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4409": ["ParametricStudyHistogram"],
        "_4410": ["ParametricStudyStaticLoad"],
        "_4411": ["ParametricStudyTool"],
        "_4412": ["ParametricStudyToolOptions"],
        "_4413": ["ParametricStudyToolResultsForReporting"],
        "_4414": ["ParametricStudyToolStepResult"],
        "_4415": ["ParametricStudyVariable"],
        "_4416": ["PartParametricStudyTool"],
        "_4417": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4418": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4419": ["PartToPartShearCouplingParametricStudyTool"],
        "_4420": ["PlanetaryConnectionParametricStudyTool"],
        "_4421": ["PlanetaryGearSetParametricStudyTool"],
        "_4422": ["PlanetCarrierParametricStudyTool"],
        "_4423": ["PointLoadParametricStudyTool"],
        "_4424": ["PowerLoadParametricStudyTool"],
        "_4425": ["PulleyParametricStudyTool"],
        "_4426": ["RingPinsParametricStudyTool"],
        "_4427": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4428": ["RollingRingAssemblyParametricStudyTool"],
        "_4429": ["RollingRingConnectionParametricStudyTool"],
        "_4430": ["RollingRingParametricStudyTool"],
        "_4431": ["RootAssemblyParametricStudyTool"],
        "_4432": ["ShaftHubConnectionParametricStudyTool"],
        "_4433": ["ShaftParametricStudyTool"],
        "_4434": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4435": ["SpecialisedAssemblyParametricStudyTool"],
        "_4436": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4437": ["SpiralBevelGearParametricStudyTool"],
        "_4438": ["SpiralBevelGearSetParametricStudyTool"],
        "_4439": ["SpringDamperConnectionParametricStudyTool"],
        "_4440": ["SpringDamperHalfParametricStudyTool"],
        "_4441": ["SpringDamperParametricStudyTool"],
        "_4442": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4443": ["StraightBevelDiffGearParametricStudyTool"],
        "_4444": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4445": ["StraightBevelGearMeshParametricStudyTool"],
        "_4446": ["StraightBevelGearParametricStudyTool"],
        "_4447": ["StraightBevelGearSetParametricStudyTool"],
        "_4448": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4449": ["StraightBevelSunGearParametricStudyTool"],
        "_4450": ["SynchroniserHalfParametricStudyTool"],
        "_4451": ["SynchroniserParametricStudyTool"],
        "_4452": ["SynchroniserPartParametricStudyTool"],
        "_4453": ["SynchroniserSleeveParametricStudyTool"],
        "_4454": ["TorqueConverterConnectionParametricStudyTool"],
        "_4455": ["TorqueConverterParametricStudyTool"],
        "_4456": ["TorqueConverterPumpParametricStudyTool"],
        "_4457": ["TorqueConverterTurbineParametricStudyTool"],
        "_4458": ["UnbalancedMassParametricStudyTool"],
        "_4459": ["VirtualComponentParametricStudyTool"],
        "_4460": ["WormGearMeshParametricStudyTool"],
        "_4461": ["WormGearParametricStudyTool"],
        "_4462": ["WormGearSetParametricStudyTool"],
        "_4463": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4464": ["ZerolBevelGearParametricStudyTool"],
        "_4465": ["ZerolBevelGearSetParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyParametricStudyTool",
    "AbstractShaftOrHousingParametricStudyTool",
    "AbstractShaftParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
    "AGMAGleasonConicalGearParametricStudyTool",
    "AGMAGleasonConicalGearSetParametricStudyTool",
    "AssemblyParametricStudyTool",
    "BearingParametricStudyTool",
    "BeltConnectionParametricStudyTool",
    "BeltDriveParametricStudyTool",
    "BevelDifferentialGearMeshParametricStudyTool",
    "BevelDifferentialGearParametricStudyTool",
    "BevelDifferentialGearSetParametricStudyTool",
    "BevelDifferentialPlanetGearParametricStudyTool",
    "BevelDifferentialSunGearParametricStudyTool",
    "BevelGearMeshParametricStudyTool",
    "BevelGearParametricStudyTool",
    "BevelGearSetParametricStudyTool",
    "BoltedJointParametricStudyTool",
    "BoltParametricStudyTool",
    "ClutchConnectionParametricStudyTool",
    "ClutchHalfParametricStudyTool",
    "ClutchParametricStudyTool",
    "CoaxialConnectionParametricStudyTool",
    "ComponentParametricStudyTool",
    "ConceptCouplingConnectionParametricStudyTool",
    "ConceptCouplingHalfParametricStudyTool",
    "ConceptCouplingParametricStudyTool",
    "ConceptGearMeshParametricStudyTool",
    "ConceptGearParametricStudyTool",
    "ConceptGearSetParametricStudyTool",
    "ConicalGearMeshParametricStudyTool",
    "ConicalGearParametricStudyTool",
    "ConicalGearSetParametricStudyTool",
    "ConnectionParametricStudyTool",
    "ConnectorParametricStudyTool",
    "CouplingConnectionParametricStudyTool",
    "CouplingHalfParametricStudyTool",
    "CouplingParametricStudyTool",
    "CVTBeltConnectionParametricStudyTool",
    "CVTParametricStudyTool",
    "CVTPulleyParametricStudyTool",
    "CycloidalAssemblyParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
    "CycloidalDiscParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    "CylindricalGearMeshParametricStudyTool",
    "CylindricalGearParametricStudyTool",
    "CylindricalGearSetParametricStudyTool",
    "CylindricalPlanetGearParametricStudyTool",
    "DatumParametricStudyTool",
    "DesignOfExperimentsVariableSetter",
    "DoeValueSpecificationOption",
    "DutyCycleResultsForAllComponents",
    "DutyCycleResultsForAllGearSets",
    "DutyCycleResultsForRootAssembly",
    "DutyCycleResultsForSingleBearing",
    "DutyCycleResultsForSingleShaft",
    "ExternalCADModelParametricStudyTool",
    "FaceGearMeshParametricStudyTool",
    "FaceGearParametricStudyTool",
    "FaceGearSetParametricStudyTool",
    "FEPartParametricStudyTool",
    "FlexiblePinAssemblyParametricStudyTool",
    "GearMeshParametricStudyTool",
    "GearParametricStudyTool",
    "GearSetParametricStudyTool",
    "GuideDxfModelParametricStudyTool",
    "HypoidGearMeshParametricStudyTool",
    "HypoidGearParametricStudyTool",
    "HypoidGearSetParametricStudyTool",
    "InterMountableComponentConnectionParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool",
    "MassDiscParametricStudyTool",
    "MeasurementComponentParametricStudyTool",
    "MonteCarloDistribution",
    "MountableComponentParametricStudyTool",
    "OilSealParametricStudyTool",
    "ParametricStudyDimension",
    "ParametricStudyDOEResultVariable",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    "ParametricStudyHistogram",
    "ParametricStudyStaticLoad",
    "ParametricStudyTool",
    "ParametricStudyToolOptions",
    "ParametricStudyToolResultsForReporting",
    "ParametricStudyToolStepResult",
    "ParametricStudyVariable",
    "PartParametricStudyTool",
    "PartToPartShearCouplingConnectionParametricStudyTool",
    "PartToPartShearCouplingHalfParametricStudyTool",
    "PartToPartShearCouplingParametricStudyTool",
    "PlanetaryConnectionParametricStudyTool",
    "PlanetaryGearSetParametricStudyTool",
    "PlanetCarrierParametricStudyTool",
    "PointLoadParametricStudyTool",
    "PowerLoadParametricStudyTool",
    "PulleyParametricStudyTool",
    "RingPinsParametricStudyTool",
    "RingPinsToDiscConnectionParametricStudyTool",
    "RollingRingAssemblyParametricStudyTool",
    "RollingRingConnectionParametricStudyTool",
    "RollingRingParametricStudyTool",
    "RootAssemblyParametricStudyTool",
    "ShaftHubConnectionParametricStudyTool",
    "ShaftParametricStudyTool",
    "ShaftToMountableComponentConnectionParametricStudyTool",
    "SpecialisedAssemblyParametricStudyTool",
    "SpiralBevelGearMeshParametricStudyTool",
    "SpiralBevelGearParametricStudyTool",
    "SpiralBevelGearSetParametricStudyTool",
    "SpringDamperConnectionParametricStudyTool",
    "SpringDamperHalfParametricStudyTool",
    "SpringDamperParametricStudyTool",
    "StraightBevelDiffGearMeshParametricStudyTool",
    "StraightBevelDiffGearParametricStudyTool",
    "StraightBevelDiffGearSetParametricStudyTool",
    "StraightBevelGearMeshParametricStudyTool",
    "StraightBevelGearParametricStudyTool",
    "StraightBevelGearSetParametricStudyTool",
    "StraightBevelPlanetGearParametricStudyTool",
    "StraightBevelSunGearParametricStudyTool",
    "SynchroniserHalfParametricStudyTool",
    "SynchroniserParametricStudyTool",
    "SynchroniserPartParametricStudyTool",
    "SynchroniserSleeveParametricStudyTool",
    "TorqueConverterConnectionParametricStudyTool",
    "TorqueConverterParametricStudyTool",
    "TorqueConverterPumpParametricStudyTool",
    "TorqueConverterTurbineParametricStudyTool",
    "UnbalancedMassParametricStudyTool",
    "VirtualComponentParametricStudyTool",
    "WormGearMeshParametricStudyTool",
    "WormGearParametricStudyTool",
    "WormGearSetParametricStudyTool",
    "ZerolBevelGearMeshParametricStudyTool",
    "ZerolBevelGearParametricStudyTool",
    "ZerolBevelGearSetParametricStudyTool",
)
