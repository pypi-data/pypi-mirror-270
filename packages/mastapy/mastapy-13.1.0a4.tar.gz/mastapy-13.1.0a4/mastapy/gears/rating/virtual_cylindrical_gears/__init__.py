"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._385 import BevelVirtualCylindricalGearISO10300MethodB2
    from ._386 import BevelVirtualCylindricalGearSetISO10300MethodB1
    from ._387 import BevelVirtualCylindricalGearSetISO10300MethodB2
    from ._388 import HypoidVirtualCylindricalGearISO10300MethodB2
    from ._389 import HypoidVirtualCylindricalGearSetISO10300MethodB1
    from ._390 import HypoidVirtualCylindricalGearSetISO10300MethodB2
    from ._391 import KlingelnbergHypoidVirtualCylindricalGear
    from ._392 import KlingelnbergSpiralBevelVirtualCylindricalGear
    from ._393 import KlingelnbergVirtualCylindricalGear
    from ._394 import KlingelnbergVirtualCylindricalGearSet
    from ._395 import VirtualCylindricalGear
    from ._396 import VirtualCylindricalGearBasic
    from ._397 import VirtualCylindricalGearISO10300MethodB1
    from ._398 import VirtualCylindricalGearISO10300MethodB2
    from ._399 import VirtualCylindricalGearSet
    from ._400 import VirtualCylindricalGearSetISO10300MethodB1
    from ._401 import VirtualCylindricalGearSetISO10300MethodB2
else:
    import_structure = {
        "_385": ["BevelVirtualCylindricalGearISO10300MethodB2"],
        "_386": ["BevelVirtualCylindricalGearSetISO10300MethodB1"],
        "_387": ["BevelVirtualCylindricalGearSetISO10300MethodB2"],
        "_388": ["HypoidVirtualCylindricalGearISO10300MethodB2"],
        "_389": ["HypoidVirtualCylindricalGearSetISO10300MethodB1"],
        "_390": ["HypoidVirtualCylindricalGearSetISO10300MethodB2"],
        "_391": ["KlingelnbergHypoidVirtualCylindricalGear"],
        "_392": ["KlingelnbergSpiralBevelVirtualCylindricalGear"],
        "_393": ["KlingelnbergVirtualCylindricalGear"],
        "_394": ["KlingelnbergVirtualCylindricalGearSet"],
        "_395": ["VirtualCylindricalGear"],
        "_396": ["VirtualCylindricalGearBasic"],
        "_397": ["VirtualCylindricalGearISO10300MethodB1"],
        "_398": ["VirtualCylindricalGearISO10300MethodB2"],
        "_399": ["VirtualCylindricalGearSet"],
        "_400": ["VirtualCylindricalGearSetISO10300MethodB1"],
        "_401": ["VirtualCylindricalGearSetISO10300MethodB2"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelVirtualCylindricalGearISO10300MethodB2",
    "BevelVirtualCylindricalGearSetISO10300MethodB1",
    "BevelVirtualCylindricalGearSetISO10300MethodB2",
    "HypoidVirtualCylindricalGearISO10300MethodB2",
    "HypoidVirtualCylindricalGearSetISO10300MethodB1",
    "HypoidVirtualCylindricalGearSetISO10300MethodB2",
    "KlingelnbergHypoidVirtualCylindricalGear",
    "KlingelnbergSpiralBevelVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGearSet",
    "VirtualCylindricalGear",
    "VirtualCylindricalGearBasic",
    "VirtualCylindricalGearISO10300MethodB1",
    "VirtualCylindricalGearISO10300MethodB2",
    "VirtualCylindricalGearSet",
    "VirtualCylindricalGearSetISO10300MethodB1",
    "VirtualCylindricalGearSetISO10300MethodB2",
)
