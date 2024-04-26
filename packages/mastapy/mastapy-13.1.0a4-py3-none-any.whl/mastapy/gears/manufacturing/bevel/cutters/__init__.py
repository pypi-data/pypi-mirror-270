"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._820 import PinionFinishCutter
    from ._821 import PinionRoughCutter
    from ._822 import WheelFinishCutter
    from ._823 import WheelRoughCutter
else:
    import_structure = {
        "_820": ["PinionFinishCutter"],
        "_821": ["PinionRoughCutter"],
        "_822": ["WheelFinishCutter"],
        "_823": ["WheelRoughCutter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "PinionFinishCutter",
    "PinionRoughCutter",
    "WheelFinishCutter",
    "WheelRoughCutter",
)
