"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1156 import CylindricalGearPairCreationOptions
    from ._1157 import GearSetCreationOptions
    from ._1158 import HypoidGearSetCreationOptions
    from ._1159 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        "_1156": ["CylindricalGearPairCreationOptions"],
        "_1157": ["GearSetCreationOptions"],
        "_1158": ["HypoidGearSetCreationOptions"],
        "_1159": ["SpiralBevelGearSetCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearPairCreationOptions",
    "GearSetCreationOptions",
    "HypoidGearSetCreationOptions",
    "SpiralBevelGearSetCreationOptions",
)
