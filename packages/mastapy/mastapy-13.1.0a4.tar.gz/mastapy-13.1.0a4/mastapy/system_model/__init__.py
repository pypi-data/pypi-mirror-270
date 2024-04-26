"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2218 import Design
    from ._2219 import ComponentDampingOption
    from ._2220 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2221 import DesignEntity
    from ._2222 import DesignEntityId
    from ._2223 import DesignSettings
    from ._2224 import DutyCycleImporter
    from ._2225 import DutyCycleImporterDesignEntityMatch
    from ._2226 import ElectricMachineGroup
    from ._2227 import ExternalFullFELoader
    from ._2228 import HypoidWindUpRemovalMethod
    from ._2229 import IncludeDutyCycleOption
    from ._2230 import MASTASettings
    from ._2231 import MemorySummary
    from ._2232 import MeshStiffnessModel
    from ._2233 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2234 import PowerLoadDragTorqueSpecificationMethod
    from ._2235 import PowerLoadInputTorqueSpecificationMethod
    from ._2236 import PowerLoadPIDControlSpeedInputType
    from ._2237 import PowerLoadType
    from ._2238 import RelativeComponentAlignment
    from ._2239 import RelativeOffsetOption
    from ._2240 import SystemReporting
    from ._2241 import ThermalExpansionOptionForGroundedNodes
    from ._2242 import TransmissionTemperatureSet
else:
    import_structure = {
        "_2218": ["Design"],
        "_2219": ["ComponentDampingOption"],
        "_2220": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_2221": ["DesignEntity"],
        "_2222": ["DesignEntityId"],
        "_2223": ["DesignSettings"],
        "_2224": ["DutyCycleImporter"],
        "_2225": ["DutyCycleImporterDesignEntityMatch"],
        "_2226": ["ElectricMachineGroup"],
        "_2227": ["ExternalFullFELoader"],
        "_2228": ["HypoidWindUpRemovalMethod"],
        "_2229": ["IncludeDutyCycleOption"],
        "_2230": ["MASTASettings"],
        "_2231": ["MemorySummary"],
        "_2232": ["MeshStiffnessModel"],
        "_2233": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_2234": ["PowerLoadDragTorqueSpecificationMethod"],
        "_2235": ["PowerLoadInputTorqueSpecificationMethod"],
        "_2236": ["PowerLoadPIDControlSpeedInputType"],
        "_2237": ["PowerLoadType"],
        "_2238": ["RelativeComponentAlignment"],
        "_2239": ["RelativeOffsetOption"],
        "_2240": ["SystemReporting"],
        "_2241": ["ThermalExpansionOptionForGroundedNodes"],
        "_2242": ["TransmissionTemperatureSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ElectricMachineGroup",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
