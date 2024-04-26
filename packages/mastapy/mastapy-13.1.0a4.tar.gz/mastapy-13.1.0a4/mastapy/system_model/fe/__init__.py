"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2373 import AlignConnectedComponentOptions
    from ._2374 import AlignmentMethod
    from ._2375 import AlignmentMethodForRaceBearing
    from ._2376 import AlignmentUsingAxialNodePositions
    from ._2377 import AngleSource
    from ._2378 import BaseFEWithSelection
    from ._2379 import BatchOperations
    from ._2380 import BearingNodeAlignmentOption
    from ._2381 import BearingNodeOption
    from ._2382 import BearingRaceNodeLink
    from ._2383 import BearingRacePosition
    from ._2384 import ComponentOrientationOption
    from ._2385 import ContactPairWithSelection
    from ._2386 import CoordinateSystemWithSelection
    from ._2387 import CreateConnectedComponentOptions
    from ._2388 import DegreeOfFreedomBoundaryCondition
    from ._2389 import DegreeOfFreedomBoundaryConditionAngular
    from ._2390 import DegreeOfFreedomBoundaryConditionLinear
    from ._2391 import ElectricMachineDataSet
    from ._2392 import ElectricMachineDynamicLoadData
    from ._2393 import ElementFaceGroupWithSelection
    from ._2394 import ElementPropertiesWithSelection
    from ._2395 import FEEntityGroupWithSelection
    from ._2396 import FEExportSettings
    from ._2397 import FEPartDRIVASurfaceSelection
    from ._2398 import FEPartWithBatchOptions
    from ._2399 import FEStiffnessGeometry
    from ._2400 import FEStiffnessTester
    from ._2401 import FESubstructure
    from ._2402 import FESubstructureExportOptions
    from ._2403 import FESubstructureNode
    from ._2404 import FESubstructureNodeModeShape
    from ._2405 import FESubstructureNodeModeShapes
    from ._2406 import FESubstructureType
    from ._2407 import FESubstructureWithBatchOptions
    from ._2408 import FESubstructureWithSelection
    from ._2409 import FESubstructureWithSelectionComponents
    from ._2410 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2411 import FESubstructureWithSelectionForModalAnalysis
    from ._2412 import FESubstructureWithSelectionForStaticAnalysis
    from ._2413 import GearMeshingOptions
    from ._2414 import IndependentMASTACreatedCondensationNode
    from ._2415 import LinkComponentAxialPositionErrorReporter
    from ._2416 import LinkNodeSource
    from ._2417 import MaterialPropertiesWithSelection
    from ._2418 import NodeBoundaryConditionStaticAnalysis
    from ._2419 import NodeGroupWithSelection
    from ._2420 import NodeSelectionDepthOption
    from ._2421 import OptionsWhenExternalFEFileAlreadyExists
    from ._2422 import PerLinkExportOptions
    from ._2423 import PerNodeExportOptions
    from ._2424 import RaceBearingFE
    from ._2425 import RaceBearingFESystemDeflection
    from ._2426 import RaceBearingFEWithSelection
    from ._2427 import ReplacedShaftSelectionHelper
    from ._2428 import SystemDeflectionFEExportOptions
    from ._2429 import ThermalExpansionOption
else:
    import_structure = {
        "_2373": ["AlignConnectedComponentOptions"],
        "_2374": ["AlignmentMethod"],
        "_2375": ["AlignmentMethodForRaceBearing"],
        "_2376": ["AlignmentUsingAxialNodePositions"],
        "_2377": ["AngleSource"],
        "_2378": ["BaseFEWithSelection"],
        "_2379": ["BatchOperations"],
        "_2380": ["BearingNodeAlignmentOption"],
        "_2381": ["BearingNodeOption"],
        "_2382": ["BearingRaceNodeLink"],
        "_2383": ["BearingRacePosition"],
        "_2384": ["ComponentOrientationOption"],
        "_2385": ["ContactPairWithSelection"],
        "_2386": ["CoordinateSystemWithSelection"],
        "_2387": ["CreateConnectedComponentOptions"],
        "_2388": ["DegreeOfFreedomBoundaryCondition"],
        "_2389": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_2390": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_2391": ["ElectricMachineDataSet"],
        "_2392": ["ElectricMachineDynamicLoadData"],
        "_2393": ["ElementFaceGroupWithSelection"],
        "_2394": ["ElementPropertiesWithSelection"],
        "_2395": ["FEEntityGroupWithSelection"],
        "_2396": ["FEExportSettings"],
        "_2397": ["FEPartDRIVASurfaceSelection"],
        "_2398": ["FEPartWithBatchOptions"],
        "_2399": ["FEStiffnessGeometry"],
        "_2400": ["FEStiffnessTester"],
        "_2401": ["FESubstructure"],
        "_2402": ["FESubstructureExportOptions"],
        "_2403": ["FESubstructureNode"],
        "_2404": ["FESubstructureNodeModeShape"],
        "_2405": ["FESubstructureNodeModeShapes"],
        "_2406": ["FESubstructureType"],
        "_2407": ["FESubstructureWithBatchOptions"],
        "_2408": ["FESubstructureWithSelection"],
        "_2409": ["FESubstructureWithSelectionComponents"],
        "_2410": ["FESubstructureWithSelectionForHarmonicAnalysis"],
        "_2411": ["FESubstructureWithSelectionForModalAnalysis"],
        "_2412": ["FESubstructureWithSelectionForStaticAnalysis"],
        "_2413": ["GearMeshingOptions"],
        "_2414": ["IndependentMASTACreatedCondensationNode"],
        "_2415": ["LinkComponentAxialPositionErrorReporter"],
        "_2416": ["LinkNodeSource"],
        "_2417": ["MaterialPropertiesWithSelection"],
        "_2418": ["NodeBoundaryConditionStaticAnalysis"],
        "_2419": ["NodeGroupWithSelection"],
        "_2420": ["NodeSelectionDepthOption"],
        "_2421": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_2422": ["PerLinkExportOptions"],
        "_2423": ["PerNodeExportOptions"],
        "_2424": ["RaceBearingFE"],
        "_2425": ["RaceBearingFESystemDeflection"],
        "_2426": ["RaceBearingFEWithSelection"],
        "_2427": ["ReplacedShaftSelectionHelper"],
        "_2428": ["SystemDeflectionFEExportOptions"],
        "_2429": ["ThermalExpansionOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
