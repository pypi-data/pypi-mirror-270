"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1839 import Database
    from ._1840 import DatabaseConnectionSettings
    from ._1841 import DatabaseKey
    from ._1842 import DatabaseSettings
    from ._1843 import NamedDatabase
    from ._1844 import NamedDatabaseItem
    from ._1845 import NamedKey
    from ._1846 import SQLDatabase
else:
    import_structure = {
        "_1839": ["Database"],
        "_1840": ["DatabaseConnectionSettings"],
        "_1841": ["DatabaseKey"],
        "_1842": ["DatabaseSettings"],
        "_1843": ["NamedDatabase"],
        "_1844": ["NamedDatabaseItem"],
        "_1845": ["NamedKey"],
        "_1846": ["SQLDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Database",
    "DatabaseConnectionSettings",
    "DatabaseKey",
    "DatabaseSettings",
    "NamedDatabase",
    "NamedDatabaseItem",
    "NamedKey",
    "SQLDatabase",
)
