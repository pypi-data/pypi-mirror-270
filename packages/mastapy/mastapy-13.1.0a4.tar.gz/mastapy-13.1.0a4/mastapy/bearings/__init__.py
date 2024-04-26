"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1886 import BearingCatalog
    from ._1887 import BasicDynamicLoadRatingCalculationMethod
    from ._1888 import BasicStaticLoadRatingCalculationMethod
    from ._1889 import BearingCageMaterial
    from ._1890 import BearingDampingMatrixOption
    from ._1891 import BearingLoadCaseResultsForPST
    from ._1892 import BearingLoadCaseResultsLightweight
    from ._1893 import BearingMeasurementType
    from ._1894 import BearingModel
    from ._1895 import BearingRow
    from ._1896 import BearingSettings
    from ._1897 import BearingSettingsDatabase
    from ._1898 import BearingSettingsItem
    from ._1899 import BearingStiffnessMatrixOption
    from ._1900 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1901 import FluidFilmTemperatureOptions
    from ._1902 import HybridSteelAll
    from ._1903 import JournalBearingType
    from ._1904 import JournalOilFeedType
    from ._1905 import MountingPointSurfaceFinishes
    from ._1906 import OuterRingMounting
    from ._1907 import RatingLife
    from ._1908 import RollerBearingProfileTypes
    from ._1909 import RollingBearingArrangement
    from ._1910 import RollingBearingDatabase
    from ._1911 import RollingBearingKey
    from ._1912 import RollingBearingRaceType
    from ._1913 import RollingBearingType
    from ._1914 import RotationalDirections
    from ._1915 import SealLocation
    from ._1916 import SKFSettings
    from ._1917 import TiltingPadTypes
else:
    import_structure = {
        "_1886": ["BearingCatalog"],
        "_1887": ["BasicDynamicLoadRatingCalculationMethod"],
        "_1888": ["BasicStaticLoadRatingCalculationMethod"],
        "_1889": ["BearingCageMaterial"],
        "_1890": ["BearingDampingMatrixOption"],
        "_1891": ["BearingLoadCaseResultsForPST"],
        "_1892": ["BearingLoadCaseResultsLightweight"],
        "_1893": ["BearingMeasurementType"],
        "_1894": ["BearingModel"],
        "_1895": ["BearingRow"],
        "_1896": ["BearingSettings"],
        "_1897": ["BearingSettingsDatabase"],
        "_1898": ["BearingSettingsItem"],
        "_1899": ["BearingStiffnessMatrixOption"],
        "_1900": ["ExponentAndReductionFactorsInISO16281Calculation"],
        "_1901": ["FluidFilmTemperatureOptions"],
        "_1902": ["HybridSteelAll"],
        "_1903": ["JournalBearingType"],
        "_1904": ["JournalOilFeedType"],
        "_1905": ["MountingPointSurfaceFinishes"],
        "_1906": ["OuterRingMounting"],
        "_1907": ["RatingLife"],
        "_1908": ["RollerBearingProfileTypes"],
        "_1909": ["RollingBearingArrangement"],
        "_1910": ["RollingBearingDatabase"],
        "_1911": ["RollingBearingKey"],
        "_1912": ["RollingBearingRaceType"],
        "_1913": ["RollingBearingType"],
        "_1914": ["RotationalDirections"],
        "_1915": ["SealLocation"],
        "_1916": ["SKFSettings"],
        "_1917": ["TiltingPadTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingCatalog",
    "BasicDynamicLoadRatingCalculationMethod",
    "BasicStaticLoadRatingCalculationMethod",
    "BearingCageMaterial",
    "BearingDampingMatrixOption",
    "BearingLoadCaseResultsForPST",
    "BearingLoadCaseResultsLightweight",
    "BearingMeasurementType",
    "BearingModel",
    "BearingRow",
    "BearingSettings",
    "BearingSettingsDatabase",
    "BearingSettingsItem",
    "BearingStiffnessMatrixOption",
    "ExponentAndReductionFactorsInISO16281Calculation",
    "FluidFilmTemperatureOptions",
    "HybridSteelAll",
    "JournalBearingType",
    "JournalOilFeedType",
    "MountingPointSurfaceFinishes",
    "OuterRingMounting",
    "RatingLife",
    "RollerBearingProfileTypes",
    "RollingBearingArrangement",
    "RollingBearingDatabase",
    "RollingBearingKey",
    "RollingBearingRaceType",
    "RollingBearingType",
    "RotationalDirections",
    "SealLocation",
    "SKFSettings",
    "TiltingPadTypes",
)
