"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._541 import AGMA2101GearSingleFlankRating
    from ._542 import AGMA2101MeshSingleFlankRating
    from ._543 import AGMA2101RateableMesh
    from ._544 import ThermalReductionFactorFactorsAndExponents
else:
    import_structure = {
        "_541": ["AGMA2101GearSingleFlankRating"],
        "_542": ["AGMA2101MeshSingleFlankRating"],
        "_543": ["AGMA2101RateableMesh"],
        "_544": ["ThermalReductionFactorFactorsAndExponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2101GearSingleFlankRating",
    "AGMA2101MeshSingleFlankRating",
    "AGMA2101RateableMesh",
    "ThermalReductionFactorFactorsAndExponents",
)
