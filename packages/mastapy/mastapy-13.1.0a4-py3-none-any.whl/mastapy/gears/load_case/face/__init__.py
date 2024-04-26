"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._886 import FaceGearLoadCase
    from ._887 import FaceGearSetLoadCase
    from ._888 import FaceMeshLoadCase
else:
    import_structure = {
        "_886": ["FaceGearLoadCase"],
        "_887": ["FaceGearSetLoadCase"],
        "_888": ["FaceMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearLoadCase",
    "FaceGearSetLoadCase",
    "FaceMeshLoadCase",
)
