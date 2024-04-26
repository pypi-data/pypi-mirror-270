"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._185 import DrawStyleForFE
    from ._186 import EigenvalueOptions
    from ._187 import ElementFaceGroup
    from ._188 import ElementGroup
    from ._189 import FEEntityGroup
    from ._190 import FEEntityGroupInteger
    from ._191 import FEModel
    from ._192 import FEModelComponentDrawStyle
    from ._193 import FEModelHarmonicAnalysisDrawStyle
    from ._194 import FEModelInstanceDrawStyle
    from ._195 import FEModelModalAnalysisDrawStyle
    from ._196 import FEModelPart
    from ._197 import FEModelSetupViewType
    from ._198 import FEModelStaticAnalysisDrawStyle
    from ._199 import FEModelTabDrawStyle
    from ._200 import FEModelTransparencyDrawStyle
    from ._201 import FENodeSelectionDrawStyle
    from ._202 import FESelectionMode
    from ._203 import FESurfaceAndNonDeformedDrawingOption
    from ._204 import FESurfaceDrawingOption
    from ._205 import MassMatrixType
    from ._206 import ModelSplittingMethod
    from ._207 import NodeGroup
    from ._208 import NoneSelectedAllOption
    from ._209 import RigidCouplingType
else:
    import_structure = {
        "_185": ["DrawStyleForFE"],
        "_186": ["EigenvalueOptions"],
        "_187": ["ElementFaceGroup"],
        "_188": ["ElementGroup"],
        "_189": ["FEEntityGroup"],
        "_190": ["FEEntityGroupInteger"],
        "_191": ["FEModel"],
        "_192": ["FEModelComponentDrawStyle"],
        "_193": ["FEModelHarmonicAnalysisDrawStyle"],
        "_194": ["FEModelInstanceDrawStyle"],
        "_195": ["FEModelModalAnalysisDrawStyle"],
        "_196": ["FEModelPart"],
        "_197": ["FEModelSetupViewType"],
        "_198": ["FEModelStaticAnalysisDrawStyle"],
        "_199": ["FEModelTabDrawStyle"],
        "_200": ["FEModelTransparencyDrawStyle"],
        "_201": ["FENodeSelectionDrawStyle"],
        "_202": ["FESelectionMode"],
        "_203": ["FESurfaceAndNonDeformedDrawingOption"],
        "_204": ["FESurfaceDrawingOption"],
        "_205": ["MassMatrixType"],
        "_206": ["ModelSplittingMethod"],
        "_207": ["NodeGroup"],
        "_208": ["NoneSelectedAllOption"],
        "_209": ["RigidCouplingType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DrawStyleForFE",
    "EigenvalueOptions",
    "ElementFaceGroup",
    "ElementGroup",
    "FEEntityGroup",
    "FEEntityGroupInteger",
    "FEModel",
    "FEModelComponentDrawStyle",
    "FEModelHarmonicAnalysisDrawStyle",
    "FEModelInstanceDrawStyle",
    "FEModelModalAnalysisDrawStyle",
    "FEModelPart",
    "FEModelSetupViewType",
    "FEModelStaticAnalysisDrawStyle",
    "FEModelTabDrawStyle",
    "FEModelTransparencyDrawStyle",
    "FENodeSelectionDrawStyle",
    "FESelectionMode",
    "FESurfaceAndNonDeformedDrawingOption",
    "FESurfaceDrawingOption",
    "MassMatrixType",
    "ModelSplittingMethod",
    "NodeGroup",
    "NoneSelectedAllOption",
    "RigidCouplingType",
)
