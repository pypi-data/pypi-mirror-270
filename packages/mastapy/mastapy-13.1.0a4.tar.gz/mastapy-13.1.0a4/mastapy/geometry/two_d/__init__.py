"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._317 import CADFace
    from ._318 import CADFaceGroup
    from ._319 import InternalExternalType
else:
    import_structure = {
        "_317": ["CADFace"],
        "_318": ["CADFaceGroup"],
        "_319": ["InternalExternalType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CADFace",
    "CADFaceGroup",
    "InternalExternalType",
)
