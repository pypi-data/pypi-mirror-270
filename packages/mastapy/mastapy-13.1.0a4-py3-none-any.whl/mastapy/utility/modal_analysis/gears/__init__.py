"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1812 import GearMeshForTE
    from ._1813 import GearOrderForTE
    from ._1814 import GearPositions
    from ._1815 import HarmonicOrderForTE
    from ._1816 import LabelOnlyOrder
    from ._1817 import OrderForTE
    from ._1818 import OrderSelector
    from ._1819 import OrderWithRadius
    from ._1820 import RollingBearingOrder
    from ._1821 import ShaftOrderForTE
    from ._1822 import UserDefinedOrderForTE
else:
    import_structure = {
        "_1812": ["GearMeshForTE"],
        "_1813": ["GearOrderForTE"],
        "_1814": ["GearPositions"],
        "_1815": ["HarmonicOrderForTE"],
        "_1816": ["LabelOnlyOrder"],
        "_1817": ["OrderForTE"],
        "_1818": ["OrderSelector"],
        "_1819": ["OrderWithRadius"],
        "_1820": ["RollingBearingOrder"],
        "_1821": ["ShaftOrderForTE"],
        "_1822": ["UserDefinedOrderForTE"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)
