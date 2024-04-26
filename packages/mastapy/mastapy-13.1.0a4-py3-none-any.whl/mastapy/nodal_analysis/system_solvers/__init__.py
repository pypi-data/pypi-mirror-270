"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._103 import BackwardEulerTransientSolver
    from ._104 import DenseStiffnessSolver
    from ._105 import DirkTransientSolver
    from ._106 import DynamicSolver
    from ._107 import InternalTransientSolver
    from ._108 import LobattoIIICTransientSolver
    from ._109 import NewmarkTransientSolver
    from ._110 import NewtonRaphsonAnalysis
    from ._111 import NewtonRaphsonDegreeOfFreedomError
    from ._112 import SimpleVelocityBasedStepHalvingTransientSolver
    from ._113 import SingularDegreeOfFreedomAnalysis
    from ._114 import SingularValuesAnalysis
    from ._115 import SingularVectorAnalysis
    from ._116 import Solver
    from ._117 import StepHalvingTransientSolver
    from ._118 import StiffnessSolver
    from ._119 import TransientSolver
    from ._120 import WilsonThetaTransientSolver
else:
    import_structure = {
        "_103": ["BackwardEulerTransientSolver"],
        "_104": ["DenseStiffnessSolver"],
        "_105": ["DirkTransientSolver"],
        "_106": ["DynamicSolver"],
        "_107": ["InternalTransientSolver"],
        "_108": ["LobattoIIICTransientSolver"],
        "_109": ["NewmarkTransientSolver"],
        "_110": ["NewtonRaphsonAnalysis"],
        "_111": ["NewtonRaphsonDegreeOfFreedomError"],
        "_112": ["SimpleVelocityBasedStepHalvingTransientSolver"],
        "_113": ["SingularDegreeOfFreedomAnalysis"],
        "_114": ["SingularValuesAnalysis"],
        "_115": ["SingularVectorAnalysis"],
        "_116": ["Solver"],
        "_117": ["StepHalvingTransientSolver"],
        "_118": ["StiffnessSolver"],
        "_119": ["TransientSolver"],
        "_120": ["WilsonThetaTransientSolver"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BackwardEulerTransientSolver",
    "DenseStiffnessSolver",
    "DirkTransientSolver",
    "DynamicSolver",
    "InternalTransientSolver",
    "LobattoIIICTransientSolver",
    "NewmarkTransientSolver",
    "NewtonRaphsonAnalysis",
    "NewtonRaphsonDegreeOfFreedomError",
    "SimpleVelocityBasedStepHalvingTransientSolver",
    "SingularDegreeOfFreedomAnalysis",
    "SingularValuesAnalysis",
    "SingularVectorAnalysis",
    "Solver",
    "StepHalvingTransientSolver",
    "StiffnessSolver",
    "TransientSolver",
    "WilsonThetaTransientSolver",
)
