"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1401 import CustomSplineHalfDesign
    from ._1402 import CustomSplineJointDesign
    from ._1403 import DetailedSplineJointSettings
    from ._1404 import DIN5480SplineHalfDesign
    from ._1405 import DIN5480SplineJointDesign
    from ._1406 import DudleyEffectiveLengthApproximationOption
    from ._1407 import FitTypes
    from ._1408 import GBT3478SplineHalfDesign
    from ._1409 import GBT3478SplineJointDesign
    from ._1410 import HeatTreatmentTypes
    from ._1411 import ISO4156SplineHalfDesign
    from ._1412 import ISO4156SplineJointDesign
    from ._1413 import JISB1603SplineJointDesign
    from ._1414 import ManufacturingTypes
    from ._1415 import Modules
    from ._1416 import PressureAngleTypes
    from ._1417 import RootTypes
    from ._1418 import SAEFatigueLifeFactorTypes
    from ._1419 import SAESplineHalfDesign
    from ._1420 import SAESplineJointDesign
    from ._1421 import SAETorqueCycles
    from ._1422 import SplineDesignTypes
    from ._1423 import FinishingMethods
    from ._1424 import SplineFitClassType
    from ._1425 import SplineFixtureTypes
    from ._1426 import SplineHalfDesign
    from ._1427 import SplineJointDesign
    from ._1428 import SplineMaterial
    from ._1429 import SplineRatingTypes
    from ._1430 import SplineToleranceClassTypes
    from ._1431 import StandardSplineHalfDesign
    from ._1432 import StandardSplineJointDesign
else:
    import_structure = {
        "_1401": ["CustomSplineHalfDesign"],
        "_1402": ["CustomSplineJointDesign"],
        "_1403": ["DetailedSplineJointSettings"],
        "_1404": ["DIN5480SplineHalfDesign"],
        "_1405": ["DIN5480SplineJointDesign"],
        "_1406": ["DudleyEffectiveLengthApproximationOption"],
        "_1407": ["FitTypes"],
        "_1408": ["GBT3478SplineHalfDesign"],
        "_1409": ["GBT3478SplineJointDesign"],
        "_1410": ["HeatTreatmentTypes"],
        "_1411": ["ISO4156SplineHalfDesign"],
        "_1412": ["ISO4156SplineJointDesign"],
        "_1413": ["JISB1603SplineJointDesign"],
        "_1414": ["ManufacturingTypes"],
        "_1415": ["Modules"],
        "_1416": ["PressureAngleTypes"],
        "_1417": ["RootTypes"],
        "_1418": ["SAEFatigueLifeFactorTypes"],
        "_1419": ["SAESplineHalfDesign"],
        "_1420": ["SAESplineJointDesign"],
        "_1421": ["SAETorqueCycles"],
        "_1422": ["SplineDesignTypes"],
        "_1423": ["FinishingMethods"],
        "_1424": ["SplineFitClassType"],
        "_1425": ["SplineFixtureTypes"],
        "_1426": ["SplineHalfDesign"],
        "_1427": ["SplineJointDesign"],
        "_1428": ["SplineMaterial"],
        "_1429": ["SplineRatingTypes"],
        "_1430": ["SplineToleranceClassTypes"],
        "_1431": ["StandardSplineHalfDesign"],
        "_1432": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)
