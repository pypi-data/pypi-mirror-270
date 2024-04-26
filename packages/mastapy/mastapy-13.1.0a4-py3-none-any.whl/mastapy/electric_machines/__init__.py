"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1253 import AbstractStator
    from ._1254 import AbstractToothAndSlot
    from ._1255 import AirGapPartition
    from ._1256 import CADConductor
    from ._1257 import CADElectricMachineDetail
    from ._1258 import CADMagnetDetails
    from ._1259 import CADMagnetsForLayer
    from ._1260 import CADRotor
    from ._1261 import CADStator
    from ._1262 import CADToothAndSlot
    from ._1263 import Coil
    from ._1264 import CoilPositionInSlot
    from ._1265 import CoolingDuctLayerSpecification
    from ._1266 import CoolingDuctShape
    from ._1267 import CoreLossBuildFactorSpecificationMethod
    from ._1268 import CoreLossCoefficients
    from ._1269 import DoubleLayerWindingSlotPositions
    from ._1270 import DQAxisConvention
    from ._1271 import Eccentricity
    from ._1272 import ElectricMachineDetail
    from ._1273 import ElectricMachineDetailInitialInformation
    from ._1274 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1275 import ElectricMachineMeshingOptions
    from ._1276 import ElectricMachineMeshingOptionsBase
    from ._1277 import ElectricMachineSetup
    from ._1278 import ElectricMachineType
    from ._1279 import FillFactorSpecificationMethod
    from ._1280 import FluxBarriers
    from ._1281 import FluxBarrierOrWeb
    from ._1282 import FluxBarrierStyle
    from ._1283 import HairpinConductor
    from ._1284 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1285 import IndividualConductorSpecificationSource
    from ._1286 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1287 import InteriorPermanentMagnetMachine
    from ._1288 import IronLossCoefficientSpecificationMethod
    from ._1289 import MagnetClearance
    from ._1290 import MagnetConfiguration
    from ._1291 import MagnetData
    from ._1292 import MagnetDesign
    from ._1293 import MagnetForLayer
    from ._1294 import MagnetisationDirection
    from ._1295 import MagnetMaterial
    from ._1296 import MagnetMaterialDatabase
    from ._1297 import MotorRotorSideFaceDetail
    from ._1298 import NonCADElectricMachineDetail
    from ._1299 import NotchShape
    from ._1300 import NotchSpecification
    from ._1301 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1302 import PermanentMagnetRotor
    from ._1303 import Phase
    from ._1304 import RegionID
    from ._1305 import Rotor
    from ._1306 import RotorInternalLayerSpecification
    from ._1307 import RotorSkewSlice
    from ._1308 import RotorType
    from ._1309 import SingleOrDoubleLayerWindings
    from ._1310 import SlotSectionDetail
    from ._1311 import Stator
    from ._1312 import StatorCutOutSpecification
    from ._1313 import StatorRotorMaterial
    from ._1314 import StatorRotorMaterialDatabase
    from ._1315 import SurfacePermanentMagnetMachine
    from ._1316 import SurfacePermanentMagnetRotor
    from ._1317 import SynchronousReluctanceMachine
    from ._1318 import ToothAndSlot
    from ._1319 import ToothSlotStyle
    from ._1320 import ToothTaperSpecification
    from ._1321 import TwoDimensionalFEModelForAnalysis
    from ._1322 import UShapedLayerSpecification
    from ._1323 import VShapedMagnetLayerSpecification
    from ._1324 import WindingConductor
    from ._1325 import WindingConnection
    from ._1326 import WindingMaterial
    from ._1327 import WindingMaterialDatabase
    from ._1328 import Windings
    from ._1329 import WindingsViewer
    from ._1330 import WindingType
    from ._1331 import WireSizeSpecificationMethod
    from ._1332 import WoundFieldSynchronousMachine
