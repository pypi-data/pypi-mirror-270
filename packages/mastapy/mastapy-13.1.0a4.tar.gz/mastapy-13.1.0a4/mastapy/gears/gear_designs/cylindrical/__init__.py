"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1006 import AddendumModificationDistributionRule
    from ._1007 import BacklashSpecification
    from ._1008 import BasicRackProfiles
    from ._1009 import CaseHardeningProperties
    from ._1010 import CreateNewSuitableCutterOption
    from ._1011 import CrossedAxisCylindricalGearPair
    from ._1012 import CrossedAxisCylindricalGearPairLineContact
    from ._1013 import CrossedAxisCylindricalGearPairPointContact
    from ._1014 import CylindricalGearAbstractRack
    from ._1015 import CylindricalGearAbstractRackFlank
    from ._1016 import CylindricalGearBasicRack
    from ._1017 import CylindricalGearBasicRackFlank
    from ._1018 import CylindricalGearCuttingOptions
    from ._1019 import CylindricalGearDefaults
    from ._1020 import CylindricalGearDesign
    from ._1021 import CylindricalGearDesignConstraint
    from ._1022 import CylindricalGearDesignConstraints
    from ._1023 import CylindricalGearDesignConstraintsDatabase
    from ._1024 import CylindricalGearDesignConstraintSettings
    from ._1025 import CylindricalGearFlankDesign
    from ._1026 import CylindricalGearMeshDesign
    from ._1027 import CylindricalGearMeshFlankDesign
    from ._1028 import CylindricalGearMicroGeometrySettings
    from ._1029 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1030 import CylindricalGearMicroGeometrySettingsItem
    from ._1031 import CylindricalGearPinionTypeCutter
    from ._1032 import CylindricalGearPinionTypeCutterFlank
    from ._1033 import CylindricalGearProfileMeasurement
    from ._1034 import CylindricalGearProfileMeasurementType
    from ._1035 import CylindricalGearProfileModifications
    from ._1036 import CylindricalGearSetDesign
    from ._1037 import CylindricalGearSetFlankDesign
    from ._1038 import CylindricalGearSetMacroGeometryOptimiser
    from ._1039 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1040 import CylindricalGearSetMicroGeometrySettings
    from ._1041 import CylindricalGearSetOptimisationWrapper
    from ._1042 import CylindricalGearTableMGItemDetail
    from ._1043 import CylindricalGearTableWithMGCharts
    from ._1044 import CylindricalGearToothThicknessSpecification
    from ._1045 import CylindricalMeshAngularBacklash
    from ._1046 import CylindricalMeshedGear
    from ._1047 import CylindricalMeshedGearFlank
    from ._1048 import CylindricalMeshLinearBacklashSpecification
    from ._1049 import CylindricalPlanetaryGearSetDesign
    from ._1050 import CylindricalPlanetGearDesign
    from ._1051 import DIN3967AllowanceSeries
    from ._1052 import DIN3967ToleranceSeries
    from ._1053 import DoubleAxisScaleAndRange
    from ._1054 import FinishToothThicknessDesignSpecification
    from ._1055 import GearFitSystems
    from ._1056 import GearManufacturingConfigSetupViewModel
    from ._1057 import GearSetManufacturingConfigurationSetup
    from ._1058 import GeometrySpecificationType
    from ._1059 import HardenedMaterialProperties
    from ._1060 import HardnessProfileCalculationMethod
    from ._1061 import HeatTreatmentType
    from ._1062 import ISO6336Geometry
    from ._1063 import ISO6336GeometryBase
    from ._1064 import ISO6336GeometryForShapedGears
    from ._1065 import ISO6336GeometryManufactured
    from ._1066 import LinearBacklashSpecification
    from ._1067 import LTCALoadCaseModifiableSettings
    from ._1068 import LTCASettings
    from ._1069 import MicroGeometryConvention
    from ._1070 import MicroGeometryProfileConvention
    from ._1071 import Micropitting
    from ._1072 import MullerResidualStressDefinition
    from ._1073 import NamedPlanetAssemblyIndex
    from ._1074 import NamedPlanetSideBandAmplitudeFactor
    from ._1075 import ReadonlyToothThicknessSpecification
    from ._1076 import RelativeMeasurementViewModel
    from ._1077 import RelativeValuesSpecification
    from ._1078 import ResidualStressCalculationMethod
    from ._1079 import RootStressSurfaceChartOption
    from ._1080 import Scuffing
    from ._1081 import ScuffingCoefficientOfFrictionMethods
    from ._1082 import ScuffingTemperatureMethodsAGMA
    from ._1083 import ScuffingTemperatureMethodsISO
    from ._1084 import ShaperEdgeTypes
    from ._1085 import SpurGearLoadSharingCodes
    from ._1086 import StandardRack
    from ._1087 import StandardRackFlank
    from ._1088 import SurfaceRoughness
    from ._1089 import ThicknessType
    from ._1090 import TiffAnalysisSettings
    from ._1091 import TipAlterationCoefficientMethod
    from ._1092 import TolerancedMetalMeasurements
    from ._1093 import TolerancedValueSpecification
    from ._1094 import ToothFlankFractureAnalysisSettings
    from ._1095 import ToothThicknessSpecification
    from ._1096 import ToothThicknessSpecificationBase
    from ._1097 import TypeOfMechanismHousing
    from ._1098 import Usage
