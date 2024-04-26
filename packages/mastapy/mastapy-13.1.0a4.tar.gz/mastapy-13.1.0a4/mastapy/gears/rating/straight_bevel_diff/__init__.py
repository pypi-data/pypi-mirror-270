"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._405 import StraightBevelDiffGearMeshRating
    from ._406 import StraightBevelDiffGearRating
    from ._407 import StraightBevelDiffGearSetRating
    from ._408 import StraightBevelDiffMeshedGearRating
else:
    import_structure = {
        "_405": ["StraightBevelDiffGearMeshRating"],
        "_406": ["StraightBevelDiffGearRating"],
        "_407": ["StraightBevelDiffGearSetRating"],
        "_408": ["StraightBevelDiffMeshedGearRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearMeshRating",
    "StraightBevelDiffGearRating",
    "StraightBevelDiffGearSetRating",
    "StraightBevelDiffMeshedGearRating",
)
