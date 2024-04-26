"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5270 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5271 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5272 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5273 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5274 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5275 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5276 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5277 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5278 import BearingCompoundModalAnalysisAtASpeed
    from ._5279 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5280 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5281 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5282 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5283 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5284 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5285 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5286 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5287 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5288 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5289 import BoltCompoundModalAnalysisAtASpeed
    from ._5290 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5291 import ClutchCompoundModalAnalysisAtASpeed
    from ._5292 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5293 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5294 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5295 import ComponentCompoundModalAnalysisAtASpeed
    from ._5296 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5297 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5298 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5299 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5300 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5301 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5302 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5303 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5304 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5305 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5306 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5307 import CouplingCompoundModalAnalysisAtASpeed
    from ._5308 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5309 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5310 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5311 import CVTCompoundModalAnalysisAtASpeed
    from ._5312 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5313 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5314 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5315 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5316 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5317 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5318 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5319 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5320 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5321 import DatumCompoundModalAnalysisAtASpeed
    from ._5322 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5323 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5324 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5325 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5326 import FEPartCompoundModalAnalysisAtASpeed
    from ._5327 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5328 import GearCompoundModalAnalysisAtASpeed
    from ._5329 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5330 import GearSetCompoundModalAnalysisAtASpeed
    from ._5331 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5332 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5333 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5334 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5335 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5336 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5337 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5338 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5339 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5340 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5341 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5342 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5343 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5344 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5345 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5346 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5347 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5348 import OilSealCompoundModalAnalysisAtASpeed
    from ._5349 import PartCompoundModalAnalysisAtASpeed
    from ._5350 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5351 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5352 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5353 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5354 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5355 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5356 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5357 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5358 import PulleyCompoundModalAnalysisAtASpeed
    from ._5359 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5360 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5361 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5362 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5363 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5364 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5365 import ShaftCompoundModalAnalysisAtASpeed
    from ._5366 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5367 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5368 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5369 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5370 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5371 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5372 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5373 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5374 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5375 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5376 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5377 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5378 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5379 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5380 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5381 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5382 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5383 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5384 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5385 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5386 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5387 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5388 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5389 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5390 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5391 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5392 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5393 import WormGearCompoundModalAnalysisAtASpeed
    from ._5394 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5395 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5396 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5397 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5398 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5270": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5271": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5272": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5273": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5274": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5275": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5276": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5277": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5278": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5279": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5280": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5281": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5282": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5283": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5284": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5285": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5286": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5287": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5288": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5289": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5290": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5291": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5292": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5293": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5294": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5295": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5296": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5297": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5298": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5299": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5300": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5301": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5302": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5303": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5304": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5305": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5306": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5307": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5308": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5309": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5310": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5311": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5312": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5313": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5314": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5315": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5316": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5317": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5318": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5319": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5320": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5321": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5322": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5323": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5324": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5325": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5326": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5327": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5328": ["GearCompoundModalAnalysisAtASpeed"],
        "_5329": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5330": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5331": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5332": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5333": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5334": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5335": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5336": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5337": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5338": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5339": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5340": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5341": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5342": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5343": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5344": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5345": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5346": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5347": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5348": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5349": ["PartCompoundModalAnalysisAtASpeed"],
        "_5350": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5351": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5352": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5353": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5354": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5355": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5356": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5357": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5358": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5359": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5360": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5361": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5362": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5363": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5364": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5365": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5366": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5367": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5368": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5369": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5370": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5371": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5372": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5373": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5374": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5375": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5376": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5377": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5378": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5379": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5380": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5381": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5382": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5383": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5384": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5385": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5386": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5387": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5388": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5389": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5390": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5391": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5392": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5393": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5394": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5395": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5396": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5397": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5398": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    "AssemblyCompoundModalAnalysisAtASpeed",
    "BearingCompoundModalAnalysisAtASpeed",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
    "BeltDriveCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearSetCompoundModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialSunGearCompoundModalAnalysisAtASpeed",
    "BevelGearCompoundModalAnalysisAtASpeed",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
    "BevelGearSetCompoundModalAnalysisAtASpeed",
    "BoltCompoundModalAnalysisAtASpeed",
    "BoltedJointCompoundModalAnalysisAtASpeed",
    "ClutchCompoundModalAnalysisAtASpeed",
    "ClutchConnectionCompoundModalAnalysisAtASpeed",
    "ClutchHalfCompoundModalAnalysisAtASpeed",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
    "ComponentCompoundModalAnalysisAtASpeed",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
    "ConceptCouplingConnectionCompoundModalAnalysisAtASpeed",
    "ConceptCouplingHalfCompoundModalAnalysisAtASpeed",
    "ConceptGearCompoundModalAnalysisAtASpeed",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
    "ConceptGearSetCompoundModalAnalysisAtASpeed",
    "ConicalGearCompoundModalAnalysisAtASpeed",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
    "ConicalGearSetCompoundModalAnalysisAtASpeed",
    "ConnectionCompoundModalAnalysisAtASpeed",
    "ConnectorCompoundModalAnalysisAtASpeed",
    "CouplingCompoundModalAnalysisAtASpeed",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
    "CVTCompoundModalAnalysisAtASpeed",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    "CylindricalGearCompoundModalAnalysisAtASpeed",
    "CylindricalGearMeshCompoundModalAnalysisAtASpeed",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
    "CylindricalPlanetGearCompoundModalAnalysisAtASpeed",
    "DatumCompoundModalAnalysisAtASpeed",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
    "FaceGearCompoundModalAnalysisAtASpeed",
    "FaceGearMeshCompoundModalAnalysisAtASpeed",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
    "FEPartCompoundModalAnalysisAtASpeed",
    "FlexiblePinAssemblyCompoundModalAnalysisAtASpeed",
    "GearCompoundModalAnalysisAtASpeed",
    "GearMeshCompoundModalAnalysisAtASpeed",
    "GearSetCompoundModalAnalysisAtASpeed",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
    "HypoidGearCompoundModalAnalysisAtASpeed",
    "HypoidGearMeshCompoundModalAnalysisAtASpeed",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
    "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "MassDiscCompoundModalAnalysisAtASpeed",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
    "MountableComponentCompoundModalAnalysisAtASpeed",
    "OilSealCompoundModalAnalysisAtASpeed",
    "PartCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    "PlanetaryConnectionCompoundModalAnalysisAtASpeed",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
    "PlanetCarrierCompoundModalAnalysisAtASpeed",
    "PointLoadCompoundModalAnalysisAtASpeed",
    "PowerLoadCompoundModalAnalysisAtASpeed",
    "PulleyCompoundModalAnalysisAtASpeed",
    "RingPinsCompoundModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed",
    "RollingRingAssemblyCompoundModalAnalysisAtASpeed",
    "RollingRingCompoundModalAnalysisAtASpeed",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
    "ShaftCompoundModalAnalysisAtASpeed",
    "ShaftHubConnectionCompoundModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "SpringDamperCompoundModalAnalysisAtASpeed",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelGearCompoundModalAnalysisAtASpeed",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
    "SynchroniserCompoundModalAnalysisAtASpeed",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
    "SynchroniserSleeveCompoundModalAnalysisAtASpeed",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
    "TorqueConverterTurbineCompoundModalAnalysisAtASpeed",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
    "WormGearCompoundModalAnalysisAtASpeed",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
    "WormGearSetCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearMeshCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)
