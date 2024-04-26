"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._590 import AGMACylindricalGearMaterial
    from ._591 import BevelGearAbstractMaterialDatabase
    from ._592 import BevelGearISOMaterial
    from ._593 import BevelGearISOMaterialDatabase
    from ._594 import BevelGearMaterial
    from ._595 import BevelGearMaterialDatabase
    from ._596 import CylindricalGearAGMAMaterialDatabase
    from ._597 import CylindricalGearISOMaterialDatabase
    from ._598 import CylindricalGearMaterial
    from ._599 import CylindricalGearMaterialDatabase
    from ._600 import CylindricalGearPlasticMaterialDatabase
    from ._601 import GearMaterial
    from ._602 import GearMaterialDatabase
    from ._603 import GearMaterialExpertSystemFactorSettings
    from ._604 import ISOCylindricalGearMaterial
    from ._605 import ISOTR1417912001CoefficientOfFrictionConstants
    from ._606 import ISOTR1417912001CoefficientOfFrictionConstantsDatabase
    from ._607 import KlingelnbergConicalGearMaterialDatabase
    from ._608 import KlingelnbergCycloPalloidConicalGearMaterial
    from ._609 import ManufactureRating
    from ._610 import PlasticCylindricalGearMaterial
    from ._611 import PlasticSNCurve
    from ._612 import RatingMethods
    from ._613 import RawMaterial
    from ._614 import RawMaterialDatabase
    from ._615 import SNCurveDefinition
else:
    import_structure = {
        "_590": ["AGMACylindricalGearMaterial"],
        "_591": ["BevelGearAbstractMaterialDatabase"],
        "_592": ["BevelGearISOMaterial"],
        "_593": ["BevelGearISOMaterialDatabase"],
        "_594": ["BevelGearMaterial"],
        "_595": ["BevelGearMaterialDatabase"],
        "_596": ["CylindricalGearAGMAMaterialDatabase"],
        "_597": ["CylindricalGearISOMaterialDatabase"],
        "_598": ["CylindricalGearMaterial"],
        "_599": ["CylindricalGearMaterialDatabase"],
        "_600": ["CylindricalGearPlasticMaterialDatabase"],
        "_601": ["GearMaterial"],
        "_602": ["GearMaterialDatabase"],
        "_603": ["GearMaterialExpertSystemFactorSettings"],
        "_604": ["ISOCylindricalGearMaterial"],
        "_605": ["ISOTR1417912001CoefficientOfFrictionConstants"],
        "_606": ["ISOTR1417912001CoefficientOfFrictionConstantsDatabase"],
        "_607": ["KlingelnbergConicalGearMaterialDatabase"],
        "_608": ["KlingelnbergCycloPalloidConicalGearMaterial"],
        "_609": ["ManufactureRating"],
        "_610": ["PlasticCylindricalGearMaterial"],
        "_611": ["PlasticSNCurve"],
        "_612": ["RatingMethods"],
        "_613": ["RawMaterial"],
        "_614": ["RawMaterialDatabase"],
        "_615": ["SNCurveDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMACylindricalGearMaterial",
    "BevelGearAbstractMaterialDatabase",
    "BevelGearISOMaterial",
    "BevelGearISOMaterialDatabase",
    "BevelGearMaterial",
    "BevelGearMaterialDatabase",
    "CylindricalGearAGMAMaterialDatabase",
    "CylindricalGearISOMaterialDatabase",
    "CylindricalGearMaterial",
    "CylindricalGearMaterialDatabase",
    "CylindricalGearPlasticMaterialDatabase",
    "GearMaterial",
    "GearMaterialDatabase",
    "GearMaterialExpertSystemFactorSettings",
    "ISOCylindricalGearMaterial",
    "ISOTR1417912001CoefficientOfFrictionConstants",
    "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
    "KlingelnbergConicalGearMaterialDatabase",
    "KlingelnbergCycloPalloidConicalGearMaterial",
    "ManufactureRating",
    "PlasticCylindricalGearMaterial",
    "PlasticSNCurve",
    "RatingMethods",
    "RawMaterial",
    "RawMaterialDatabase",
    "SNCurveDefinition",
)
