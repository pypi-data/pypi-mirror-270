"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1249 import ProSolveMpcType
    from ._1250 import ProSolveSolverType
else:
    import_structure = {
        "_1249": ["ProSolveMpcType"],
        "_1250": ["ProSolveSolverType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProSolveMpcType",
    "ProSolveSolverType",
)
