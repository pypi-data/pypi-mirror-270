"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._121 import ElementScalarState
    from ._122 import ElementVectorState
    from ._123 import EntityVectorState
    from ._124 import NodeScalarState
    from ._125 import NodeVectorState
else:
    import_structure = {
        "_121": ["ElementScalarState"],
        "_122": ["ElementVectorState"],
        "_123": ["EntityVectorState"],
        "_124": ["NodeScalarState"],
        "_125": ["NodeVectorState"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementScalarState",
    "ElementVectorState",
    "EntityVectorState",
    "NodeScalarState",
    "NodeVectorState",
)
