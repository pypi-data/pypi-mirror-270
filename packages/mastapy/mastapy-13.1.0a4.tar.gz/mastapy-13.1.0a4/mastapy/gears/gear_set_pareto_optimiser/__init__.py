"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._909 import BarForPareto
    from ._910 import CandidateDisplayChoice
    from ._911 import ChartInfoBase
    from ._912 import CylindricalGearSetParetoOptimiser
    from ._913 import DesignSpaceSearchBase
    from ._914 import DesignSpaceSearchCandidateBase
    from ._915 import FaceGearSetParetoOptimiser
    from ._916 import GearNameMapper
    from ._917 import GearNamePicker
    from ._918 import GearSetOptimiserCandidate
    from ._919 import GearSetParetoOptimiser
    from ._920 import HypoidGearSetParetoOptimiser
    from ._921 import InputSliderForPareto
    from ._922 import LargerOrSmaller
    from ._923 import MicroGeometryDesignSpaceSearch
    from ._924 import MicroGeometryDesignSpaceSearchCandidate
    from ._925 import MicroGeometryDesignSpaceSearchChartInformation
    from ._926 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._927 import MicroGeometryGearSetDesignSpaceSearch
    from ._928 import MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
    from ._929 import MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
    from ._930 import OptimisationTarget
    from ._931 import ParetoConicalRatingOptimisationStrategyDatabase
    from ._932 import ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
    from ._933 import ParetoCylindricalGearSetOptimisationStrategyDatabase
    from ._934 import ParetoCylindricalRatingOptimisationStrategyDatabase
    from ._935 import ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
    from ._936 import ParetoFaceGearSetOptimisationStrategyDatabase
    from ._937 import ParetoFaceRatingOptimisationStrategyDatabase
    from ._938 import ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
    from ._939 import ParetoHypoidGearSetOptimisationStrategyDatabase
    from ._940 import ParetoOptimiserChartInformation
    from ._941 import ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._942 import ParetoSpiralBevelGearSetOptimisationStrategyDatabase
    from ._943 import ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._944 import ParetoStraightBevelGearSetOptimisationStrategyDatabase
    from ._945 import ReasonsForInvalidDesigns
    from ._946 import SpiralBevelGearSetParetoOptimiser
    from ._947 import StraightBevelGearSetParetoOptimiser
else:
    import_structure = {
        "_909": ["BarForPareto"],
        "_910": ["CandidateDisplayChoice"],
        "_911": ["ChartInfoBase"],
        "_912": ["CylindricalGearSetParetoOptimiser"],
        "_913": ["DesignSpaceSearchBase"],
        "_914": ["DesignSpaceSearchCandidateBase"],
        "_915": ["FaceGearSetParetoOptimiser"],
        "_916": ["GearNameMapper"],
        "_917": ["GearNamePicker"],
        "_918": ["GearSetOptimiserCandidate"],
        "_919": ["GearSetParetoOptimiser"],
        "_920": ["HypoidGearSetParetoOptimiser"],
        "_921": ["InputSliderForPareto"],
        "_922": ["LargerOrSmaller"],
        "_923": ["MicroGeometryDesignSpaceSearch"],
        "_924": ["MicroGeometryDesignSpaceSearchCandidate"],
        "_925": ["MicroGeometryDesignSpaceSearchChartInformation"],
        "_926": ["MicroGeometryDesignSpaceSearchStrategyDatabase"],
        "_927": ["MicroGeometryGearSetDesignSpaceSearch"],
        "_928": ["MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"],
        "_929": ["MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"],
        "_930": ["OptimisationTarget"],
        "_931": ["ParetoConicalRatingOptimisationStrategyDatabase"],
        "_932": ["ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"],
        "_933": ["ParetoCylindricalGearSetOptimisationStrategyDatabase"],
        "_934": ["ParetoCylindricalRatingOptimisationStrategyDatabase"],
        "_935": ["ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase"],
        "_936": ["ParetoFaceGearSetOptimisationStrategyDatabase"],
        "_937": ["ParetoFaceRatingOptimisationStrategyDatabase"],
        "_938": ["ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase"],
        "_939": ["ParetoHypoidGearSetOptimisationStrategyDatabase"],
        "_940": ["ParetoOptimiserChartInformation"],
        "_941": ["ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_942": ["ParetoSpiralBevelGearSetOptimisationStrategyDatabase"],
        "_943": ["ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_944": ["ParetoStraightBevelGearSetOptimisationStrategyDatabase"],
        "_945": ["ReasonsForInvalidDesigns"],
        "_946": ["SpiralBevelGearSetParetoOptimiser"],
        "_947": ["StraightBevelGearSetParetoOptimiser"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BarForPareto",
    "CandidateDisplayChoice",
    "ChartInfoBase",
    "CylindricalGearSetParetoOptimiser",
    "DesignSpaceSearchBase",
    "DesignSpaceSearchCandidateBase",
    "FaceGearSetParetoOptimiser",
    "GearNameMapper",
    "GearNamePicker",
    "GearSetOptimiserCandidate",
    "GearSetParetoOptimiser",
    "HypoidGearSetParetoOptimiser",
    "InputSliderForPareto",
    "LargerOrSmaller",
    "MicroGeometryDesignSpaceSearch",
    "MicroGeometryDesignSpaceSearchCandidate",
    "MicroGeometryDesignSpaceSearchChartInformation",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDesignSpaceSearch",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    "OptimisationTarget",
    "ParetoConicalRatingOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
    "ParetoCylindricalRatingOptimisationStrategyDatabase",
    "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
    "ParetoFaceRatingOptimisationStrategyDatabase",
    "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoHypoidGearSetOptimisationStrategyDatabase",
    "ParetoOptimiserChartInformation",
    "ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
    "ReasonsForInvalidDesigns",
    "SpiralBevelGearSetParetoOptimiser",
    "StraightBevelGearSetParetoOptimiser",
)
