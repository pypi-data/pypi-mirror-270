"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1142 import AGMA2000A88AccuracyGrader
    from ._1143 import AGMA20151A01AccuracyGrader
    from ._1144 import AGMA20151AccuracyGrades
    from ._1145 import AGMAISO13281B14AccuracyGrader
    from ._1146 import CylindricalAccuracyGrader
    from ._1147 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1148 import CylindricalAccuracyGrades
    from ._1149 import CylindricalGearAccuracyTolerances
    from ._1150 import DIN3967SystemOfGearFits
    from ._1151 import ISO132811995AccuracyGrader
    from ._1152 import ISO132812013AccuracyGrader
    from ._1153 import ISO1328AccuracyGraderCommon
    from ._1154 import ISO1328AccuracyGrades
    from ._1155 import OverridableTolerance
else:
    import_structure = {
        "_1142": ["AGMA2000A88AccuracyGrader"],
        "_1143": ["AGMA20151A01AccuracyGrader"],
        "_1144": ["AGMA20151AccuracyGrades"],
        "_1145": ["AGMAISO13281B14AccuracyGrader"],
        "_1146": ["CylindricalAccuracyGrader"],
        "_1147": ["CylindricalAccuracyGraderWithProfileFormAndSlope"],
        "_1148": ["CylindricalAccuracyGrades"],
        "_1149": ["CylindricalGearAccuracyTolerances"],
        "_1150": ["DIN3967SystemOfGearFits"],
        "_1151": ["ISO132811995AccuracyGrader"],
        "_1152": ["ISO132812013AccuracyGrader"],
        "_1153": ["ISO1328AccuracyGraderCommon"],
        "_1154": ["ISO1328AccuracyGrades"],
        "_1155": ["OverridableTolerance"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2000A88AccuracyGrader",
    "AGMA20151A01AccuracyGrader",
    "AGMA20151AccuracyGrades",
    "AGMAISO13281B14AccuracyGrader",
    "CylindricalAccuracyGrader",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
    "CylindricalAccuracyGrades",
    "CylindricalGearAccuracyTolerances",
    "DIN3967SystemOfGearFits",
    "ISO132811995AccuracyGrader",
    "ISO132812013AccuracyGrader",
    "ISO1328AccuracyGraderCommon",
    "ISO1328AccuracyGrades",
    "OverridableTolerance",
)
