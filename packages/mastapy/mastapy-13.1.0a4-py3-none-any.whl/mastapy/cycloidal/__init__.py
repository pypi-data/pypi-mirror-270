"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1463 import ContactSpecification
    from ._1464 import CrowningSpecificationMethod
    from ._1465 import CycloidalAssemblyDesign
    from ._1466 import CycloidalDiscDesign
    from ._1467 import CycloidalDiscDesignExporter
    from ._1468 import CycloidalDiscMaterial
    from ._1469 import CycloidalDiscMaterialDatabase
    from ._1470 import CycloidalDiscModificationsSpecification
    from ._1471 import DirectionOfMeasuredModifications
    from ._1472 import GeometryToExport
    from ._1473 import NamedDiscPhase
    from ._1474 import RingPinsDesign
    from ._1475 import RingPinsMaterial
    from ._1476 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1463": ["ContactSpecification"],
        "_1464": ["CrowningSpecificationMethod"],
        "_1465": ["CycloidalAssemblyDesign"],
        "_1466": ["CycloidalDiscDesign"],
        "_1467": ["CycloidalDiscDesignExporter"],
        "_1468": ["CycloidalDiscMaterial"],
        "_1469": ["CycloidalDiscMaterialDatabase"],
        "_1470": ["CycloidalDiscModificationsSpecification"],
        "_1471": ["DirectionOfMeasuredModifications"],
        "_1472": ["GeometryToExport"],
        "_1473": ["NamedDiscPhase"],
        "_1474": ["RingPinsDesign"],
        "_1475": ["RingPinsMaterial"],
        "_1476": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
