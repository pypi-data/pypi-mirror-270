"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1501 import Range
    from ._1502 import AcousticWeighting
    from ._1503 import AlignmentAxis
    from ._1504 import Axis
    from ._1505 import CirclesOnAxis
    from ._1506 import ComplexMatrix
    from ._1507 import ComplexPartDisplayOption
    from ._1508 import ComplexVector
    from ._1509 import ComplexVector3D
    from ._1510 import ComplexVector6D
    from ._1511 import CoordinateSystem3D
    from ._1512 import CoordinateSystemEditor
    from ._1513 import CoordinateSystemForRotation
    from ._1514 import CoordinateSystemForRotationOrigin
    from ._1515 import DataPrecision
    from ._1516 import DegreeOfFreedom
    from ._1517 import DynamicsResponseScalarResult
    from ._1518 import DynamicsResponseScaling
    from ._1519 import Eigenmode
    from ._1520 import Eigenmodes
    from ._1521 import EulerParameters
    from ._1522 import ExtrapolationOptions
    from ._1523 import FacetedBody
    from ._1524 import FacetedSurface
    from ._1525 import FourierSeries
    from ._1526 import GenericMatrix
    from ._1527 import GriddedSurface
    from ._1528 import HarmonicValue
    from ._1529 import InertiaTensor
    from ._1530 import MassProperties
    from ._1531 import MaxMinMean
    from ._1532 import ComplexMagnitudeMethod
    from ._1533 import MultipleFourierSeriesInterpolator
    from ._1534 import Named2DLocation
    from ._1535 import PIDControlUpdateMethod
    from ._1536 import Quaternion
    from ._1537 import RealMatrix
    from ._1538 import RealVector
    from ._1539 import ResultOptionsFor3DVector
    from ._1540 import RotationAxis
    from ._1541 import RoundedOrder
    from ._1542 import SinCurve
    from ._1543 import SquareMatrix
    from ._1544 import StressPoint
    from ._1545 import TransformMatrix3D
    from ._1546 import TranslationRotation
    from ._1547 import Vector2DListAccessor
    from ._1548 import Vector6D
else:
    import_structure = {
        "_1501": ["Range"],
        "_1502": ["AcousticWeighting"],
        "_1503": ["AlignmentAxis"],
        "_1504": ["Axis"],
        "_1505": ["CirclesOnAxis"],
        "_1506": ["ComplexMatrix"],
        "_1507": ["ComplexPartDisplayOption"],
        "_1508": ["ComplexVector"],
        "_1509": ["ComplexVector3D"],
        "_1510": ["ComplexVector6D"],
        "_1511": ["CoordinateSystem3D"],
        "_1512": ["CoordinateSystemEditor"],
        "_1513": ["CoordinateSystemForRotation"],
        "_1514": ["CoordinateSystemForRotationOrigin"],
        "_1515": ["DataPrecision"],
        "_1516": ["DegreeOfFreedom"],
        "_1517": ["DynamicsResponseScalarResult"],
        "_1518": ["DynamicsResponseScaling"],
        "_1519": ["Eigenmode"],
        "_1520": ["Eigenmodes"],
        "_1521": ["EulerParameters"],
        "_1522": ["ExtrapolationOptions"],
        "_1523": ["FacetedBody"],
        "_1524": ["FacetedSurface"],
        "_1525": ["FourierSeries"],
        "_1526": ["GenericMatrix"],
        "_1527": ["GriddedSurface"],
        "_1528": ["HarmonicValue"],
        "_1529": ["InertiaTensor"],
        "_1530": ["MassProperties"],
        "_1531": ["MaxMinMean"],
        "_1532": ["ComplexMagnitudeMethod"],
        "_1533": ["MultipleFourierSeriesInterpolator"],
        "_1534": ["Named2DLocation"],
        "_1535": ["PIDControlUpdateMethod"],
        "_1536": ["Quaternion"],
        "_1537": ["RealMatrix"],
        "_1538": ["RealVector"],
        "_1539": ["ResultOptionsFor3DVector"],
        "_1540": ["RotationAxis"],
        "_1541": ["RoundedOrder"],
        "_1542": ["SinCurve"],
        "_1543": ["SquareMatrix"],
        "_1544": ["StressPoint"],
        "_1545": ["TransformMatrix3D"],
        "_1546": ["TranslationRotation"],
        "_1547": ["Vector2DListAccessor"],
        "_1548": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
