"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1103 import CylindricalGearBiasModification
    from ._1104 import CylindricalGearCommonFlankMicroGeometry
    from ._1105 import CylindricalGearFlankMicroGeometry
    from ._1106 import CylindricalGearLeadModification
    from ._1107 import CylindricalGearLeadModificationAtProfilePosition
    from ._1108 import CylindricalGearMeshMicroGeometry
    from ._1109 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1110 import CylindricalGearMicroGeometry
    from ._1111 import CylindricalGearMicroGeometryBase
    from ._1112 import CylindricalGearMicroGeometryDutyCycle
    from ._1113 import CylindricalGearMicroGeometryMap
    from ._1114 import CylindricalGearMicroGeometryPerTooth
    from ._1115 import CylindricalGearProfileModification
    from ._1116 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1117 import CylindricalGearSetMicroGeometry
    from ._1118 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1119 import CylindricalGearToothMicroGeometry
    from ._1120 import CylindricalGearTriangularEndModification
    from ._1121 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1122 import DrawDefiningGearOrBoth
    from ._1123 import GearAlignment
    from ._1124 import LeadFormReliefWithDeviation
    from ._1125 import LeadReliefWithDeviation
    from ._1126 import LeadSlopeReliefWithDeviation
    from ._1127 import LinearCylindricalGearTriangularEndModification
    from ._1128 import MeasuredMapDataTypes
    from ._1129 import MeshAlignment
    from ._1130 import MeshedCylindricalGearFlankMicroGeometry
    from ._1131 import MeshedCylindricalGearMicroGeometry
    from ._1132 import MicroGeometryLeadToleranceChartView
    from ._1133 import MicroGeometryViewingOptions
    from ._1134 import ParabolicCylindricalGearTriangularEndModification
    from ._1135 import ProfileFormReliefWithDeviation
    from ._1136 import ProfileReliefWithDeviation
    from ._1137 import ProfileSlopeReliefWithDeviation
    from ._1138 import ReliefWithDeviation
    from ._1139 import SingleCylindricalGearTriangularEndModification
    from ._1140 import TotalLeadReliefWithDeviation
    from ._1141 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        "_1103": ["CylindricalGearBiasModification"],
        "_1104": ["CylindricalGearCommonFlankMicroGeometry"],
        "_1105": ["CylindricalGearFlankMicroGeometry"],
        "_1106": ["CylindricalGearLeadModification"],
        "_1107": ["CylindricalGearLeadModificationAtProfilePosition"],
        "_1108": ["CylindricalGearMeshMicroGeometry"],
        "_1109": ["CylindricalGearMeshMicroGeometryDutyCycle"],
        "_1110": ["CylindricalGearMicroGeometry"],
        "_1111": ["CylindricalGearMicroGeometryBase"],
        "_1112": ["CylindricalGearMicroGeometryDutyCycle"],
        "_1113": ["CylindricalGearMicroGeometryMap"],
        "_1114": ["CylindricalGearMicroGeometryPerTooth"],
        "_1115": ["CylindricalGearProfileModification"],
        "_1116": ["CylindricalGearProfileModificationAtFaceWidthPosition"],
        "_1117": ["CylindricalGearSetMicroGeometry"],
        "_1118": ["CylindricalGearSetMicroGeometryDutyCycle"],
        "_1119": ["CylindricalGearToothMicroGeometry"],
        "_1120": ["CylindricalGearTriangularEndModification"],
        "_1121": ["CylindricalGearTriangularEndModificationAtOrientation"],
        "_1122": ["DrawDefiningGearOrBoth"],
        "_1123": ["GearAlignment"],
        "_1124": ["LeadFormReliefWithDeviation"],
        "_1125": ["LeadReliefWithDeviation"],
        "_1126": ["LeadSlopeReliefWithDeviation"],
        "_1127": ["LinearCylindricalGearTriangularEndModification"],
        "_1128": ["MeasuredMapDataTypes"],
        "_1129": ["MeshAlignment"],
        "_1130": ["MeshedCylindricalGearFlankMicroGeometry"],
        "_1131": ["MeshedCylindricalGearMicroGeometry"],
        "_1132": ["MicroGeometryLeadToleranceChartView"],
        "_1133": ["MicroGeometryViewingOptions"],
        "_1134": ["ParabolicCylindricalGearTriangularEndModification"],
        "_1135": ["ProfileFormReliefWithDeviation"],
        "_1136": ["ProfileReliefWithDeviation"],
        "_1137": ["ProfileSlopeReliefWithDeviation"],
        "_1138": ["ReliefWithDeviation"],
        "_1139": ["SingleCylindricalGearTriangularEndModification"],
        "_1140": ["TotalLeadReliefWithDeviation"],
        "_1141": ["TotalProfileReliefWithDeviation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)
