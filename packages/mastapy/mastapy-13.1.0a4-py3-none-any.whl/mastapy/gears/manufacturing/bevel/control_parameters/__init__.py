"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._824 import ConicalGearManufacturingControlParameters
    from ._825 import ConicalManufacturingSGMControlParameters
    from ._826 import ConicalManufacturingSGTControlParameters
    from ._827 import ConicalManufacturingSMTControlParameters
else:
    import_structure = {
        "_824": ["ConicalGearManufacturingControlParameters"],
        "_825": ["ConicalManufacturingSGMControlParameters"],
        "_826": ["ConicalManufacturingSGTControlParameters"],
        "_827": ["ConicalManufacturingSMTControlParameters"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearManufacturingControlParameters",
    "ConicalManufacturingSGMControlParameters",
    "ConicalManufacturingSGTControlParameters",
    "ConicalManufacturingSMTControlParameters",
)
