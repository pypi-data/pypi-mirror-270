"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1189 import AGMAGleasonConicalGearGeometryMethods
    from ._1190 import BevelGearDesign
    from ._1191 import BevelGearMeshDesign
    from ._1192 import BevelGearSetDesign
    from ._1193 import BevelMeshedGearDesign
    from ._1194 import DrivenMachineCharacteristicGleason
    from ._1195 import EdgeRadiusType
    from ._1196 import FinishingMethods
    from ._1197 import MachineCharacteristicAGMAKlingelnberg
    from ._1198 import PrimeMoverCharacteristicGleason
    from ._1199 import ToothProportionsInputMethod
    from ._1200 import ToothThicknessSpecificationMethod
    from ._1201 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        "_1189": ["AGMAGleasonConicalGearGeometryMethods"],
        "_1190": ["BevelGearDesign"],
        "_1191": ["BevelGearMeshDesign"],
        "_1192": ["BevelGearSetDesign"],
        "_1193": ["BevelMeshedGearDesign"],
        "_1194": ["DrivenMachineCharacteristicGleason"],
        "_1195": ["EdgeRadiusType"],
        "_1196": ["FinishingMethods"],
        "_1197": ["MachineCharacteristicAGMAKlingelnberg"],
        "_1198": ["PrimeMoverCharacteristicGleason"],
        "_1199": ["ToothProportionsInputMethod"],
        "_1200": ["ToothThicknessSpecificationMethod"],
        "_1201": ["WheelFinishCutterPointWidthRestrictionMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)
