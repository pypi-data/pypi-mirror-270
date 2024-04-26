"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._545 import ConicalGearDutyCycleRating
    from ._546 import ConicalGearMeshRating
    from ._547 import ConicalGearRating
    from ._548 import ConicalGearSetDutyCycleRating
    from ._549 import ConicalGearSetRating
    from ._550 import ConicalGearSingleFlankRating
    from ._551 import ConicalMeshDutyCycleRating
    from ._552 import ConicalMeshedGearRating
    from ._553 import ConicalMeshSingleFlankRating
    from ._554 import ConicalRateableMesh
else:
    import_structure = {
        "_545": ["ConicalGearDutyCycleRating"],
        "_546": ["ConicalGearMeshRating"],
        "_547": ["ConicalGearRating"],
        "_548": ["ConicalGearSetDutyCycleRating"],
        "_549": ["ConicalGearSetRating"],
        "_550": ["ConicalGearSingleFlankRating"],
        "_551": ["ConicalMeshDutyCycleRating"],
        "_552": ["ConicalMeshedGearRating"],
        "_553": ["ConicalMeshSingleFlankRating"],
        "_554": ["ConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearDutyCycleRating",
    "ConicalGearMeshRating",
    "ConicalGearRating",
    "ConicalGearSetDutyCycleRating",
    "ConicalGearSetRating",
    "ConicalGearSingleFlankRating",
    "ConicalMeshDutyCycleRating",
    "ConicalMeshedGearRating",
    "ConicalMeshSingleFlankRating",
    "ConicalRateableMesh",
)
