"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2244 import ConicalGearOptimisationStrategy
    from ._2245 import ConicalGearOptimizationStep
    from ._2246 import ConicalGearOptimizationStrategyDatabase
    from ._2247 import CylindricalGearOptimisationStrategy
    from ._2248 import CylindricalGearOptimizationStep
    from ._2249 import MeasuredAndFactorViewModel
    from ._2250 import MicroGeometryOptimisationTarget
    from ._2251 import OptimizationStep
    from ._2252 import OptimizationStrategy
    from ._2253 import OptimizationStrategyBase
    from ._2254 import OptimizationStrategyDatabase
else:
    import_structure = {
        "_2244": ["ConicalGearOptimisationStrategy"],
        "_2245": ["ConicalGearOptimizationStep"],
        "_2246": ["ConicalGearOptimizationStrategyDatabase"],
        "_2247": ["CylindricalGearOptimisationStrategy"],
        "_2248": ["CylindricalGearOptimizationStep"],
        "_2249": ["MeasuredAndFactorViewModel"],
        "_2250": ["MicroGeometryOptimisationTarget"],
        "_2251": ["OptimizationStep"],
        "_2252": ["OptimizationStrategy"],
        "_2253": ["OptimizationStrategyBase"],
        "_2254": ["OptimizationStrategyDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
