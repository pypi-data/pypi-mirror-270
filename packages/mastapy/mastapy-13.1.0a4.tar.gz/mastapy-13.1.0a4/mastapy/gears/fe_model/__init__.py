"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1207 import GearFEModel
    from ._1208 import GearMeshFEModel
    from ._1209 import GearMeshingElementOptions
    from ._1210 import GearSetFEModel
else:
    import_structure = {
        "_1207": ["GearFEModel"],
        "_1208": ["GearMeshFEModel"],
        "_1209": ["GearMeshingElementOptions"],
        "_1210": ["GearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearFEModel",
    "GearMeshFEModel",
    "GearMeshingElementOptions",
    "GearSetFEModel",
)
