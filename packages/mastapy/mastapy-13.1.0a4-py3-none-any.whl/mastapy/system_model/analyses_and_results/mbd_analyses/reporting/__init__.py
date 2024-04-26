"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5548 import AbstractMeasuredDynamicResponseAtTime
    from ._5549 import DynamicForceResultAtTime
    from ._5550 import DynamicForceVector3DResult
    from ._5551 import DynamicTorqueResultAtTime
    from ._5552 import DynamicTorqueVector3DResult
    from ._5553 import NodeInformation
else:
    import_structure = {
        "_5548": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5549": ["DynamicForceResultAtTime"],
        "_5550": ["DynamicForceVector3DResult"],
        "_5551": ["DynamicTorqueResultAtTime"],
        "_5552": ["DynamicTorqueVector3DResult"],
        "_5553": ["NodeInformation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractMeasuredDynamicResponseAtTime",
    "DynamicForceResultAtTime",
    "DynamicForceVector3DResult",
    "DynamicTorqueResultAtTime",
    "DynamicTorqueVector3DResult",
    "NodeInformation",
)
