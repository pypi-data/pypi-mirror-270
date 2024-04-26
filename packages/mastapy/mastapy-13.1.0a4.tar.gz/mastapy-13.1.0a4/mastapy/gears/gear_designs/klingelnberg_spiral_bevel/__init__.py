"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._981 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._982 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._983 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._984 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_981": ["KlingelnbergCycloPalloidSpiralBevelGearDesign"],
        "_982": ["KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"],
        "_983": ["KlingelnbergCycloPalloidSpiralBevelGearSetDesign"],
        "_984": ["KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearSetDesign",
    "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
)
