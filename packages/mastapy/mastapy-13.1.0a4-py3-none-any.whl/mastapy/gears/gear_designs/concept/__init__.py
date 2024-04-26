"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1186 import ConceptGearDesign
    from ._1187 import ConceptGearMeshDesign
    from ._1188 import ConceptGearSetDesign
else:
    import_structure = {
        "_1186": ["ConceptGearDesign"],
        "_1187": ["ConceptGearMeshDesign"],
        "_1188": ["ConceptGearSetDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDesign",
    "ConceptGearMeshDesign",
    "ConceptGearSetDesign",
)
