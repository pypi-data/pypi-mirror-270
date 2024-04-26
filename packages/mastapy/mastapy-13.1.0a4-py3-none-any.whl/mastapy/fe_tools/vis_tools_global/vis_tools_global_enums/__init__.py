"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1244 import BeamSectionType
    from ._1245 import ContactPairConstrainedSurfaceType
    from ._1246 import ContactPairReferenceSurfaceType
    from ._1247 import ElementPropertiesShellWallType
else:
    import_structure = {
        "_1244": ["BeamSectionType"],
        "_1245": ["ContactPairConstrainedSurfaceType"],
        "_1246": ["ContactPairReferenceSurfaceType"],
        "_1247": ["ElementPropertiesShellWallType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeamSectionType",
    "ContactPairConstrainedSurfaceType",
    "ContactPairReferenceSurfaceType",
    "ElementPropertiesShellWallType",
)
