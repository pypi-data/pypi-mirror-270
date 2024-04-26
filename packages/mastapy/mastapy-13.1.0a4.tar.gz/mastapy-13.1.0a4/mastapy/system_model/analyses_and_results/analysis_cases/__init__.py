"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7561 import AnalysisCase
    from ._7562 import AbstractAnalysisOptions
    from ._7563 import CompoundAnalysisCase
    from ._7564 import ConnectionAnalysisCase
    from ._7565 import ConnectionCompoundAnalysis
    from ._7566 import ConnectionFEAnalysis
    from ._7567 import ConnectionStaticLoadAnalysisCase
    from ._7568 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7569 import DesignEntityCompoundAnalysis
    from ._7570 import FEAnalysis
    from ._7571 import PartAnalysisCase
    from ._7572 import PartCompoundAnalysis
    from ._7573 import PartFEAnalysis
    from ._7574 import PartStaticLoadAnalysisCase
    from ._7575 import PartTimeSeriesLoadAnalysisCase
    from ._7576 import StaticLoadAnalysisCase
    from ._7577 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7561": ["AnalysisCase"],
        "_7562": ["AbstractAnalysisOptions"],
        "_7563": ["CompoundAnalysisCase"],
        "_7564": ["ConnectionAnalysisCase"],
        "_7565": ["ConnectionCompoundAnalysis"],
        "_7566": ["ConnectionFEAnalysis"],
        "_7567": ["ConnectionStaticLoadAnalysisCase"],
        "_7568": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7569": ["DesignEntityCompoundAnalysis"],
        "_7570": ["FEAnalysis"],
        "_7571": ["PartAnalysisCase"],
        "_7572": ["PartCompoundAnalysis"],
        "_7573": ["PartFEAnalysis"],
        "_7574": ["PartStaticLoadAnalysisCase"],
        "_7575": ["PartTimeSeriesLoadAnalysisCase"],
        "_7576": ["StaticLoadAnalysisCase"],
        "_7577": ["TimeSeriesLoadAnalysisCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)
