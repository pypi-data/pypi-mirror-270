"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._969 import StraightBevelGearDesign
    from ._970 import StraightBevelGearMeshDesign
    from ._971 import StraightBevelGearSetDesign
    from ._972 import StraightBevelMeshedGearDesign
else:
    import_structure = {
        "_969": ["StraightBevelGearDesign"],
        "_970": ["StraightBevelGearMeshDesign"],
        "_971": ["StraightBevelGearSetDesign"],
        "_972": ["StraightBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearDesign",
    "StraightBevelGearMeshDesign",
    "StraightBevelGearSetDesign",
    "StraightBevelMeshedGearDesign",
)
