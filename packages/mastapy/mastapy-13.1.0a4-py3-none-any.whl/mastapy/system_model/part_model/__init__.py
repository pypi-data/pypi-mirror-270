"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2451 import Assembly
    from ._2452 import AbstractAssembly
    from ._2453 import AbstractShaft
    from ._2454 import AbstractShaftOrHousing
    from ._2455 import AGMALoadSharingTableApplicationLevel
    from ._2456 import AxialInternalClearanceTolerance
    from ._2457 import Bearing
    from ._2458 import BearingF0InputMethod
    from ._2459 import BearingRaceMountingOptions
    from ._2460 import Bolt
    from ._2461 import BoltedJoint
    from ._2462 import Component
    from ._2463 import ComponentsConnectedResult
    from ._2464 import ConnectedSockets
    from ._2465 import Connector
    from ._2466 import Datum
    from ._2467 import ElectricMachineSearchRegionSpecificationMethod
    from ._2468 import EnginePartLoad
    from ._2469 import EngineSpeed
    from ._2470 import ExternalCADModel
    from ._2471 import FEPart
    from ._2472 import FlexiblePinAssembly
    from ._2473 import GuideDxfModel
    from ._2474 import GuideImage
    from ._2475 import GuideModelUsage
    from ._2476 import InnerBearingRaceMountingOptions
    from ._2477 import InternalClearanceTolerance
    from ._2478 import LoadSharingModes
    from ._2479 import LoadSharingSettings
    from ._2480 import MassDisc
    from ._2481 import MeasurementComponent
    from ._2482 import MountableComponent
    from ._2483 import OilLevelSpecification
    from ._2484 import OilSeal
    from ._2485 import OuterBearingRaceMountingOptions
    from ._2486 import Part
    from ._2487 import PlanetCarrier
    from ._2488 import PlanetCarrierSettings
    from ._2489 import PointLoad
    from ._2490 import PowerLoad
    from ._2491 import RadialInternalClearanceTolerance
    from ._2492 import RootAssembly
    from ._2493 import ShaftDiameterModificationDueToRollingBearingRing
    from ._2494 import SpecialisedAssembly
    from ._2495 import UnbalancedMass
    from ._2496 import UnbalancedMassInclusionOption
    from ._2497 import VirtualComponent
    from ._2498 import WindTurbineBladeModeDetails
    from ._2499 import WindTurbineSingleBladeDetails
else:
    import_structure = {
        "_2451": ["Assembly"],
        "_2452": ["AbstractAssembly"],
        "_2453": ["AbstractShaft"],
        "_2454": ["AbstractShaftOrHousing"],
        "_2455": ["AGMALoadSharingTableApplicationLevel"],
        "_2456": ["AxialInternalClearanceTolerance"],
        "_2457": ["Bearing"],
        "_2458": ["BearingF0InputMethod"],
        "_2459": ["BearingRaceMountingOptions"],
        "_2460": ["Bolt"],
        "_2461": ["BoltedJoint"],
        "_2462": ["Component"],
        "_2463": ["ComponentsConnectedResult"],
        "_2464": ["ConnectedSockets"],
        "_2465": ["Connector"],
        "_2466": ["Datum"],
        "_2467": ["ElectricMachineSearchRegionSpecificationMethod"],
        "_2468": ["EnginePartLoad"],
        "_2469": ["EngineSpeed"],
        "_2470": ["ExternalCADModel"],
        "_2471": ["FEPart"],
        "_2472": ["FlexiblePinAssembly"],
        "_2473": ["GuideDxfModel"],
        "_2474": ["GuideImage"],
        "_2475": ["GuideModelUsage"],
        "_2476": ["InnerBearingRaceMountingOptions"],
        "_2477": ["InternalClearanceTolerance"],
        "_2478": ["LoadSharingModes"],
        "_2479": ["LoadSharingSettings"],
        "_2480": ["MassDisc"],
        "_2481": ["MeasurementComponent"],
        "_2482": ["MountableComponent"],
        "_2483": ["OilLevelSpecification"],
        "_2484": ["OilSeal"],
        "_2485": ["OuterBearingRaceMountingOptions"],
        "_2486": ["Part"],
        "_2487": ["PlanetCarrier"],
        "_2488": ["PlanetCarrierSettings"],
        "_2489": ["PointLoad"],
        "_2490": ["PowerLoad"],
        "_2491": ["RadialInternalClearanceTolerance"],
        "_2492": ["RootAssembly"],
        "_2493": ["ShaftDiameterModificationDueToRollingBearingRing"],
        "_2494": ["SpecialisedAssembly"],
        "_2495": ["UnbalancedMass"],
        "_2496": ["UnbalancedMassInclusionOption"],
        "_2497": ["VirtualComponent"],
        "_2498": ["WindTurbineBladeModeDetails"],
        "_2499": ["WindTurbineSingleBladeDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)
