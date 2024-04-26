"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._738 import CutterSimulationCalc
    from ._739 import CylindricalCutterSimulatableGear
    from ._740 import CylindricalGearSpecification
    from ._741 import CylindricalManufacturedRealGearInMesh
    from ._742 import CylindricalManufacturedVirtualGearInMesh
    from ._743 import FinishCutterSimulation
    from ._744 import FinishStockPoint
    from ._745 import FormWheelGrindingSimulationCalculator
    from ._746 import GearCutterSimulation
    from ._747 import HobSimulationCalculator
    from ._748 import ManufacturingOperationConstraints
    from ._749 import ManufacturingProcessControls
    from ._750 import RackSimulationCalculator
    from ._751 import RoughCutterSimulation
    from ._752 import ShaperSimulationCalculator
    from ._753 import ShavingSimulationCalculator
    from ._754 import VirtualSimulationCalculator
    from ._755 import WormGrinderSimulationCalculator
else:
    import_structure = {
        "_738": ["CutterSimulationCalc"],
        "_739": ["CylindricalCutterSimulatableGear"],
        "_740": ["CylindricalGearSpecification"],
        "_741": ["CylindricalManufacturedRealGearInMesh"],
        "_742": ["CylindricalManufacturedVirtualGearInMesh"],
        "_743": ["FinishCutterSimulation"],
        "_744": ["FinishStockPoint"],
        "_745": ["FormWheelGrindingSimulationCalculator"],
        "_746": ["GearCutterSimulation"],
        "_747": ["HobSimulationCalculator"],
        "_748": ["ManufacturingOperationConstraints"],
        "_749": ["ManufacturingProcessControls"],
        "_750": ["RackSimulationCalculator"],
        "_751": ["RoughCutterSimulation"],
        "_752": ["ShaperSimulationCalculator"],
        "_753": ["ShavingSimulationCalculator"],
        "_754": ["VirtualSimulationCalculator"],
        "_755": ["WormGrinderSimulationCalculator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterSimulationCalc",
    "CylindricalCutterSimulatableGear",
    "CylindricalGearSpecification",
    "CylindricalManufacturedRealGearInMesh",
    "CylindricalManufacturedVirtualGearInMesh",
    "FinishCutterSimulation",
    "FinishStockPoint",
    "FormWheelGrindingSimulationCalculator",
    "GearCutterSimulation",
    "HobSimulationCalculator",
    "ManufacturingOperationConstraints",
    "ManufacturingProcessControls",
    "RackSimulationCalculator",
    "RoughCutterSimulation",
    "ShaperSimulationCalculator",
    "ShavingSimulationCalculator",
    "VirtualSimulationCalculator",
    "WormGrinderSimulationCalculator",
)
