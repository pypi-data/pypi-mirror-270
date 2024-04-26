"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5698 import AbstractAssemblyStaticLoadCaseGroup
    from ._5699 import ComponentStaticLoadCaseGroup
    from ._5700 import ConnectionStaticLoadCaseGroup
    from ._5701 import DesignEntityStaticLoadCaseGroup
    from ._5702 import GearSetStaticLoadCaseGroup
    from ._5703 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5698": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5699": ["ComponentStaticLoadCaseGroup"],
        "_5700": ["ConnectionStaticLoadCaseGroup"],
        "_5701": ["DesignEntityStaticLoadCaseGroup"],
        "_5702": ["GearSetStaticLoadCaseGroup"],
        "_5703": ["PartStaticLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStaticLoadCaseGroup",
    "ComponentStaticLoadCaseGroup",
    "ConnectionStaticLoadCaseGroup",
    "DesignEntityStaticLoadCaseGroup",
    "GearSetStaticLoadCaseGroup",
    "PartStaticLoadCaseGroup",
)
