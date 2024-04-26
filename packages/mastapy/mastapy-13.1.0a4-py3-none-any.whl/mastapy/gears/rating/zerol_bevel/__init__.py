"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._376 import ZerolBevelGearMeshRating
    from ._377 import ZerolBevelGearRating
    from ._378 import ZerolBevelGearSetRating
else:
    import_structure = {
        "_376": ["ZerolBevelGearMeshRating"],
        "_377": ["ZerolBevelGearRating"],
        "_378": ["ZerolBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearMeshRating",
    "ZerolBevelGearRating",
    "ZerolBevelGearSetRating",
)
