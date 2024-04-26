"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1214 import ConicalGearFEModel
    from ._1215 import ConicalMeshFEModel
    from ._1216 import ConicalSetFEModel
    from ._1217 import FlankDataSource
else:
    import_structure = {
        "_1214": ["ConicalGearFEModel"],
        "_1215": ["ConicalMeshFEModel"],
        "_1216": ["ConicalSetFEModel"],
        "_1217": ["FlankDataSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFEModel",
    "ConicalMeshFEModel",
    "ConicalSetFEModel",
    "FlankDataSource",
)
