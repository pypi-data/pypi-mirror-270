"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._210 import ContactPairReporting
    from ._211 import CoordinateSystemReporting
    from ._212 import DegreeOfFreedomType
    from ._213 import ElasticModulusOrthotropicComponents
    from ._214 import ElementDetailsForFEModel
    from ._215 import ElementPropertiesBase
    from ._216 import ElementPropertiesBeam
    from ._217 import ElementPropertiesInterface
    from ._218 import ElementPropertiesMass
    from ._219 import ElementPropertiesRigid
    from ._220 import ElementPropertiesShell
    from ._221 import ElementPropertiesSolid
    from ._222 import ElementPropertiesSpringDashpot
    from ._223 import ElementPropertiesWithMaterial
    from ._224 import MaterialPropertiesReporting
    from ._225 import NodeDetailsForFEModel
    from ._226 import PoissonRatioOrthotropicComponents
    from ._227 import RigidElementNodeDegreesOfFreedom
    from ._228 import ShearModulusOrthotropicComponents
    from ._229 import ThermalExpansionOrthotropicComponents
else:
    import_structure = {
        "_210": ["ContactPairReporting"],
        "_211": ["CoordinateSystemReporting"],
        "_212": ["DegreeOfFreedomType"],
        "_213": ["ElasticModulusOrthotropicComponents"],
        "_214": ["ElementDetailsForFEModel"],
        "_215": ["ElementPropertiesBase"],
        "_216": ["ElementPropertiesBeam"],
        "_217": ["ElementPropertiesInterface"],
        "_218": ["ElementPropertiesMass"],
        "_219": ["ElementPropertiesRigid"],
        "_220": ["ElementPropertiesShell"],
        "_221": ["ElementPropertiesSolid"],
        "_222": ["ElementPropertiesSpringDashpot"],
        "_223": ["ElementPropertiesWithMaterial"],
        "_224": ["MaterialPropertiesReporting"],
        "_225": ["NodeDetailsForFEModel"],
        "_226": ["PoissonRatioOrthotropicComponents"],
        "_227": ["RigidElementNodeDegreesOfFreedom"],
        "_228": ["ShearModulusOrthotropicComponents"],
        "_229": ["ThermalExpansionOrthotropicComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactPairReporting",
    "CoordinateSystemReporting",
    "DegreeOfFreedomType",
    "ElasticModulusOrthotropicComponents",
    "ElementDetailsForFEModel",
    "ElementPropertiesBase",
    "ElementPropertiesBeam",
    "ElementPropertiesInterface",
    "ElementPropertiesMass",
    "ElementPropertiesRigid",
    "ElementPropertiesShell",
    "ElementPropertiesSolid",
    "ElementPropertiesSpringDashpot",
    "ElementPropertiesWithMaterial",
    "MaterialPropertiesReporting",
    "NodeDetailsForFEModel",
    "PoissonRatioOrthotropicComponents",
    "RigidElementNodeDegreesOfFreedom",
    "ShearModulusOrthotropicComponents",
    "ThermalExpansionOrthotropicComponents",
)
