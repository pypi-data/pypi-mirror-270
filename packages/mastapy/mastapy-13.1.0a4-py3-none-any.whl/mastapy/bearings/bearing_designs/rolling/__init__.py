"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2153 import AngularContactBallBearing
    from ._2154 import AngularContactThrustBallBearing
    from ._2155 import AsymmetricSphericalRollerBearing
    from ._2156 import AxialThrustCylindricalRollerBearing
    from ._2157 import AxialThrustNeedleRollerBearing
    from ._2158 import BallBearing
    from ._2159 import BallBearingShoulderDefinition
    from ._2160 import BarrelRollerBearing
    from ._2161 import BearingProtection
    from ._2162 import BearingProtectionDetailsModifier
    from ._2163 import BearingProtectionLevel
    from ._2164 import BearingTypeExtraInformation
    from ._2165 import CageBridgeShape
    from ._2166 import CrossedRollerBearing
    from ._2167 import CylindricalRollerBearing
    from ._2168 import DeepGrooveBallBearing
    from ._2169 import DiameterSeries
    from ._2170 import FatigueLoadLimitCalculationMethodEnum
    from ._2171 import FourPointContactAngleDefinition
    from ._2172 import FourPointContactBallBearing
    from ._2173 import GeometricConstants
    from ._2174 import GeometricConstantsForRollingFrictionalMoments
    from ._2175 import GeometricConstantsForSlidingFrictionalMoments
    from ._2176 import HeightSeries
    from ._2177 import MultiPointContactBallBearing
    from ._2178 import NeedleRollerBearing
    from ._2179 import NonBarrelRollerBearing
    from ._2180 import RollerBearing
    from ._2181 import RollerEndShape
    from ._2182 import RollerRibDetail
    from ._2183 import RollingBearing
    from ._2184 import SelfAligningBallBearing
    from ._2185 import SKFSealFrictionalMomentConstants
    from ._2186 import SleeveType
    from ._2187 import SphericalRollerBearing
    from ._2188 import SphericalRollerThrustBearing
    from ._2189 import TaperRollerBearing
    from ._2190 import ThreePointContactBallBearing
    from ._2191 import ThrustBallBearing
    from ._2192 import ToroidalRollerBearing
    from ._2193 import WidthSeries
else:
    import_structure = {
        "_2153": ["AngularContactBallBearing"],
        "_2154": ["AngularContactThrustBallBearing"],
        "_2155": ["AsymmetricSphericalRollerBearing"],
        "_2156": ["AxialThrustCylindricalRollerBearing"],
        "_2157": ["AxialThrustNeedleRollerBearing"],
        "_2158": ["BallBearing"],
        "_2159": ["BallBearingShoulderDefinition"],
        "_2160": ["BarrelRollerBearing"],
        "_2161": ["BearingProtection"],
        "_2162": ["BearingProtectionDetailsModifier"],
        "_2163": ["BearingProtectionLevel"],
        "_2164": ["BearingTypeExtraInformation"],
        "_2165": ["CageBridgeShape"],
        "_2166": ["CrossedRollerBearing"],
        "_2167": ["CylindricalRollerBearing"],
        "_2168": ["DeepGrooveBallBearing"],
        "_2169": ["DiameterSeries"],
        "_2170": ["FatigueLoadLimitCalculationMethodEnum"],
        "_2171": ["FourPointContactAngleDefinition"],
        "_2172": ["FourPointContactBallBearing"],
        "_2173": ["GeometricConstants"],
        "_2174": ["GeometricConstantsForRollingFrictionalMoments"],
        "_2175": ["GeometricConstantsForSlidingFrictionalMoments"],
        "_2176": ["HeightSeries"],
        "_2177": ["MultiPointContactBallBearing"],
        "_2178": ["NeedleRollerBearing"],
        "_2179": ["NonBarrelRollerBearing"],
        "_2180": ["RollerBearing"],
        "_2181": ["RollerEndShape"],
        "_2182": ["RollerRibDetail"],
        "_2183": ["RollingBearing"],
        "_2184": ["SelfAligningBallBearing"],
        "_2185": ["SKFSealFrictionalMomentConstants"],
        "_2186": ["SleeveType"],
        "_2187": ["SphericalRollerBearing"],
        "_2188": ["SphericalRollerThrustBearing"],
        "_2189": ["TaperRollerBearing"],
        "_2190": ["ThreePointContactBallBearing"],
        "_2191": ["ThrustBallBearing"],
        "_2192": ["ToroidalRollerBearing"],
        "_2193": ["WidthSeries"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
