"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1160 import ActiveConicalFlank
    from ._1161 import BacklashDistributionRule
    from ._1162 import ConicalFlanks
    from ._1163 import ConicalGearCutter
    from ._1164 import ConicalGearDesign
    from ._1165 import ConicalGearMeshDesign
    from ._1166 import ConicalGearSetDesign
    from ._1167 import ConicalMachineSettingCalculationMethods
    from ._1168 import ConicalManufactureMethods
    from ._1169 import ConicalMeshedGearDesign
    from ._1170 import ConicalMeshMisalignments
    from ._1171 import CutterBladeType
    from ._1172 import CutterGaugeLengths
    from ._1173 import DummyConicalGearCutter
    from ._1174 import FrontEndTypes
    from ._1175 import GleasonSafetyRequirements
    from ._1176 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1177 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1178 import KlingelnbergFinishingMethods
    from ._1179 import LoadDistributionFactorMethods
    from ._1180 import TopremEntryType
    from ._1181 import TopremLetter
else:
    import_structure = {
        "_1160": ["ActiveConicalFlank"],
        "_1161": ["BacklashDistributionRule"],
        "_1162": ["ConicalFlanks"],
        "_1163": ["ConicalGearCutter"],
        "_1164": ["ConicalGearDesign"],
        "_1165": ["ConicalGearMeshDesign"],
        "_1166": ["ConicalGearSetDesign"],
        "_1167": ["ConicalMachineSettingCalculationMethods"],
        "_1168": ["ConicalManufactureMethods"],
        "_1169": ["ConicalMeshedGearDesign"],
        "_1170": ["ConicalMeshMisalignments"],
        "_1171": ["CutterBladeType"],
        "_1172": ["CutterGaugeLengths"],
        "_1173": ["DummyConicalGearCutter"],
        "_1174": ["FrontEndTypes"],
        "_1175": ["GleasonSafetyRequirements"],
        "_1176": ["KIMoSBevelHypoidSingleLoadCaseResultsData"],
        "_1177": ["KIMoSBevelHypoidSingleRotationAngleResult"],
        "_1178": ["KlingelnbergFinishingMethods"],
        "_1179": ["LoadDistributionFactorMethods"],
        "_1180": ["TopremEntryType"],
        "_1181": ["TopremLetter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)
