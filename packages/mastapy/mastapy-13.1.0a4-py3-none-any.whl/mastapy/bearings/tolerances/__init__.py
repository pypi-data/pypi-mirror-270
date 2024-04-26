"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1918 import BearingConnectionComponent
    from ._1919 import InternalClearanceClass
    from ._1920 import BearingToleranceClass
    from ._1921 import BearingToleranceDefinitionOptions
    from ._1922 import FitType
    from ._1923 import InnerRingTolerance
    from ._1924 import InnerSupportTolerance
    from ._1925 import InterferenceDetail
    from ._1926 import InterferenceTolerance
    from ._1927 import ITDesignation
    from ._1928 import MountingSleeveDiameterDetail
    from ._1929 import OuterRingTolerance
    from ._1930 import OuterSupportTolerance
    from ._1931 import RaceDetail
    from ._1932 import RaceRoundnessAtAngle
    from ._1933 import RadialSpecificationMethod
    from ._1934 import RingTolerance
    from ._1935 import RoundnessSpecification
    from ._1936 import RoundnessSpecificationType
    from ._1937 import SupportDetail
    from ._1938 import SupportMaterialSource
    from ._1939 import SupportTolerance
    from ._1940 import SupportToleranceLocationDesignation
    from ._1941 import ToleranceCombination
    from ._1942 import TypeOfFit
else:
    import_structure = {
        "_1918": ["BearingConnectionComponent"],
        "_1919": ["InternalClearanceClass"],
        "_1920": ["BearingToleranceClass"],
        "_1921": ["BearingToleranceDefinitionOptions"],
        "_1922": ["FitType"],
        "_1923": ["InnerRingTolerance"],
        "_1924": ["InnerSupportTolerance"],
        "_1925": ["InterferenceDetail"],
        "_1926": ["InterferenceTolerance"],
        "_1927": ["ITDesignation"],
        "_1928": ["MountingSleeveDiameterDetail"],
        "_1929": ["OuterRingTolerance"],
        "_1930": ["OuterSupportTolerance"],
        "_1931": ["RaceDetail"],
        "_1932": ["RaceRoundnessAtAngle"],
        "_1933": ["RadialSpecificationMethod"],
        "_1934": ["RingTolerance"],
        "_1935": ["RoundnessSpecification"],
        "_1936": ["RoundnessSpecificationType"],
        "_1937": ["SupportDetail"],
        "_1938": ["SupportMaterialSource"],
        "_1939": ["SupportTolerance"],
        "_1940": ["SupportToleranceLocationDesignation"],
        "_1941": ["ToleranceCombination"],
        "_1942": ["TypeOfFit"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
