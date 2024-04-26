"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._497 import MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
    from ._498 import PlasticGearVDI2736AbstractGearSingleFlankRating
    from ._499 import PlasticGearVDI2736AbstractMeshSingleFlankRating
    from ._500 import PlasticGearVDI2736AbstractRateableMesh
    from ._501 import PlasticPlasticVDI2736MeshSingleFlankRating
    from ._502 import PlasticSNCurveForTheSpecifiedOperatingConditions
    from ._503 import (
        PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh,
    )
    from ._504 import PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
    from ._505 import VDI2736MetalPlasticRateableMesh
    from ._506 import VDI2736PlasticMetalRateableMesh
    from ._507 import VDI2736PlasticPlasticRateableMesh
else:
    import_structure = {
        "_497": ["MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating"],
        "_498": ["PlasticGearVDI2736AbstractGearSingleFlankRating"],
        "_499": ["PlasticGearVDI2736AbstractMeshSingleFlankRating"],
        "_500": ["PlasticGearVDI2736AbstractRateableMesh"],
        "_501": ["PlasticPlasticVDI2736MeshSingleFlankRating"],
        "_502": ["PlasticSNCurveForTheSpecifiedOperatingConditions"],
        "_503": [
            "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ],
        "_504": ["PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh"],
        "_505": ["VDI2736MetalPlasticRateableMesh"],
        "_506": ["VDI2736PlasticMetalRateableMesh"],
        "_507": ["VDI2736PlasticPlasticRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
    "PlasticGearVDI2736AbstractGearSingleFlankRating",
    "PlasticGearVDI2736AbstractMeshSingleFlankRating",
    "PlasticGearVDI2736AbstractRateableMesh",
    "PlasticPlasticVDI2736MeshSingleFlankRating",
    "PlasticSNCurveForTheSpecifiedOperatingConditions",
    "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh",
    "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
    "VDI2736MetalPlasticRateableMesh",
    "VDI2736PlasticMetalRateableMesh",
    "VDI2736PlasticPlasticRateableMesh",
)
