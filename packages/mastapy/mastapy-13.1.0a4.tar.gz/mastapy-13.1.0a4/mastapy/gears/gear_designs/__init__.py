"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._948 import BevelHypoidGearDesignSettingsDatabase
    from ._949 import BevelHypoidGearDesignSettingsItem
    from ._950 import BevelHypoidGearRatingSettingsDatabase
    from ._951 import BevelHypoidGearRatingSettingsItem
    from ._952 import DesignConstraint
    from ._953 import DesignConstraintCollectionDatabase
    from ._954 import DesignConstraintsCollection
    from ._955 import GearDesign
    from ._956 import GearDesignComponent
    from ._957 import GearMeshDesign
    from ._958 import GearSetDesign
    from ._959 import SelectedDesignConstraintsCollection
else:
    import_structure = {
        "_948": ["BevelHypoidGearDesignSettingsDatabase"],
        "_949": ["BevelHypoidGearDesignSettingsItem"],
        "_950": ["BevelHypoidGearRatingSettingsDatabase"],
        "_951": ["BevelHypoidGearRatingSettingsItem"],
        "_952": ["DesignConstraint"],
        "_953": ["DesignConstraintCollectionDatabase"],
        "_954": ["DesignConstraintsCollection"],
        "_955": ["GearDesign"],
        "_956": ["GearDesignComponent"],
        "_957": ["GearMeshDesign"],
        "_958": ["GearSetDesign"],
        "_959": ["SelectedDesignConstraintsCollection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelHypoidGearDesignSettingsDatabase",
    "BevelHypoidGearDesignSettingsItem",
    "BevelHypoidGearRatingSettingsDatabase",
    "BevelHypoidGearRatingSettingsItem",
    "DesignConstraint",
    "DesignConstraintCollectionDatabase",
    "DesignConstraintsCollection",
    "GearDesign",
    "GearDesignComponent",
    "GearMeshDesign",
    "GearSetDesign",
    "SelectedDesignConstraintsCollection",
)
