"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._449 import GleasonHypoidGearSingleFlankRating
    from ._450 import GleasonHypoidMeshSingleFlankRating
    from ._451 import HypoidRateableMesh
else:
    import_structure = {
        "_449": ["GleasonHypoidGearSingleFlankRating"],
        "_450": ["GleasonHypoidMeshSingleFlankRating"],
        "_451": ["HypoidRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GleasonHypoidGearSingleFlankRating",
    "GleasonHypoidMeshSingleFlankRating",
    "HypoidRateableMesh",
)
