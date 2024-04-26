"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2511 import AbstractShaftFromCAD
    from ._2512 import ClutchFromCAD
    from ._2513 import ComponentFromCAD
    from ._2514 import ConceptBearingFromCAD
    from ._2515 import ConnectorFromCAD
    from ._2516 import CylindricalGearFromCAD
    from ._2517 import CylindricalGearInPlanetarySetFromCAD
    from ._2518 import CylindricalPlanetGearFromCAD
    from ._2519 import CylindricalRingGearFromCAD
    from ._2520 import CylindricalSunGearFromCAD
    from ._2521 import HousedOrMounted
    from ._2522 import MountableComponentFromCAD
    from ._2523 import PlanetShaftFromCAD
    from ._2524 import PulleyFromCAD
    from ._2525 import RigidConnectorFromCAD
    from ._2526 import RollingBearingFromCAD
    from ._2527 import ShaftFromCAD
else:
    import_structure = {
        "_2511": ["AbstractShaftFromCAD"],
        "_2512": ["ClutchFromCAD"],
        "_2513": ["ComponentFromCAD"],
        "_2514": ["ConceptBearingFromCAD"],
        "_2515": ["ConnectorFromCAD"],
        "_2516": ["CylindricalGearFromCAD"],
        "_2517": ["CylindricalGearInPlanetarySetFromCAD"],
        "_2518": ["CylindricalPlanetGearFromCAD"],
        "_2519": ["CylindricalRingGearFromCAD"],
        "_2520": ["CylindricalSunGearFromCAD"],
        "_2521": ["HousedOrMounted"],
        "_2522": ["MountableComponentFromCAD"],
        "_2523": ["PlanetShaftFromCAD"],
        "_2524": ["PulleyFromCAD"],
        "_2525": ["RigidConnectorFromCAD"],
        "_2526": ["RollingBearingFromCAD"],
        "_2527": ["ShaftFromCAD"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)
