"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1202 import AGMAGleasonConicalAccuracyGrades
    from ._1203 import AGMAGleasonConicalGearDesign
    from ._1204 import AGMAGleasonConicalGearMeshDesign
    from ._1205 import AGMAGleasonConicalGearSetDesign
    from ._1206 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        "_1202": ["AGMAGleasonConicalAccuracyGrades"],
        "_1203": ["AGMAGleasonConicalGearDesign"],
        "_1204": ["AGMAGleasonConicalGearMeshDesign"],
        "_1205": ["AGMAGleasonConicalGearSetDesign"],
        "_1206": ["AGMAGleasonConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalAccuracyGrades",
    "AGMAGleasonConicalGearDesign",
    "AGMAGleasonConicalGearMeshDesign",
    "AGMAGleasonConicalGearSetDesign",
    "AGMAGleasonConicalMeshedGearDesign",
)
