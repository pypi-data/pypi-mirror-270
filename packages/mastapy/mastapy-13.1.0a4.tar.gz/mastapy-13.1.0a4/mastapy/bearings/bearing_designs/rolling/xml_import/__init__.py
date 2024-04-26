"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2194 import AbstractXmlVariableAssignment
    from ._2195 import BearingImportFile
    from ._2196 import RollingBearingImporter
    from ._2197 import XmlBearingTypeMapping
    from ._2198 import XMLVariableAssignment
else:
    import_structure = {
        "_2194": ["AbstractXmlVariableAssignment"],
        "_2195": ["BearingImportFile"],
        "_2196": ["RollingBearingImporter"],
        "_2197": ["XmlBearingTypeMapping"],
        "_2198": ["XMLVariableAssignment"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractXmlVariableAssignment",
    "BearingImportFile",
    "RollingBearingImporter",
    "XmlBearingTypeMapping",
    "XMLVariableAssignment",
)
