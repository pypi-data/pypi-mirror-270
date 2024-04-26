"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1399 import DetailedRigidConnectorDesign
    from ._1400 import DetailedRigidConnectorHalfDesign
else:
    import_structure = {
        "_1399": ["DetailedRigidConnectorDesign"],
        "_1400": ["DetailedRigidConnectorHalfDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DetailedRigidConnectorDesign",
    "DetailedRigidConnectorHalfDesign",
)
