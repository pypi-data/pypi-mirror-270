"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._997 import FaceGearDesign
    from ._998 import FaceGearDiameterFaceWidthSpecificationMethod
    from ._999 import FaceGearMeshDesign
    from ._1000 import FaceGearMeshMicroGeometry
    from ._1001 import FaceGearMicroGeometry
    from ._1002 import FaceGearPinionDesign
    from ._1003 import FaceGearSetDesign
    from ._1004 import FaceGearSetMicroGeometry
    from ._1005 import FaceGearWheelDesign
else:
    import_structure = {
        "_997": ["FaceGearDesign"],
        "_998": ["FaceGearDiameterFaceWidthSpecificationMethod"],
        "_999": ["FaceGearMeshDesign"],
        "_1000": ["FaceGearMeshMicroGeometry"],
        "_1001": ["FaceGearMicroGeometry"],
        "_1002": ["FaceGearPinionDesign"],
        "_1003": ["FaceGearSetDesign"],
        "_1004": ["FaceGearSetMicroGeometry"],
        "_1005": ["FaceGearWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDesign",
    "FaceGearDiameterFaceWidthSpecificationMethod",
    "FaceGearMeshDesign",
    "FaceGearMeshMicroGeometry",
    "FaceGearMicroGeometry",
    "FaceGearPinionDesign",
    "FaceGearSetDesign",
    "FaceGearSetMicroGeometry",
    "FaceGearWheelDesign",
)
