"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2573 import BoostPressureInputOptions
    from ._2574 import InputPowerInputOptions
    from ._2575 import PressureRatioInputOptions
    from ._2576 import RotorSetDataInputFileOptions
    from ._2577 import RotorSetMeasuredPoint
    from ._2578 import RotorSpeedInputOptions
    from ._2579 import SuperchargerMap
    from ._2580 import SuperchargerMaps
    from ._2581 import SuperchargerRotorSet
    from ._2582 import SuperchargerRotorSetDatabase
    from ._2583 import YVariableForImportedData
else:
    import_structure = {
        "_2573": ["BoostPressureInputOptions"],
        "_2574": ["InputPowerInputOptions"],
        "_2575": ["PressureRatioInputOptions"],
        "_2576": ["RotorSetDataInputFileOptions"],
        "_2577": ["RotorSetMeasuredPoint"],
        "_2578": ["RotorSpeedInputOptions"],
        "_2579": ["SuperchargerMap"],
        "_2580": ["SuperchargerMaps"],
        "_2581": ["SuperchargerRotorSet"],
        "_2582": ["SuperchargerRotorSetDatabase"],
        "_2583": ["YVariableForImportedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)
