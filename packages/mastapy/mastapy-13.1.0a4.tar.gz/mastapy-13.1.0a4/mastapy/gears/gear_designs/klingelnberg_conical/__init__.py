"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._989 import KlingelnbergConicalGearDesign
    from ._990 import KlingelnbergConicalGearMeshDesign
    from ._991 import KlingelnbergConicalGearSetDesign
    from ._992 import KlingelnbergConicalMeshedGearDesign
else:
    import_structure = {
        "_989": ["KlingelnbergConicalGearDesign"],
        "_990": ["KlingelnbergConicalGearMeshDesign"],
        "_991": ["KlingelnbergConicalGearSetDesign"],
        "_992": ["KlingelnbergConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalGearDesign",
    "KlingelnbergConicalGearMeshDesign",
    "KlingelnbergConicalGearSetDesign",
    "KlingelnbergConicalMeshedGearDesign",
)
