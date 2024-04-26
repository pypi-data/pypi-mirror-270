"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._576 import BiasModification
    from ._577 import FlankMicroGeometry
    from ._578 import FlankSide
    from ._579 import LeadModification
    from ._580 import LocationOfEvaluationLowerLimit
    from ._581 import LocationOfEvaluationUpperLimit
    from ._582 import LocationOfRootReliefEvaluation
    from ._583 import LocationOfTipReliefEvaluation
    from ._584 import MainProfileReliefEndsAtTheStartOfRootReliefOption
    from ._585 import MainProfileReliefEndsAtTheStartOfTipReliefOption
    from ._586 import Modification
    from ._587 import ParabolicRootReliefStartsTangentToMainProfileRelief
    from ._588 import ParabolicTipReliefStartsTangentToMainProfileRelief
    from ._589 import ProfileModification
else:
    import_structure = {
        "_576": ["BiasModification"],
        "_577": ["FlankMicroGeometry"],
        "_578": ["FlankSide"],
        "_579": ["LeadModification"],
        "_580": ["LocationOfEvaluationLowerLimit"],
        "_581": ["LocationOfEvaluationUpperLimit"],
        "_582": ["LocationOfRootReliefEvaluation"],
        "_583": ["LocationOfTipReliefEvaluation"],
        "_584": ["MainProfileReliefEndsAtTheStartOfRootReliefOption"],
        "_585": ["MainProfileReliefEndsAtTheStartOfTipReliefOption"],
        "_586": ["Modification"],
        "_587": ["ParabolicRootReliefStartsTangentToMainProfileRelief"],
        "_588": ["ParabolicTipReliefStartsTangentToMainProfileRelief"],
        "_589": ["ProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BiasModification",
    "FlankMicroGeometry",
    "FlankSide",
    "LeadModification",
    "LocationOfEvaluationLowerLimit",
    "LocationOfEvaluationUpperLimit",
    "LocationOfRootReliefEvaluation",
    "LocationOfTipReliefEvaluation",
    "MainProfileReliefEndsAtTheStartOfRootReliefOption",
    "MainProfileReliefEndsAtTheStartOfTipReliefOption",
    "Modification",
    "ParabolicRootReliefStartsTangentToMainProfileRelief",
    "ParabolicTipReliefStartsTangentToMainProfileRelief",
    "ProfileModification",
)
