"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._445 import HypoidGearMeshRating
    from ._446 import HypoidGearRating
    from ._447 import HypoidGearSetRating
    from ._448 import HypoidRatingMethod
else:
    import_structure = {
        "_445": ["HypoidGearMeshRating"],
        "_446": ["HypoidGearRating"],
        "_447": ["HypoidGearSetRating"],
        "_448": ["HypoidRatingMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearMeshRating",
    "HypoidGearRating",
    "HypoidGearSetRating",
    "HypoidRatingMethod",
)
