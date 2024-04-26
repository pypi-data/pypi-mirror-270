"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2279 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2280 import ExcitationAnalysisViewOption
    from ._2281 import ModalContributionViewOptions
else:
    import_structure = {
        "_2279": ["AdvancedTimeSteppingAnalysisForModulationModeViewOptions"],
        "_2280": ["ExcitationAnalysisViewOption"],
        "_2281": ["ModalContributionViewOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    "ExcitationAnalysisViewOption",
    "ModalContributionViewOptions",
)
