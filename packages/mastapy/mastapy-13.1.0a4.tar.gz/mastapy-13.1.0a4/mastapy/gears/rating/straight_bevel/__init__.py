"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._402 import StraightBevelGearMeshRating
    from ._403 import StraightBevelGearRating
    from ._404 import StraightBevelGearSetRating
else:
    import_structure = {
        "_402": ["StraightBevelGearMeshRating"],
        "_403": ["StraightBevelGearRating"],
        "_404": ["StraightBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearMeshRating",
    "StraightBevelGearRating",
    "StraightBevelGearSetRating",
)
