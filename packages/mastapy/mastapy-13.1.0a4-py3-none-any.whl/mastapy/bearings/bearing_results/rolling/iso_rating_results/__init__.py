"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2119 import BallISO2812007Results
    from ._2120 import BallISOTS162812008Results
    from ._2121 import ISO2812007Results
    from ._2122 import ISO762006Results
    from ._2123 import ISOResults
    from ._2124 import ISOTS162812008Results
    from ._2125 import RollerISO2812007Results
    from ._2126 import RollerISOTS162812008Results
    from ._2127 import StressConcentrationMethod
else:
    import_structure = {
        "_2119": ["BallISO2812007Results"],
        "_2120": ["BallISOTS162812008Results"],
        "_2121": ["ISO2812007Results"],
        "_2122": ["ISO762006Results"],
        "_2123": ["ISOResults"],
        "_2124": ["ISOTS162812008Results"],
        "_2125": ["RollerISO2812007Results"],
        "_2126": ["RollerISOTS162812008Results"],
        "_2127": ["StressConcentrationMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallISO2812007Results",
    "BallISOTS162812008Results",
    "ISO2812007Results",
    "ISO762006Results",
    "ISOResults",
    "ISOTS162812008Results",
    "RollerISO2812007Results",
    "RollerISOTS162812008Results",
    "StressConcentrationMethod",
)
