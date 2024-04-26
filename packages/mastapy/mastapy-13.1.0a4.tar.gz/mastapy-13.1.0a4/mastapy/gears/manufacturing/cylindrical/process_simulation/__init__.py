"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._646 import CutterProcessSimulation
    from ._647 import FormWheelGrindingProcessSimulation
    from ._648 import ShapingProcessSimulation
else:
    import_structure = {
        "_646": ["CutterProcessSimulation"],
        "_647": ["FormWheelGrindingProcessSimulation"],
        "_648": ["ShapingProcessSimulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterProcessSimulation",
    "FormWheelGrindingProcessSimulation",
    "ShapingProcessSimulation",
)
