"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._313 import ClippingPlane
    from ._314 import DrawStyle
    from ._315 import DrawStyleBase
    from ._316 import PackagingLimits
else:
    import_structure = {
        "_313": ["ClippingPlane"],
        "_314": ["DrawStyle"],
        "_315": ["DrawStyleBase"],
        "_316": ["PackagingLimits"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClippingPlane",
    "DrawStyle",
    "DrawStyleBase",
    "PackagingLimits",
)
