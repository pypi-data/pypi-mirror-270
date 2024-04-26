"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5140 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5141 import AbstractShaftModalAnalysisAtASpeed
    from ._5142 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5143 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5144 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5145 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5146 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5147 import AssemblyModalAnalysisAtASpeed
    from ._5148 import BearingModalAnalysisAtASpeed
    from ._5149 import BeltConnectionModalAnalysisAtASpeed
    from ._5150 import BeltDriveModalAnalysisAtASpeed
    from ._5151 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5152 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5153 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5154 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5155 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5156 import BevelGearMeshModalAnalysisAtASpeed
    from ._5157 import BevelGearModalAnalysisAtASpeed
    from ._5158 import BevelGearSetModalAnalysisAtASpeed
    from ._5159 import BoltedJointModalAnalysisAtASpeed
    from ._5160 import BoltModalAnalysisAtASpeed
    from ._5161 import ClutchConnectionModalAnalysisAtASpeed
    from ._5162 import ClutchHalfModalAnalysisAtASpeed
    from ._5163 import ClutchModalAnalysisAtASpeed
    from ._5164 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5165 import ComponentModalAnalysisAtASpeed
    from ._5166 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5167 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5168 import ConceptCouplingModalAnalysisAtASpeed
    from ._5169 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5170 import ConceptGearModalAnalysisAtASpeed
    from ._5171 import ConceptGearSetModalAnalysisAtASpeed
    from ._5172 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5173 import ConicalGearModalAnalysisAtASpeed
    from ._5174 import ConicalGearSetModalAnalysisAtASpeed
    from ._5175 import ConnectionModalAnalysisAtASpeed
    from ._5176 import ConnectorModalAnalysisAtASpeed
    from ._5177 import CouplingConnectionModalAnalysisAtASpeed
    from ._5178 import CouplingHalfModalAnalysisAtASpeed
    from ._5179 import CouplingModalAnalysisAtASpeed
    from ._5180 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5181 import CVTModalAnalysisAtASpeed
    from ._5182 import CVTPulleyModalAnalysisAtASpeed
    from ._5183 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5184 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5185 import CycloidalDiscModalAnalysisAtASpeed
    from ._5186 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5187 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5188 import CylindricalGearModalAnalysisAtASpeed
    from ._5189 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5190 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5191 import DatumModalAnalysisAtASpeed
    from ._5192 import ExternalCADModelModalAnalysisAtASpeed
    from ._5193 import FaceGearMeshModalAnalysisAtASpeed
    from ._5194 import FaceGearModalAnalysisAtASpeed
    from ._5195 import FaceGearSetModalAnalysisAtASpeed
    from ._5196 import FEPartModalAnalysisAtASpeed
    from ._5197 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5198 import GearMeshModalAnalysisAtASpeed
    from ._5199 import GearModalAnalysisAtASpeed
    from ._5200 import GearSetModalAnalysisAtASpeed
    from ._5201 import GuideDxfModelModalAnalysisAtASpeed
    from ._5202 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5203 import HypoidGearModalAnalysisAtASpeed
    from ._5204 import HypoidGearSetModalAnalysisAtASpeed
    from ._5205 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5206 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5207 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5208 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5209 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5210 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5211 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5212 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5213 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5214 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5215 import MassDiscModalAnalysisAtASpeed
    from ._5216 import MeasurementComponentModalAnalysisAtASpeed
    from ._5217 import ModalAnalysisAtASpeed
    from ._5218 import MountableComponentModalAnalysisAtASpeed
    from ._5219 import OilSealModalAnalysisAtASpeed
    from ._5220 import PartModalAnalysisAtASpeed
    from ._5221 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5222 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5223 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5224 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5225 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5226 import PlanetCarrierModalAnalysisAtASpeed
    from ._5227 import PointLoadModalAnalysisAtASpeed
    from ._5228 import PowerLoadModalAnalysisAtASpeed
    from ._5229 import PulleyModalAnalysisAtASpeed
    from ._5230 import RingPinsModalAnalysisAtASpeed
    from ._5231 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5232 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5233 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5234 import RollingRingModalAnalysisAtASpeed
    from ._5235 import RootAssemblyModalAnalysisAtASpeed
    from ._5236 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5237 import ShaftModalAnalysisAtASpeed
    from ._5238 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5239 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5240 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5241 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5242 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5243 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5244 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5245 import SpringDamperModalAnalysisAtASpeed
    from ._5246 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5247 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5248 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5249 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5250 import StraightBevelGearModalAnalysisAtASpeed
    from ._5251 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5252 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5253 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5254 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5255 import SynchroniserModalAnalysisAtASpeed
    from ._5256 import SynchroniserPartModalAnalysisAtASpeed
    from ._5257 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5258 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5259 import TorqueConverterModalAnalysisAtASpeed
    from ._5260 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5261 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5262 import UnbalancedMassModalAnalysisAtASpeed
    from ._5263 import VirtualComponentModalAnalysisAtASpeed
    from ._5264 import WormGearMeshModalAnalysisAtASpeed
    from ._5265 import WormGearModalAnalysisAtASpeed
    from ._5266 import WormGearSetModalAnalysisAtASpeed
    from ._5267 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5268 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5269 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5140": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5141": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5142": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5143": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5144": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5145": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5146": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5147": ["AssemblyModalAnalysisAtASpeed"],
        "_5148": ["BearingModalAnalysisAtASpeed"],
        "_5149": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5150": ["BeltDriveModalAnalysisAtASpeed"],
        "_5151": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5152": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5153": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5154": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5155": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5156": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5157": ["BevelGearModalAnalysisAtASpeed"],
        "_5158": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5159": ["BoltedJointModalAnalysisAtASpeed"],
        "_5160": ["BoltModalAnalysisAtASpeed"],
        "_5161": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5162": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5163": ["ClutchModalAnalysisAtASpeed"],
        "_5164": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5165": ["ComponentModalAnalysisAtASpeed"],
        "_5166": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5167": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5168": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5169": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5170": ["ConceptGearModalAnalysisAtASpeed"],
        "_5171": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5172": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5173": ["ConicalGearModalAnalysisAtASpeed"],
        "_5174": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5175": ["ConnectionModalAnalysisAtASpeed"],
        "_5176": ["ConnectorModalAnalysisAtASpeed"],
        "_5177": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5178": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5179": ["CouplingModalAnalysisAtASpeed"],
        "_5180": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5181": ["CVTModalAnalysisAtASpeed"],
        "_5182": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5183": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5184": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5185": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5186": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5187": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5188": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5189": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5190": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5191": ["DatumModalAnalysisAtASpeed"],
        "_5192": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5193": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5194": ["FaceGearModalAnalysisAtASpeed"],
        "_5195": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5196": ["FEPartModalAnalysisAtASpeed"],
        "_5197": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5198": ["GearMeshModalAnalysisAtASpeed"],
        "_5199": ["GearModalAnalysisAtASpeed"],
        "_5200": ["GearSetModalAnalysisAtASpeed"],
        "_5201": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5202": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5203": ["HypoidGearModalAnalysisAtASpeed"],
        "_5204": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5205": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5206": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5207": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5208": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5209": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5210": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5211": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5212": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5213": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5214": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5215": ["MassDiscModalAnalysisAtASpeed"],
        "_5216": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5217": ["ModalAnalysisAtASpeed"],
        "_5218": ["MountableComponentModalAnalysisAtASpeed"],
        "_5219": ["OilSealModalAnalysisAtASpeed"],
        "_5220": ["PartModalAnalysisAtASpeed"],
        "_5221": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5222": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5223": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5224": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5225": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5226": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5227": ["PointLoadModalAnalysisAtASpeed"],
        "_5228": ["PowerLoadModalAnalysisAtASpeed"],
        "_5229": ["PulleyModalAnalysisAtASpeed"],
        "_5230": ["RingPinsModalAnalysisAtASpeed"],
        "_5231": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5232": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5233": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5234": ["RollingRingModalAnalysisAtASpeed"],
        "_5235": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5236": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5237": ["ShaftModalAnalysisAtASpeed"],
        "_5238": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5239": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5240": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5241": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5242": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5243": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5244": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5245": ["SpringDamperModalAnalysisAtASpeed"],
        "_5246": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5247": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5248": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5249": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5250": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5251": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5252": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5253": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5254": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5255": ["SynchroniserModalAnalysisAtASpeed"],
        "_5256": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5257": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5258": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5259": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5260": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5261": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5262": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5263": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5264": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5265": ["WormGearModalAnalysisAtASpeed"],
        "_5266": ["WormGearSetModalAnalysisAtASpeed"],
        "_5267": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5268": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5269": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysisAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
    "AssemblyModalAnalysisAtASpeed",
    "BearingModalAnalysisAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
    "BevelGearModalAnalysisAtASpeed",
    "BevelGearSetModalAnalysisAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
    "BoltModalAnalysisAtASpeed",
    "ClutchConnectionModalAnalysisAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
    "ClutchModalAnalysisAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
    "ComponentModalAnalysisAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
    "ConceptCouplingHalfModalAnalysisAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
    "ConceptGearModalAnalysisAtASpeed",
    "ConceptGearSetModalAnalysisAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
    "ConicalGearModalAnalysisAtASpeed",
    "ConicalGearSetModalAnalysisAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
    "CouplingModalAnalysisAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
    "CVTModalAnalysisAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
    "CycloidalAssemblyModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    "CylindricalGearMeshModalAnalysisAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
    "DatumModalAnalysisAtASpeed",
    "ExternalCADModelModalAnalysisAtASpeed",
    "FaceGearMeshModalAnalysisAtASpeed",
    "FaceGearModalAnalysisAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
    "FEPartModalAnalysisAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
    "GearModalAnalysisAtASpeed",
    "GearSetModalAnalysisAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
    "HypoidGearMeshModalAnalysisAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
    "HypoidGearSetModalAnalysisAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
    "ModalAnalysisAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
    "OilSealModalAnalysisAtASpeed",
    "PartModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
    "PartToPartShearCouplingModalAnalysisAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
    "PowerLoadModalAnalysisAtASpeed",
    "PulleyModalAnalysisAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
    "RollingRingModalAnalysisAtASpeed",
    "RootAssemblyModalAnalysisAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
    "ShaftModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
    "SpiralBevelGearModalAnalysisAtASpeed",
    "SpiralBevelGearSetModalAnalysisAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
    "SpringDamperHalfModalAnalysisAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshModalAnalysisAtASpeed",
    "StraightBevelDiffGearModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
    "StraightBevelGearMeshModalAnalysisAtASpeed",
    "StraightBevelGearModalAnalysisAtASpeed",
    "StraightBevelGearSetModalAnalysisAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
    "SynchroniserHalfModalAnalysisAtASpeed",
    "SynchroniserModalAnalysisAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
    "SynchroniserSleeveModalAnalysisAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
    "TorqueConverterModalAnalysisAtASpeed",
    "TorqueConverterPumpModalAnalysisAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
    "WormGearModalAnalysisAtASpeed",
    "WormGearSetModalAnalysisAtASpeed",
    "ZerolBevelGearMeshModalAnalysisAtASpeed",
    "ZerolBevelGearModalAnalysisAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)
