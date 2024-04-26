"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2634 import ActiveFESubstructureSelection
    from ._2635 import ActiveFESubstructureSelectionGroup
    from ._2636 import ActiveShaftDesignSelection
    from ._2637 import ActiveShaftDesignSelectionGroup
    from ._2638 import BearingDetailConfiguration
    from ._2639 import BearingDetailSelection
    from ._2640 import PartDetailConfiguration
    from ._2641 import PartDetailSelection
else:
    import_structure = {
        "_2634": ["ActiveFESubstructureSelection"],
        "_2635": ["ActiveFESubstructureSelectionGroup"],
        "_2636": ["ActiveShaftDesignSelection"],
        "_2637": ["ActiveShaftDesignSelectionGroup"],
        "_2638": ["BearingDetailConfiguration"],
        "_2639": ["BearingDetailSelection"],
        "_2640": ["PartDetailConfiguration"],
        "_2641": ["PartDetailSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveFESubstructureSelection",
    "ActiveFESubstructureSelectionGroup",
    "ActiveShaftDesignSelection",
    "ActiveShaftDesignSelectionGroup",
    "BearingDetailConfiguration",
    "BearingDetailSelection",
    "PartDetailConfiguration",
    "PartDetailSelection",
)
