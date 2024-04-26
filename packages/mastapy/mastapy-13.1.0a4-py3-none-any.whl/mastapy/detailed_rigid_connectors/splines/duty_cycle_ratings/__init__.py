"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1445 import AGMA6123SplineJointDutyCycleRating
    from ._1446 import GBT17855SplineJointDutyCycleRating
    from ._1447 import SAESplineJointDutyCycleRating
else:
    import_structure = {
        "_1445": ["AGMA6123SplineJointDutyCycleRating"],
        "_1446": ["GBT17855SplineJointDutyCycleRating"],
        "_1447": ["SAESplineJointDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineJointDutyCycleRating",
    "GBT17855SplineJointDutyCycleRating",
    "SAESplineJointDutyCycleRating",
)
