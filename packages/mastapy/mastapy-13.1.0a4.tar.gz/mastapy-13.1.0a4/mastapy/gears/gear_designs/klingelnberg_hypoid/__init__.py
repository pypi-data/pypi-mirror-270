"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._985 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._986 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._987 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._988 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
else:
    import_structure = {
        "_985": ["KlingelnbergCycloPalloidHypoidGearDesign"],
        "_986": ["KlingelnbergCycloPalloidHypoidGearMeshDesign"],
        "_987": ["KlingelnbergCycloPalloidHypoidGearSetDesign"],
        "_988": ["KlingelnbergCycloPalloidHypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearDesign",
    "KlingelnbergCycloPalloidHypoidGearMeshDesign",
    "KlingelnbergCycloPalloidHypoidGearSetDesign",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)
