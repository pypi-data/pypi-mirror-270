"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4049 import RotorDynamicsDrawStyle
    from ._4050 import ShaftComplexShape
    from ._4051 import ShaftForcedComplexShape
    from ._4052 import ShaftModalComplexShape
    from ._4053 import ShaftModalComplexShapeAtSpeeds
    from ._4054 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        "_4049": ["RotorDynamicsDrawStyle"],
        "_4050": ["ShaftComplexShape"],
        "_4051": ["ShaftForcedComplexShape"],
        "_4052": ["ShaftModalComplexShape"],
        "_4053": ["ShaftModalComplexShapeAtSpeeds"],
        "_4054": ["ShaftModalComplexShapeAtStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "RotorDynamicsDrawStyle",
    "ShaftComplexShape",
    "ShaftForcedComplexShape",
    "ShaftModalComplexShape",
    "ShaftModalComplexShapeAtSpeeds",
    "ShaftModalComplexShapeAtStiffness",
)
