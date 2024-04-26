"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1225 import AbstractGearAnalysis
    from ._1226 import AbstractGearMeshAnalysis
    from ._1227 import AbstractGearSetAnalysis
    from ._1228 import GearDesignAnalysis
    from ._1229 import GearImplementationAnalysis
    from ._1230 import GearImplementationAnalysisDutyCycle
    from ._1231 import GearImplementationDetail
    from ._1232 import GearMeshDesignAnalysis
    from ._1233 import GearMeshImplementationAnalysis
    from ._1234 import GearMeshImplementationAnalysisDutyCycle
    from ._1235 import GearMeshImplementationDetail
    from ._1236 import GearSetDesignAnalysis
    from ._1237 import GearSetGroupDutyCycle
    from ._1238 import GearSetImplementationAnalysis
    from ._1239 import GearSetImplementationAnalysisAbstract
    from ._1240 import GearSetImplementationAnalysisDutyCycle
    from ._1241 import GearSetImplementationDetail
else:
    import_structure = {
        "_1225": ["AbstractGearAnalysis"],
        "_1226": ["AbstractGearMeshAnalysis"],
        "_1227": ["AbstractGearSetAnalysis"],
        "_1228": ["GearDesignAnalysis"],
        "_1229": ["GearImplementationAnalysis"],
        "_1230": ["GearImplementationAnalysisDutyCycle"],
        "_1231": ["GearImplementationDetail"],
        "_1232": ["GearMeshDesignAnalysis"],
        "_1233": ["GearMeshImplementationAnalysis"],
        "_1234": ["GearMeshImplementationAnalysisDutyCycle"],
        "_1235": ["GearMeshImplementationDetail"],
        "_1236": ["GearSetDesignAnalysis"],
        "_1237": ["GearSetGroupDutyCycle"],
        "_1238": ["GearSetImplementationAnalysis"],
        "_1239": ["GearSetImplementationAnalysisAbstract"],
        "_1240": ["GearSetImplementationAnalysisDutyCycle"],
        "_1241": ["GearSetImplementationDetail"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)
