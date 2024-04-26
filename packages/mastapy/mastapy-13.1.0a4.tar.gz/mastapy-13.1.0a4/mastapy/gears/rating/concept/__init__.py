"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._555 import ConceptGearDutyCycleRating
    from ._556 import ConceptGearMeshDutyCycleRating
    from ._557 import ConceptGearMeshRating
    from ._558 import ConceptGearRating
    from ._559 import ConceptGearSetDutyCycleRating
    from ._560 import ConceptGearSetRating
else:
    import_structure = {
        "_555": ["ConceptGearDutyCycleRating"],
        "_556": ["ConceptGearMeshDutyCycleRating"],
        "_557": ["ConceptGearMeshRating"],
        "_558": ["ConceptGearRating"],
        "_559": ["ConceptGearSetDutyCycleRating"],
        "_560": ["ConceptGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDutyCycleRating",
    "ConceptGearMeshDutyCycleRating",
    "ConceptGearMeshRating",
    "ConceptGearRating",
    "ConceptGearSetDutyCycleRating",
    "ConceptGearSetRating",
)
