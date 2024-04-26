"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2199 import AxialFeedJournalBearing
    from ._2200 import AxialGrooveJournalBearing
    from ._2201 import AxialHoleJournalBearing
    from ._2202 import CircumferentialFeedJournalBearing
    from ._2203 import CylindricalHousingJournalBearing
    from ._2204 import MachineryEncasedJournalBearing
    from ._2205 import PadFluidFilmBearing
    from ._2206 import PedestalJournalBearing
    from ._2207 import PlainGreaseFilledJournalBearing
    from ._2208 import PlainGreaseFilledJournalBearingHousingType
    from ._2209 import PlainJournalBearing
    from ._2210 import PlainJournalHousing
    from ._2211 import PlainOilFedJournalBearing
    from ._2212 import TiltingPadJournalBearing
    from ._2213 import TiltingPadThrustBearing
else:
    import_structure = {
        "_2199": ["AxialFeedJournalBearing"],
        "_2200": ["AxialGrooveJournalBearing"],
        "_2201": ["AxialHoleJournalBearing"],
        "_2202": ["CircumferentialFeedJournalBearing"],
        "_2203": ["CylindricalHousingJournalBearing"],
        "_2204": ["MachineryEncasedJournalBearing"],
        "_2205": ["PadFluidFilmBearing"],
        "_2206": ["PedestalJournalBearing"],
        "_2207": ["PlainGreaseFilledJournalBearing"],
        "_2208": ["PlainGreaseFilledJournalBearingHousingType"],
        "_2209": ["PlainJournalBearing"],
        "_2210": ["PlainJournalHousing"],
        "_2211": ["PlainOilFedJournalBearing"],
        "_2212": ["TiltingPadJournalBearing"],
        "_2213": ["TiltingPadThrustBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialFeedJournalBearing",
    "AxialGrooveJournalBearing",
    "AxialHoleJournalBearing",
    "CircumferentialFeedJournalBearing",
    "CylindricalHousingJournalBearing",
    "MachineryEncasedJournalBearing",
    "PadFluidFilmBearing",
    "PedestalJournalBearing",
    "PlainGreaseFilledJournalBearing",
    "PlainGreaseFilledJournalBearingHousingType",
    "PlainJournalBearing",
    "PlainJournalHousing",
    "PlainOilFedJournalBearing",
    "TiltingPadJournalBearing",
    "TiltingPadThrustBearing",
)
