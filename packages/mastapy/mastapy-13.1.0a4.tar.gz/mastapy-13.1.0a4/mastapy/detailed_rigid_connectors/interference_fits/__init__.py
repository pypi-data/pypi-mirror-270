"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1455 import AssemblyMethods
    from ._1456 import CalculationMethods
    from ._1457 import InterferenceFitDesign
    from ._1458 import InterferenceFitHalfDesign
    from ._1459 import StressRegions
    from ._1460 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1455": ["AssemblyMethods"],
        "_1456": ["CalculationMethods"],
        "_1457": ["InterferenceFitDesign"],
        "_1458": ["InterferenceFitHalfDesign"],
        "_1459": ["StressRegions"],
        "_1460": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)
