"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1251 import ElementPropertyClass
    from ._1252 import MaterialPropertyClass
else:
    import_structure = {
        "_1251": ["ElementPropertyClass"],
        "_1252": ["MaterialPropertyClass"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementPropertyClass",
    "MaterialPropertyClass",
)
