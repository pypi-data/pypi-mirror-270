"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._756 import ActiveProfileRangeCalculationSource
    from ._757 import AxialShaverRedressing
    from ._758 import ConventionalShavingDynamics
    from ._759 import ConventionalShavingDynamicsCalculationForDesignedGears
    from ._760 import ConventionalShavingDynamicsCalculationForHobbedGears
    from ._761 import ConventionalShavingDynamicsViewModel
    from ._762 import PlungeShaverDynamics
    from ._763 import PlungeShaverDynamicSettings
    from ._764 import PlungeShaverRedressing
    from ._765 import PlungeShavingDynamicsCalculationForDesignedGears
    from ._766 import PlungeShavingDynamicsCalculationForHobbedGears
    from ._767 import PlungeShavingDynamicsViewModel
    from ._768 import RedressingSettings
    from ._769 import RollAngleRangeRelativeToAccuracy
    from ._770 import RollAngleReportObject
    from ._771 import ShaverRedressing
    from ._772 import ShavingDynamics
    from ._773 import ShavingDynamicsCalculation
    from ._774 import ShavingDynamicsCalculationForDesignedGears
    from ._775 import ShavingDynamicsCalculationForHobbedGears
    from ._776 import ShavingDynamicsConfiguration
    from ._777 import ShavingDynamicsViewModel
    from ._778 import ShavingDynamicsViewModelBase
else:
    import_structure = {
        "_756": ["ActiveProfileRangeCalculationSource"],
        "_757": ["AxialShaverRedressing"],
        "_758": ["ConventionalShavingDynamics"],
        "_759": ["ConventionalShavingDynamicsCalculationForDesignedGears"],
        "_760": ["ConventionalShavingDynamicsCalculationForHobbedGears"],
        "_761": ["ConventionalShavingDynamicsViewModel"],
        "_762": ["PlungeShaverDynamics"],
        "_763": ["PlungeShaverDynamicSettings"],
        "_764": ["PlungeShaverRedressing"],
        "_765": ["PlungeShavingDynamicsCalculationForDesignedGears"],
        "_766": ["PlungeShavingDynamicsCalculationForHobbedGears"],
        "_767": ["PlungeShavingDynamicsViewModel"],
        "_768": ["RedressingSettings"],
        "_769": ["RollAngleRangeRelativeToAccuracy"],
        "_770": ["RollAngleReportObject"],
        "_771": ["ShaverRedressing"],
        "_772": ["ShavingDynamics"],
        "_773": ["ShavingDynamicsCalculation"],
        "_774": ["ShavingDynamicsCalculationForDesignedGears"],
        "_775": ["ShavingDynamicsCalculationForHobbedGears"],
        "_776": ["ShavingDynamicsConfiguration"],
        "_777": ["ShavingDynamicsViewModel"],
        "_778": ["ShavingDynamicsViewModelBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProfileRangeCalculationSource",
    "AxialShaverRedressing",
    "ConventionalShavingDynamics",
    "ConventionalShavingDynamicsCalculationForDesignedGears",
    "ConventionalShavingDynamicsCalculationForHobbedGears",
    "ConventionalShavingDynamicsViewModel",
    "PlungeShaverDynamics",
    "PlungeShaverDynamicSettings",
    "PlungeShaverRedressing",
    "PlungeShavingDynamicsCalculationForDesignedGears",
    "PlungeShavingDynamicsCalculationForHobbedGears",
    "PlungeShavingDynamicsViewModel",
    "RedressingSettings",
    "RollAngleRangeRelativeToAccuracy",
    "RollAngleReportObject",
    "ShaverRedressing",
    "ShavingDynamics",
    "ShavingDynamicsCalculation",
    "ShavingDynamicsCalculationForDesignedGears",
    "ShavingDynamicsCalculationForHobbedGears",
    "ShavingDynamicsConfiguration",
    "ShavingDynamicsViewModel",
    "ShavingDynamicsViewModelBase",
)
