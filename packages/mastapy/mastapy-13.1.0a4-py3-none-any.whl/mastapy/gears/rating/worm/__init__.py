"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._379 import WormGearDutyCycleRating
    from ._380 import WormGearMeshRating
    from ._381 import WormGearRating
    from ._382 import WormGearSetDutyCycleRating
    from ._383 import WormGearSetRating
    from ._384 import WormMeshDutyCycleRating
else:
    import_structure = {
        "_379": ["WormGearDutyCycleRating"],
        "_380": ["WormGearMeshRating"],
        "_381": ["WormGearRating"],
        "_382": ["WormGearSetDutyCycleRating"],
        "_383": ["WormGearSetRating"],
        "_384": ["WormMeshDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearDutyCycleRating",
    "WormGearMeshRating",
    "WormGearRating",
    "WormGearSetDutyCycleRating",
    "WormGearSetRating",
    "WormMeshDutyCycleRating",
)
