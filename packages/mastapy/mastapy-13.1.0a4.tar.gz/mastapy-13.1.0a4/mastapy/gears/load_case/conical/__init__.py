"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._892 import ConicalGearLoadCase
    from ._893 import ConicalGearSetLoadCase
    from ._894 import ConicalMeshLoadCase
else:
    import_structure = {
        "_892": ["ConicalGearLoadCase"],
        "_893": ["ConicalGearSetLoadCase"],
        "_894": ["ConicalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearLoadCase",
    "ConicalGearSetLoadCase",
    "ConicalMeshLoadCase",
)
