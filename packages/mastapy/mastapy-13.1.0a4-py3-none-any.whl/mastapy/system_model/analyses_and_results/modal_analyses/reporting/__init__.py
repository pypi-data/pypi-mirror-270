"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4739 import CalculateFullFEResultsForMode
    from ._4740 import CampbellDiagramReport
    from ._4741 import ComponentPerModeResult
    from ._4742 import DesignEntityModalAnalysisGroupResults
    from ._4743 import ModalCMSResultsForModeAndFE
    from ._4744 import PerModeResultsReport
    from ._4745 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4746 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4747 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4748 import ShaftPerModeResult
    from ._4749 import SingleExcitationResultsModalAnalysis
    from ._4750 import SingleModeResults
else:
    import_structure = {
        "_4739": ["CalculateFullFEResultsForMode"],
        "_4740": ["CampbellDiagramReport"],
        "_4741": ["ComponentPerModeResult"],
        "_4742": ["DesignEntityModalAnalysisGroupResults"],
        "_4743": ["ModalCMSResultsForModeAndFE"],
        "_4744": ["PerModeResultsReport"],
        "_4745": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4746": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4747": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4748": ["ShaftPerModeResult"],
        "_4749": ["SingleExcitationResultsModalAnalysis"],
        "_4750": ["SingleModeResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculateFullFEResultsForMode",
    "CampbellDiagramReport",
    "ComponentPerModeResult",
    "DesignEntityModalAnalysisGroupResults",
    "ModalCMSResultsForModeAndFE",
    "PerModeResultsReport",
    "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    "RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
    "ShaftPerModeResult",
    "SingleExcitationResultsModalAnalysis",
    "SingleModeResults",
)
