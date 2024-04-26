"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._901 import CylindricalGearMeshTIFFAnalysis
    from ._902 import CylindricalGearMeshTIFFAnalysisDutyCycle
    from ._903 import CylindricalGearSetTIFFAnalysis
    from ._904 import CylindricalGearSetTIFFAnalysisDutyCycle
    from ._905 import CylindricalGearTIFFAnalysis
    from ._906 import CylindricalGearTIFFAnalysisDutyCycle
    from ._907 import CylindricalGearTwoDimensionalFEAnalysis
    from ._908 import FindleyCriticalPlaneAnalysis
else:
    import_structure = {
        "_901": ["CylindricalGearMeshTIFFAnalysis"],
        "_902": ["CylindricalGearMeshTIFFAnalysisDutyCycle"],
        "_903": ["CylindricalGearSetTIFFAnalysis"],
        "_904": ["CylindricalGearSetTIFFAnalysisDutyCycle"],
        "_905": ["CylindricalGearTIFFAnalysis"],
        "_906": ["CylindricalGearTIFFAnalysisDutyCycle"],
        "_907": ["CylindricalGearTwoDimensionalFEAnalysis"],
        "_908": ["FindleyCriticalPlaneAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshTIFFAnalysis",
    "CylindricalGearMeshTIFFAnalysisDutyCycle",
    "CylindricalGearSetTIFFAnalysis",
    "CylindricalGearSetTIFFAnalysisDutyCycle",
    "CylindricalGearTIFFAnalysis",
    "CylindricalGearTIFFAnalysisDutyCycle",
    "CylindricalGearTwoDimensionalFEAnalysis",
    "FindleyCriticalPlaneAnalysis",
)
