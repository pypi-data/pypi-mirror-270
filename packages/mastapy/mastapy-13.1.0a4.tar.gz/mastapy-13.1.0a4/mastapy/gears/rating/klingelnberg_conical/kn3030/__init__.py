"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._421 import KlingelnbergConicalMeshSingleFlankRating
    from ._422 import KlingelnbergConicalRateableMesh
    from ._423 import KlingelnbergCycloPalloidConicalGearSingleFlankRating
    from ._424 import KlingelnbergCycloPalloidHypoidGearSingleFlankRating
    from ._425 import KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
    from ._426 import KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
else:
    import_structure = {
        "_421": ["KlingelnbergConicalMeshSingleFlankRating"],
        "_422": ["KlingelnbergConicalRateableMesh"],
        "_423": ["KlingelnbergCycloPalloidConicalGearSingleFlankRating"],
        "_424": ["KlingelnbergCycloPalloidHypoidGearSingleFlankRating"],
        "_425": ["KlingelnbergCycloPalloidHypoidMeshSingleFlankRating"],
        "_426": ["KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalMeshSingleFlankRating",
    "KlingelnbergConicalRateableMesh",
    "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidMeshSingleFlankRating",
    "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
)
