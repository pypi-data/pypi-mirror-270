"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._889 import CylindricalGearLoadCase
    from ._890 import CylindricalGearSetLoadCase
    from ._891 import CylindricalMeshLoadCase
else:
    import_structure = {
        "_889": ["CylindricalGearLoadCase"],
        "_890": ["CylindricalGearSetLoadCase"],
        "_891": ["CylindricalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLoadCase",
    "CylindricalGearSetLoadCase",
    "CylindricalMeshLoadCase",
)
