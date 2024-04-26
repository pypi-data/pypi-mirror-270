"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7296 import AbstractAssemblyAdvancedSystemDeflection
    from ._7297 import AbstractShaftAdvancedSystemDeflection
    from ._7298 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7299 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7300 import AdvancedSystemDeflection
    from ._7301 import AdvancedSystemDeflectionOptions
    from ._7302 import AdvancedSystemDeflectionSubAnalysis
    from ._7303 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7304 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7305 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7306 import AssemblyAdvancedSystemDeflection
    from ._7307 import BearingAdvancedSystemDeflection
    from ._7308 import BeltConnectionAdvancedSystemDeflection
    from ._7309 import BeltDriveAdvancedSystemDeflection
    from ._7310 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7311 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7312 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7313 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7314 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7315 import BevelGearAdvancedSystemDeflection
    from ._7316 import BevelGearMeshAdvancedSystemDeflection
    from ._7317 import BevelGearSetAdvancedSystemDeflection
    from ._7318 import BoltAdvancedSystemDeflection
    from ._7319 import BoltedJointAdvancedSystemDeflection
    from ._7320 import ClutchAdvancedSystemDeflection
    from ._7321 import ClutchConnectionAdvancedSystemDeflection
    from ._7322 import ClutchHalfAdvancedSystemDeflection
    from ._7323 import CoaxialConnectionAdvancedSystemDeflection
    from ._7324 import ComponentAdvancedSystemDeflection
    from ._7325 import ConceptCouplingAdvancedSystemDeflection
    from ._7326 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7327 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7328 import ConceptGearAdvancedSystemDeflection
    from ._7329 import ConceptGearMeshAdvancedSystemDeflection
    from ._7330 import ConceptGearSetAdvancedSystemDeflection
    from ._7331 import ConicalGearAdvancedSystemDeflection
    from ._7332 import ConicalGearMeshAdvancedSystemDeflection
    from ._7333 import ConicalGearSetAdvancedSystemDeflection
    from ._7334 import ConnectionAdvancedSystemDeflection
    from ._7335 import ConnectorAdvancedSystemDeflection
    from ._7336 import ContactChartPerToothPass
    from ._7337 import CouplingAdvancedSystemDeflection
    from ._7338 import CouplingConnectionAdvancedSystemDeflection
    from ._7339 import CouplingHalfAdvancedSystemDeflection
    from ._7340 import CVTAdvancedSystemDeflection
    from ._7341 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7342 import CVTPulleyAdvancedSystemDeflection
    from ._7343 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7344 import CycloidalDiscAdvancedSystemDeflection
    from ._7345 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7346 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7347 import CylindricalGearAdvancedSystemDeflection
    from ._7348 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7349 import CylindricalGearSetAdvancedSystemDeflection
    from ._7350 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7351 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7352 import DatumAdvancedSystemDeflection
    from ._7353 import ExternalCADModelAdvancedSystemDeflection
    from ._7354 import FaceGearAdvancedSystemDeflection
    from ._7355 import FaceGearMeshAdvancedSystemDeflection
    from ._7356 import FaceGearSetAdvancedSystemDeflection
    from ._7357 import FEPartAdvancedSystemDeflection
    from ._7358 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7359 import GearAdvancedSystemDeflection
    from ._7360 import GearMeshAdvancedSystemDeflection
    from ._7361 import GearSetAdvancedSystemDeflection
    from ._7362 import GuideDxfModelAdvancedSystemDeflection
    from ._7363 import HypoidGearAdvancedSystemDeflection
    from ._7364 import HypoidGearMeshAdvancedSystemDeflection
    from ._7365 import HypoidGearSetAdvancedSystemDeflection
    from ._7366 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7367 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7368 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7369 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7370 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7371 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7372 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7373 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7374 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7375 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7376 import UseLtcaInAsdOption
    from ._7377 import MassDiscAdvancedSystemDeflection
    from ._7378 import MeasurementComponentAdvancedSystemDeflection
    from ._7379 import MountableComponentAdvancedSystemDeflection
    from ._7380 import OilSealAdvancedSystemDeflection
    from ._7381 import PartAdvancedSystemDeflection
    from ._7382 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7383 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7384 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7385 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7386 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7387 import PlanetCarrierAdvancedSystemDeflection
    from ._7388 import PointLoadAdvancedSystemDeflection
    from ._7389 import PowerLoadAdvancedSystemDeflection
    from ._7390 import PulleyAdvancedSystemDeflection
    from ._7391 import RingPinsAdvancedSystemDeflection
    from ._7392 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7393 import RollingRingAdvancedSystemDeflection
    from ._7394 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7395 import RollingRingConnectionAdvancedSystemDeflection
    from ._7396 import RootAssemblyAdvancedSystemDeflection
    from ._7397 import ShaftAdvancedSystemDeflection
    from ._7398 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7399 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7400 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7401 import SpiralBevelGearAdvancedSystemDeflection
    from ._7402 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7403 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7404 import SpringDamperAdvancedSystemDeflection
    from ._7405 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7406 import SpringDamperHalfAdvancedSystemDeflection
    from ._7407 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7408 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7409 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7410 import StraightBevelGearAdvancedSystemDeflection
    from ._7411 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7412 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7413 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7414 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7415 import SynchroniserAdvancedSystemDeflection
    from ._7416 import SynchroniserHalfAdvancedSystemDeflection
    from ._7417 import SynchroniserPartAdvancedSystemDeflection
    from ._7418 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7419 import TorqueConverterAdvancedSystemDeflection
    from ._7420 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7421 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7422 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7423 import TransmissionErrorToOtherPowerLoad
    from ._7424 import UnbalancedMassAdvancedSystemDeflection
    from ._7425 import VirtualComponentAdvancedSystemDeflection
    from ._7426 import WormGearAdvancedSystemDeflection
    from ._7427 import WormGearMeshAdvancedSystemDeflection
    from ._7428 import WormGearSetAdvancedSystemDeflection
    from ._7429 import ZerolBevelGearAdvancedSystemDeflection
    from ._7430 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7431 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7296": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7297": ["AbstractShaftAdvancedSystemDeflection"],
        "_7298": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7299": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7300": ["AdvancedSystemDeflection"],
        "_7301": ["AdvancedSystemDeflectionOptions"],
        "_7302": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7303": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7304": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7305": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7306": ["AssemblyAdvancedSystemDeflection"],
        "_7307": ["BearingAdvancedSystemDeflection"],
        "_7308": ["BeltConnectionAdvancedSystemDeflection"],
        "_7309": ["BeltDriveAdvancedSystemDeflection"],
        "_7310": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7311": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7312": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7313": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7314": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7315": ["BevelGearAdvancedSystemDeflection"],
        "_7316": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7317": ["BevelGearSetAdvancedSystemDeflection"],
        "_7318": ["BoltAdvancedSystemDeflection"],
        "_7319": ["BoltedJointAdvancedSystemDeflection"],
        "_7320": ["ClutchAdvancedSystemDeflection"],
        "_7321": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7322": ["ClutchHalfAdvancedSystemDeflection"],
        "_7323": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7324": ["ComponentAdvancedSystemDeflection"],
        "_7325": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7326": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7327": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7328": ["ConceptGearAdvancedSystemDeflection"],
        "_7329": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7330": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7331": ["ConicalGearAdvancedSystemDeflection"],
        "_7332": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7333": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7334": ["ConnectionAdvancedSystemDeflection"],
        "_7335": ["ConnectorAdvancedSystemDeflection"],
        "_7336": ["ContactChartPerToothPass"],
        "_7337": ["CouplingAdvancedSystemDeflection"],
        "_7338": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7339": ["CouplingHalfAdvancedSystemDeflection"],
        "_7340": ["CVTAdvancedSystemDeflection"],
        "_7341": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7342": ["CVTPulleyAdvancedSystemDeflection"],
        "_7343": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7344": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7345": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7346": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7347": ["CylindricalGearAdvancedSystemDeflection"],
        "_7348": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7349": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7350": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7351": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7352": ["DatumAdvancedSystemDeflection"],
        "_7353": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7354": ["FaceGearAdvancedSystemDeflection"],
        "_7355": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7356": ["FaceGearSetAdvancedSystemDeflection"],
        "_7357": ["FEPartAdvancedSystemDeflection"],
        "_7358": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7359": ["GearAdvancedSystemDeflection"],
        "_7360": ["GearMeshAdvancedSystemDeflection"],
        "_7361": ["GearSetAdvancedSystemDeflection"],
        "_7362": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7363": ["HypoidGearAdvancedSystemDeflection"],
        "_7364": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7365": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7366": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7367": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7368": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7369": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7370": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7371": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7372": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7373": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7374": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7375": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7376": ["UseLtcaInAsdOption"],
        "_7377": ["MassDiscAdvancedSystemDeflection"],
        "_7378": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7379": ["MountableComponentAdvancedSystemDeflection"],
        "_7380": ["OilSealAdvancedSystemDeflection"],
        "_7381": ["PartAdvancedSystemDeflection"],
        "_7382": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7383": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7384": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7385": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7386": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7387": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7388": ["PointLoadAdvancedSystemDeflection"],
        "_7389": ["PowerLoadAdvancedSystemDeflection"],
        "_7390": ["PulleyAdvancedSystemDeflection"],
        "_7391": ["RingPinsAdvancedSystemDeflection"],
        "_7392": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7393": ["RollingRingAdvancedSystemDeflection"],
        "_7394": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7395": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7396": ["RootAssemblyAdvancedSystemDeflection"],
        "_7397": ["ShaftAdvancedSystemDeflection"],
        "_7398": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7399": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7400": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7401": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7402": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7403": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7404": ["SpringDamperAdvancedSystemDeflection"],
        "_7405": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7406": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7407": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7408": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7409": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7410": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7411": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7412": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7413": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7414": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7415": ["SynchroniserAdvancedSystemDeflection"],
        "_7416": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7417": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7418": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7419": ["TorqueConverterAdvancedSystemDeflection"],
        "_7420": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7421": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7422": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7423": ["TransmissionErrorToOtherPowerLoad"],
        "_7424": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7425": ["VirtualComponentAdvancedSystemDeflection"],
        "_7426": ["WormGearAdvancedSystemDeflection"],
        "_7427": ["WormGearMeshAdvancedSystemDeflection"],
        "_7428": ["WormGearSetAdvancedSystemDeflection"],
        "_7429": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7430": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7431": ["ZerolBevelGearSetAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedSystemDeflection",
    "AbstractShaftAdvancedSystemDeflection",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "AdvancedSystemDeflection",
    "AdvancedSystemDeflectionOptions",
    "AdvancedSystemDeflectionSubAnalysis",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
    "AssemblyAdvancedSystemDeflection",
    "BearingAdvancedSystemDeflection",
    "BeltConnectionAdvancedSystemDeflection",
    "BeltDriveAdvancedSystemDeflection",
    "BevelDifferentialGearAdvancedSystemDeflection",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
    "BevelDifferentialGearSetAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearAdvancedSystemDeflection",
    "BevelDifferentialSunGearAdvancedSystemDeflection",
    "BevelGearAdvancedSystemDeflection",
    "BevelGearMeshAdvancedSystemDeflection",
    "BevelGearSetAdvancedSystemDeflection",
    "BoltAdvancedSystemDeflection",
    "BoltedJointAdvancedSystemDeflection",
    "ClutchAdvancedSystemDeflection",
    "ClutchConnectionAdvancedSystemDeflection",
    "ClutchHalfAdvancedSystemDeflection",
    "CoaxialConnectionAdvancedSystemDeflection",
    "ComponentAdvancedSystemDeflection",
    "ConceptCouplingAdvancedSystemDeflection",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
    "ConceptCouplingHalfAdvancedSystemDeflection",
    "ConceptGearAdvancedSystemDeflection",
    "ConceptGearMeshAdvancedSystemDeflection",
    "ConceptGearSetAdvancedSystemDeflection",
    "ConicalGearAdvancedSystemDeflection",
    "ConicalGearMeshAdvancedSystemDeflection",
    "ConicalGearSetAdvancedSystemDeflection",
    "ConnectionAdvancedSystemDeflection",
    "ConnectorAdvancedSystemDeflection",
    "ContactChartPerToothPass",
    "CouplingAdvancedSystemDeflection",
    "CouplingConnectionAdvancedSystemDeflection",
    "CouplingHalfAdvancedSystemDeflection",
    "CVTAdvancedSystemDeflection",
    "CVTBeltConnectionAdvancedSystemDeflection",
    "CVTPulleyAdvancedSystemDeflection",
    "CycloidalAssemblyAdvancedSystemDeflection",
    "CycloidalDiscAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection",
    "CylindricalGearAdvancedSystemDeflection",
    "CylindricalGearMeshAdvancedSystemDeflection",
    "CylindricalGearSetAdvancedSystemDeflection",
    "CylindricalMeshedGearAdvancedSystemDeflection",
    "CylindricalPlanetGearAdvancedSystemDeflection",
    "DatumAdvancedSystemDeflection",
    "ExternalCADModelAdvancedSystemDeflection",
    "FaceGearAdvancedSystemDeflection",
    "FaceGearMeshAdvancedSystemDeflection",
    "FaceGearSetAdvancedSystemDeflection",
    "FEPartAdvancedSystemDeflection",
    "FlexiblePinAssemblyAdvancedSystemDeflection",
    "GearAdvancedSystemDeflection",
    "GearMeshAdvancedSystemDeflection",
    "GearSetAdvancedSystemDeflection",
    "GuideDxfModelAdvancedSystemDeflection",
    "HypoidGearAdvancedSystemDeflection",
    "HypoidGearMeshAdvancedSystemDeflection",
    "HypoidGearSetAdvancedSystemDeflection",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    "UseLtcaInAsdOption",
    "MassDiscAdvancedSystemDeflection",
    "MeasurementComponentAdvancedSystemDeflection",
    "MountableComponentAdvancedSystemDeflection",
    "OilSealAdvancedSystemDeflection",
    "PartAdvancedSystemDeflection",
    "PartToPartShearCouplingAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
    "PlanetaryConnectionAdvancedSystemDeflection",
    "PlanetaryGearSetAdvancedSystemDeflection",
    "PlanetCarrierAdvancedSystemDeflection",
    "PointLoadAdvancedSystemDeflection",
    "PowerLoadAdvancedSystemDeflection",
    "PulleyAdvancedSystemDeflection",
    "RingPinsAdvancedSystemDeflection",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
    "RollingRingAdvancedSystemDeflection",
    "RollingRingAssemblyAdvancedSystemDeflection",
    "RollingRingConnectionAdvancedSystemDeflection",
    "RootAssemblyAdvancedSystemDeflection",
    "ShaftAdvancedSystemDeflection",
    "ShaftHubConnectionAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "SpecialisedAssemblyAdvancedSystemDeflection",
    "SpiralBevelGearAdvancedSystemDeflection",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
    "SpiralBevelGearSetAdvancedSystemDeflection",
    "SpringDamperAdvancedSystemDeflection",
    "SpringDamperConnectionAdvancedSystemDeflection",
    "SpringDamperHalfAdvancedSystemDeflection",
    "StraightBevelDiffGearAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
    "StraightBevelGearAdvancedSystemDeflection",
    "StraightBevelGearMeshAdvancedSystemDeflection",
    "StraightBevelGearSetAdvancedSystemDeflection",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
    "StraightBevelSunGearAdvancedSystemDeflection",
    "SynchroniserAdvancedSystemDeflection",
    "SynchroniserHalfAdvancedSystemDeflection",
    "SynchroniserPartAdvancedSystemDeflection",
    "SynchroniserSleeveAdvancedSystemDeflection",
    "TorqueConverterAdvancedSystemDeflection",
    "TorqueConverterConnectionAdvancedSystemDeflection",
    "TorqueConverterPumpAdvancedSystemDeflection",
    "TorqueConverterTurbineAdvancedSystemDeflection",
    "TransmissionErrorToOtherPowerLoad",
    "UnbalancedMassAdvancedSystemDeflection",
    "VirtualComponentAdvancedSystemDeflection",
    "WormGearAdvancedSystemDeflection",
    "WormGearMeshAdvancedSystemDeflection",
    "WormGearSetAdvancedSystemDeflection",
    "ZerolBevelGearAdvancedSystemDeflection",
    "ZerolBevelGearMeshAdvancedSystemDeflection",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)
