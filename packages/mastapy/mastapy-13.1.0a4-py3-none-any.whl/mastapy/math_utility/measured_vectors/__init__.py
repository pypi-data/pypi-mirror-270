"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1571 import AbstractForceAndDisplacementResults
    from ._1572 import ForceAndDisplacementResults
    from ._1573 import ForceResults
    from ._1574 import NodeResults
    from ._1575 import OverridableDisplacementBoundaryCondition
    from ._1576 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        "_1571": ["AbstractForceAndDisplacementResults"],
        "_1572": ["ForceAndDisplacementResults"],
        "_1573": ["ForceResults"],
        "_1574": ["NodeResults"],
        "_1575": ["OverridableDisplacementBoundaryCondition"],
        "_1576": ["VectorWithLinearAndAngularComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractForceAndDisplacementResults",
    "ForceAndDisplacementResults",
    "ForceResults",
    "NodeResults",
    "OverridableDisplacementBoundaryCondition",
    "VectorWithLinearAndAngularComponents",
)
