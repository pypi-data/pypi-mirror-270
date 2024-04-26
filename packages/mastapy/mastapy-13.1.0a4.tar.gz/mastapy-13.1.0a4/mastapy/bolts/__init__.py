"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1477 import AxialLoadType
    from ._1478 import BoltedJointMaterial
    from ._1479 import BoltedJointMaterialDatabase
    from ._1480 import BoltGeometry
    from ._1481 import BoltGeometryDatabase
    from ._1482 import BoltMaterial
    from ._1483 import BoltMaterialDatabase
    from ._1484 import BoltSection
    from ._1485 import BoltShankType
    from ._1486 import BoltTypes
    from ._1487 import ClampedSection
    from ._1488 import ClampedSectionMaterialDatabase
    from ._1489 import DetailedBoltDesign
    from ._1490 import DetailedBoltedJointDesign
    from ._1491 import HeadCapTypes
    from ._1492 import JointGeometries
    from ._1493 import JointTypes
    from ._1494 import LoadedBolt
    from ._1495 import RolledBeforeOrAfterHeatTreatment
    from ._1496 import StandardSizes
    from ._1497 import StrengthGrades
    from ._1498 import ThreadTypes
    from ._1499 import TighteningTechniques
else:
    import_structure = {
        "_1477": ["AxialLoadType"],
        "_1478": ["BoltedJointMaterial"],
        "_1479": ["BoltedJointMaterialDatabase"],
        "_1480": ["BoltGeometry"],
        "_1481": ["BoltGeometryDatabase"],
        "_1482": ["BoltMaterial"],
        "_1483": ["BoltMaterialDatabase"],
        "_1484": ["BoltSection"],
        "_1485": ["BoltShankType"],
        "_1486": ["BoltTypes"],
        "_1487": ["ClampedSection"],
        "_1488": ["ClampedSectionMaterialDatabase"],
        "_1489": ["DetailedBoltDesign"],
        "_1490": ["DetailedBoltedJointDesign"],
        "_1491": ["HeadCapTypes"],
        "_1492": ["JointGeometries"],
        "_1493": ["JointTypes"],
        "_1494": ["LoadedBolt"],
        "_1495": ["RolledBeforeOrAfterHeatTreatment"],
        "_1496": ["StandardSizes"],
        "_1497": ["StrengthGrades"],
        "_1498": ["ThreadTypes"],
        "_1499": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
