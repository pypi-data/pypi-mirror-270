"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._182 import Data
    from ._183 import Data1D
    from ._184 import Data3D
else:
    import_structure = {
        "_182": ["Data"],
        "_183": ["Data1D"],
        "_184": ["Data3D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Data",
    "Data1D",
    "Data3D",
)
