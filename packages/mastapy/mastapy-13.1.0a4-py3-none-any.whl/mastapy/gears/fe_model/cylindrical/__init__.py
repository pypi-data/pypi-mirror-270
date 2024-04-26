"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1211 import CylindricalGearFEModel
    from ._1212 import CylindricalGearMeshFEModel
    from ._1213 import CylindricalGearSetFEModel
else:
    import_structure = {
        "_1211": ["CylindricalGearFEModel"],
        "_1212": ["CylindricalGearMeshFEModel"],
        "_1213": ["CylindricalGearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearFEModel",
    "CylindricalGearMeshFEModel",
    "CylindricalGearSetFEModel",
)
