"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1433 import FitAndTolerance
    from ._1434 import SAESplineTolerances
else:
    import_structure = {
        "_1433": ["FitAndTolerance"],
        "_1434": ["SAESplineTolerances"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FitAndTolerance",
    "SAESplineTolerances",
)
