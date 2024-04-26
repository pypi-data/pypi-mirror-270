"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7032 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7034 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7035 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7036 import AdvancedTimeSteppingAnalysisForModulation
    from ._7037 import AtsamExcitationsOrOthers
    from ._7038 import AtsamNaturalFrequencyViewOption
    from ._7039 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7040 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7042 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7043 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import ATSAMResultsVsLargeTimeStepSettings
    from ._7045 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7047 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7050 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7052 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7054 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7057 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7065 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7074 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7075 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7076 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7077 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7078 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7079 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7080 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7081 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7082 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7083 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7084 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7085 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7086 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7087 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7090 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7091 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7092 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7093 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7094 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7095 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7100 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7102 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7103 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7104 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7105 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7106 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7107 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7108 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7109 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7110 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7111 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7112 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7113 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7115 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7116 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7118 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7120 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7121 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7127 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7131 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7136 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7140 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7141 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7142 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7143 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7144 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7145 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7146 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7147 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7149 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7150 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7151 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7152 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7153 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7154 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7155 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7156 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7157 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7162 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7163 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7165 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7166 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7032": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7033": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7034": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7035": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7036": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7037": ["AtsamExcitationsOrOthers"],
        "_7038": ["AtsamNaturalFrequencyViewOption"],
        "_7039": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7040": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7042": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7045": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7047": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7052": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7053": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7054": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7055": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7056": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7057": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7058": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7065": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7066": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7070": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7071": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7073": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7074": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7075": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7076": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7077": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7078": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7079": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7080": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7081": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7082": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7083": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7084": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7085": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7086": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7087": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7088": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7089": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7090": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7091": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7092": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7093": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7094": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7095": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7099": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7100": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7101": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7102": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7103": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7104": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7105": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7106": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7107": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7108": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7109": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7110": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7111": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7112": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7113": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7115": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7116": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7118": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7120": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7121": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7131": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7136": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7137": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7138": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7140": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7141": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7142": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7143": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7144": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7145": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7146": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7147": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7148": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7149": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7150": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7151": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7152": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7153": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7154": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7155": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7156": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7157": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7161": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7162": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7163": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7164": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7165": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7166": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
    "AtsamExcitationsOrOthers",
    "AtsamNaturalFrequencyViewOption",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ATSAMResultsVsLargeTimeStepSettings",
    "BearingAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BoltAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointAdvancedTimeSteppingAnalysisForModulation",
    "ClutchAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ComponentAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "DatumAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "GearAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ShaftAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    "WormGearAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)
