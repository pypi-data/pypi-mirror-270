"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2502 import SpecifiedConcentricPartGroupDrawingOrder
    from ._2503 import SpecifiedParallelPartGroupDrawingOrder
else:
    import_structure = {
        "_2502": ["SpecifiedConcentricPartGroupDrawingOrder"],
        "_2503": ["SpecifiedParallelPartGroupDrawingOrder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpecifiedConcentricPartGroupDrawingOrder",
    "SpecifiedParallelPartGroupDrawingOrder",
)
