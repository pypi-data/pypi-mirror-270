"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7015 import AdditionalForcesObtainedFrom
    from ._7016 import BoostPressureLoadCaseInputOptions
    from ._7017 import DesignStateOptions
    from ._7018 import DestinationDesignState
    from ._7019 import ForceInputOptions
    from ._7020 import GearRatioInputOptions
    from ._7021 import LoadCaseNameOptions
    from ._7022 import MomentInputOptions
    from ._7023 import MultiTimeSeriesDataInputFileOptions
    from ._7024 import PointLoadInputOptions
    from ._7025 import PowerLoadInputOptions
    from ._7026 import RampOrSteadyStateInputOptions
    from ._7027 import SpeedInputOptions
    from ._7028 import TimeSeriesImporter
    from ._7029 import TimeStepInputOptions
    from ._7030 import TorqueInputOptions
    from ._7031 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_7015": ["AdditionalForcesObtainedFrom"],
        "_7016": ["BoostPressureLoadCaseInputOptions"],
        "_7017": ["DesignStateOptions"],
        "_7018": ["DestinationDesignState"],
        "_7019": ["ForceInputOptions"],
        "_7020": ["GearRatioInputOptions"],
        "_7021": ["LoadCaseNameOptions"],
        "_7022": ["MomentInputOptions"],
        "_7023": ["MultiTimeSeriesDataInputFileOptions"],
        "_7024": ["PointLoadInputOptions"],
        "_7025": ["PowerLoadInputOptions"],
        "_7026": ["RampOrSteadyStateInputOptions"],
        "_7027": ["SpeedInputOptions"],
        "_7028": ["TimeSeriesImporter"],
        "_7029": ["TimeStepInputOptions"],
        "_7030": ["TorqueInputOptions"],
        "_7031": ["TorqueValuesObtainedFrom"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)
