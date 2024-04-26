"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._858 import CylindricalGearBendingStiffness
    from ._859 import CylindricalGearBendingStiffnessNode
    from ._860 import CylindricalGearContactStiffness
    from ._861 import CylindricalGearContactStiffnessNode
    from ._862 import CylindricalGearFESettings
    from ._863 import CylindricalGearLoadDistributionAnalysis
    from ._864 import CylindricalGearMeshLoadDistributionAnalysis
    from ._865 import CylindricalGearMeshLoadedContactLine
    from ._866 import CylindricalGearMeshLoadedContactPoint
    from ._867 import CylindricalGearSetLoadDistributionAnalysis
    from ._868 import CylindricalMeshLoadDistributionAtRotation
    from ._869 import FaceGearSetLoadDistributionAnalysis
else:
    import_structure = {
        "_858": ["CylindricalGearBendingStiffness"],
        "_859": ["CylindricalGearBendingStiffnessNode"],
        "_860": ["CylindricalGearContactStiffness"],
        "_861": ["CylindricalGearContactStiffnessNode"],
        "_862": ["CylindricalGearFESettings"],
        "_863": ["CylindricalGearLoadDistributionAnalysis"],
        "_864": ["CylindricalGearMeshLoadDistributionAnalysis"],
        "_865": ["CylindricalGearMeshLoadedContactLine"],
        "_866": ["CylindricalGearMeshLoadedContactPoint"],
        "_867": ["CylindricalGearSetLoadDistributionAnalysis"],
        "_868": ["CylindricalMeshLoadDistributionAtRotation"],
        "_869": ["FaceGearSetLoadDistributionAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBendingStiffness",
    "CylindricalGearBendingStiffnessNode",
    "CylindricalGearContactStiffness",
    "CylindricalGearContactStiffnessNode",
    "CylindricalGearFESettings",
    "CylindricalGearLoadDistributionAnalysis",
    "CylindricalGearMeshLoadDistributionAnalysis",
    "CylindricalGearMeshLoadedContactLine",
    "CylindricalGearMeshLoadedContactPoint",
    "CylindricalGearSetLoadDistributionAnalysis",
    "CylindricalMeshLoadDistributionAtRotation",
    "FaceGearSetLoadDistributionAnalysis",
)
