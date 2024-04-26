"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._172 import BoundaryConditionType
    from ._173 import FEExportFormat
    from ._174 import FESubstructuringFileFormat
else:
    import_structure = {
        "_172": ["BoundaryConditionType"],
        "_173": ["FEExportFormat"],
        "_174": ["FESubstructuringFileFormat"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoundaryConditionType",
    "FEExportFormat",
    "FESubstructuringFileFormat",
)
