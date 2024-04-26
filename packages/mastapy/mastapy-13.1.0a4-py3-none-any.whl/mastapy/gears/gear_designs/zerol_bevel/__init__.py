"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._960 import ZerolBevelGearDesign
    from ._961 import ZerolBevelGearMeshDesign
    from ._962 import ZerolBevelGearSetDesign
    from ._963 import ZerolBevelMeshedGearDesign
else:
    import_structure = {
        "_960": ["ZerolBevelGearDesign"],
        "_961": ["ZerolBevelGearMeshDesign"],
        "_962": ["ZerolBevelGearSetDesign"],
        "_963": ["ZerolBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearDesign",
    "ZerolBevelGearMeshDesign",
    "ZerolBevelGearSetDesign",
    "ZerolBevelMeshedGearDesign",
)
