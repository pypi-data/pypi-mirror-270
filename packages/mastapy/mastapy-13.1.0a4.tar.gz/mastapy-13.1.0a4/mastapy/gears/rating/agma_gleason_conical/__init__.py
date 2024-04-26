"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._572 import AGMAGleasonConicalGearMeshRating
    from ._573 import AGMAGleasonConicalGearRating
    from ._574 import AGMAGleasonConicalGearSetRating
    from ._575 import AGMAGleasonConicalRateableMesh
else:
    import_structure = {
        "_572": ["AGMAGleasonConicalGearMeshRating"],
        "_573": ["AGMAGleasonConicalGearRating"],
        "_574": ["AGMAGleasonConicalGearSetRating"],
        "_575": ["AGMAGleasonConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMeshRating",
    "AGMAGleasonConicalGearRating",
    "AGMAGleasonConicalGearSetRating",
    "AGMAGleasonConicalRateableMesh",
)
