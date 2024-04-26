"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1551 import AbstractOptimisable
    from ._1552 import DesignSpaceSearchStrategyDatabase
    from ._1553 import InputSetter
    from ._1554 import Optimisable
    from ._1555 import OptimisationHistory
    from ._1556 import OptimizationInput
    from ._1557 import OptimizationVariable
    from ._1558 import ParetoOptimisationFilter
    from ._1559 import ParetoOptimisationInput
    from ._1560 import ParetoOptimisationOutput
    from ._1561 import ParetoOptimisationStrategy
    from ._1562 import ParetoOptimisationStrategyBars
    from ._1563 import ParetoOptimisationStrategyChartInformation
    from ._1564 import ParetoOptimisationStrategyDatabase
    from ._1565 import ParetoOptimisationVariable
    from ._1566 import ParetoOptimisationVariableBase
    from ._1567 import PropertyTargetForDominantCandidateSearch
    from ._1568 import ReportingOptimizationInput
    from ._1569 import SpecifyOptimisationInputAs
    from ._1570 import TargetingPropertyTo
else:
    import_structure = {
        "_1551": ["AbstractOptimisable"],
        "_1552": ["DesignSpaceSearchStrategyDatabase"],
        "_1553": ["InputSetter"],
        "_1554": ["Optimisable"],
        "_1555": ["OptimisationHistory"],
        "_1556": ["OptimizationInput"],
        "_1557": ["OptimizationVariable"],
        "_1558": ["ParetoOptimisationFilter"],
        "_1559": ["ParetoOptimisationInput"],
        "_1560": ["ParetoOptimisationOutput"],
        "_1561": ["ParetoOptimisationStrategy"],
        "_1562": ["ParetoOptimisationStrategyBars"],
        "_1563": ["ParetoOptimisationStrategyChartInformation"],
        "_1564": ["ParetoOptimisationStrategyDatabase"],
        "_1565": ["ParetoOptimisationVariable"],
        "_1566": ["ParetoOptimisationVariableBase"],
        "_1567": ["PropertyTargetForDominantCandidateSearch"],
        "_1568": ["ReportingOptimizationInput"],
        "_1569": ["SpecifyOptimisationInputAs"],
        "_1570": ["TargetingPropertyTo"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)
