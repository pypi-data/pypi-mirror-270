"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1849 import PlaneVectorFieldData
    from ._1850 import PlaneScalarFieldData
else:
    import_structure = {
        "_1849": ["PlaneVectorFieldData"],
        "_1850": ["PlaneScalarFieldData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "PlaneVectorFieldData",
    "PlaneScalarFieldData",
)
