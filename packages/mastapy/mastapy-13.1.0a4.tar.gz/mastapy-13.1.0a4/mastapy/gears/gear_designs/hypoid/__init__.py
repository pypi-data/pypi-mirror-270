"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._993 import HypoidGearDesign
    from ._994 import HypoidGearMeshDesign
    from ._995 import HypoidGearSetDesign
    from ._996 import HypoidMeshedGearDesign
else:
    import_structure = {
        "_993": ["HypoidGearDesign"],
        "_994": ["HypoidGearMeshDesign"],
        "_995": ["HypoidGearSetDesign"],
        "_996": ["HypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearDesign",
    "HypoidGearMeshDesign",
    "HypoidGearSetDesign",
    "HypoidMeshedGearDesign",
)
