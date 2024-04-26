"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._870 import ConicalGearBendingStiffness
    from ._871 import ConicalGearBendingStiffnessNode
    from ._872 import ConicalGearContactStiffness
    from ._873 import ConicalGearContactStiffnessNode
    from ._874 import ConicalGearLoadDistributionAnalysis
    from ._875 import ConicalGearSetLoadDistributionAnalysis
    from ._876 import ConicalMeshedGearLoadDistributionAnalysis
    from ._877 import ConicalMeshLoadDistributionAnalysis
    from ._878 import ConicalMeshLoadDistributionAtRotation
    from ._879 import ConicalMeshLoadedContactLine
else:
    import_structure = {
        "_870": ["ConicalGearBendingStiffness"],
        "_871": ["ConicalGearBendingStiffnessNode"],
        "_872": ["ConicalGearContactStiffness"],
        "_873": ["ConicalGearContactStiffnessNode"],
        "_874": ["ConicalGearLoadDistributionAnalysis"],
        "_875": ["ConicalGearSetLoadDistributionAnalysis"],
        "_876": ["ConicalMeshedGearLoadDistributionAnalysis"],
        "_877": ["ConicalMeshLoadDistributionAnalysis"],
        "_878": ["ConicalMeshLoadDistributionAtRotation"],
        "_879": ["ConicalMeshLoadedContactLine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBendingStiffness",
    "ConicalGearBendingStiffnessNode",
    "ConicalGearContactStiffness",
    "ConicalGearContactStiffnessNode",
    "ConicalGearLoadDistributionAnalysis",
    "ConicalGearSetLoadDistributionAnalysis",
    "ConicalMeshedGearLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAtRotation",
    "ConicalMeshLoadedContactLine",
)
