"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1615 import DegreesMinutesSeconds
    from ._1616 import EnumUnit
    from ._1617 import InverseUnit
    from ._1618 import MeasurementBase
    from ._1619 import MeasurementSettings
    from ._1620 import MeasurementSystem
    from ._1621 import SafetyFactorUnit
    from ._1622 import TimeUnit
    from ._1623 import Unit
    from ._1624 import UnitGradient
else:
    import_structure = {
        "_1615": ["DegreesMinutesSeconds"],
        "_1616": ["EnumUnit"],
        "_1617": ["InverseUnit"],
        "_1618": ["MeasurementBase"],
        "_1619": ["MeasurementSettings"],
        "_1620": ["MeasurementSystem"],
        "_1621": ["SafetyFactorUnit"],
        "_1622": ["TimeUnit"],
        "_1623": ["Unit"],
        "_1624": ["UnitGradient"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)
