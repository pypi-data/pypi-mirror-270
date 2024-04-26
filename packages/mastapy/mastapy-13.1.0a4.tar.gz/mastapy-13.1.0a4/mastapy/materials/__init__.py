"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._243 import AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
    from ._244 import AcousticRadiationEfficiency
    from ._245 import AcousticRadiationEfficiencyInputType
    from ._246 import AGMALubricantType
    from ._247 import AGMAMaterialApplications
    from ._248 import AGMAMaterialClasses
    from ._249 import AGMAMaterialGrade
    from ._250 import AirProperties
    from ._251 import BearingLubricationCondition
    from ._252 import BearingMaterial
    from ._253 import BearingMaterialDatabase
    from ._254 import BHCurveExtrapolationMethod
    from ._255 import BHCurveSpecification
    from ._256 import ComponentMaterialDatabase
    from ._257 import CompositeFatigueSafetyFactorItem
    from ._258 import CylindricalGearRatingMethods
    from ._259 import DensitySpecificationMethod
    from ._260 import FatigueSafetyFactorItem
    from ._261 import FatigueSafetyFactorItemBase
    from ._262 import GearingTypes
    from ._263 import GeneralTransmissionProperties
    from ._264 import GreaseContaminationOptions
    from ._265 import HardnessType
    from ._266 import ISO76StaticSafetyFactorLimits
    from ._267 import ISOLubricantType
    from ._268 import LubricantDefinition
    from ._269 import LubricantDelivery
    from ._270 import LubricantViscosityClassAGMA
    from ._271 import LubricantViscosityClassification
    from ._272 import LubricantViscosityClassISO
    from ._273 import LubricantViscosityClassSAE
    from ._274 import LubricationDetail
    from ._275 import LubricationDetailDatabase
    from ._276 import Material
    from ._277 import MaterialDatabase
    from ._278 import MaterialsSettings
    from ._279 import MaterialsSettingsDatabase
    from ._280 import MaterialsSettingsItem
    from ._281 import MaterialStandards
    from ._282 import MetalPlasticType
    from ._283 import OilFiltrationOptions
    from ._284 import PressureViscosityCoefficientMethod
    from ._285 import QualityGrade
    from ._286 import SafetyFactorGroup
    from ._287 import SafetyFactorItem
    from ._288 import SNCurve
    from ._289 import SNCurvePoint
    from ._290 import SoundPressureEnclosure
    from ._291 import SoundPressureEnclosureType
    from ._292 import StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial
    from ._293 import StressCyclesDataForTheContactSNCurveOfAPlasticMaterial
    from ._294 import TransmissionApplications
    from ._295 import VDI2736LubricantType
    from ._296 import VehicleDynamicsProperties
    from ._297 import WindTurbineStandards
    from ._298 import WorkingCharacteristics
else:
    import_structure = {
        "_243": ["AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"],
        "_244": ["AcousticRadiationEfficiency"],
        "_245": ["AcousticRadiationEfficiencyInputType"],
        "_246": ["AGMALubricantType"],
        "_247": ["AGMAMaterialApplications"],
        "_248": ["AGMAMaterialClasses"],
        "_249": ["AGMAMaterialGrade"],
        "_250": ["AirProperties"],
        "_251": ["BearingLubricationCondition"],
        "_252": ["BearingMaterial"],
        "_253": ["BearingMaterialDatabase"],
        "_254": ["BHCurveExtrapolationMethod"],
        "_255": ["BHCurveSpecification"],
        "_256": ["ComponentMaterialDatabase"],
        "_257": ["CompositeFatigueSafetyFactorItem"],
        "_258": ["CylindricalGearRatingMethods"],
        "_259": ["DensitySpecificationMethod"],
        "_260": ["FatigueSafetyFactorItem"],
        "_261": ["FatigueSafetyFactorItemBase"],
        "_262": ["GearingTypes"],
        "_263": ["GeneralTransmissionProperties"],
        "_264": ["GreaseContaminationOptions"],
        "_265": ["HardnessType"],
        "_266": ["ISO76StaticSafetyFactorLimits"],
        "_267": ["ISOLubricantType"],
        "_268": ["LubricantDefinition"],
        "_269": ["LubricantDelivery"],
        "_270": ["LubricantViscosityClassAGMA"],
        "_271": ["LubricantViscosityClassification"],
        "_272": ["LubricantViscosityClassISO"],
        "_273": ["LubricantViscosityClassSAE"],
        "_274": ["LubricationDetail"],
        "_275": ["LubricationDetailDatabase"],
        "_276": ["Material"],
        "_277": ["MaterialDatabase"],
        "_278": ["MaterialsSettings"],
        "_279": ["MaterialsSettingsDatabase"],
        "_280": ["MaterialsSettingsItem"],
        "_281": ["MaterialStandards"],
        "_282": ["MetalPlasticType"],
        "_283": ["OilFiltrationOptions"],
        "_284": ["PressureViscosityCoefficientMethod"],
        "_285": ["QualityGrade"],
        "_286": ["SafetyFactorGroup"],
        "_287": ["SafetyFactorItem"],
        "_288": ["SNCurve"],
        "_289": ["SNCurvePoint"],
        "_290": ["SoundPressureEnclosure"],
        "_291": ["SoundPressureEnclosureType"],
        "_292": ["StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial"],
        "_293": ["StressCyclesDataForTheContactSNCurveOfAPlasticMaterial"],
        "_294": ["TransmissionApplications"],
        "_295": ["VDI2736LubricantType"],
        "_296": ["VehicleDynamicsProperties"],
        "_297": ["WindTurbineStandards"],
        "_298": ["WorkingCharacteristics"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
    "AcousticRadiationEfficiency",
    "AcousticRadiationEfficiencyInputType",
    "AGMALubricantType",
    "AGMAMaterialApplications",
    "AGMAMaterialClasses",
    "AGMAMaterialGrade",
    "AirProperties",
    "BearingLubricationCondition",
    "BearingMaterial",
    "BearingMaterialDatabase",
    "BHCurveExtrapolationMethod",
    "BHCurveSpecification",
    "ComponentMaterialDatabase",
    "CompositeFatigueSafetyFactorItem",
    "CylindricalGearRatingMethods",
    "DensitySpecificationMethod",
    "FatigueSafetyFactorItem",
    "FatigueSafetyFactorItemBase",
    "GearingTypes",
    "GeneralTransmissionProperties",
    "GreaseContaminationOptions",
    "HardnessType",
    "ISO76StaticSafetyFactorLimits",
    "ISOLubricantType",
    "LubricantDefinition",
    "LubricantDelivery",
    "LubricantViscosityClassAGMA",
    "LubricantViscosityClassification",
    "LubricantViscosityClassISO",
    "LubricantViscosityClassSAE",
    "LubricationDetail",
    "LubricationDetailDatabase",
    "Material",
    "MaterialDatabase",
    "MaterialsSettings",
    "MaterialsSettingsDatabase",
    "MaterialsSettingsItem",
    "MaterialStandards",
    "MetalPlasticType",
    "OilFiltrationOptions",
    "PressureViscosityCoefficientMethod",
    "QualityGrade",
    "SafetyFactorGroup",
    "SafetyFactorItem",
    "SNCurve",
    "SNCurvePoint",
    "SoundPressureEnclosure",
    "SoundPressureEnclosureType",
    "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
    "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
    "TransmissionApplications",
    "VDI2736LubricantType",
    "VehicleDynamicsProperties",
    "WindTurbineStandards",
    "WorkingCharacteristics",
)
