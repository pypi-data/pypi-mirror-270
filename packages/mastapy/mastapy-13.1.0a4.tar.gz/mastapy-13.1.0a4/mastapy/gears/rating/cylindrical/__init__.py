"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._458 import AGMAScuffingResultsRow
    from ._459 import CylindricalGearDesignAndRatingSettings
    from ._460 import CylindricalGearDesignAndRatingSettingsDatabase
    from ._461 import CylindricalGearDesignAndRatingSettingsItem
    from ._462 import CylindricalGearDutyCycleRating
    from ._463 import CylindricalGearFlankDutyCycleRating
    from ._464 import CylindricalGearFlankRating
    from ._465 import CylindricalGearMeshRating
    from ._466 import CylindricalGearMicroPittingResults
    from ._467 import CylindricalGearRating
    from ._468 import CylindricalGearRatingGeometryDataSource
    from ._469 import CylindricalGearScuffingResults
    from ._470 import CylindricalGearSetDutyCycleRating
    from ._471 import CylindricalGearSetRating
    from ._472 import CylindricalGearSingleFlankRating
    from ._473 import CylindricalMeshDutyCycleRating
    from ._474 import CylindricalMeshSingleFlankRating
    from ._475 import CylindricalPlasticGearRatingSettings
    from ._476 import CylindricalPlasticGearRatingSettingsDatabase
    from ._477 import CylindricalPlasticGearRatingSettingsItem
    from ._478 import CylindricalRateableMesh
    from ._479 import DynamicFactorMethods
    from ._480 import GearBlankFactorCalculationOptions
    from ._481 import ISOScuffingResultsRow
    from ._482 import MeshRatingForReports
    from ._483 import MicropittingRatingMethod
    from ._484 import MicroPittingResultsRow
    from ._485 import MisalignmentContactPatternEnhancements
    from ._486 import RatingMethod
    from ._487 import ReducedCylindricalGearSetDutyCycleRating
    from ._488 import ScuffingFlashTemperatureRatingMethod
    from ._489 import ScuffingIntegralTemperatureRatingMethod
    from ._490 import ScuffingMethods
    from ._491 import ScuffingResultsRow
    from ._492 import ScuffingResultsRowGear
    from ._493 import TipReliefScuffingOptions
    from ._494 import ToothThicknesses
    from ._495 import VDI2737SafetyFactorReportingObject
else:
    import_structure = {
        "_458": ["AGMAScuffingResultsRow"],
        "_459": ["CylindricalGearDesignAndRatingSettings"],
        "_460": ["CylindricalGearDesignAndRatingSettingsDatabase"],
        "_461": ["CylindricalGearDesignAndRatingSettingsItem"],
        "_462": ["CylindricalGearDutyCycleRating"],
        "_463": ["CylindricalGearFlankDutyCycleRating"],
        "_464": ["CylindricalGearFlankRating"],
        "_465": ["CylindricalGearMeshRating"],
        "_466": ["CylindricalGearMicroPittingResults"],
        "_467": ["CylindricalGearRating"],
        "_468": ["CylindricalGearRatingGeometryDataSource"],
        "_469": ["CylindricalGearScuffingResults"],
        "_470": ["CylindricalGearSetDutyCycleRating"],
        "_471": ["CylindricalGearSetRating"],
        "_472": ["CylindricalGearSingleFlankRating"],
        "_473": ["CylindricalMeshDutyCycleRating"],
        "_474": ["CylindricalMeshSingleFlankRating"],
        "_475": ["CylindricalPlasticGearRatingSettings"],
        "_476": ["CylindricalPlasticGearRatingSettingsDatabase"],
        "_477": ["CylindricalPlasticGearRatingSettingsItem"],
        "_478": ["CylindricalRateableMesh"],
        "_479": ["DynamicFactorMethods"],
        "_480": ["GearBlankFactorCalculationOptions"],
        "_481": ["ISOScuffingResultsRow"],
        "_482": ["MeshRatingForReports"],
        "_483": ["MicropittingRatingMethod"],
        "_484": ["MicroPittingResultsRow"],
        "_485": ["MisalignmentContactPatternEnhancements"],
        "_486": ["RatingMethod"],
        "_487": ["ReducedCylindricalGearSetDutyCycleRating"],
        "_488": ["ScuffingFlashTemperatureRatingMethod"],
        "_489": ["ScuffingIntegralTemperatureRatingMethod"],
        "_490": ["ScuffingMethods"],
        "_491": ["ScuffingResultsRow"],
        "_492": ["ScuffingResultsRowGear"],
        "_493": ["TipReliefScuffingOptions"],
        "_494": ["ToothThicknesses"],
        "_495": ["VDI2737SafetyFactorReportingObject"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAScuffingResultsRow",
    "CylindricalGearDesignAndRatingSettings",
    "CylindricalGearDesignAndRatingSettingsDatabase",
    "CylindricalGearDesignAndRatingSettingsItem",
    "CylindricalGearDutyCycleRating",
    "CylindricalGearFlankDutyCycleRating",
    "CylindricalGearFlankRating",
    "CylindricalGearMeshRating",
    "CylindricalGearMicroPittingResults",
    "CylindricalGearRating",
    "CylindricalGearRatingGeometryDataSource",
    "CylindricalGearScuffingResults",
    "CylindricalGearSetDutyCycleRating",
    "CylindricalGearSetRating",
    "CylindricalGearSingleFlankRating",
    "CylindricalMeshDutyCycleRating",
    "CylindricalMeshSingleFlankRating",
    "CylindricalPlasticGearRatingSettings",
    "CylindricalPlasticGearRatingSettingsDatabase",
    "CylindricalPlasticGearRatingSettingsItem",
    "CylindricalRateableMesh",
    "DynamicFactorMethods",
    "GearBlankFactorCalculationOptions",
    "ISOScuffingResultsRow",
    "MeshRatingForReports",
    "MicropittingRatingMethod",
    "MicroPittingResultsRow",
    "MisalignmentContactPatternEnhancements",
    "RatingMethod",
    "ReducedCylindricalGearSetDutyCycleRating",
    "ScuffingFlashTemperatureRatingMethod",
    "ScuffingIntegralTemperatureRatingMethod",
    "ScuffingMethods",
    "ScuffingResultsRow",
    "ScuffingResultsRowGear",
    "TipReliefScuffingOptions",
    "ToothThicknesses",
    "VDI2737SafetyFactorReportingObject",
)
