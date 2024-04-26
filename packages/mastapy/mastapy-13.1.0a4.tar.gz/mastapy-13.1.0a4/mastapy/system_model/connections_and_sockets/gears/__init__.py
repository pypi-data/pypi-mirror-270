"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2317 import AGMAGleasonConicalGearMesh
    from ._2318 import AGMAGleasonConicalGearTeethSocket
    from ._2319 import BevelDifferentialGearMesh
    from ._2320 import BevelDifferentialGearTeethSocket
    from ._2321 import BevelGearMesh
    from ._2322 import BevelGearTeethSocket
    from ._2323 import ConceptGearMesh
    from ._2324 import ConceptGearTeethSocket
    from ._2325 import ConicalGearMesh
    from ._2326 import ConicalGearTeethSocket
    from ._2327 import CylindricalGearMesh
    from ._2328 import CylindricalGearTeethSocket
    from ._2329 import FaceGearMesh
    from ._2330 import FaceGearTeethSocket
    from ._2331 import GearMesh
    from ._2332 import GearTeethSocket
    from ._2333 import HypoidGearMesh
    from ._2334 import HypoidGearTeethSocket
    from ._2335 import KlingelnbergConicalGearTeethSocket
    from ._2336 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2337 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2338 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2339 import KlingelnbergHypoidGearTeethSocket
    from ._2340 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2341 import SpiralBevelGearMesh
    from ._2342 import SpiralBevelGearTeethSocket
    from ._2343 import StraightBevelDiffGearMesh
    from ._2344 import StraightBevelDiffGearTeethSocket
    from ._2345 import StraightBevelGearMesh
    from ._2346 import StraightBevelGearTeethSocket
    from ._2347 import WormGearMesh
    from ._2348 import WormGearTeethSocket
    from ._2349 import ZerolBevelGearMesh
    from ._2350 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        "_2317": ["AGMAGleasonConicalGearMesh"],
        "_2318": ["AGMAGleasonConicalGearTeethSocket"],
        "_2319": ["BevelDifferentialGearMesh"],
        "_2320": ["BevelDifferentialGearTeethSocket"],
        "_2321": ["BevelGearMesh"],
        "_2322": ["BevelGearTeethSocket"],
        "_2323": ["ConceptGearMesh"],
        "_2324": ["ConceptGearTeethSocket"],
        "_2325": ["ConicalGearMesh"],
        "_2326": ["ConicalGearTeethSocket"],
        "_2327": ["CylindricalGearMesh"],
        "_2328": ["CylindricalGearTeethSocket"],
        "_2329": ["FaceGearMesh"],
        "_2330": ["FaceGearTeethSocket"],
        "_2331": ["GearMesh"],
        "_2332": ["GearTeethSocket"],
        "_2333": ["HypoidGearMesh"],
        "_2334": ["HypoidGearTeethSocket"],
        "_2335": ["KlingelnbergConicalGearTeethSocket"],
        "_2336": ["KlingelnbergCycloPalloidConicalGearMesh"],
        "_2337": ["KlingelnbergCycloPalloidHypoidGearMesh"],
        "_2338": ["KlingelnbergCycloPalloidSpiralBevelGearMesh"],
        "_2339": ["KlingelnbergHypoidGearTeethSocket"],
        "_2340": ["KlingelnbergSpiralBevelGearTeethSocket"],
        "_2341": ["SpiralBevelGearMesh"],
        "_2342": ["SpiralBevelGearTeethSocket"],
        "_2343": ["StraightBevelDiffGearMesh"],
        "_2344": ["StraightBevelDiffGearTeethSocket"],
        "_2345": ["StraightBevelGearMesh"],
        "_2346": ["StraightBevelGearTeethSocket"],
        "_2347": ["WormGearMesh"],
        "_2348": ["WormGearTeethSocket"],
        "_2349": ["ZerolBevelGearMesh"],
        "_2350": ["ZerolBevelGearTeethSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMesh",
    "AGMAGleasonConicalGearTeethSocket",
    "BevelDifferentialGearMesh",
    "BevelDifferentialGearTeethSocket",
    "BevelGearMesh",
    "BevelGearTeethSocket",
    "ConceptGearMesh",
    "ConceptGearTeethSocket",
    "ConicalGearMesh",
    "ConicalGearTeethSocket",
    "CylindricalGearMesh",
    "CylindricalGearTeethSocket",
    "FaceGearMesh",
    "FaceGearTeethSocket",
    "GearMesh",
    "GearTeethSocket",
    "HypoidGearMesh",
    "HypoidGearTeethSocket",
    "KlingelnbergConicalGearTeethSocket",
    "KlingelnbergCycloPalloidConicalGearMesh",
    "KlingelnbergCycloPalloidHypoidGearMesh",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
    "KlingelnbergHypoidGearTeethSocket",
    "KlingelnbergSpiralBevelGearTeethSocket",
    "SpiralBevelGearMesh",
    "SpiralBevelGearTeethSocket",
    "StraightBevelDiffGearMesh",
    "StraightBevelDiffGearTeethSocket",
    "StraightBevelGearMesh",
    "StraightBevelGearTeethSocket",
    "WormGearMesh",
    "WormGearTeethSocket",
    "ZerolBevelGearMesh",
    "ZerolBevelGearTeethSocket",
)
