"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5880 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5881 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5882 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5883 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5884 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5885 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5886 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5887 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5888 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5889 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5890 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5891 import HarmonicAnalysisResultsPropertyAccessor
    from ._5892 import ResultsForMultipleOrders
    from ._5893 import ResultsForMultipleOrdersForFESurface
    from ._5894 import ResultsForMultipleOrdersForGroups
    from ._5895 import ResultsForOrder
    from ._5896 import ResultsForOrderIncludingGroups
    from ._5897 import ResultsForOrderIncludingNodes
    from ._5898 import ResultsForOrderIncludingSurfaces
    from ._5899 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5900 import ResultsForResponseOfANodeOnAHarmonic
    from ._5901 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5902 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5903 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5904 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5880": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5881": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5882": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5883": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5884": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5885": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5886": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5887": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5888": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5889": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5890": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5891": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5892": ["ResultsForMultipleOrders"],
        "_5893": ["ResultsForMultipleOrdersForFESurface"],
        "_5894": ["ResultsForMultipleOrdersForGroups"],
        "_5895": ["ResultsForOrder"],
        "_5896": ["ResultsForOrderIncludingGroups"],
        "_5897": ["ResultsForOrderIncludingNodes"],
        "_5898": ["ResultsForOrderIncludingSurfaces"],
        "_5899": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5900": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5901": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5902": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5903": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5904": ["SingleWhineAnalysisResultsPropertyAccessor"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
    "HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    "HarmonicAnalysisResultsPropertyAccessor",
    "ResultsForMultipleOrders",
    "ResultsForMultipleOrdersForFESurface",
    "ResultsForMultipleOrdersForGroups",
    "ResultsForOrder",
    "ResultsForOrderIncludingGroups",
    "ResultsForOrderIncludingNodes",
    "ResultsForOrderIncludingSurfaces",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
    "ResultsForResponseOfANodeOnAHarmonic",
    "ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    "SingleWhineAnalysisResultsPropertyAccessor",
)
