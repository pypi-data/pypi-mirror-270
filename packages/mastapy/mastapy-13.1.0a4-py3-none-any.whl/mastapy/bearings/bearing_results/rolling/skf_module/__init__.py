"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2094 import AdjustedSpeed
    from ._2095 import AdjustmentFactors
    from ._2096 import BearingLoads
    from ._2097 import BearingRatingLife
    from ._2098 import DynamicAxialLoadCarryingCapacity
    from ._2099 import Frequencies
    from ._2100 import FrequencyOfOverRolling
    from ._2101 import Friction
    from ._2102 import FrictionalMoment
    from ._2103 import FrictionSources
    from ._2104 import Grease
    from ._2105 import GreaseLifeAndRelubricationInterval
    from ._2106 import GreaseQuantity
    from ._2107 import InitialFill
    from ._2108 import LifeModel
    from ._2109 import MinimumLoad
    from ._2110 import OperatingViscosity
    from ._2111 import PermissibleAxialLoad
    from ._2112 import RotationalFrequency
    from ._2113 import SKFAuthentication
    from ._2114 import SKFCalculationResult
    from ._2115 import SKFCredentials
    from ._2116 import SKFModuleResults
    from ._2117 import StaticSafetyFactors
    from ._2118 import Viscosities
else:
    import_structure = {
        "_2094": ["AdjustedSpeed"],
        "_2095": ["AdjustmentFactors"],
        "_2096": ["BearingLoads"],
        "_2097": ["BearingRatingLife"],
        "_2098": ["DynamicAxialLoadCarryingCapacity"],
        "_2099": ["Frequencies"],
        "_2100": ["FrequencyOfOverRolling"],
        "_2101": ["Friction"],
        "_2102": ["FrictionalMoment"],
        "_2103": ["FrictionSources"],
        "_2104": ["Grease"],
        "_2105": ["GreaseLifeAndRelubricationInterval"],
        "_2106": ["GreaseQuantity"],
        "_2107": ["InitialFill"],
        "_2108": ["LifeModel"],
        "_2109": ["MinimumLoad"],
        "_2110": ["OperatingViscosity"],
        "_2111": ["PermissibleAxialLoad"],
        "_2112": ["RotationalFrequency"],
        "_2113": ["SKFAuthentication"],
        "_2114": ["SKFCalculationResult"],
        "_2115": ["SKFCredentials"],
        "_2116": ["SKFModuleResults"],
        "_2117": ["StaticSafetyFactors"],
        "_2118": ["Viscosities"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdjustedSpeed",
    "AdjustmentFactors",
    "BearingLoads",
    "BearingRatingLife",
    "DynamicAxialLoadCarryingCapacity",
    "Frequencies",
    "FrequencyOfOverRolling",
    "Friction",
    "FrictionalMoment",
    "FrictionSources",
    "Grease",
    "GreaseLifeAndRelubricationInterval",
    "GreaseQuantity",
    "InitialFill",
    "LifeModel",
    "MinimumLoad",
    "OperatingViscosity",
    "PermissibleAxialLoad",
    "RotationalFrequency",
    "SKFAuthentication",
    "SKFCalculationResult",
    "SKFCredentials",
    "SKFModuleResults",
    "StaticSafetyFactors",
    "Viscosities",
)
