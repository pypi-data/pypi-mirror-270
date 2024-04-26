"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2504 import ConcentricOrParallelPartGroup
    from ._2505 import ConcentricPartGroup
    from ._2506 import ConcentricPartGroupParallelToThis
    from ._2507 import DesignMeasurements
    from ._2508 import ParallelPartGroup
    from ._2509 import ParallelPartGroupSelection
    from ._2510 import PartGroup
else:
    import_structure = {
        "_2504": ["ConcentricOrParallelPartGroup"],
        "_2505": ["ConcentricPartGroup"],
        "_2506": ["ConcentricPartGroupParallelToThis"],
        "_2507": ["DesignMeasurements"],
        "_2508": ["ParallelPartGroup"],
        "_2509": ["ParallelPartGroupSelection"],
        "_2510": ["PartGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConcentricOrParallelPartGroup",
    "ConcentricPartGroup",
    "ConcentricPartGroupParallelToThis",
    "DesignMeasurements",
    "ParallelPartGroup",
    "ParallelPartGroupSelection",
    "PartGroup",
)
