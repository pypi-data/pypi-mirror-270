"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._880 import GearLoadCaseBase
    from ._881 import GearSetLoadCaseBase
    from ._882 import MeshLoadCase
else:
    import_structure = {
        "_880": ["GearLoadCaseBase"],
        "_881": ["GearSetLoadCaseBase"],
        "_882": ["MeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearLoadCaseBase",
    "GearSetLoadCaseBase",
    "MeshLoadCase",
)
