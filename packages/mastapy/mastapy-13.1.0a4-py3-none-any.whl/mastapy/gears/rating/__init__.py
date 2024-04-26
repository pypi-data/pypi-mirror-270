"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._360 import AbstractGearMeshRating
    from ._361 import AbstractGearRating
    from ._362 import AbstractGearSetRating
    from ._363 import BendingAndContactReportingObject
    from ._364 import FlankLoadingState
    from ._365 import GearDutyCycleRating
    from ._366 import GearFlankRating
    from ._367 import GearMeshRating
    from ._368 import GearRating
    from ._369 import GearSetDutyCycleRating
    from ._370 import GearSetRating
    from ._371 import GearSingleFlankRating
    from ._372 import MeshDutyCycleRating
    from ._373 import MeshSingleFlankRating
    from ._374 import RateableMesh
    from ._375 import SafetyFactorResults
else:
    import_structure = {
        "_360": ["AbstractGearMeshRating"],
        "_361": ["AbstractGearRating"],
        "_362": ["AbstractGearSetRating"],
        "_363": ["BendingAndContactReportingObject"],
        "_364": ["FlankLoadingState"],
        "_365": ["GearDutyCycleRating"],
        "_366": ["GearFlankRating"],
        "_367": ["GearMeshRating"],
        "_368": ["GearRating"],
        "_369": ["GearSetDutyCycleRating"],
        "_370": ["GearSetRating"],
        "_371": ["GearSingleFlankRating"],
        "_372": ["MeshDutyCycleRating"],
        "_373": ["MeshSingleFlankRating"],
        "_374": ["RateableMesh"],
        "_375": ["SafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearMeshRating",
    "AbstractGearRating",
    "AbstractGearSetRating",
    "BendingAndContactReportingObject",
    "FlankLoadingState",
    "GearDutyCycleRating",
    "GearFlankRating",
    "GearMeshRating",
    "GearRating",
    "GearSetDutyCycleRating",
    "GearSetRating",
    "GearSingleFlankRating",
    "MeshDutyCycleRating",
    "MeshSingleFlankRating",
    "RateableMesh",
    "SafetyFactorResults",
)
