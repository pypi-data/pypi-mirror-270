"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2589 import BeltCreationOptions
    from ._2590 import CycloidalAssemblyCreationOptions
    from ._2591 import CylindricalGearLinearTrainCreationOptions
    from ._2592 import PlanetCarrierCreationOptions
    from ._2593 import ShaftCreationOptions
else:
    import_structure = {
        "_2589": ["BeltCreationOptions"],
        "_2590": ["CycloidalAssemblyCreationOptions"],
        "_2591": ["CylindricalGearLinearTrainCreationOptions"],
        "_2592": ["PlanetCarrierCreationOptions"],
        "_2593": ["ShaftCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)
