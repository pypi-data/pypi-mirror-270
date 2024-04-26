"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1804 import Fix
    from ._1805 import Severity
    from ._1806 import Status
    from ._1807 import StatusItem
    from ._1808 import StatusItemSeverity
    from ._1809 import StatusItemWrapper
    from ._1810 import StatusWrapper
else:
    import_structure = {
        "_1804": ["Fix"],
        "_1805": ["Severity"],
        "_1806": ["Status"],
        "_1807": ["StatusItem"],
        "_1808": ["StatusItemSeverity"],
        "_1809": ["StatusItemWrapper"],
        "_1810": ["StatusWrapper"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Fix",
    "Severity",
    "Status",
    "StatusItem",
    "StatusItemSeverity",
    "StatusItemWrapper",
    "StatusWrapper",
)
