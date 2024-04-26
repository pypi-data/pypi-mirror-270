"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._321 import AccuracyGrades
    from ._322 import AGMAToleranceStandard
    from ._323 import BevelHypoidGearDesignSettings
    from ._324 import BevelHypoidGearRatingSettings
    from ._325 import CentreDistanceChangeMethod
    from ._326 import CoefficientOfFrictionCalculationMethod
    from ._327 import ConicalGearToothSurface
    from ._328 import ContactRatioDataSource
    from ._329 import ContactRatioRequirements
    from ._330 import CylindricalFlanks
    from ._331 import CylindricalMisalignmentDataSource
    from ._332 import DeflectionFromBendingOption
    from ._333 import GearFlanks
    from ._334 import GearNURBSSurface
    from ._335 import GearSetDesignGroup
    from ._336 import GearSetModes
    from ._337 import GearSetOptimisationResult
    from ._338 import GearSetOptimisationResults
    from ._339 import GearSetOptimiser
    from ._340 import Hand
    from ._341 import ISOToleranceStandard
    from ._342 import LubricationMethods
    from ._343 import MicroGeometryInputTypes
    from ._344 import MicroGeometryModel
    from ._345 import MicropittingCoefficientOfFrictionCalculationMethod
    from ._346 import NamedPlanetAngle
    from ._347 import PlanetaryDetail
    from ._348 import PlanetaryRatingLoadSharingOption
    from ._349 import PocketingPowerLossCoefficients
    from ._350 import PocketingPowerLossCoefficientsDatabase
    from ._351 import QualityGradeTypes
    from ._352 import SafetyRequirementsAGMA
    from ._353 import SpecificationForTheEffectOfOilKinematicViscosity
    from ._354 import SpiralBevelRootLineTilt
    from ._355 import SpiralBevelToothTaper
    from ._356 import TESpecificationType
    from ._357 import WormAddendumFactor
    from ._358 import WormType
    from ._359 import ZerolBevelGleasonToothTaperOption
else:
    import_structure = {
        "_321": ["AccuracyGrades"],
        "_322": ["AGMAToleranceStandard"],
        "_323": ["BevelHypoidGearDesignSettings"],
        "_324": ["BevelHypoidGearRatingSettings"],
        "_325": ["CentreDistanceChangeMethod"],
        "_326": ["CoefficientOfFrictionCalculationMethod"],
        "_327": ["ConicalGearToothSurface"],
        "_328": ["ContactRatioDataSource"],
        "_329": ["ContactRatioRequirements"],
        "_330": ["CylindricalFlanks"],
        "_331": ["CylindricalMisalignmentDataSource"],
        "_332": ["DeflectionFromBendingOption"],
        "_333": ["GearFlanks"],
        "_334": ["GearNURBSSurface"],
        "_335": ["GearSetDesignGroup"],
        "_336": ["GearSetModes"],
        "_337": ["GearSetOptimisationResult"],
        "_338": ["GearSetOptimisationResults"],
        "_339": ["GearSetOptimiser"],
        "_340": ["Hand"],
        "_341": ["ISOToleranceStandard"],
        "_342": ["LubricationMethods"],
        "_343": ["MicroGeometryInputTypes"],
        "_344": ["MicroGeometryModel"],
        "_345": ["MicropittingCoefficientOfFrictionCalculationMethod"],
        "_346": ["NamedPlanetAngle"],
        "_347": ["PlanetaryDetail"],
        "_348": ["PlanetaryRatingLoadSharingOption"],
        "_349": ["PocketingPowerLossCoefficients"],
        "_350": ["PocketingPowerLossCoefficientsDatabase"],
        "_351": ["QualityGradeTypes"],
        "_352": ["SafetyRequirementsAGMA"],
        "_353": ["SpecificationForTheEffectOfOilKinematicViscosity"],
        "_354": ["SpiralBevelRootLineTilt"],
        "_355": ["SpiralBevelToothTaper"],
        "_356": ["TESpecificationType"],
        "_357": ["WormAddendumFactor"],
        "_358": ["WormType"],
        "_359": ["ZerolBevelGleasonToothTaperOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AccuracyGrades",
    "AGMAToleranceStandard",
    "BevelHypoidGearDesignSettings",
    "BevelHypoidGearRatingSettings",
    "CentreDistanceChangeMethod",
    "CoefficientOfFrictionCalculationMethod",
    "ConicalGearToothSurface",
    "ContactRatioDataSource",
    "ContactRatioRequirements",
    "CylindricalFlanks",
    "CylindricalMisalignmentDataSource",
    "DeflectionFromBendingOption",
    "GearFlanks",
    "GearNURBSSurface",
    "GearSetDesignGroup",
    "GearSetModes",
    "GearSetOptimisationResult",
    "GearSetOptimisationResults",
    "GearSetOptimiser",
    "Hand",
    "ISOToleranceStandard",
    "LubricationMethods",
    "MicroGeometryInputTypes",
    "MicroGeometryModel",
    "MicropittingCoefficientOfFrictionCalculationMethod",
    "NamedPlanetAngle",
    "PlanetaryDetail",
    "PlanetaryRatingLoadSharingOption",
    "PocketingPowerLossCoefficients",
    "PocketingPowerLossCoefficientsDatabase",
    "QualityGradeTypes",
    "SafetyRequirementsAGMA",
    "SpecificationForTheEffectOfOilKinematicViscosity",
    "SpiralBevelRootLineTilt",
    "SpiralBevelToothTaper",
    "TESpecificationType",
    "WormAddendumFactor",
    "WormType",
    "ZerolBevelGleasonToothTaperOption",
)
