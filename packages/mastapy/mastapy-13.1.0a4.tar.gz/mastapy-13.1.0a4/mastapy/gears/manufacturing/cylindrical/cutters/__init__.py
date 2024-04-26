"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._710 import CurveInLinkedList
    from ._711 import CustomisableEdgeProfile
    from ._712 import CylindricalFormedWheelGrinderDatabase
    from ._713 import CylindricalGearAbstractCutterDesign
    from ._714 import CylindricalGearFormGrindingWheel
    from ._715 import CylindricalGearGrindingWorm
    from ._716 import CylindricalGearHobDesign
    from ._717 import CylindricalGearPlungeShaver
    from ._718 import CylindricalGearPlungeShaverDatabase
    from ._719 import CylindricalGearRackDesign
    from ._720 import CylindricalGearRealCutterDesign
    from ._721 import CylindricalGearShaper
    from ._722 import CylindricalGearShaver
    from ._723 import CylindricalGearShaverDatabase
    from ._724 import CylindricalWormGrinderDatabase
    from ._725 import InvoluteCutterDesign
    from ._726 import MutableCommon
    from ._727 import MutableCurve
    from ._728 import MutableFillet
    from ._729 import RoughCutterCreationSettings
else:
    import_structure = {
        "_710": ["CurveInLinkedList"],
        "_711": ["CustomisableEdgeProfile"],
        "_712": ["CylindricalFormedWheelGrinderDatabase"],
        "_713": ["CylindricalGearAbstractCutterDesign"],
        "_714": ["CylindricalGearFormGrindingWheel"],
        "_715": ["CylindricalGearGrindingWorm"],
        "_716": ["CylindricalGearHobDesign"],
        "_717": ["CylindricalGearPlungeShaver"],
        "_718": ["CylindricalGearPlungeShaverDatabase"],
        "_719": ["CylindricalGearRackDesign"],
        "_720": ["CylindricalGearRealCutterDesign"],
        "_721": ["CylindricalGearShaper"],
        "_722": ["CylindricalGearShaver"],
        "_723": ["CylindricalGearShaverDatabase"],
        "_724": ["CylindricalWormGrinderDatabase"],
        "_725": ["InvoluteCutterDesign"],
        "_726": ["MutableCommon"],
        "_727": ["MutableCurve"],
        "_728": ["MutableFillet"],
        "_729": ["RoughCutterCreationSettings"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CurveInLinkedList",
    "CustomisableEdgeProfile",
    "CylindricalFormedWheelGrinderDatabase",
    "CylindricalGearAbstractCutterDesign",
    "CylindricalGearFormGrindingWheel",
    "CylindricalGearGrindingWorm",
    "CylindricalGearHobDesign",
    "CylindricalGearPlungeShaver",
    "CylindricalGearPlungeShaverDatabase",
    "CylindricalGearRackDesign",
    "CylindricalGearRealCutterDesign",
    "CylindricalGearShaper",
    "CylindricalGearShaver",
    "CylindricalGearShaverDatabase",
    "CylindricalWormGrinderDatabase",
    "InvoluteCutterDesign",
    "MutableCommon",
    "MutableCurve",
    "MutableFillet",
    "RoughCutterCreationSettings",
)
