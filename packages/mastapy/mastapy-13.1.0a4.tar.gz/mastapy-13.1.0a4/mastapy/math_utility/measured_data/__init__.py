"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1577 import GriddedSurfaceAccessor
    from ._1578 import LookupTableBase
    from ._1579 import OnedimensionalFunctionLookupTable
    from ._1580 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        "_1577": ["GriddedSurfaceAccessor"],
        "_1578": ["LookupTableBase"],
        "_1579": ["OnedimensionalFunctionLookupTable"],
        "_1580": ["TwodimensionalFunctionLookupTable"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GriddedSurfaceAccessor",
    "LookupTableBase",
    "OnedimensionalFunctionLookupTable",
    "TwodimensionalFunctionLookupTable",
)
