"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1834 import BearingForceArrowOption
    from ._1835 import TableAndChartOptions
    from ._1836 import ThreeDViewContourOption
    from ._1837 import ThreeDViewContourOptionFirstSelection
    from ._1838 import ThreeDViewContourOptionSecondSelection
else:
    import_structure = {
        "_1834": ["BearingForceArrowOption"],
        "_1835": ["TableAndChartOptions"],
        "_1836": ["ThreeDViewContourOption"],
        "_1837": ["ThreeDViewContourOptionFirstSelection"],
        "_1838": ["ThreeDViewContourOptionSecondSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
