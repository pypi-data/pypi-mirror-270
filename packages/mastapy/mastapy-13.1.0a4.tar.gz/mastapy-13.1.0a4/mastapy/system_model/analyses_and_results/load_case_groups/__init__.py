"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5684 import AbstractDesignStateLoadCaseGroup
    from ._5685 import AbstractLoadCaseGroup
    from ._5686 import AbstractStaticLoadCaseGroup
    from ._5687 import ClutchEngagementStatus
    from ._5688 import ConceptSynchroGearEngagementStatus
    from ._5689 import DesignState
    from ._5690 import DutyCycle
    from ._5691 import GenericClutchEngagementStatus
    from ._5692 import LoadCaseGroupHistograms
    from ._5693 import SubGroupInSingleDesignState
    from ._5694 import SystemOptimisationGearSet
    from ._5695 import SystemOptimiserGearSetOptimisation
    from ._5696 import SystemOptimiserTargets
    from ._5697 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5684": ["AbstractDesignStateLoadCaseGroup"],
        "_5685": ["AbstractLoadCaseGroup"],
        "_5686": ["AbstractStaticLoadCaseGroup"],
        "_5687": ["ClutchEngagementStatus"],
        "_5688": ["ConceptSynchroGearEngagementStatus"],
        "_5689": ["DesignState"],
        "_5690": ["DutyCycle"],
        "_5691": ["GenericClutchEngagementStatus"],
        "_5692": ["LoadCaseGroupHistograms"],
        "_5693": ["SubGroupInSingleDesignState"],
        "_5694": ["SystemOptimisationGearSet"],
        "_5695": ["SystemOptimiserGearSetOptimisation"],
        "_5696": ["SystemOptimiserTargets"],
        "_5697": ["TimeSeriesLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)
