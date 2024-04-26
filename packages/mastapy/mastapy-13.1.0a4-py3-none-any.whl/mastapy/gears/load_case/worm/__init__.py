"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._883 import WormGearLoadCase
    from ._884 import WormGearSetLoadCase
    from ._885 import WormMeshLoadCase
else:
    import_structure = {
        "_883": ["WormGearLoadCase"],
        "_884": ["WormGearSetLoadCase"],
        "_885": ["WormMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearLoadCase",
    "WormGearSetLoadCase",
    "WormMeshLoadCase",
)
