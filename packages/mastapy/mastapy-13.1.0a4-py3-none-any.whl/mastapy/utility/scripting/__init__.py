"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1752 import ScriptingSetup
    from ._1753 import UserDefinedPropertyKey
    from ._1754 import UserSpecifiedData
else:
    import_structure = {
        "_1752": ["ScriptingSetup"],
        "_1753": ["UserDefinedPropertyKey"],
        "_1754": ["UserSpecifiedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ScriptingSetup",
    "UserDefinedPropertyKey",
    "UserSpecifiedData",
)
