"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2148 import BearingDesign
    from ._2149 import DetailedBearing
    from ._2150 import DummyRollingBearing
    from ._2151 import LinearBearing
    from ._2152 import NonLinearBearing
else:
    import_structure = {
        "_2148": ["BearingDesign"],
        "_2149": ["DetailedBearing"],
        "_2150": ["DummyRollingBearing"],
        "_2151": ["LinearBearing"],
        "_2152": ["NonLinearBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingDesign",
    "DetailedBearing",
    "DummyRollingBearing",
    "LinearBearing",
    "NonLinearBearing",
)
