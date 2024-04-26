"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5870 import ConnectedComponentType
    from ._5871 import ExcitationSourceSelection
    from ._5872 import ExcitationSourceSelectionBase
    from ._5873 import ExcitationSourceSelectionGroup
    from ._5874 import HarmonicSelection
    from ._5875 import ModalContributionDisplayMethod
    from ._5876 import ModalContributionFilteringMethod
    from ._5877 import ResultLocationSelectionGroup
    from ._5878 import ResultLocationSelectionGroups
    from ._5879 import ResultNodeSelection
else:
    import_structure = {
        "_5870": ["ConnectedComponentType"],
        "_5871": ["ExcitationSourceSelection"],
        "_5872": ["ExcitationSourceSelectionBase"],
        "_5873": ["ExcitationSourceSelectionGroup"],
        "_5874": ["HarmonicSelection"],
        "_5875": ["ModalContributionDisplayMethod"],
        "_5876": ["ModalContributionFilteringMethod"],
        "_5877": ["ResultLocationSelectionGroup"],
        "_5878": ["ResultLocationSelectionGroups"],
        "_5879": ["ResultNodeSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)
