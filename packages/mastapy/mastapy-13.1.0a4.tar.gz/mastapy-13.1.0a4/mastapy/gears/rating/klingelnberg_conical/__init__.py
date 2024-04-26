"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._418 import KlingelnbergCycloPalloidConicalGearMeshRating
    from ._419 import KlingelnbergCycloPalloidConicalGearRating
    from ._420 import KlingelnbergCycloPalloidConicalGearSetRating
else:
    import_structure = {
        "_418": ["KlingelnbergCycloPalloidConicalGearMeshRating"],
        "_419": ["KlingelnbergCycloPalloidConicalGearRating"],
        "_420": ["KlingelnbergCycloPalloidConicalGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidConicalGearMeshRating",
    "KlingelnbergCycloPalloidConicalGearRating",
    "KlingelnbergCycloPalloidConicalGearSetRating",
)
