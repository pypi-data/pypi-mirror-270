"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._159 import BaseGeometryModellerDimension
    from ._160 import GeometryModellerAngleDimension
    from ._161 import GeometryModellerCountDimension
    from ._162 import GeometryModellerDesignInformation
    from ._163 import GeometryModellerDimension
    from ._164 import GeometryModellerDimensions
    from ._165 import GeometryModellerDimensionType
    from ._166 import GeometryModellerLengthDimension
    from ._167 import GeometryModellerSettings
    from ._168 import GeometryModellerUnitlessDimension
    from ._169 import MeshRequest
    from ._170 import MeshRequestResult
    from ._171 import RepositionComponentDetails
else:
    import_structure = {
        "_159": ["BaseGeometryModellerDimension"],
        "_160": ["GeometryModellerAngleDimension"],
        "_161": ["GeometryModellerCountDimension"],
        "_162": ["GeometryModellerDesignInformation"],
        "_163": ["GeometryModellerDimension"],
        "_164": ["GeometryModellerDimensions"],
        "_165": ["GeometryModellerDimensionType"],
        "_166": ["GeometryModellerLengthDimension"],
        "_167": ["GeometryModellerSettings"],
        "_168": ["GeometryModellerUnitlessDimension"],
        "_169": ["MeshRequest"],
        "_170": ["MeshRequestResult"],
        "_171": ["RepositionComponentDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BaseGeometryModellerDimension",
    "GeometryModellerAngleDimension",
    "GeometryModellerCountDimension",
    "GeometryModellerDesignInformation",
    "GeometryModellerDimension",
    "GeometryModellerDimensions",
    "GeometryModellerDimensionType",
    "GeometryModellerLengthDimension",
    "GeometryModellerSettings",
    "GeometryModellerUnitlessDimension",
    "MeshRequest",
    "MeshRequestResult",
    "RepositionComponentDetails",
)
