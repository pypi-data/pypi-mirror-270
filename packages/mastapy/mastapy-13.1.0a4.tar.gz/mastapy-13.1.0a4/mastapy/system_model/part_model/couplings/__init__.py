"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2594 import BeltDrive
    from ._2595 import BeltDriveType
    from ._2596 import Clutch
    from ._2597 import ClutchHalf
    from ._2598 import ClutchType
    from ._2599 import ConceptCoupling
    from ._2600 import ConceptCouplingHalf
    from ._2601 import ConceptCouplingHalfPositioning
    from ._2602 import Coupling
    from ._2603 import CouplingHalf
    from ._2604 import CrowningSpecification
    from ._2605 import CVT
    from ._2606 import CVTPulley
    from ._2607 import PartToPartShearCoupling
    from ._2608 import PartToPartShearCouplingHalf
    from ._2609 import PitchErrorFlankOptions
    from ._2610 import Pulley
    from ._2611 import RigidConnectorStiffnessType
    from ._2612 import RigidConnectorTiltStiffnessTypes
    from ._2613 import RigidConnectorToothLocation
    from ._2614 import RigidConnectorToothSpacingType
    from ._2615 import RigidConnectorTypes
    from ._2616 import RollingRing
    from ._2617 import RollingRingAssembly
    from ._2618 import ShaftHubConnection
    from ._2619 import SplineFitOptions
    from ._2620 import SplineLeadRelief
    from ._2621 import SplinePitchErrorInputType
    from ._2622 import SplinePitchErrorOptions
    from ._2623 import SpringDamper
    from ._2624 import SpringDamperHalf
    from ._2625 import Synchroniser
    from ._2626 import SynchroniserCone
    from ._2627 import SynchroniserHalf
    from ._2628 import SynchroniserPart
    from ._2629 import SynchroniserSleeve
    from ._2630 import TorqueConverter
    from ._2631 import TorqueConverterPump
    from ._2632 import TorqueConverterSpeedRatio
    from ._2633 import TorqueConverterTurbine
else:
    import_structure = {
        "_2594": ["BeltDrive"],
        "_2595": ["BeltDriveType"],
        "_2596": ["Clutch"],
        "_2597": ["ClutchHalf"],
        "_2598": ["ClutchType"],
        "_2599": ["ConceptCoupling"],
        "_2600": ["ConceptCouplingHalf"],
        "_2601": ["ConceptCouplingHalfPositioning"],
        "_2602": ["Coupling"],
        "_2603": ["CouplingHalf"],
        "_2604": ["CrowningSpecification"],
        "_2605": ["CVT"],
        "_2606": ["CVTPulley"],
        "_2607": ["PartToPartShearCoupling"],
        "_2608": ["PartToPartShearCouplingHalf"],
        "_2609": ["PitchErrorFlankOptions"],
        "_2610": ["Pulley"],
        "_2611": ["RigidConnectorStiffnessType"],
        "_2612": ["RigidConnectorTiltStiffnessTypes"],
        "_2613": ["RigidConnectorToothLocation"],
        "_2614": ["RigidConnectorToothSpacingType"],
        "_2615": ["RigidConnectorTypes"],
        "_2616": ["RollingRing"],
        "_2617": ["RollingRingAssembly"],
        "_2618": ["ShaftHubConnection"],
        "_2619": ["SplineFitOptions"],
        "_2620": ["SplineLeadRelief"],
        "_2621": ["SplinePitchErrorInputType"],
        "_2622": ["SplinePitchErrorOptions"],
        "_2623": ["SpringDamper"],
        "_2624": ["SpringDamperHalf"],
        "_2625": ["Synchroniser"],
        "_2626": ["SynchroniserCone"],
        "_2627": ["SynchroniserHalf"],
        "_2628": ["SynchroniserPart"],
        "_2629": ["SynchroniserSleeve"],
        "_2630": ["TorqueConverter"],
        "_2631": ["TorqueConverterPump"],
        "_2632": ["TorqueConverterSpeedRatio"],
        "_2633": ["TorqueConverterTurbine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "ConceptCouplingHalfPositioning",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "PitchErrorFlankOptions",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineFitOptions",
    "SplineLeadRelief",
    "SplinePitchErrorInputType",
    "SplinePitchErrorOptions",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)
