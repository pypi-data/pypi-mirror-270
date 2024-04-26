"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._964 import WormDesign
    from ._965 import WormGearDesign
    from ._966 import WormGearMeshDesign
    from ._967 import WormGearSetDesign
    from ._968 import WormWheelDesign
else:
    import_structure = {
        "_964": ["WormDesign"],
        "_965": ["WormGearDesign"],
        "_966": ["WormGearMeshDesign"],
        "_967": ["WormGearSetDesign"],
        "_968": ["WormWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormDesign",
    "WormGearDesign",
    "WormGearMeshDesign",
    "WormGearSetDesign",
    "WormWheelDesign",
)
