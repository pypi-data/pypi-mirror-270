"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7167 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7168 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7169 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7170 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7171 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7172 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7173 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7174 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7176 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7177 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7178 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7179 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7180 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7181 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7182 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7183 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7184 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7185 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7186 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7187 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7188 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7189 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7190 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7191 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7192 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7195 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7196 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7198 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7199 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7203 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7204 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7205 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7206 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7207 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7208 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7209 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7210 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7211 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7212 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7213 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7214 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7215 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7216 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7217 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7218 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7219 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7220 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7221 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7222 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7223 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7224 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7225 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7228 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7229 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7230 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7231 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7232 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7233 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7234 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7235 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7236 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7237 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7238 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7239 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7240 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7241 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7242 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7243 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7244 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7245 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7246 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7247 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7248 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7249 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7250 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7251 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7252 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7253 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7254 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7255 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7256 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7257 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7258 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7259 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7260 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7261 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7262 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7263 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7264 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7265 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7266 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7267 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7268 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7269 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7270 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7271 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7272 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7273 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7274 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7275 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7276 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7277 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7278 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7279 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7280 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7281 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7282 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7283 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7284 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7285 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7286 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7287 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7288 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7289 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7290 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7291 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7292 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7293 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7294 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7295 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7167": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7168": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7169": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7170": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7171": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7172": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7173": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7174": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7175": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7176": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7177": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7178": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7179": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7180": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7181": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7182": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7183": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7184": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7185": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7186": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7187": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7188": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7189": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7190": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7191": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7192": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7194": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7195": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7196": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7198": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7199": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7200": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7201": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7203": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7204": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7205": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7206": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7207": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7208": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7209": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7210": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7211": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7212": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7213": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7214": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7215": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7216": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7217": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7218": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7219": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7220": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7221": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7222": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7223": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7224": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7225": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7226": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7227": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7228": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7229": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7230": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7231": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7232": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7233": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7234": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7235": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7236": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7237": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7238": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7239": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7240": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7241": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7242": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7243": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7244": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7245": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7246": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7247": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7248": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7249": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7250": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7251": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7252": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7253": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7254": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7255": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7256": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7257": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7258": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7259": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7260": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7261": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7262": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7263": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7264": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7265": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7266": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7267": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7268": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7269": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7270": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7271": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7272": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7273": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7274": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7275": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7276": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7277": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7278": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7279": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7280": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7281": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7282": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7283": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7284": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7285": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7286": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7287": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7288": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7289": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7290": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7291": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7292": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7293": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7294": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7295": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BearingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "DatumCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FEPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)
