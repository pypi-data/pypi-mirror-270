"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._779 import AbstractTCA
    from ._780 import BevelMachineSettingOptimizationResult
    from ._781 import ConicalFlankDeviationsData
    from ._782 import ConicalGearManufacturingAnalysis
    from ._783 import ConicalGearManufacturingConfig
    from ._784 import ConicalGearMicroGeometryConfig
    from ._785 import ConicalGearMicroGeometryConfigBase
    from ._786 import ConicalMeshedGearManufacturingAnalysis
    from ._787 import ConicalMeshedWheelFlankManufacturingConfig
    from ._788 import ConicalMeshFlankManufacturingConfig
    from ._789 import ConicalMeshFlankMicroGeometryConfig
    from ._790 import ConicalMeshFlankNURBSMicroGeometryConfig
    from ._791 import ConicalMeshManufacturingAnalysis
    from ._792 import ConicalMeshManufacturingConfig
    from ._793 import ConicalMeshMicroGeometryConfig
    from ._794 import ConicalMeshMicroGeometryConfigBase
    from ._795 import ConicalPinionManufacturingConfig
    from ._796 import ConicalPinionMicroGeometryConfig
    from ._797 import ConicalSetManufacturingAnalysis
    from ._798 import ConicalSetManufacturingConfig
    from ._799 import ConicalSetMicroGeometryConfig
    from ._800 import ConicalSetMicroGeometryConfigBase
    from ._801 import ConicalWheelManufacturingConfig
    from ._802 import EaseOffBasedTCA
    from ._803 import FlankMeasurementBorder
    from ._804 import HypoidAdvancedLibrary
    from ._805 import MachineTypes
    from ._806 import ManufacturingMachine
    from ._807 import ManufacturingMachineDatabase
    from ._808 import PinionBevelGeneratingModifiedRollMachineSettings
    from ._809 import PinionBevelGeneratingTiltMachineSettings
    from ._810 import PinionConcave
    from ._811 import PinionConicalMachineSettingsSpecified
    from ._812 import PinionConvex
    from ._813 import PinionFinishMachineSettings
    from ._814 import PinionHypoidFormateTiltMachineSettings
    from ._815 import PinionHypoidGeneratingTiltMachineSettings
    from ._816 import PinionMachineSettingsSMT
    from ._817 import PinionRoughMachineSetting
    from ._818 import Wheel
    from ._819 import WheelFormatMachineTypes
else:
    import_structure = {
        "_779": ["AbstractTCA"],
        "_780": ["BevelMachineSettingOptimizationResult"],
        "_781": ["ConicalFlankDeviationsData"],
        "_782": ["ConicalGearManufacturingAnalysis"],
        "_783": ["ConicalGearManufacturingConfig"],
        "_784": ["ConicalGearMicroGeometryConfig"],
        "_785": ["ConicalGearMicroGeometryConfigBase"],
        "_786": ["ConicalMeshedGearManufacturingAnalysis"],
        "_787": ["ConicalMeshedWheelFlankManufacturingConfig"],
        "_788": ["ConicalMeshFlankManufacturingConfig"],
        "_789": ["ConicalMeshFlankMicroGeometryConfig"],
        "_790": ["ConicalMeshFlankNURBSMicroGeometryConfig"],
        "_791": ["ConicalMeshManufacturingAnalysis"],
        "_792": ["ConicalMeshManufacturingConfig"],
        "_793": ["ConicalMeshMicroGeometryConfig"],
        "_794": ["ConicalMeshMicroGeometryConfigBase"],
        "_795": ["ConicalPinionManufacturingConfig"],
        "_796": ["ConicalPinionMicroGeometryConfig"],
        "_797": ["ConicalSetManufacturingAnalysis"],
        "_798": ["ConicalSetManufacturingConfig"],
        "_799": ["ConicalSetMicroGeometryConfig"],
        "_800": ["ConicalSetMicroGeometryConfigBase"],
        "_801": ["ConicalWheelManufacturingConfig"],
        "_802": ["EaseOffBasedTCA"],
        "_803": ["FlankMeasurementBorder"],
        "_804": ["HypoidAdvancedLibrary"],
        "_805": ["MachineTypes"],
        "_806": ["ManufacturingMachine"],
        "_807": ["ManufacturingMachineDatabase"],
        "_808": ["PinionBevelGeneratingModifiedRollMachineSettings"],
        "_809": ["PinionBevelGeneratingTiltMachineSettings"],
        "_810": ["PinionConcave"],
        "_811": ["PinionConicalMachineSettingsSpecified"],
        "_812": ["PinionConvex"],
        "_813": ["PinionFinishMachineSettings"],
        "_814": ["PinionHypoidFormateTiltMachineSettings"],
        "_815": ["PinionHypoidGeneratingTiltMachineSettings"],
        "_816": ["PinionMachineSettingsSMT"],
        "_817": ["PinionRoughMachineSetting"],
        "_818": ["Wheel"],
        "_819": ["WheelFormatMachineTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractTCA",
    "BevelMachineSettingOptimizationResult",
    "ConicalFlankDeviationsData",
    "ConicalGearManufacturingAnalysis",
    "ConicalGearManufacturingConfig",
    "ConicalGearMicroGeometryConfig",
    "ConicalGearMicroGeometryConfigBase",
    "ConicalMeshedGearManufacturingAnalysis",
    "ConicalMeshedWheelFlankManufacturingConfig",
    "ConicalMeshFlankManufacturingConfig",
    "ConicalMeshFlankMicroGeometryConfig",
    "ConicalMeshFlankNURBSMicroGeometryConfig",
    "ConicalMeshManufacturingAnalysis",
    "ConicalMeshManufacturingConfig",
    "ConicalMeshMicroGeometryConfig",
    "ConicalMeshMicroGeometryConfigBase",
    "ConicalPinionManufacturingConfig",
    "ConicalPinionMicroGeometryConfig",
    "ConicalSetManufacturingAnalysis",
    "ConicalSetManufacturingConfig",
    "ConicalSetMicroGeometryConfig",
    "ConicalSetMicroGeometryConfigBase",
    "ConicalWheelManufacturingConfig",
    "EaseOffBasedTCA",
    "FlankMeasurementBorder",
    "HypoidAdvancedLibrary",
    "MachineTypes",
    "ManufacturingMachine",
    "ManufacturingMachineDatabase",
    "PinionBevelGeneratingModifiedRollMachineSettings",
    "PinionBevelGeneratingTiltMachineSettings",
    "PinionConcave",
    "PinionConicalMachineSettingsSpecified",
    "PinionConvex",
    "PinionFinishMachineSettings",
    "PinionHypoidFormateTiltMachineSettings",
    "PinionHypoidGeneratingTiltMachineSettings",
    "PinionMachineSettingsSMT",
    "PinionRoughMachineSetting",
    "Wheel",
    "WheelFormatMachineTypes",
)
