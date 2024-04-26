"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1500 import LicenceServer
    from ._7598 import LicenceServerDetails
    from ._7599 import ModuleDetails
    from ._7600 import ModuleLicenceStatus
else:
    import_structure = {
        "_1500": ["LicenceServer"],
        "_7598": ["LicenceServerDetails"],
        "_7599": ["ModuleDetails"],
        "_7600": ["ModuleLicenceStatus"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LicenceServer",
    "LicenceServerDetails",
    "ModuleDetails",
    "ModuleLicenceStatus",
)
