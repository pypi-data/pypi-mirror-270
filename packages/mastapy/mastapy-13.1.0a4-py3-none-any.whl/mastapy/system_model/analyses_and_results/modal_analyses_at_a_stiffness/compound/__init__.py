"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5011 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._5012 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._5013 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._5014 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5015 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._5016 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5017 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5018 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._5019 import BearingCompoundModalAnalysisAtAStiffness
    from ._5020 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5021 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._5022 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._5023 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._5024 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._5025 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5026 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5027 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5028 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5029 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5030 import BoltCompoundModalAnalysisAtAStiffness
    from ._5031 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5032 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5033 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5034 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5035 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5036 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5037 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5038 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5039 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5040 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5041 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5042 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5043 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5044 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5045 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5046 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5047 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5048 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5049 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5050 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5051 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5052 import CVTCompoundModalAnalysisAtAStiffness
    from ._5053 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5054 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5055 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5056 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5057 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5058 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5059 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5060 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5061 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5062 import DatumCompoundModalAnalysisAtAStiffness
    from ._5063 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5064 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5065 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5066 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5067 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5068 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5069 import GearCompoundModalAnalysisAtAStiffness
    from ._5070 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5071 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5072 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5073 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5074 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5075 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5076 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5077 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5078 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5079 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5080 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5081 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5082 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5083 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5084 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5085 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5086 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5087 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5088 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5089 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5090 import PartCompoundModalAnalysisAtAStiffness
    from ._5091 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5092 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5093 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5094 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5095 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5096 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5097 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5098 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5099 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5100 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5101 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5102 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5103 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5104 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5105 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5106 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5107 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5108 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5109 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5110 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5111 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5112 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5113 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5114 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5115 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5116 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5117 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5118 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5119 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5120 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5121 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5122 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5123 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5124 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5125 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5126 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5127 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5128 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5129 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5130 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5131 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5132 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5133 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5134 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5135 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5136 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5137 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5138 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5139 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_5011": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5012": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_5013": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_5014": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5015": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5016": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5017": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5018": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_5019": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_5020": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5021": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_5022": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_5023": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5024": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_5025": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5026": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5027": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5028": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5029": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5030": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5031": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5032": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5033": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5034": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5035": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5036": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5037": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5038": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5039": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5040": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5041": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5042": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5043": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5044": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5045": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5046": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5047": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5048": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5049": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5050": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5051": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5052": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5053": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5054": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5055": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5056": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5057": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5058": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5059": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5060": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5061": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5062": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5063": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5064": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5065": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5066": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5067": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5068": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5069": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5070": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5071": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5072": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5073": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5074": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5075": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5076": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5077": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5078": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5079": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5080": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5081": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5082": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5083": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5084": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5085": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5086": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5087": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5088": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5089": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5090": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5091": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5092": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5093": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5094": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5095": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5096": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5097": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5098": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5099": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5100": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5101": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5102": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5103": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5104": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5105": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5106": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5107": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5108": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5109": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5110": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5111": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5112": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5113": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5114": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5115": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5116": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5117": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5118": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5119": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5120": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5121": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5122": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5123": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5124": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5125": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5126": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5127": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5128": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5129": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5130": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5131": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5132": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5133": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5134": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5135": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5136": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5137": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5138": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5139": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness",
    "AssemblyCompoundModalAnalysisAtAStiffness",
    "BearingCompoundModalAnalysisAtAStiffness",
    "BeltConnectionCompoundModalAnalysisAtAStiffness",
    "BeltDriveCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness",
    "BevelGearCompoundModalAnalysisAtAStiffness",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
    "BoltCompoundModalAnalysisAtAStiffness",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
    "ClutchCompoundModalAnalysisAtAStiffness",
    "ClutchConnectionCompoundModalAnalysisAtAStiffness",
    "ClutchHalfCompoundModalAnalysisAtAStiffness",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
    "ComponentCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingHalfCompoundModalAnalysisAtAStiffness",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
    "ConceptGearMeshCompoundModalAnalysisAtAStiffness",
    "ConceptGearSetCompoundModalAnalysisAtAStiffness",
    "ConicalGearCompoundModalAnalysisAtAStiffness",
    "ConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "ConicalGearSetCompoundModalAnalysisAtAStiffness",
    "ConnectionCompoundModalAnalysisAtAStiffness",
    "ConnectorCompoundModalAnalysisAtAStiffness",
    "CouplingCompoundModalAnalysisAtAStiffness",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
    "CVTCompoundModalAnalysisAtAStiffness",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
    "CycloidalAssemblyCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
    "CylindricalGearMeshCompoundModalAnalysisAtAStiffness",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    "DatumCompoundModalAnalysisAtAStiffness",
    "ExternalCADModelCompoundModalAnalysisAtAStiffness",
    "FaceGearCompoundModalAnalysisAtAStiffness",
    "FaceGearMeshCompoundModalAnalysisAtAStiffness",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
    "FEPartCompoundModalAnalysisAtAStiffness",
    "FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness",
    "GearCompoundModalAnalysisAtAStiffness",
    "GearMeshCompoundModalAnalysisAtAStiffness",
    "GearSetCompoundModalAnalysisAtAStiffness",
    "GuideDxfModelCompoundModalAnalysisAtAStiffness",
    "HypoidGearCompoundModalAnalysisAtAStiffness",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "HypoidGearSetCompoundModalAnalysisAtAStiffness",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "MassDiscCompoundModalAnalysisAtAStiffness",
    "MeasurementComponentCompoundModalAnalysisAtAStiffness",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
    "OilSealCompoundModalAnalysisAtAStiffness",
    "PartCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
    "PlanetCarrierCompoundModalAnalysisAtAStiffness",
    "PointLoadCompoundModalAnalysisAtAStiffness",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
    "PulleyCompoundModalAnalysisAtAStiffness",
    "RingPinsCompoundModalAnalysisAtAStiffness",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    "RollingRingAssemblyCompoundModalAnalysisAtAStiffness",
    "RollingRingCompoundModalAnalysisAtAStiffness",
    "RollingRingConnectionCompoundModalAnalysisAtAStiffness",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
    "ShaftCompoundModalAnalysisAtAStiffness",
    "ShaftHubConnectionCompoundModalAnalysisAtAStiffness",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
    "SpringDamperConnectionCompoundModalAnalysisAtAStiffness",
    "SpringDamperHalfCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
    "SynchroniserHalfCompoundModalAnalysisAtAStiffness",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
    "TorqueConverterCompoundModalAnalysisAtAStiffness",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    "TorqueConverterPumpCompoundModalAnalysisAtAStiffness",
    "TorqueConverterTurbineCompoundModalAnalysisAtAStiffness",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
    "WormGearCompoundModalAnalysisAtAStiffness",
    "WormGearMeshCompoundModalAnalysisAtAStiffness",
    "WormGearSetCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)
