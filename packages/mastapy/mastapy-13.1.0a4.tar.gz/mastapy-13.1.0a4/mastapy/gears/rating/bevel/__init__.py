"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._561 import BevelGearMeshRating
    from ._562 import BevelGearRating
    from ._563 import BevelGearSetRating
else:
    import_structure = {
        "_561": ["BevelGearMeshRating"],
        "_562": ["BevelGearRating"],
        "_563": ["BevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelGearMeshRating",
    "BevelGearRating",
    "BevelGearSetRating",
)
