"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1218 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1219 import CylindricalGearLTCAContactCharts
    from ._1220 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1221 import CylindricalGearWorstLTCAContactCharts
    from ._1222 import GearLTCAContactChartDataAsTextFile
    from ._1223 import GearLTCAContactCharts
    from ._1224 import PointsWithWorstResults
else:
    import_structure = {
        "_1218": ["CylindricalGearLTCAContactChartDataAsTextFile"],
        "_1219": ["CylindricalGearLTCAContactCharts"],
        "_1220": ["CylindricalGearWorstLTCAContactChartDataAsTextFile"],
        "_1221": ["CylindricalGearWorstLTCAContactCharts"],
        "_1222": ["GearLTCAContactChartDataAsTextFile"],
        "_1223": ["GearLTCAContactCharts"],
        "_1224": ["PointsWithWorstResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)
