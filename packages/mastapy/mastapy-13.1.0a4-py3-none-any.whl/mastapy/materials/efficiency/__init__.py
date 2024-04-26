"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._299 import BearingEfficiencyRatingMethod
    from ._300 import CombinedResistiveTorque
    from ._301 import EfficiencyRatingMethod
    from ._302 import IndependentPowerLoss
    from ._303 import IndependentResistiveTorque
    from ._304 import LoadAndSpeedCombinedPowerLoss
    from ._305 import OilPumpDetail
    from ._306 import OilPumpDriveType
    from ._307 import OilSealLossCalculationMethod
    from ._308 import OilSealMaterialType
    from ._309 import PowerLoss
    from ._310 import ResistiveTorque
else:
    import_structure = {
        "_299": ["BearingEfficiencyRatingMethod"],
        "_300": ["CombinedResistiveTorque"],
        "_301": ["EfficiencyRatingMethod"],
        "_302": ["IndependentPowerLoss"],
        "_303": ["IndependentResistiveTorque"],
        "_304": ["LoadAndSpeedCombinedPowerLoss"],
        "_305": ["OilPumpDetail"],
        "_306": ["OilPumpDriveType"],
        "_307": ["OilSealLossCalculationMethod"],
        "_308": ["OilSealMaterialType"],
        "_309": ["PowerLoss"],
        "_310": ["ResistiveTorque"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingEfficiencyRatingMethod",
    "CombinedResistiveTorque",
    "EfficiencyRatingMethod",
    "IndependentPowerLoss",
    "IndependentResistiveTorque",
    "LoadAndSpeedCombinedPowerLoss",
    "OilPumpDetail",
    "OilPumpDriveType",
    "OilSealLossCalculationMethod",
    "OilSealMaterialType",
    "PowerLoss",
    "ResistiveTorque",
)
