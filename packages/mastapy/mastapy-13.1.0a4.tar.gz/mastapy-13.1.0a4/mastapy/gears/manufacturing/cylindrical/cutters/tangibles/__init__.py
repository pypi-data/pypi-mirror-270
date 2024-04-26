"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._730 import CutterShapeDefinition
    from ._731 import CylindricalGearFormedWheelGrinderTangible
    from ._732 import CylindricalGearHobShape
    from ._733 import CylindricalGearShaperTangible
    from ._734 import CylindricalGearShaverTangible
    from ._735 import CylindricalGearWormGrinderShape
    from ._736 import NamedPoint
    from ._737 import RackShape
else:
    import_structure = {
        "_730": ["CutterShapeDefinition"],
        "_731": ["CylindricalGearFormedWheelGrinderTangible"],
        "_732": ["CylindricalGearHobShape"],
        "_733": ["CylindricalGearShaperTangible"],
        "_734": ["CylindricalGearShaverTangible"],
        "_735": ["CylindricalGearWormGrinderShape"],
        "_736": ["NamedPoint"],
        "_737": ["RackShape"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterShapeDefinition",
    "CylindricalGearFormedWheelGrinderTangible",
    "CylindricalGearHobShape",
    "CylindricalGearShaperTangible",
    "CylindricalGearShaverTangible",
    "CylindricalGearWormGrinderShape",
    "NamedPoint",
    "RackShape",
)
