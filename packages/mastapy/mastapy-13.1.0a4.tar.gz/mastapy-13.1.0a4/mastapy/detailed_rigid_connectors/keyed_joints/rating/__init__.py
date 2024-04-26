"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1453 import KeywayHalfRating
    from ._1454 import KeywayRating
else:
    import_structure = {
        "_1453": ["KeywayHalfRating"],
        "_1454": ["KeywayRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeywayHalfRating",
    "KeywayRating",
)
