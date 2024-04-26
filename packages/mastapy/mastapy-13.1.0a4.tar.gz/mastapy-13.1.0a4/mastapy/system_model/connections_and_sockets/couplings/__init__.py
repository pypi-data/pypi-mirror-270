"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2360 import ClutchConnection
    from ._2361 import ClutchSocket
    from ._2362 import ConceptCouplingConnection
    from ._2363 import ConceptCouplingSocket
    from ._2364 import CouplingConnection
    from ._2365 import CouplingSocket
    from ._2366 import PartToPartShearCouplingConnection
    from ._2367 import PartToPartShearCouplingSocket
    from ._2368 import SpringDamperConnection
    from ._2369 import SpringDamperSocket
    from ._2370 import TorqueConverterConnection
    from ._2371 import TorqueConverterPumpSocket
    from ._2372 import TorqueConverterTurbineSocket
else:
    import_structure = {
        "_2360": ["ClutchConnection"],
        "_2361": ["ClutchSocket"],
        "_2362": ["ConceptCouplingConnection"],
        "_2363": ["ConceptCouplingSocket"],
        "_2364": ["CouplingConnection"],
        "_2365": ["CouplingSocket"],
        "_2366": ["PartToPartShearCouplingConnection"],
        "_2367": ["PartToPartShearCouplingSocket"],
        "_2368": ["SpringDamperConnection"],
        "_2369": ["SpringDamperSocket"],
        "_2370": ["TorqueConverterConnection"],
        "_2371": ["TorqueConverterPumpSocket"],
        "_2372": ["TorqueConverterTurbineSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)