else:
    import_structure = {
        "_1253": ["AbstractStator"],
        "_1254": ["AbstractToothAndSlot"],
        "_1255": ["AirGapPartition"],
        "_1256": ["CADConductor"],
        "_1257": ["CADElectricMachineDetail"],
        "_1258": ["CADMagnetDetails"],
        "_1259": ["CADMagnetsForLayer"],
        "_1260": ["CADRotor"],
        "_1261": ["CADStator"],
        "_1262": ["CADToothAndSlot"],
        "_1263": ["Coil"],
        "_1264": ["CoilPositionInSlot"],
        "_1265": ["CoolingDuctLayerSpecification"],
        "_1266": ["CoolingDuctShape"],
        "_1267": ["CoreLossBuildFactorSpecificationMethod"],
        "_1268": ["CoreLossCoefficients"],
        "_1269": ["DoubleLayerWindingSlotPositions"],
        "_1270": ["DQAxisConvention"],
        "_1271": ["Eccentricity"],
        "_1272": ["ElectricMachineDetail"],
        "_1273": ["ElectricMachineDetailInitialInformation"],
        "_1274": ["ElectricMachineMechanicalAnalysisMeshingOptions"],
        "_1275": ["ElectricMachineMeshingOptions"],
        "_1276": ["ElectricMachineMeshingOptionsBase"],
        "_1277": ["ElectricMachineSetup"],
        "_1278": ["ElectricMachineType"],
        "_1279": ["FillFactorSpecificationMethod"],
        "_1280": ["FluxBarriers"],
        "_1281": ["FluxBarrierOrWeb"],
        "_1282": ["FluxBarrierStyle"],
        "_1283": ["HairpinConductor"],
        "_1284": ["HarmonicLoadDataControlExcitationOptionForElectricMachineMode"],
        "_1285": ["IndividualConductorSpecificationSource"],
        "_1286": ["InteriorPermanentMagnetAndSynchronousReluctanceRotor"],
        "_1287": ["InteriorPermanentMagnetMachine"],
        "_1288": ["IronLossCoefficientSpecificationMethod"],
        "_1289": ["MagnetClearance"],
        "_1290": ["MagnetConfiguration"],
        "_1291": ["MagnetData"],
        "_1292": ["MagnetDesign"],
        "_1293": ["MagnetForLayer"],
        "_1294": ["MagnetisationDirection"],
        "_1295": ["MagnetMaterial"],
        "_1296": ["MagnetMaterialDatabase"],
        "_1297": ["MotorRotorSideFaceDetail"],
        "_1298": ["NonCADElectricMachineDetail"],
        "_1299": ["NotchShape"],
        "_1300": ["NotchSpecification"],
        "_1301": ["PermanentMagnetAssistedSynchronousReluctanceMachine"],
        "_1302": ["PermanentMagnetRotor"],
        "_1303": ["Phase"],
        "_1304": ["RegionID"],
        "_1305": ["Rotor"],
        "_1306": ["RotorInternalLayerSpecification"],
        "_1307": ["RotorSkewSlice"],
        "_1308": ["RotorType"],
        "_1309": ["SingleOrDoubleLayerWindings"],
        "_1310": ["SlotSectionDetail"],
        "_1311": ["Stator"],
        "_1312": ["StatorCutOutSpecification"],
        "_1313": ["StatorRotorMaterial"],
        "_1314": ["StatorRotorMaterialDatabase"],
        "_1315": ["SurfacePermanentMagnetMachine"],
        "_1316": ["SurfacePermanentMagnetRotor"],
        "_1317": ["SynchronousReluctanceMachine"],
        "_1318": ["ToothAndSlot"],
        "_1319": ["ToothSlotStyle"],
        "_1320": ["ToothTaperSpecification"],
        "_1321": ["TwoDimensionalFEModelForAnalysis"],
        "_1322": ["UShapedLayerSpecification"],
        "_1323": ["VShapedMagnetLayerSpecification"],
        "_1324": ["WindingConductor"],
        "_1325": ["WindingConnection"],
        "_1326": ["WindingMaterial"],
        "_1327": ["WindingMaterialDatabase"],
        "_1328": ["Windings"],
        "_1329": ["WindingsViewer"],
        "_1330": ["WindingType"],
        "_1331": ["WireSizeSpecificationMethod"],
        "_1332": ["WoundFieldSynchronousMachine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "AirGapPartition",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADMagnetDetails",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FillFactorSpecificationMethod",
    "FluxBarriers",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetData",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetisationDirection",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutOutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
)
