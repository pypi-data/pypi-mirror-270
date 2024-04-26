"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1358 import BasicDynamicForceLoadCase
    from ._1359 import DynamicForceAnalysis
    from ._1360 import DynamicForceLoadCase
    from ._1361 import DynamicForcesOperatingPoint
    from ._1362 import EfficiencyMapAnalysis
    from ._1363 import EfficiencyMapLoadCase
    from ._1364 import ElectricMachineAnalysis
    from ._1365 import ElectricMachineBasicMechanicalLossSettings
    from ._1366 import ElectricMachineControlStrategy
    from ._1367 import ElectricMachineEfficiencyMapSettings
    from ._1368 import ElectricMachineFEAnalysis
    from ._1369 import ElectricMachineFEMechanicalAnalysis
    from ._1370 import ElectricMachineLoadCase
    from ._1371 import ElectricMachineLoadCaseBase
    from ._1372 import ElectricMachineLoadCaseGroup
    from ._1373 import ElectricMachineMechanicalLoadCase
    from ._1374 import EndWindingInductanceMethod
    from ._1375 import LeadingOrLagging
    from ._1376 import LoadCaseType
    from ._1377 import LoadCaseTypeSelector
    from ._1378 import MotoringOrGenerating
    from ._1379 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1380 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1381 import OperatingPointsSpecificationMethod
    from ._1382 import SingleOperatingPointAnalysis
    from ._1383 import SlotDetailForAnalysis
    from ._1384 import SpecifyTorqueOrCurrent
    from ._1385 import SpeedPointsDistribution
    from ._1386 import SpeedTorqueCurveAnalysis
    from ._1387 import SpeedTorqueCurveLoadCase
    from ._1388 import SpeedTorqueLoadCase
    from ._1389 import Temperatures
else:
    import_structure = {
        "_1358": ["BasicDynamicForceLoadCase"],
        "_1359": ["DynamicForceAnalysis"],
        "_1360": ["DynamicForceLoadCase"],
        "_1361": ["DynamicForcesOperatingPoint"],
        "_1362": ["EfficiencyMapAnalysis"],
        "_1363": ["EfficiencyMapLoadCase"],
        "_1364": ["ElectricMachineAnalysis"],
        "_1365": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1366": ["ElectricMachineControlStrategy"],
        "_1367": ["ElectricMachineEfficiencyMapSettings"],
        "_1368": ["ElectricMachineFEAnalysis"],
        "_1369": ["ElectricMachineFEMechanicalAnalysis"],
        "_1370": ["ElectricMachineLoadCase"],
        "_1371": ["ElectricMachineLoadCaseBase"],
        "_1372": ["ElectricMachineLoadCaseGroup"],
        "_1373": ["ElectricMachineMechanicalLoadCase"],
        "_1374": ["EndWindingInductanceMethod"],
        "_1375": ["LeadingOrLagging"],
        "_1376": ["LoadCaseType"],
        "_1377": ["LoadCaseTypeSelector"],
        "_1378": ["MotoringOrGenerating"],
        "_1379": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1380": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1381": ["OperatingPointsSpecificationMethod"],
        "_1382": ["SingleOperatingPointAnalysis"],
        "_1383": ["SlotDetailForAnalysis"],
        "_1384": ["SpecifyTorqueOrCurrent"],
        "_1385": ["SpeedPointsDistribution"],
        "_1386": ["SpeedTorqueCurveAnalysis"],
        "_1387": ["SpeedTorqueCurveLoadCase"],
        "_1388": ["SpeedTorqueLoadCase"],
        "_1389": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
