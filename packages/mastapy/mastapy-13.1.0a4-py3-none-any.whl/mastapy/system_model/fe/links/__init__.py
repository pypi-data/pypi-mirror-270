"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2436 import FELink
    from ._2437 import ElectricMachineStatorFELink
    from ._2438 import FELinkWithSelection
    from ._2439 import GearMeshFELink
    from ._2440 import GearWithDuplicatedMeshesFELink
    from ._2441 import MultiAngleConnectionFELink
    from ._2442 import MultiNodeConnectorFELink
    from ._2443 import MultiNodeFELink
    from ._2444 import PlanetaryConnectorMultiNodeFELink
    from ._2445 import PlanetBasedFELink
    from ._2446 import PlanetCarrierFELink
    from ._2447 import PointLoadFELink
    from ._2448 import RollingRingConnectionFELink
    from ._2449 import ShaftHubConnectionFELink
    from ._2450 import SingleNodeFELink
else:
    import_structure = {
        "_2436": ["FELink"],
        "_2437": ["ElectricMachineStatorFELink"],
        "_2438": ["FELinkWithSelection"],
        "_2439": ["GearMeshFELink"],
        "_2440": ["GearWithDuplicatedMeshesFELink"],
        "_2441": ["MultiAngleConnectionFELink"],
        "_2442": ["MultiNodeConnectorFELink"],
        "_2443": ["MultiNodeFELink"],
        "_2444": ["PlanetaryConnectorMultiNodeFELink"],
        "_2445": ["PlanetBasedFELink"],
        "_2446": ["PlanetCarrierFELink"],
        "_2447": ["PointLoadFELink"],
        "_2448": ["RollingRingConnectionFELink"],
        "_2449": ["ShaftHubConnectionFELink"],
        "_2450": ["SingleNodeFELink"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)
