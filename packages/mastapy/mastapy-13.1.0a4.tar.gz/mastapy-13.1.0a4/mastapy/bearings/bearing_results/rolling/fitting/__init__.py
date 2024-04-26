"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2128 import InnerRingFittingThermalResults
    from ._2129 import InterferenceComponents
    from ._2130 import OuterRingFittingThermalResults
    from ._2131 import RingFittingThermalResults
else:
    import_structure = {
        "_2128": ["InnerRingFittingThermalResults"],
        "_2129": ["InterferenceComponents"],
        "_2130": ["OuterRingFittingThermalResults"],
        "_2131": ["RingFittingThermalResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "InnerRingFittingThermalResults",
    "InterferenceComponents",
    "OuterRingFittingThermalResults",
    "RingFittingThermalResults",
)
