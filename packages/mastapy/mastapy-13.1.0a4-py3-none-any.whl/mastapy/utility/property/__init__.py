"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1851 import EnumWithSelectedValue
    from ._1853 import DeletableCollectionMember
    from ._1854 import DutyCyclePropertySummary
    from ._1855 import DutyCyclePropertySummaryForce
    from ._1856 import DutyCyclePropertySummaryPercentage
    from ._1857 import DutyCyclePropertySummarySmallAngle
    from ._1858 import DutyCyclePropertySummaryStress
    from ._1859 import DutyCyclePropertySummaryVeryShortLength
    from ._1860 import EnumWithBoolean
    from ._1861 import NamedRangeWithOverridableMinAndMax
    from ._1862 import TypedObjectsWithOption
else:
    import_structure = {
        "_1851": ["EnumWithSelectedValue"],
        "_1853": ["DeletableCollectionMember"],
        "_1854": ["DutyCyclePropertySummary"],
        "_1855": ["DutyCyclePropertySummaryForce"],
        "_1856": ["DutyCyclePropertySummaryPercentage"],
        "_1857": ["DutyCyclePropertySummarySmallAngle"],
        "_1858": ["DutyCyclePropertySummaryStress"],
        "_1859": ["DutyCyclePropertySummaryVeryShortLength"],
        "_1860": ["EnumWithBoolean"],
        "_1861": ["NamedRangeWithOverridableMinAndMax"],
        "_1862": ["TypedObjectsWithOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue",
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)
