"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1182 import ConicalGearBiasModification
    from ._1183 import ConicalGearFlankMicroGeometry
    from ._1184 import ConicalGearLeadModification
    from ._1185 import ConicalGearProfileModification
else:
    import_structure = {
        "_1182": ["ConicalGearBiasModification"],
        "_1183": ["ConicalGearFlankMicroGeometry"],
        "_1184": ["ConicalGearLeadModification"],
        "_1185": ["ConicalGearProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBiasModification",
    "ConicalGearFlankMicroGeometry",
    "ConicalGearLeadModification",
    "ConicalGearProfileModification",
)
