"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._898 import BevelLoadCase
    from ._899 import BevelMeshLoadCase
    from ._900 import BevelSetLoadCase
else:
    import_structure = {
        "_898": ["BevelLoadCase"],
        "_899": ["BevelMeshLoadCase"],
        "_900": ["BevelSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelLoadCase",
    "BevelMeshLoadCase",
    "BevelSetLoadCase",
)
