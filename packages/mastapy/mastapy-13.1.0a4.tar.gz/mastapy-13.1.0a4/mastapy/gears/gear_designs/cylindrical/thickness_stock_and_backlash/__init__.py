"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1099 import FinishStockSpecification
    from ._1100 import FinishStockType
    from ._1101 import NominalValueSpecification
    from ._1102 import NoValueSpecification
else:
    import_structure = {
        "_1099": ["FinishStockSpecification"],
        "_1100": ["FinishStockType"],
        "_1101": ["NominalValueSpecification"],
        "_1102": ["NoValueSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FinishStockSpecification",
    "FinishStockType",
    "NominalValueSpecification",
    "NoValueSpecification",
)
