"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6294 import CombinationAnalysis
    from ._6295 import FlexiblePinAnalysis
    from ._6296 import FlexiblePinAnalysisConceptLevel
    from ._6297 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6298 import FlexiblePinAnalysisGearAndBearingRating
    from ._6299 import FlexiblePinAnalysisManufactureLevel
    from ._6300 import FlexiblePinAnalysisOptions
    from ._6301 import FlexiblePinAnalysisStopStartAnalysis
    from ._6302 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6294": ["CombinationAnalysis"],
        "_6295": ["FlexiblePinAnalysis"],
        "_6296": ["FlexiblePinAnalysisConceptLevel"],
        "_6297": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6298": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6299": ["FlexiblePinAnalysisManufactureLevel"],
        "_6300": ["FlexiblePinAnalysisOptions"],
        "_6301": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6302": ["WindTurbineCertificationReport"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CombinationAnalysis",
    "FlexiblePinAnalysis",
    "FlexiblePinAnalysisConceptLevel",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    "FlexiblePinAnalysisGearAndBearingRating",
    "FlexiblePinAnalysisManufactureLevel",
    "FlexiblePinAnalysisOptions",
    "FlexiblePinAnalysisStopStartAnalysis",
    "WindTurbineCertificationReport",
)
