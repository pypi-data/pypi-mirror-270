"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._415 import KlingelnbergCycloPalloidHypoidGearMeshRating
    from ._416 import KlingelnbergCycloPalloidHypoidGearRating
    from ._417 import KlingelnbergCycloPalloidHypoidGearSetRating
else:
    import_structure = {
        "_415": ["KlingelnbergCycloPalloidHypoidGearMeshRating"],
        "_416": ["KlingelnbergCycloPalloidHypoidGearRating"],
        "_417": ["KlingelnbergCycloPalloidHypoidGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearMeshRating",
    "KlingelnbergCycloPalloidHypoidGearRating",
    "KlingelnbergCycloPalloidHypoidGearSetRating",
)
