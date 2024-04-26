"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2255 import DesignStateTargetRatio
    from ._2256 import PlanetGearOptions
    from ._2257 import SystemOptimiser
    from ._2258 import SystemOptimiserDetails
    from ._2259 import ToothNumberFinder
else:
    import_structure = {
        "_2255": ["DesignStateTargetRatio"],
        "_2256": ["PlanetGearOptions"],
        "_2257": ["SystemOptimiser"],
        "_2258": ["SystemOptimiserDetails"],
        "_2259": ["ToothNumberFinder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)
