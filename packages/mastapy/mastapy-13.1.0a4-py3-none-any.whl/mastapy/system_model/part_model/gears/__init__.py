"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2528 import ActiveCylindricalGearSetDesignSelection
    from ._2529 import ActiveGearSetDesignSelection
    from ._2530 import ActiveGearSetDesignSelectionGroup
    from ._2531 import AGMAGleasonConicalGear
    from ._2532 import AGMAGleasonConicalGearSet
    from ._2533 import BevelDifferentialGear
    from ._2534 import BevelDifferentialGearSet
    from ._2535 import BevelDifferentialPlanetGear
    from ._2536 import BevelDifferentialSunGear
    from ._2537 import BevelGear
    from ._2538 import BevelGearSet
    from ._2539 import ConceptGear
    from ._2540 import ConceptGearSet
    from ._2541 import ConicalGear
    from ._2542 import ConicalGearSet
    from ._2543 import CylindricalGear
    from ._2544 import CylindricalGearSet
    from ._2545 import CylindricalPlanetGear
    from ._2546 import FaceGear
    from ._2547 import FaceGearSet
    from ._2548 import Gear
    from ._2549 import GearOrientations
    from ._2550 import GearSet
    from ._2551 import GearSetConfiguration
    from ._2552 import HypoidGear
    from ._2553 import HypoidGearSet
    from ._2554 import KlingelnbergCycloPalloidConicalGear
    from ._2555 import KlingelnbergCycloPalloidConicalGearSet
    from ._2556 import KlingelnbergCycloPalloidHypoidGear
    from ._2557 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2558 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2559 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2560 import PlanetaryGearSet
    from ._2561 import SpiralBevelGear
    from ._2562 import SpiralBevelGearSet
    from ._2563 import StraightBevelDiffGear
    from ._2564 import StraightBevelDiffGearSet
    from ._2565 import StraightBevelGear
    from ._2566 import StraightBevelGearSet
    from ._2567 import StraightBevelPlanetGear
    from ._2568 import StraightBevelSunGear
    from ._2569 import WormGear
    from ._2570 import WormGearSet
    from ._2571 import ZerolBevelGear
    from ._2572 import ZerolBevelGearSet
else:
    import_structure = {
        "_2528": ["ActiveCylindricalGearSetDesignSelection"],
        "_2529": ["ActiveGearSetDesignSelection"],
        "_2530": ["ActiveGearSetDesignSelectionGroup"],
        "_2531": ["AGMAGleasonConicalGear"],
        "_2532": ["AGMAGleasonConicalGearSet"],
        "_2533": ["BevelDifferentialGear"],
        "_2534": ["BevelDifferentialGearSet"],
        "_2535": ["BevelDifferentialPlanetGear"],
        "_2536": ["BevelDifferentialSunGear"],
        "_2537": ["BevelGear"],
        "_2538": ["BevelGearSet"],
        "_2539": ["ConceptGear"],
        "_2540": ["ConceptGearSet"],
        "_2541": ["ConicalGear"],
        "_2542": ["ConicalGearSet"],
        "_2543": ["CylindricalGear"],
        "_2544": ["CylindricalGearSet"],
        "_2545": ["CylindricalPlanetGear"],
        "_2546": ["FaceGear"],
        "_2547": ["FaceGearSet"],
        "_2548": ["Gear"],
        "_2549": ["GearOrientations"],
        "_2550": ["GearSet"],
        "_2551": ["GearSetConfiguration"],
        "_2552": ["HypoidGear"],
        "_2553": ["HypoidGearSet"],
        "_2554": ["KlingelnbergCycloPalloidConicalGear"],
        "_2555": ["KlingelnbergCycloPalloidConicalGearSet"],
        "_2556": ["KlingelnbergCycloPalloidHypoidGear"],
        "_2557": ["KlingelnbergCycloPalloidHypoidGearSet"],
        "_2558": ["KlingelnbergCycloPalloidSpiralBevelGear"],
        "_2559": ["KlingelnbergCycloPalloidSpiralBevelGearSet"],
        "_2560": ["PlanetaryGearSet"],
        "_2561": ["SpiralBevelGear"],
        "_2562": ["SpiralBevelGearSet"],
        "_2563": ["StraightBevelDiffGear"],
        "_2564": ["StraightBevelDiffGearSet"],
        "_2565": ["StraightBevelGear"],
        "_2566": ["StraightBevelGearSet"],
        "_2567": ["StraightBevelPlanetGear"],
        "_2568": ["StraightBevelSunGear"],
        "_2569": ["WormGear"],
        "_2570": ["WormGearSet"],
        "_2571": ["ZerolBevelGear"],
        "_2572": ["ZerolBevelGearSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)
