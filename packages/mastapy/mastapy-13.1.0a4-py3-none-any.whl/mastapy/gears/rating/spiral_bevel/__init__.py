"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._409 import SpiralBevelGearMeshRating
    from ._410 import SpiralBevelGearRating
    from ._411 import SpiralBevelGearSetRating
else:
    import_structure = {
        "_409": ["SpiralBevelGearMeshRating"],
        "_410": ["SpiralBevelGearRating"],
        "_411": ["SpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearMeshRating",
    "SpiralBevelGearRating",
    "SpiralBevelGearSetRating",
)
