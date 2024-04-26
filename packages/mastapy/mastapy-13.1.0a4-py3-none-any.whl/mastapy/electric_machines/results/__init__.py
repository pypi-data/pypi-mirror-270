"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1333 import DynamicForceResults
    from ._1334 import EfficiencyResults
    from ._1335 import ElectricMachineDQModel
    from ._1336 import ElectricMachineMechanicalResults
    from ._1337 import ElectricMachineMechanicalResultsViewable
    from ._1338 import ElectricMachineResults
    from ._1339 import ElectricMachineResultsForConductorTurn
    from ._1340 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1341 import ElectricMachineResultsForLineToLine
    from ._1342 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1343 import ElectricMachineResultsForPhase
    from ._1344 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1345 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1346 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1347 import ElectricMachineResultsTimeStep
    from ._1348 import ElectricMachineResultsTimeStepAtLocation
    from ._1349 import ElectricMachineResultsViewable
    from ._1350 import ElectricMachineForceViewOptions
    from ._1352 import LinearDQModel
    from ._1353 import MaximumTorqueResultsPoints
    from ._1354 import NonLinearDQModel
    from ._1355 import NonLinearDQModelGeneratorSettings
    from ._1356 import OnLoadElectricMachineResults
    from ._1357 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1333": ["DynamicForceResults"],
        "_1334": ["EfficiencyResults"],
        "_1335": ["ElectricMachineDQModel"],
        "_1336": ["ElectricMachineMechanicalResults"],
        "_1337": ["ElectricMachineMechanicalResultsViewable"],
        "_1338": ["ElectricMachineResults"],
        "_1339": ["ElectricMachineResultsForConductorTurn"],
        "_1340": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1341": ["ElectricMachineResultsForLineToLine"],
        "_1342": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1343": ["ElectricMachineResultsForPhase"],
        "_1344": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1345": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1346": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1347": ["ElectricMachineResultsTimeStep"],
        "_1348": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1349": ["ElectricMachineResultsViewable"],
        "_1350": ["ElectricMachineForceViewOptions"],
        "_1352": ["LinearDQModel"],
        "_1353": ["MaximumTorqueResultsPoints"],
        "_1354": ["NonLinearDQModel"],
        "_1355": ["NonLinearDQModelGeneratorSettings"],
        "_1356": ["OnLoadElectricMachineResults"],
        "_1357": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)
