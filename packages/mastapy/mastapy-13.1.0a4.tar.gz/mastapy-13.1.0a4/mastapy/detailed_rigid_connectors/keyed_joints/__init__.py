"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1449 import KeyedJointDesign
    from ._1450 import KeyTypes
    from ._1451 import KeywayJointHalfDesign
    from ._1452 import NumberOfKeys
else:
    import_structure = {
        "_1449": ["KeyedJointDesign"],
        "_1450": ["KeyTypes"],
        "_1451": ["KeywayJointHalfDesign"],
        "_1452": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)
