"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._828 import BasicConicalGearMachineSettings
    from ._829 import BasicConicalGearMachineSettingsFormate
    from ._830 import BasicConicalGearMachineSettingsGenerated
    from ._831 import CradleStyleConicalMachineSettingsGenerated
else:
    import_structure = {
        "_828": ["BasicConicalGearMachineSettings"],
        "_829": ["BasicConicalGearMachineSettingsFormate"],
        "_830": ["BasicConicalGearMachineSettingsGenerated"],
        "_831": ["CradleStyleConicalMachineSettingsGenerated"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicConicalGearMachineSettings",
    "BasicConicalGearMachineSettingsFormate",
    "BasicConicalGearMachineSettingsGenerated",
    "CradleStyleConicalMachineSettingsGenerated",
)
