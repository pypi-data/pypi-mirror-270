"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._508 import CylindricalGearSetRatingOptimisationHelper
    from ._509 import OptimisationResultsPair
    from ._510 import SafetyFactorOptimisationResults
    from ._511 import SafetyFactorOptimisationStepResult
    from ._512 import SafetyFactorOptimisationStepResultAngle
    from ._513 import SafetyFactorOptimisationStepResultNumber
    from ._514 import SafetyFactorOptimisationStepResultShortLength
else:
    import_structure = {
        "_508": ["CylindricalGearSetRatingOptimisationHelper"],
        "_509": ["OptimisationResultsPair"],
        "_510": ["SafetyFactorOptimisationResults"],
        "_511": ["SafetyFactorOptimisationStepResult"],
        "_512": ["SafetyFactorOptimisationStepResultAngle"],
        "_513": ["SafetyFactorOptimisationStepResultNumber"],
        "_514": ["SafetyFactorOptimisationStepResultShortLength"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearSetRatingOptimisationHelper",
    "OptimisationResultsPair",
    "SafetyFactorOptimisationResults",
    "SafetyFactorOptimisationStepResult",
    "SafetyFactorOptimisationStepResultAngle",
    "SafetyFactorOptimisationStepResultNumber",
    "SafetyFactorOptimisationStepResultShortLength",
)
