"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1864 import ColumnInputOptions
    from ._1865 import DataInputFileOptions
    from ._1866 import DataLoggerItem
    from ._1867 import DataLoggerWithCharts
    from ._1868 import ScalingDrawStyle
else:
    import_structure = {
        "_1864": ["ColumnInputOptions"],
        "_1865": ["DataInputFileOptions"],
        "_1866": ["DataLoggerItem"],
        "_1867": ["DataLoggerWithCharts"],
        "_1868": ["ScalingDrawStyle"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnInputOptions",
    "DataInputFileOptions",
    "DataLoggerItem",
    "DataLoggerWithCharts",
    "ScalingDrawStyle",
)
