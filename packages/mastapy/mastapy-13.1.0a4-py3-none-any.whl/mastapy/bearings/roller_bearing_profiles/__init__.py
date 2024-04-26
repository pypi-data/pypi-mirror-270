"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1944 import ProfileDataToUse
    from ._1945 import ProfileSet
    from ._1946 import ProfileToFit
    from ._1947 import RollerBearingConicalProfile
    from ._1948 import RollerBearingCrownedProfile
    from ._1949 import RollerBearingDinLundbergProfile
    from ._1950 import RollerBearingFlatProfile
    from ._1951 import RollerBearingJohnsGoharProfile
    from ._1952 import RollerBearingLundbergProfile
    from ._1953 import RollerBearingProfile
    from ._1954 import RollerBearingTangentialCrownedProfile
    from ._1955 import RollerBearingUserSpecifiedProfile
    from ._1956 import RollerRaceProfilePoint
    from ._1957 import UserSpecifiedProfilePoint
    from ._1958 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        "_1944": ["ProfileDataToUse"],
        "_1945": ["ProfileSet"],
        "_1946": ["ProfileToFit"],
        "_1947": ["RollerBearingConicalProfile"],
        "_1948": ["RollerBearingCrownedProfile"],
        "_1949": ["RollerBearingDinLundbergProfile"],
        "_1950": ["RollerBearingFlatProfile"],
        "_1951": ["RollerBearingJohnsGoharProfile"],
        "_1952": ["RollerBearingLundbergProfile"],
        "_1953": ["RollerBearingProfile"],
        "_1954": ["RollerBearingTangentialCrownedProfile"],
        "_1955": ["RollerBearingUserSpecifiedProfile"],
        "_1956": ["RollerRaceProfilePoint"],
        "_1957": ["UserSpecifiedProfilePoint"],
        "_1958": ["UserSpecifiedRollerRaceProfilePoint"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingTangentialCrownedProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
