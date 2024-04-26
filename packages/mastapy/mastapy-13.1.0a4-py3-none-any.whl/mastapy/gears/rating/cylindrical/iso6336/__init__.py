"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._515 import CylindricalGearToothFatigueFractureResults
    from ._516 import CylindricalGearToothFatigueFractureResultsN1457
    from ._517 import HelicalGearMicroGeometryOption
    from ._518 import ISO63361996GearSingleFlankRating
    from ._519 import ISO63361996MeshSingleFlankRating
    from ._520 import ISO63362006GearSingleFlankRating
    from ._521 import ISO63362006MeshSingleFlankRating
    from ._522 import ISO63362019GearSingleFlankRating
    from ._523 import ISO63362019MeshSingleFlankRating
    from ._524 import ISO6336AbstractGearSingleFlankRating
    from ._525 import ISO6336AbstractMeshSingleFlankRating
    from ._526 import ISO6336AbstractMetalGearSingleFlankRating
    from ._527 import ISO6336AbstractMetalMeshSingleFlankRating
    from ._528 import ISO6336MeanStressInfluenceFactor
    from ._529 import ISO6336MetalRateableMesh
    from ._530 import ISO6336RateableMesh
    from ._531 import ToothFlankFractureAnalysisContactPoint
    from ._532 import ToothFlankFractureAnalysisContactPointCommon
    from ._533 import ToothFlankFractureAnalysisContactPointMethodA
    from ._534 import ToothFlankFractureAnalysisContactPointN1457
    from ._535 import ToothFlankFractureAnalysisPoint
    from ._536 import ToothFlankFractureAnalysisPointN1457
    from ._537 import ToothFlankFractureAnalysisRowN1457
    from ._538 import ToothFlankFractureStressStepAtAnalysisPointN1457
else:
    import_structure = {
        "_515": ["CylindricalGearToothFatigueFractureResults"],
        "_516": ["CylindricalGearToothFatigueFractureResultsN1457"],
        "_517": ["HelicalGearMicroGeometryOption"],
        "_518": ["ISO63361996GearSingleFlankRating"],
        "_519": ["ISO63361996MeshSingleFlankRating"],
        "_520": ["ISO63362006GearSingleFlankRating"],
        "_521": ["ISO63362006MeshSingleFlankRating"],
        "_522": ["ISO63362019GearSingleFlankRating"],
        "_523": ["ISO63362019MeshSingleFlankRating"],
        "_524": ["ISO6336AbstractGearSingleFlankRating"],
        "_525": ["ISO6336AbstractMeshSingleFlankRating"],
        "_526": ["ISO6336AbstractMetalGearSingleFlankRating"],
        "_527": ["ISO6336AbstractMetalMeshSingleFlankRating"],
        "_528": ["ISO6336MeanStressInfluenceFactor"],
        "_529": ["ISO6336MetalRateableMesh"],
        "_530": ["ISO6336RateableMesh"],
        "_531": ["ToothFlankFractureAnalysisContactPoint"],
        "_532": ["ToothFlankFractureAnalysisContactPointCommon"],
        "_533": ["ToothFlankFractureAnalysisContactPointMethodA"],
        "_534": ["ToothFlankFractureAnalysisContactPointN1457"],
        "_535": ["ToothFlankFractureAnalysisPoint"],
        "_536": ["ToothFlankFractureAnalysisPointN1457"],
        "_537": ["ToothFlankFractureAnalysisRowN1457"],
        "_538": ["ToothFlankFractureStressStepAtAnalysisPointN1457"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearToothFatigueFractureResults",
    "CylindricalGearToothFatigueFractureResultsN1457",
    "HelicalGearMicroGeometryOption",
    "ISO63361996GearSingleFlankRating",
    "ISO63361996MeshSingleFlankRating",
    "ISO63362006GearSingleFlankRating",
    "ISO63362006MeshSingleFlankRating",
    "ISO63362019GearSingleFlankRating",
    "ISO63362019MeshSingleFlankRating",
    "ISO6336AbstractGearSingleFlankRating",
    "ISO6336AbstractMeshSingleFlankRating",
    "ISO6336AbstractMetalGearSingleFlankRating",
    "ISO6336AbstractMetalMeshSingleFlankRating",
    "ISO6336MeanStressInfluenceFactor",
    "ISO6336MetalRateableMesh",
    "ISO6336RateableMesh",
    "ToothFlankFractureAnalysisContactPoint",
    "ToothFlankFractureAnalysisContactPointCommon",
    "ToothFlankFractureAnalysisContactPointMethodA",
    "ToothFlankFractureAnalysisContactPointN1457",
    "ToothFlankFractureAnalysisPoint",
    "ToothFlankFractureAnalysisPointN1457",
    "ToothFlankFractureAnalysisRowN1457",
    "ToothFlankFractureStressStepAtAnalysisPointN1457",
)
