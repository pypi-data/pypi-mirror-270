"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1581 import DataScalingOptions
    from ._1582 import DataScalingReferenceValues
    from ._1583 import DataScalingReferenceValuesBase
else:
    import_structure = {
        "_1581": ["DataScalingOptions"],
        "_1582": ["DataScalingReferenceValues"],
        "_1583": ["DataScalingReferenceValuesBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)
