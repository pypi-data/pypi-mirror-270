"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._539 import DIN3990GearSingleFlankRating
    from ._540 import DIN3990MeshSingleFlankRating
else:
    import_structure = {
        "_539": ["DIN3990GearSingleFlankRating"],
        "_540": ["DIN3990MeshSingleFlankRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DIN3990GearSingleFlankRating",
    "DIN3990MeshSingleFlankRating",
)
