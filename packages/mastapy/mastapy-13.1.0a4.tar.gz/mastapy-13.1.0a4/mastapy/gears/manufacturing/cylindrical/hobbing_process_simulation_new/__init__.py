"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._665 import ActiveProcessMethod
    from ._666 import AnalysisMethod
    from ._667 import CalculateLeadDeviationAccuracy
    from ._668 import CalculatePitchDeviationAccuracy
    from ._669 import CalculateProfileDeviationAccuracy
    from ._670 import CentreDistanceOffsetMethod
    from ._671 import CutterHeadSlideError
    from ._672 import GearMountingError
    from ._673 import HobbingProcessCalculation
    from ._674 import HobbingProcessGearShape
    from ._675 import HobbingProcessLeadCalculation
    from ._676 import HobbingProcessMarkOnShaft
    from ._677 import HobbingProcessPitchCalculation
    from ._678 import HobbingProcessProfileCalculation
    from ._679 import HobbingProcessSimulationInput
    from ._680 import HobbingProcessSimulationNew
    from ._681 import HobbingProcessSimulationViewModel
    from ._682 import HobbingProcessTotalModificationCalculation
    from ._683 import HobManufactureError
    from ._684 import HobResharpeningError
    from ._685 import ManufacturedQualityGrade
    from ._686 import MountingError
    from ._687 import ProcessCalculation
    from ._688 import ProcessGearShape
    from ._689 import ProcessLeadCalculation
    from ._690 import ProcessPitchCalculation
    from ._691 import ProcessProfileCalculation
    from ._692 import ProcessSimulationInput
    from ._693 import ProcessSimulationNew
    from ._694 import ProcessSimulationViewModel
    from ._695 import ProcessTotalModificationCalculation
    from ._696 import RackManufactureError
    from ._697 import RackMountingError
    from ._698 import WormGrinderManufactureError
    from ._699 import WormGrindingCutterCalculation
    from ._700 import WormGrindingLeadCalculation
    from ._701 import WormGrindingProcessCalculation
    from ._702 import WormGrindingProcessGearShape
    from ._703 import WormGrindingProcessMarkOnShaft
    from ._704 import WormGrindingProcessPitchCalculation
    from ._705 import WormGrindingProcessProfileCalculation
    from ._706 import WormGrindingProcessSimulationInput
    from ._707 import WormGrindingProcessSimulationNew
    from ._708 import WormGrindingProcessSimulationViewModel
    from ._709 import WormGrindingProcessTotalModificationCalculation
else:
    import_structure = {
        "_665": ["ActiveProcessMethod"],
        "_666": ["AnalysisMethod"],
        "_667": ["CalculateLeadDeviationAccuracy"],
        "_668": ["CalculatePitchDeviationAccuracy"],
        "_669": ["CalculateProfileDeviationAccuracy"],
        "_670": ["CentreDistanceOffsetMethod"],
        "_671": ["CutterHeadSlideError"],
        "_672": ["GearMountingError"],
        "_673": ["HobbingProcessCalculation"],
        "_674": ["HobbingProcessGearShape"],
        "_675": ["HobbingProcessLeadCalculation"],
        "_676": ["HobbingProcessMarkOnShaft"],
        "_677": ["HobbingProcessPitchCalculation"],
        "_678": ["HobbingProcessProfileCalculation"],
        "_679": ["HobbingProcessSimulationInput"],
        "_680": ["HobbingProcessSimulationNew"],
        "_681": ["HobbingProcessSimulationViewModel"],
        "_682": ["HobbingProcessTotalModificationCalculation"],
        "_683": ["HobManufactureError"],
        "_684": ["HobResharpeningError"],
        "_685": ["ManufacturedQualityGrade"],
        "_686": ["MountingError"],
        "_687": ["ProcessCalculation"],
        "_688": ["ProcessGearShape"],
        "_689": ["ProcessLeadCalculation"],
        "_690": ["ProcessPitchCalculation"],
        "_691": ["ProcessProfileCalculation"],
        "_692": ["ProcessSimulationInput"],
        "_693": ["ProcessSimulationNew"],
        "_694": ["ProcessSimulationViewModel"],
        "_695": ["ProcessTotalModificationCalculation"],
        "_696": ["RackManufactureError"],
        "_697": ["RackMountingError"],
        "_698": ["WormGrinderManufactureError"],
        "_699": ["WormGrindingCutterCalculation"],
        "_700": ["WormGrindingLeadCalculation"],
        "_701": ["WormGrindingProcessCalculation"],
        "_702": ["WormGrindingProcessGearShape"],
        "_703": ["WormGrindingProcessMarkOnShaft"],
        "_704": ["WormGrindingProcessPitchCalculation"],
        "_705": ["WormGrindingProcessProfileCalculation"],
        "_706": ["WormGrindingProcessSimulationInput"],
        "_707": ["WormGrindingProcessSimulationNew"],
        "_708": ["WormGrindingProcessSimulationViewModel"],
        "_709": ["WormGrindingProcessTotalModificationCalculation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProcessMethod",
    "AnalysisMethod",
    "CalculateLeadDeviationAccuracy",
    "CalculatePitchDeviationAccuracy",
    "CalculateProfileDeviationAccuracy",
    "CentreDistanceOffsetMethod",
    "CutterHeadSlideError",
    "GearMountingError",
    "HobbingProcessCalculation",
    "HobbingProcessGearShape",
    "HobbingProcessLeadCalculation",
    "HobbingProcessMarkOnShaft",
    "HobbingProcessPitchCalculation",
    "HobbingProcessProfileCalculation",
    "HobbingProcessSimulationInput",
    "HobbingProcessSimulationNew",
    "HobbingProcessSimulationViewModel",
    "HobbingProcessTotalModificationCalculation",
    "HobManufactureError",
    "HobResharpeningError",
    "ManufacturedQualityGrade",
    "MountingError",
    "ProcessCalculation",
    "ProcessGearShape",
    "ProcessLeadCalculation",
    "ProcessPitchCalculation",
    "ProcessProfileCalculation",
    "ProcessSimulationInput",
    "ProcessSimulationNew",
    "ProcessSimulationViewModel",
    "ProcessTotalModificationCalculation",
    "RackManufactureError",
    "RackMountingError",
    "WormGrinderManufactureError",
    "WormGrindingCutterCalculation",
    "WormGrindingLeadCalculation",
    "WormGrindingProcessCalculation",
    "WormGrindingProcessGearShape",
    "WormGrindingProcessMarkOnShaft",
    "WormGrindingProcessPitchCalculation",
    "WormGrindingProcessProfileCalculation",
    "WormGrindingProcessSimulationInput",
    "WormGrindingProcessSimulationNew",
    "WormGrindingProcessSimulationViewModel",
    "WormGrindingProcessTotalModificationCalculation",
)
