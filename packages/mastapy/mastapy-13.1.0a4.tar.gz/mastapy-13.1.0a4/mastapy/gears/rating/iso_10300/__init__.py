"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._427 import GeneralLoadFactorCalculationMethod
    from ._428 import Iso10300FinishingMethods
    from ._429 import ISO10300MeshSingleFlankRating
    from ._430 import ISO10300MeshSingleFlankRatingBevelMethodB2
    from ._431 import ISO10300MeshSingleFlankRatingHypoidMethodB2
    from ._432 import ISO10300MeshSingleFlankRatingMethodB1
    from ._433 import ISO10300MeshSingleFlankRatingMethodB2
    from ._434 import ISO10300RateableMesh
    from ._435 import ISO10300RatingMethod
    from ._436 import ISO10300SingleFlankRating
    from ._437 import ISO10300SingleFlankRatingBevelMethodB2
    from ._438 import ISO10300SingleFlankRatingHypoidMethodB2
    from ._439 import ISO10300SingleFlankRatingMethodB1
    from ._440 import ISO10300SingleFlankRatingMethodB2
    from ._441 import MountingConditionsOfPinionAndWheel
    from ._442 import PittingFactorCalculationMethod
    from ._443 import ProfileCrowningSetting
    from ._444 import VerificationOfContactPattern
else:
    import_structure = {
        "_427": ["GeneralLoadFactorCalculationMethod"],
        "_428": ["Iso10300FinishingMethods"],
        "_429": ["ISO10300MeshSingleFlankRating"],
        "_430": ["ISO10300MeshSingleFlankRatingBevelMethodB2"],
        "_431": ["ISO10300MeshSingleFlankRatingHypoidMethodB2"],
        "_432": ["ISO10300MeshSingleFlankRatingMethodB1"],
        "_433": ["ISO10300MeshSingleFlankRatingMethodB2"],
        "_434": ["ISO10300RateableMesh"],
        "_435": ["ISO10300RatingMethod"],
        "_436": ["ISO10300SingleFlankRating"],
        "_437": ["ISO10300SingleFlankRatingBevelMethodB2"],
        "_438": ["ISO10300SingleFlankRatingHypoidMethodB2"],
        "_439": ["ISO10300SingleFlankRatingMethodB1"],
        "_440": ["ISO10300SingleFlankRatingMethodB2"],
        "_441": ["MountingConditionsOfPinionAndWheel"],
        "_442": ["PittingFactorCalculationMethod"],
        "_443": ["ProfileCrowningSetting"],
        "_444": ["VerificationOfContactPattern"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GeneralLoadFactorCalculationMethod",
    "Iso10300FinishingMethods",
    "ISO10300MeshSingleFlankRating",
    "ISO10300MeshSingleFlankRatingBevelMethodB2",
    "ISO10300MeshSingleFlankRatingHypoidMethodB2",
    "ISO10300MeshSingleFlankRatingMethodB1",
    "ISO10300MeshSingleFlankRatingMethodB2",
    "ISO10300RateableMesh",
    "ISO10300RatingMethod",
    "ISO10300SingleFlankRating",
    "ISO10300SingleFlankRatingBevelMethodB2",
    "ISO10300SingleFlankRatingHypoidMethodB2",
    "ISO10300SingleFlankRatingMethodB1",
    "ISO10300SingleFlankRatingMethodB2",
    "MountingConditionsOfPinionAndWheel",
    "PittingFactorCalculationMethod",
    "ProfileCrowningSetting",
    "VerificationOfContactPattern",
)
