"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2586 import CycloidalAssembly
    from ._2587 import CycloidalDisc
    from ._2588 import RingPins
else:
    import_structure = {
        "_2586": ["CycloidalAssembly"],
        "_2587": ["CycloidalDisc"],
        "_2588": ["RingPins"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalAssembly",
    "CycloidalDisc",
    "RingPins",
)
