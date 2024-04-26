"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2351 import CycloidalDiscAxialLeftSocket
    from ._2352 import CycloidalDiscAxialRightSocket
    from ._2353 import CycloidalDiscCentralBearingConnection
    from ._2354 import CycloidalDiscInnerSocket
    from ._2355 import CycloidalDiscOuterSocket
    from ._2356 import CycloidalDiscPlanetaryBearingConnection
    from ._2357 import CycloidalDiscPlanetaryBearingSocket
    from ._2358 import RingPinsSocket
    from ._2359 import RingPinsToDiscConnection
else:
    import_structure = {
        "_2351": ["CycloidalDiscAxialLeftSocket"],
        "_2352": ["CycloidalDiscAxialRightSocket"],
        "_2353": ["CycloidalDiscCentralBearingConnection"],
        "_2354": ["CycloidalDiscInnerSocket"],
        "_2355": ["CycloidalDiscOuterSocket"],
        "_2356": ["CycloidalDiscPlanetaryBearingConnection"],
        "_2357": ["CycloidalDiscPlanetaryBearingSocket"],
        "_2358": ["RingPinsSocket"],
        "_2359": ["RingPinsToDiscConnection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
