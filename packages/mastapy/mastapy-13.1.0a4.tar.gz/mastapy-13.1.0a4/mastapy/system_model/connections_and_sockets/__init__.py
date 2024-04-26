"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2283 import AbstractShaftToMountableComponentConnection
    from ._2284 import BearingInnerSocket
    from ._2285 import BearingOuterSocket
    from ._2286 import BeltConnection
    from ._2287 import CoaxialConnection
    from ._2288 import ComponentConnection
    from ._2289 import ComponentMeasurer
    from ._2290 import Connection
    from ._2291 import CVTBeltConnection
    from ._2292 import CVTPulleySocket
    from ._2293 import CylindricalComponentConnection
    from ._2294 import CylindricalSocket
    from ._2295 import DatumMeasurement
    from ._2296 import ElectricMachineStatorSocket
    from ._2297 import InnerShaftSocket
    from ._2298 import InnerShaftSocketBase
    from ._2299 import InterMountableComponentConnection
    from ._2300 import MountableComponentInnerSocket
    from ._2301 import MountableComponentOuterSocket
    from ._2302 import MountableComponentSocket
    from ._2303 import OuterShaftSocket
    from ._2304 import OuterShaftSocketBase
    from ._2305 import PlanetaryConnection
    from ._2306 import PlanetarySocket
    from ._2307 import PlanetarySocketBase
    from ._2308 import PulleySocket
    from ._2309 import RealignmentResult
    from ._2310 import RollingRingConnection
    from ._2311 import RollingRingSocket
    from ._2312 import ShaftSocket
    from ._2313 import ShaftToMountableComponentConnection
    from ._2314 import Socket
    from ._2315 import SocketConnectionOptions
    from ._2316 import SocketConnectionSelection
else:
    import_structure = {
        "_2283": ["AbstractShaftToMountableComponentConnection"],
        "_2284": ["BearingInnerSocket"],
        "_2285": ["BearingOuterSocket"],
        "_2286": ["BeltConnection"],
        "_2287": ["CoaxialConnection"],
        "_2288": ["ComponentConnection"],
        "_2289": ["ComponentMeasurer"],
        "_2290": ["Connection"],
        "_2291": ["CVTBeltConnection"],
        "_2292": ["CVTPulleySocket"],
        "_2293": ["CylindricalComponentConnection"],
        "_2294": ["CylindricalSocket"],
        "_2295": ["DatumMeasurement"],
        "_2296": ["ElectricMachineStatorSocket"],
        "_2297": ["InnerShaftSocket"],
        "_2298": ["InnerShaftSocketBase"],
        "_2299": ["InterMountableComponentConnection"],
        "_2300": ["MountableComponentInnerSocket"],
        "_2301": ["MountableComponentOuterSocket"],
        "_2302": ["MountableComponentSocket"],
        "_2303": ["OuterShaftSocket"],
        "_2304": ["OuterShaftSocketBase"],
        "_2305": ["PlanetaryConnection"],
        "_2306": ["PlanetarySocket"],
        "_2307": ["PlanetarySocketBase"],
        "_2308": ["PulleySocket"],
        "_2309": ["RealignmentResult"],
        "_2310": ["RollingRingConnection"],
        "_2311": ["RollingRingSocket"],
        "_2312": ["ShaftSocket"],
        "_2313": ["ShaftToMountableComponentConnection"],
        "_2314": ["Socket"],
        "_2315": ["SocketConnectionOptions"],
        "_2316": ["SocketConnectionSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
