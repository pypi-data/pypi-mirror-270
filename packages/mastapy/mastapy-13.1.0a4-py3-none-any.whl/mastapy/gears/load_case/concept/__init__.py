"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._895 import ConceptGearLoadCase
    from ._896 import ConceptGearSetLoadCase
    from ._897 import ConceptMeshLoadCase
else:
    import_structure = {
        "_895": ["ConceptGearLoadCase"],
        "_896": ["ConceptGearSetLoadCase"],
        "_897": ["ConceptMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearLoadCase",
    "ConceptGearSetLoadCase",
    "ConceptMeshLoadCase",
)
