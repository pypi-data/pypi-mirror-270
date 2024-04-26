"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._832 import ConicalGearFilletStressResults
    from ._833 import ConicalGearRootFilletStressResults
    from ._834 import ContactResultType
    from ._835 import CylindricalGearFilletNodeStressResults
    from ._836 import CylindricalGearFilletNodeStressResultsColumn
    from ._837 import CylindricalGearFilletNodeStressResultsRow
    from ._838 import CylindricalGearRootFilletStressResults
    from ._839 import CylindricalMeshedGearLoadDistributionAnalysis
    from ._840 import GearBendingStiffness
    from ._841 import GearBendingStiffnessNode
    from ._842 import GearContactStiffness
    from ._843 import GearContactStiffnessNode
    from ._844 import GearFilletNodeStressResults
    from ._845 import GearFilletNodeStressResultsColumn
    from ._846 import GearFilletNodeStressResultsRow
    from ._847 import GearLoadDistributionAnalysis
    from ._848 import GearMeshLoadDistributionAnalysis
    from ._849 import GearMeshLoadDistributionAtRotation
    from ._850 import GearMeshLoadedContactLine
    from ._851 import GearMeshLoadedContactPoint
    from ._852 import GearRootFilletStressResults
    from ._853 import GearSetLoadDistributionAnalysis
    from ._854 import GearStiffness
    from ._855 import GearStiffnessNode
    from ._856 import MeshedGearLoadDistributionAnalysisAtRotation
    from ._857 import UseAdvancedLTCAOptions
else:
    import_structure = {
        "_832": ["ConicalGearFilletStressResults"],
        "_833": ["ConicalGearRootFilletStressResults"],
        "_834": ["ContactResultType"],
        "_835": ["CylindricalGearFilletNodeStressResults"],
        "_836": ["CylindricalGearFilletNodeStressResultsColumn"],
        "_837": ["CylindricalGearFilletNodeStressResultsRow"],
        "_838": ["CylindricalGearRootFilletStressResults"],
        "_839": ["CylindricalMeshedGearLoadDistributionAnalysis"],
        "_840": ["GearBendingStiffness"],
        "_841": ["GearBendingStiffnessNode"],
        "_842": ["GearContactStiffness"],
        "_843": ["GearContactStiffnessNode"],
        "_844": ["GearFilletNodeStressResults"],
        "_845": ["GearFilletNodeStressResultsColumn"],
        "_846": ["GearFilletNodeStressResultsRow"],
        "_847": ["GearLoadDistributionAnalysis"],
        "_848": ["GearMeshLoadDistributionAnalysis"],
        "_849": ["GearMeshLoadDistributionAtRotation"],
        "_850": ["GearMeshLoadedContactLine"],
        "_851": ["GearMeshLoadedContactPoint"],
        "_852": ["GearRootFilletStressResults"],
        "_853": ["GearSetLoadDistributionAnalysis"],
        "_854": ["GearStiffness"],
        "_855": ["GearStiffnessNode"],
        "_856": ["MeshedGearLoadDistributionAnalysisAtRotation"],
        "_857": ["UseAdvancedLTCAOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFilletStressResults",
    "ConicalGearRootFilletStressResults",
    "ContactResultType",
    "CylindricalGearFilletNodeStressResults",
    "CylindricalGearFilletNodeStressResultsColumn",
    "CylindricalGearFilletNodeStressResultsRow",
    "CylindricalGearRootFilletStressResults",
    "CylindricalMeshedGearLoadDistributionAnalysis",
    "GearBendingStiffness",
    "GearBendingStiffnessNode",
    "GearContactStiffness",
    "GearContactStiffnessNode",
    "GearFilletNodeStressResults",
    "GearFilletNodeStressResultsColumn",
    "GearFilletNodeStressResultsRow",
    "GearLoadDistributionAnalysis",
    "GearMeshLoadDistributionAnalysis",
    "GearMeshLoadDistributionAtRotation",
    "GearMeshLoadedContactLine",
    "GearMeshLoadedContactPoint",
    "GearRootFilletStressResults",
    "GearSetLoadDistributionAnalysis",
    "GearStiffness",
    "GearStiffnessNode",
    "MeshedGearLoadDistributionAnalysisAtRotation",
    "UseAdvancedLTCAOptions",
)
