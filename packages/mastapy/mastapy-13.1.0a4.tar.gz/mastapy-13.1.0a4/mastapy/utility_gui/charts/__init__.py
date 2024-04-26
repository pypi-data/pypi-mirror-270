"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1869 import BubbleChartDefinition
    from ._1870 import ConstantLine
    from ._1871 import CustomLineChart
    from ._1872 import CustomTableAndChart
    from ._1873 import LegacyChartMathChartDefinition
    from ._1874 import MatrixVisualisationDefinition
    from ._1875 import ModeConstantLine
    from ._1876 import NDChartDefinition
    from ._1877 import ParallelCoordinatesChartDefinition
    from ._1878 import PointsForSurface
    from ._1879 import ScatterChartDefinition
    from ._1880 import Series2D
    from ._1881 import SMTAxis
    from ._1882 import ThreeDChartDefinition
    from ._1883 import ThreeDVectorChartDefinition
    from ._1884 import TwoDChartDefinition
else:
    import_structure = {
        "_1869": ["BubbleChartDefinition"],
        "_1870": ["ConstantLine"],
        "_1871": ["CustomLineChart"],
        "_1872": ["CustomTableAndChart"],
        "_1873": ["LegacyChartMathChartDefinition"],
        "_1874": ["MatrixVisualisationDefinition"],
        "_1875": ["ModeConstantLine"],
        "_1876": ["NDChartDefinition"],
        "_1877": ["ParallelCoordinatesChartDefinition"],
        "_1878": ["PointsForSurface"],
        "_1879": ["ScatterChartDefinition"],
        "_1880": ["Series2D"],
        "_1881": ["SMTAxis"],
        "_1882": ["ThreeDChartDefinition"],
        "_1883": ["ThreeDVectorChartDefinition"],
        "_1884": ["TwoDChartDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)
