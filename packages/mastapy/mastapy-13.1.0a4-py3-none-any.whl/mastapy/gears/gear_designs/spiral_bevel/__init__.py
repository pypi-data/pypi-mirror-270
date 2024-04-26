"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._977 import SpiralBevelGearDesign
    from ._978 import SpiralBevelGearMeshDesign
    from ._979 import SpiralBevelGearSetDesign
    from ._980 import SpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_977": ["SpiralBevelGearDesign"],
        "_978": ["SpiralBevelGearMeshDesign"],
        "_979": ["SpiralBevelGearSetDesign"],
        "_980": ["SpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearDesign",
    "SpiralBevelGearMeshDesign",
    "SpiralBevelGearSetDesign",
    "SpiralBevelMeshedGearDesign",
)
