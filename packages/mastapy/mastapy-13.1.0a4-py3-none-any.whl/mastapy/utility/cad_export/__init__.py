"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1847 import CADExportSettings
    from ._1848 import StockDrawings
else:
    import_structure = {
        "_1847": ["CADExportSettings"],
        "_1848": ["StockDrawings"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CADExportSettings",
    "StockDrawings",
)
