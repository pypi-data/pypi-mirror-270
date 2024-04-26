"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._412 import KlingelnbergCycloPalloidSpiralBevelGearMeshRating
    from ._413 import KlingelnbergCycloPalloidSpiralBevelGearRating
    from ._414 import KlingelnbergCycloPalloidSpiralBevelGearSetRating
else:
    import_structure = {
        "_412": ["KlingelnbergCycloPalloidSpiralBevelGearMeshRating"],
        "_413": ["KlingelnbergCycloPalloidSpiralBevelGearRating"],
        "_414": ["KlingelnbergCycloPalloidSpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
    "KlingelnbergCycloPalloidSpiralBevelGearSetRating",
)