else:
    import_structure = {
        "_1006": ["AddendumModificationDistributionRule"],
        "_1007": ["BacklashSpecification"],
        "_1008": ["BasicRackProfiles"],
        "_1009": ["CaseHardeningProperties"],
        "_1010": ["CreateNewSuitableCutterOption"],
        "_1011": ["CrossedAxisCylindricalGearPair"],
        "_1012": ["CrossedAxisCylindricalGearPairLineContact"],
        "_1013": ["CrossedAxisCylindricalGearPairPointContact"],
        "_1014": ["CylindricalGearAbstractRack"],
        "_1015": ["CylindricalGearAbstractRackFlank"],
        "_1016": ["CylindricalGearBasicRack"],
        "_1017": ["CylindricalGearBasicRackFlank"],
        "_1018": ["CylindricalGearCuttingOptions"],
        "_1019": ["CylindricalGearDefaults"],
        "_1020": ["CylindricalGearDesign"],
        "_1021": ["CylindricalGearDesignConstraint"],
        "_1022": ["CylindricalGearDesignConstraints"],
        "_1023": ["CylindricalGearDesignConstraintsDatabase"],
        "_1024": ["CylindricalGearDesignConstraintSettings"],
        "_1025": ["CylindricalGearFlankDesign"],
        "_1026": ["CylindricalGearMeshDesign"],
        "_1027": ["CylindricalGearMeshFlankDesign"],
        "_1028": ["CylindricalGearMicroGeometrySettings"],
        "_1029": ["CylindricalGearMicroGeometrySettingsDatabase"],
        "_1030": ["CylindricalGearMicroGeometrySettingsItem"],
        "_1031": ["CylindricalGearPinionTypeCutter"],
        "_1032": ["CylindricalGearPinionTypeCutterFlank"],
        "_1033": ["CylindricalGearProfileMeasurement"],
        "_1034": ["CylindricalGearProfileMeasurementType"],
        "_1035": ["CylindricalGearProfileModifications"],
        "_1036": ["CylindricalGearSetDesign"],
        "_1037": ["CylindricalGearSetFlankDesign"],
        "_1038": ["CylindricalGearSetMacroGeometryOptimiser"],
        "_1039": ["CylindricalGearSetManufacturingConfigurationSelection"],
        "_1040": ["CylindricalGearSetMicroGeometrySettings"],
        "_1041": ["CylindricalGearSetOptimisationWrapper"],
        "_1042": ["CylindricalGearTableMGItemDetail"],
        "_1043": ["CylindricalGearTableWithMGCharts"],
        "_1044": ["CylindricalGearToothThicknessSpecification"],
        "_1045": ["CylindricalMeshAngularBacklash"],
        "_1046": ["CylindricalMeshedGear"],
        "_1047": ["CylindricalMeshedGearFlank"],
        "_1048": ["CylindricalMeshLinearBacklashSpecification"],
        "_1049": ["CylindricalPlanetaryGearSetDesign"],
        "_1050": ["CylindricalPlanetGearDesign"],
        "_1051": ["DIN3967AllowanceSeries"],
        "_1052": ["DIN3967ToleranceSeries"],
        "_1053": ["DoubleAxisScaleAndRange"],
        "_1054": ["FinishToothThicknessDesignSpecification"],
        "_1055": ["GearFitSystems"],
        "_1056": ["GearManufacturingConfigSetupViewModel"],
        "_1057": ["GearSetManufacturingConfigurationSetup"],
        "_1058": ["GeometrySpecificationType"],
        "_1059": ["HardenedMaterialProperties"],
        "_1060": ["HardnessProfileCalculationMethod"],
        "_1061": ["HeatTreatmentType"],
        "_1062": ["ISO6336Geometry"],
        "_1063": ["ISO6336GeometryBase"],
        "_1064": ["ISO6336GeometryForShapedGears"],
        "_1065": ["ISO6336GeometryManufactured"],
        "_1066": ["LinearBacklashSpecification"],
        "_1067": ["LTCALoadCaseModifiableSettings"],
        "_1068": ["LTCASettings"],
        "_1069": ["MicroGeometryConvention"],
        "_1070": ["MicroGeometryProfileConvention"],
        "_1071": ["Micropitting"],
        "_1072": ["MullerResidualStressDefinition"],
        "_1073": ["NamedPlanetAssemblyIndex"],
        "_1074": ["NamedPlanetSideBandAmplitudeFactor"],
        "_1075": ["ReadonlyToothThicknessSpecification"],
        "_1076": ["RelativeMeasurementViewModel"],
        "_1077": ["RelativeValuesSpecification"],
        "_1078": ["ResidualStressCalculationMethod"],
        "_1079": ["RootStressSurfaceChartOption"],
        "_1080": ["Scuffing"],
        "_1081": ["ScuffingCoefficientOfFrictionMethods"],
        "_1082": ["ScuffingTemperatureMethodsAGMA"],
        "_1083": ["ScuffingTemperatureMethodsISO"],
        "_1084": ["ShaperEdgeTypes"],
        "_1085": ["SpurGearLoadSharingCodes"],
        "_1086": ["StandardRack"],
        "_1087": ["StandardRackFlank"],
        "_1088": ["SurfaceRoughness"],
        "_1089": ["ThicknessType"],
        "_1090": ["TiffAnalysisSettings"],
        "_1091": ["TipAlterationCoefficientMethod"],
        "_1092": ["TolerancedMetalMeasurements"],
        "_1093": ["TolerancedValueSpecification"],
        "_1094": ["ToothFlankFractureAnalysisSettings"],
        "_1095": ["ToothThicknessSpecification"],
        "_1096": ["ToothThicknessSpecificationBase"],
        "_1097": ["TypeOfMechanismHousing"],
        "_1098": ["Usage"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddendumModificationDistributionRule",
    "BacklashSpecification",
    "BasicRackProfiles",
    "CaseHardeningProperties",
    "CreateNewSuitableCutterOption",
    "CrossedAxisCylindricalGearPair",
    "CrossedAxisCylindricalGearPairLineContact",
    "CrossedAxisCylindricalGearPairPointContact",
    "CylindricalGearAbstractRack",
    "CylindricalGearAbstractRackFlank",
    "CylindricalGearBasicRack",
    "CylindricalGearBasicRackFlank",
    "CylindricalGearCuttingOptions",
    "CylindricalGearDefaults",
    "CylindricalGearDesign",
    "CylindricalGearDesignConstraint",
    "CylindricalGearDesignConstraints",
    "CylindricalGearDesignConstraintsDatabase",
    "CylindricalGearDesignConstraintSettings",
    "CylindricalGearFlankDesign",
    "CylindricalGearMeshDesign",
    "CylindricalGearMeshFlankDesign",
    "CylindricalGearMicroGeometrySettings",
    "CylindricalGearMicroGeometrySettingsDatabase",
    "CylindricalGearMicroGeometrySettingsItem",
    "CylindricalGearPinionTypeCutter",
    "CylindricalGearPinionTypeCutterFlank",
    "CylindricalGearProfileMeasurement",
    "CylindricalGearProfileMeasurementType",
    "CylindricalGearProfileModifications",
    "CylindricalGearSetDesign",
    "CylindricalGearSetFlankDesign",
    "CylindricalGearSetMacroGeometryOptimiser",
    "CylindricalGearSetManufacturingConfigurationSelection",
    "CylindricalGearSetMicroGeometrySettings",
    "CylindricalGearSetOptimisationWrapper",
    "CylindricalGearTableMGItemDetail",
    "CylindricalGearTableWithMGCharts",
    "CylindricalGearToothThicknessSpecification",
    "CylindricalMeshAngularBacklash",
    "CylindricalMeshedGear",
    "CylindricalMeshedGearFlank",
    "CylindricalMeshLinearBacklashSpecification",
    "CylindricalPlanetaryGearSetDesign",
    "CylindricalPlanetGearDesign",
    "DIN3967AllowanceSeries",
    "DIN3967ToleranceSeries",
    "DoubleAxisScaleAndRange",
    "FinishToothThicknessDesignSpecification",
    "GearFitSystems",
    "GearManufacturingConfigSetupViewModel",
    "GearSetManufacturingConfigurationSetup",
    "GeometrySpecificationType",
    "HardenedMaterialProperties",
    "HardnessProfileCalculationMethod",
    "HeatTreatmentType",
    "ISO6336Geometry",
    "ISO6336GeometryBase",
    "ISO6336GeometryForShapedGears",
    "ISO6336GeometryManufactured",
    "LinearBacklashSpecification",
    "LTCALoadCaseModifiableSettings",
    "LTCASettings",
    "MicroGeometryConvention",
    "MicroGeometryProfileConvention",
    "Micropitting",
    "MullerResidualStressDefinition",
    "NamedPlanetAssemblyIndex",
    "NamedPlanetSideBandAmplitudeFactor",
    "ReadonlyToothThicknessSpecification",
    "RelativeMeasurementViewModel",
    "RelativeValuesSpecification",
    "ResidualStressCalculationMethod",
    "RootStressSurfaceChartOption",
    "Scuffing",
    "ScuffingCoefficientOfFrictionMethods",
    "ScuffingTemperatureMethodsAGMA",
    "ScuffingTemperatureMethodsISO",
    "ShaperEdgeTypes",
    "SpurGearLoadSharingCodes",
    "StandardRack",
    "StandardRackFlank",
    "SurfaceRoughness",
    "ThicknessType",
    "TiffAnalysisSettings",
    "TipAlterationCoefficientMethod",
    "TolerancedMetalMeasurements",
    "TolerancedValueSpecification",
    "ToothFlankFractureAnalysisSettings",
    "ToothThicknessSpecification",
    "ToothThicknessSpecificationBase",
    "TypeOfMechanismHousing",
    "Usage",
)
