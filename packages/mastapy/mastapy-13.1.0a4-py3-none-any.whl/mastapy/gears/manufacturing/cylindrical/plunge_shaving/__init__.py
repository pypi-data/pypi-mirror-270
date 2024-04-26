"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._649 import CalculationError
    from ._650 import ChartType
    from ._651 import GearPointCalculationError
    from ._652 import MicroGeometryDefinitionMethod
    from ._653 import MicroGeometryDefinitionType
    from ._654 import PlungeShaverCalculation
    from ._655 import PlungeShaverCalculationInputs
    from ._656 import PlungeShaverGeneration
    from ._657 import PlungeShaverInputsAndMicroGeometry
    from ._658 import PlungeShaverOutputs
    from ._659 import PlungeShaverSettings
    from ._660 import PointOfInterest
    from ._661 import RealPlungeShaverOutputs
    from ._662 import ShaverPointCalculationError
    from ._663 import ShaverPointOfInterest
    from ._664 import VirtualPlungeShaverOutputs
else:
    import_structure = {
        "_649": ["CalculationError"],
        "_650": ["ChartType"],
        "_651": ["GearPointCalculationError"],
        "_652": ["MicroGeometryDefinitionMethod"],
        "_653": ["MicroGeometryDefinitionType"],
        "_654": ["PlungeShaverCalculation"],
        "_655": ["PlungeShaverCalculationInputs"],
        "_656": ["PlungeShaverGeneration"],
        "_657": ["PlungeShaverInputsAndMicroGeometry"],
        "_658": ["PlungeShaverOutputs"],
        "_659": ["PlungeShaverSettings"],
        "_660": ["PointOfInterest"],
        "_661": ["RealPlungeShaverOutputs"],
        "_662": ["ShaverPointCalculationError"],
        "_663": ["ShaverPointOfInterest"],
        "_664": ["VirtualPlungeShaverOutputs"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculationError",
    "ChartType",
    "GearPointCalculationError",
    "MicroGeometryDefinitionMethod",
    "MicroGeometryDefinitionType",
    "PlungeShaverCalculation",
    "PlungeShaverCalculationInputs",
    "PlungeShaverGeneration",
    "PlungeShaverInputsAndMicroGeometry",
    "PlungeShaverOutputs",
    "PlungeShaverSettings",
    "PointOfInterest",
    "RealPlungeShaverOutputs",
    "ShaverPointCalculationError",
    "ShaverPointOfInterest",
    "VirtualPlungeShaverOutputs",
)
