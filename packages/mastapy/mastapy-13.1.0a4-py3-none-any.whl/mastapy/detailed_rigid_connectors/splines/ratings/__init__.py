"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1435 import AGMA6123SplineHalfRating
    from ._1436 import AGMA6123SplineJointRating
    from ._1437 import DIN5466SplineHalfRating
    from ._1438 import DIN5466SplineRating
    from ._1439 import GBT17855SplineHalfRating
    from ._1440 import GBT17855SplineJointRating
    from ._1441 import SAESplineHalfRating
    from ._1442 import SAESplineJointRating
    from ._1443 import SplineHalfRating
    from ._1444 import SplineJointRating
else:
    import_structure = {
        "_1435": ["AGMA6123SplineHalfRating"],
        "_1436": ["AGMA6123SplineJointRating"],
        "_1437": ["DIN5466SplineHalfRating"],
        "_1438": ["DIN5466SplineRating"],
        "_1439": ["GBT17855SplineHalfRating"],
        "_1440": ["GBT17855SplineJointRating"],
        "_1441": ["SAESplineHalfRating"],
        "_1442": ["SAESplineJointRating"],
        "_1443": ["SplineHalfRating"],
        "_1444": ["SplineJointRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineHalfRating",
    "AGMA6123SplineJointRating",
    "DIN5466SplineHalfRating",
    "DIN5466SplineRating",
    "GBT17855SplineHalfRating",
    "GBT17855SplineJointRating",
    "SAESplineHalfRating",
    "SAESplineJointRating",
    "SplineHalfRating",
    "SplineJointRating",
)
