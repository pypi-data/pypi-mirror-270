"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._175 import ContactType
    from ._176 import ElectricMachineAnalysisPeriod
    from ._177 import ElmerResults
    from ._178 import ElmerResultsFromElectromagneticAnalysis
    from ._179 import ElmerResultsViewable
    from ._180 import ElmerResultType
    from ._181 import MechanicalContactSpecification
else:
    import_structure = {
        "_175": ["ContactType"],
        "_176": ["ElectricMachineAnalysisPeriod"],
        "_177": ["ElmerResults"],
        "_178": ["ElmerResultsFromElectromagneticAnalysis"],
        "_179": ["ElmerResultsViewable"],
        "_180": ["ElmerResultType"],
        "_181": ["MechanicalContactSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactType",
    "ElectricMachineAnalysisPeriod",
    "ElmerResults",
    "ElmerResultsFromElectromagneticAnalysis",
    "ElmerResultsViewable",
    "ElmerResultType",
    "MechanicalContactSpecification",
)
