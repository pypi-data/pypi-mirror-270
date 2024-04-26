"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._616 import CutterFlankSections
    from ._617 import CylindricalCutterDatabase
    from ._618 import CylindricalGearBlank
    from ._619 import CylindricalGearManufacturingConfig
    from ._620 import CylindricalGearSpecifiedMicroGeometry
    from ._621 import CylindricalGearSpecifiedProfile
    from ._622 import CylindricalHobDatabase
    from ._623 import CylindricalManufacturedGearDutyCycle
    from ._624 import CylindricalManufacturedGearLoadCase
    from ._625 import CylindricalManufacturedGearMeshDutyCycle
    from ._626 import CylindricalManufacturedGearMeshLoadCase
    from ._627 import CylindricalManufacturedGearSetDutyCycle
    from ._628 import CylindricalManufacturedGearSetLoadCase
    from ._629 import CylindricalMeshManufacturingConfig
    from ._630 import CylindricalMftFinishingMethods
    from ._631 import CylindricalMftRoughingMethods
    from ._632 import CylindricalSetManufacturingConfig
    from ._633 import CylindricalShaperDatabase
    from ._634 import Flank
    from ._635 import GearManufacturingConfigurationViewModel
    from ._636 import GearManufacturingConfigurationViewModelPlaceholder
    from ._637 import GearSetConfigViewModel
    from ._638 import HobEdgeTypes
    from ._639 import LeadModificationSegment
    from ._640 import MicroGeometryInputs
    from ._641 import MicroGeometryInputsLead
    from ._642 import MicroGeometryInputsProfile
    from ._643 import ModificationSegment
    from ._644 import ProfileModificationSegment
    from ._645 import SuitableCutterSetup
else:
    import_structure = {
        "_616": ["CutterFlankSections"],
        "_617": ["CylindricalCutterDatabase"],
        "_618": ["CylindricalGearBlank"],
        "_619": ["CylindricalGearManufacturingConfig"],
        "_620": ["CylindricalGearSpecifiedMicroGeometry"],
        "_621": ["CylindricalGearSpecifiedProfile"],
        "_622": ["CylindricalHobDatabase"],
        "_623": ["CylindricalManufacturedGearDutyCycle"],
        "_624": ["CylindricalManufacturedGearLoadCase"],
        "_625": ["CylindricalManufacturedGearMeshDutyCycle"],
        "_626": ["CylindricalManufacturedGearMeshLoadCase"],
        "_627": ["CylindricalManufacturedGearSetDutyCycle"],
        "_628": ["CylindricalManufacturedGearSetLoadCase"],
        "_629": ["CylindricalMeshManufacturingConfig"],
        "_630": ["CylindricalMftFinishingMethods"],
        "_631": ["CylindricalMftRoughingMethods"],
        "_632": ["CylindricalSetManufacturingConfig"],
        "_633": ["CylindricalShaperDatabase"],
        "_634": ["Flank"],
        "_635": ["GearManufacturingConfigurationViewModel"],
        "_636": ["GearManufacturingConfigurationViewModelPlaceholder"],
        "_637": ["GearSetConfigViewModel"],
        "_638": ["HobEdgeTypes"],
        "_639": ["LeadModificationSegment"],
        "_640": ["MicroGeometryInputs"],
        "_641": ["MicroGeometryInputsLead"],
        "_642": ["MicroGeometryInputsProfile"],
        "_643": ["ModificationSegment"],
        "_644": ["ProfileModificationSegment"],
        "_645": ["SuitableCutterSetup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterFlankSections",
    "CylindricalCutterDatabase",
    "CylindricalGearBlank",
    "CylindricalGearManufacturingConfig",
    "CylindricalGearSpecifiedMicroGeometry",
    "CylindricalGearSpecifiedProfile",
    "CylindricalHobDatabase",
    "CylindricalManufacturedGearDutyCycle",
    "CylindricalManufacturedGearLoadCase",
    "CylindricalManufacturedGearMeshDutyCycle",
    "CylindricalManufacturedGearMeshLoadCase",
    "CylindricalManufacturedGearSetDutyCycle",
    "CylindricalManufacturedGearSetLoadCase",
    "CylindricalMeshManufacturingConfig",
    "CylindricalMftFinishingMethods",
    "CylindricalMftRoughingMethods",
    "CylindricalSetManufacturingConfig",
    "CylindricalShaperDatabase",
    "Flank",
    "GearManufacturingConfigurationViewModel",
    "GearManufacturingConfigurationViewModelPlaceholder",
    "GearSetConfigViewModel",
    "HobEdgeTypes",
    "LeadModificationSegment",
    "MicroGeometryInputs",
    "MicroGeometryInputsLead",
    "MicroGeometryInputsProfile",
    "ModificationSegment",
    "ProfileModificationSegment",
    "SuitableCutterSetup",
)
