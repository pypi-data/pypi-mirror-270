"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._564 import AGMASpiralBevelGearSingleFlankRating
    from ._565 import AGMASpiralBevelMeshSingleFlankRating
    from ._566 import GleasonSpiralBevelGearSingleFlankRating
    from ._567 import GleasonSpiralBevelMeshSingleFlankRating
    from ._568 import SpiralBevelGearSingleFlankRating
    from ._569 import SpiralBevelMeshSingleFlankRating
    from ._570 import SpiralBevelRateableGear
    from ._571 import SpiralBevelRateableMesh
else:
    import_structure = {
        "_564": ["AGMASpiralBevelGearSingleFlankRating"],
        "_565": ["AGMASpiralBevelMeshSingleFlankRating"],
        "_566": ["GleasonSpiralBevelGearSingleFlankRating"],
        "_567": ["GleasonSpiralBevelMeshSingleFlankRating"],
        "_568": ["SpiralBevelGearSingleFlankRating"],
        "_569": ["SpiralBevelMeshSingleFlankRating"],
        "_570": ["SpiralBevelRateableGear"],
        "_571": ["SpiralBevelRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMASpiralBevelGearSingleFlankRating",
    "AGMASpiralBevelMeshSingleFlankRating",
    "GleasonSpiralBevelGearSingleFlankRating",
    "GleasonSpiralBevelMeshSingleFlankRating",
    "SpiralBevelGearSingleFlankRating",
    "SpiralBevelMeshSingleFlankRating",
    "SpiralBevelRateableGear",
    "SpiralBevelRateableMesh",
)
