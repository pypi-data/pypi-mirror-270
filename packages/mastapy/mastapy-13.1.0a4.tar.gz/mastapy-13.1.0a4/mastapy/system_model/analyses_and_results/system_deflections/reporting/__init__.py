"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2865 import CylindricalGearMeshMisalignmentValue
    from ._2866 import FlexibleGearChart
    from ._2867 import GearInMeshDeflectionResults
    from ._2868 import MeshDeflectionResults
    from ._2869 import PlanetCarrierWindup
    from ._2870 import PlanetPinWindup
    from ._2871 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2872 import ShaftSystemDeflectionSectionsReport
    from ._2873 import SplineFlankContactReporting
else:
    import_structure = {
        "_2865": ["CylindricalGearMeshMisalignmentValue"],
        "_2866": ["FlexibleGearChart"],
        "_2867": ["GearInMeshDeflectionResults"],
        "_2868": ["MeshDeflectionResults"],
        "_2869": ["PlanetCarrierWindup"],
        "_2870": ["PlanetPinWindup"],
        "_2871": ["RigidlyConnectedComponentGroupSystemDeflection"],
        "_2872": ["ShaftSystemDeflectionSectionsReport"],
        "_2873": ["SplineFlankContactReporting"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshMisalignmentValue",
    "FlexibleGearChart",
    "GearInMeshDeflectionResults",
    "MeshDeflectionResults",
    "PlanetCarrierWindup",
    "PlanetPinWindup",
    "RigidlyConnectedComponentGroupSystemDeflection",
    "ShaftSystemDeflectionSectionsReport",
    "SplineFlankContactReporting",
)
