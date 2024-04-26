"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._973 import StraightBevelDiffGearDesign
    from ._974 import StraightBevelDiffGearMeshDesign
    from ._975 import StraightBevelDiffGearSetDesign
    from ._976 import StraightBevelDiffMeshedGearDesign
else:
    import_structure = {
        "_973": ["StraightBevelDiffGearDesign"],
        "_974": ["StraightBevelDiffGearMeshDesign"],
        "_975": ["StraightBevelDiffGearSetDesign"],
        "_976": ["StraightBevelDiffMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearDesign",
    "StraightBevelDiffGearMeshDesign",
    "StraightBevelDiffGearSetDesign",
    "StraightBevelDiffMeshedGearDesign",
)
