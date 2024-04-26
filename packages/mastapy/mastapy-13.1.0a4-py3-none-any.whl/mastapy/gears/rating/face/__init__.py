"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._452 import FaceGearDutyCycleRating
    from ._453 import FaceGearMeshDutyCycleRating
    from ._454 import FaceGearMeshRating
    from ._455 import FaceGearRating
    from ._456 import FaceGearSetDutyCycleRating
    from ._457 import FaceGearSetRating
else:
    import_structure = {
        "_452": ["FaceGearDutyCycleRating"],
        "_453": ["FaceGearMeshDutyCycleRating"],
        "_454": ["FaceGearMeshRating"],
        "_455": ["FaceGearRating"],
        "_456": ["FaceGearSetDutyCycleRating"],
        "_457": ["FaceGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDutyCycleRating",
    "FaceGearMeshDutyCycleRating",
    "FaceGearMeshRating",
    "FaceGearRating",
    "FaceGearSetDutyCycleRating",
    "FaceGearSetRating",
)
