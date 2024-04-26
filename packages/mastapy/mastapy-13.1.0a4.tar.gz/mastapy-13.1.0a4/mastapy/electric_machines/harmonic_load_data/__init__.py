"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1390 import ElectricMachineHarmonicLoadDataBase
    from ._1391 import ForceDisplayOption
    from ._1392 import HarmonicLoadDataBase
    from ._1393 import HarmonicLoadDataControlExcitationOptionBase
    from ._1394 import HarmonicLoadDataType
    from ._1395 import SpeedDependentHarmonicLoadData
    from ._1396 import StatorToothInterpolator
    from ._1397 import StatorToothLoadInterpolator
    from ._1398 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1390": ["ElectricMachineHarmonicLoadDataBase"],
        "_1391": ["ForceDisplayOption"],
        "_1392": ["HarmonicLoadDataBase"],
        "_1393": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1394": ["HarmonicLoadDataType"],
        "_1395": ["SpeedDependentHarmonicLoadData"],
        "_1396": ["StatorToothInterpolator"],
        "_1397": ["StatorToothLoadInterpolator"],
        "_1398": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
