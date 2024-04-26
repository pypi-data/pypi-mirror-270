"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7588 import ApiEnumForAttribute
    from ._7589 import ApiVersion
    from ._7590 import SMTBitmap
    from ._7592 import MastaPropertyAttribute
    from ._7593 import PythonCommand
    from ._7594 import ScriptingCommand
    from ._7595 import ScriptingExecutionCommand
    from ._7596 import ScriptingObjectCommand
    from ._7597 import ApiVersioning
else:
    import_structure = {
        "_7588": ["ApiEnumForAttribute"],
        "_7589": ["ApiVersion"],
        "_7590": ["SMTBitmap"],
        "_7592": ["MastaPropertyAttribute"],
        "_7593": ["PythonCommand"],
        "_7594": ["ScriptingCommand"],
        "_7595": ["ScriptingExecutionCommand"],
        "_7596": ["ScriptingObjectCommand"],
        "_7597": ["ApiVersioning"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ApiEnumForAttribute",
    "ApiVersion",
    "SMTBitmap",
    "MastaPropertyAttribute",
    "PythonCommand",
    "ScriptingCommand",
    "ScriptingExecutionCommand",
    "ScriptingObjectCommand",
    "ApiVersioning",
)
