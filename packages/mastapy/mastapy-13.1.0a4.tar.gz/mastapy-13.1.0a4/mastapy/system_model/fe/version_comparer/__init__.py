"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2430 import DesignResults
    from ._2431 import FESubstructureResults
    from ._2432 import FESubstructureVersionComparer
    from ._2433 import LoadCaseResults
    from ._2434 import LoadCasesToRun
    from ._2435 import NodeComparisonResult
else:
    import_structure = {
        "_2430": ["DesignResults"],
        "_2431": ["FESubstructureResults"],
        "_2432": ["FESubstructureVersionComparer"],
        "_2433": ["LoadCaseResults"],
        "_2434": ["LoadCasesToRun"],
        "_2435": ["NodeComparisonResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignResults",
    "FESubstructureResults",
    "FESubstructureVersionComparer",
    "LoadCaseResults",
    "LoadCasesToRun",
    "NodeComparisonResult",
)
