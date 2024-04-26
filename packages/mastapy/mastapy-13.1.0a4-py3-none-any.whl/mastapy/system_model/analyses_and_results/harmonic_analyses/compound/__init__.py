"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5905 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5906 import AbstractShaftCompoundHarmonicAnalysis
    from ._5907 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5908 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5909 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5910 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5911 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5912 import AssemblyCompoundHarmonicAnalysis
    from ._5913 import BearingCompoundHarmonicAnalysis
    from ._5914 import BeltConnectionCompoundHarmonicAnalysis
    from ._5915 import BeltDriveCompoundHarmonicAnalysis
    from ._5916 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5917 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5918 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5919 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5920 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5921 import BevelGearCompoundHarmonicAnalysis
    from ._5922 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5923 import BevelGearSetCompoundHarmonicAnalysis
    from ._5924 import BoltCompoundHarmonicAnalysis
    from ._5925 import BoltedJointCompoundHarmonicAnalysis
    from ._5926 import ClutchCompoundHarmonicAnalysis
    from ._5927 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5928 import ClutchHalfCompoundHarmonicAnalysis
    from ._5929 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5930 import ComponentCompoundHarmonicAnalysis
    from ._5931 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5932 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5933 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5934 import ConceptGearCompoundHarmonicAnalysis
    from ._5935 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5936 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5937 import ConicalGearCompoundHarmonicAnalysis
    from ._5938 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5939 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5940 import ConnectionCompoundHarmonicAnalysis
    from ._5941 import ConnectorCompoundHarmonicAnalysis
    from ._5942 import CouplingCompoundHarmonicAnalysis
    from ._5943 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5944 import CouplingHalfCompoundHarmonicAnalysis
    from ._5945 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5946 import CVTCompoundHarmonicAnalysis
    from ._5947 import CVTPulleyCompoundHarmonicAnalysis
    from ._5948 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5949 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5950 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5951 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5952 import CylindricalGearCompoundHarmonicAnalysis
    from ._5953 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5954 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5955 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5956 import DatumCompoundHarmonicAnalysis
    from ._5957 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5958 import FaceGearCompoundHarmonicAnalysis
    from ._5959 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5960 import FaceGearSetCompoundHarmonicAnalysis
    from ._5961 import FEPartCompoundHarmonicAnalysis
    from ._5962 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5963 import GearCompoundHarmonicAnalysis
    from ._5964 import GearMeshCompoundHarmonicAnalysis
    from ._5965 import GearSetCompoundHarmonicAnalysis
    from ._5966 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5967 import HypoidGearCompoundHarmonicAnalysis
    from ._5968 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5969 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5970 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5971 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5972 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5973 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5974 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5975 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5976 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5977 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5978 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5979 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5980 import MassDiscCompoundHarmonicAnalysis
    from ._5981 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5982 import MountableComponentCompoundHarmonicAnalysis
    from ._5983 import OilSealCompoundHarmonicAnalysis
    from ._5984 import PartCompoundHarmonicAnalysis
    from ._5985 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5986 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5987 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5988 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5989 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5990 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5991 import PointLoadCompoundHarmonicAnalysis
    from ._5992 import PowerLoadCompoundHarmonicAnalysis
    from ._5993 import PulleyCompoundHarmonicAnalysis
    from ._5994 import RingPinsCompoundHarmonicAnalysis
    from ._5995 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5996 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5997 import RollingRingCompoundHarmonicAnalysis
    from ._5998 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5999 import RootAssemblyCompoundHarmonicAnalysis
    from ._6000 import ShaftCompoundHarmonicAnalysis
    from ._6001 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._6002 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._6003 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._6004 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._6005 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._6006 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._6007 import SpringDamperCompoundHarmonicAnalysis
    from ._6008 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._6009 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._6010 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._6011 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._6012 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._6013 import StraightBevelGearCompoundHarmonicAnalysis
    from ._6014 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._6015 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._6016 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._6017 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._6018 import SynchroniserCompoundHarmonicAnalysis
    from ._6019 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._6020 import SynchroniserPartCompoundHarmonicAnalysis
    from ._6021 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._6022 import TorqueConverterCompoundHarmonicAnalysis
    from ._6023 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._6024 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._6025 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._6026 import UnbalancedMassCompoundHarmonicAnalysis
    from ._6027 import VirtualComponentCompoundHarmonicAnalysis
    from ._6028 import WormGearCompoundHarmonicAnalysis
    from ._6029 import WormGearMeshCompoundHarmonicAnalysis
    from ._6030 import WormGearSetCompoundHarmonicAnalysis
    from ._6031 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6032 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6033 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5905": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5906": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5907": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5908": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5909": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5910": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5911": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5912": ["AssemblyCompoundHarmonicAnalysis"],
        "_5913": ["BearingCompoundHarmonicAnalysis"],
        "_5914": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5915": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5916": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5917": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5918": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5919": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5920": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5921": ["BevelGearCompoundHarmonicAnalysis"],
        "_5922": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5923": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5924": ["BoltCompoundHarmonicAnalysis"],
        "_5925": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5926": ["ClutchCompoundHarmonicAnalysis"],
        "_5927": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5928": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5929": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5930": ["ComponentCompoundHarmonicAnalysis"],
        "_5931": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5932": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5933": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5934": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5935": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5936": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5937": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5938": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5939": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5940": ["ConnectionCompoundHarmonicAnalysis"],
        "_5941": ["ConnectorCompoundHarmonicAnalysis"],
        "_5942": ["CouplingCompoundHarmonicAnalysis"],
        "_5943": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5944": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5945": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5946": ["CVTCompoundHarmonicAnalysis"],
        "_5947": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5948": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5949": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5950": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5951": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5952": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5953": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5954": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5955": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5956": ["DatumCompoundHarmonicAnalysis"],
        "_5957": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5958": ["FaceGearCompoundHarmonicAnalysis"],
        "_5959": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5960": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5961": ["FEPartCompoundHarmonicAnalysis"],
        "_5962": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5963": ["GearCompoundHarmonicAnalysis"],
        "_5964": ["GearMeshCompoundHarmonicAnalysis"],
        "_5965": ["GearSetCompoundHarmonicAnalysis"],
        "_5966": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5967": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5968": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5969": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5970": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5971": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5972": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5973": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5974": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5975": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5976": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5977": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5978": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5979": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5980": ["MassDiscCompoundHarmonicAnalysis"],
        "_5981": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5982": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5983": ["OilSealCompoundHarmonicAnalysis"],
        "_5984": ["PartCompoundHarmonicAnalysis"],
        "_5985": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5986": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5987": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5988": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5989": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5990": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5991": ["PointLoadCompoundHarmonicAnalysis"],
        "_5992": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5993": ["PulleyCompoundHarmonicAnalysis"],
        "_5994": ["RingPinsCompoundHarmonicAnalysis"],
        "_5995": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5996": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5997": ["RollingRingCompoundHarmonicAnalysis"],
        "_5998": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5999": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_6000": ["ShaftCompoundHarmonicAnalysis"],
        "_6001": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_6002": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_6003": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_6004": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_6005": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_6006": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_6007": ["SpringDamperCompoundHarmonicAnalysis"],
        "_6008": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_6009": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_6010": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_6011": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_6012": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_6013": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_6014": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_6015": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_6016": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_6017": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_6018": ["SynchroniserCompoundHarmonicAnalysis"],
        "_6019": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_6020": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_6021": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_6022": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_6023": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_6024": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_6025": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_6026": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_6027": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_6028": ["WormGearCompoundHarmonicAnalysis"],
        "_6029": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6030": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6031": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6032": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6033": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundHarmonicAnalysis",
    "AbstractShaftCompoundHarmonicAnalysis",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
    "AssemblyCompoundHarmonicAnalysis",
    "BearingCompoundHarmonicAnalysis",
    "BeltConnectionCompoundHarmonicAnalysis",
    "BeltDriveCompoundHarmonicAnalysis",
    "BevelDifferentialGearCompoundHarmonicAnalysis",
    "BevelDifferentialGearMeshCompoundHarmonicAnalysis",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
    "BevelGearCompoundHarmonicAnalysis",
    "BevelGearMeshCompoundHarmonicAnalysis",
    "BevelGearSetCompoundHarmonicAnalysis",
    "BoltCompoundHarmonicAnalysis",
    "BoltedJointCompoundHarmonicAnalysis",
    "ClutchCompoundHarmonicAnalysis",
    "ClutchConnectionCompoundHarmonicAnalysis",
    "ClutchHalfCompoundHarmonicAnalysis",
    "CoaxialConnectionCompoundHarmonicAnalysis",
    "ComponentCompoundHarmonicAnalysis",
    "ConceptCouplingCompoundHarmonicAnalysis",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
    "ConceptGearCompoundHarmonicAnalysis",
    "ConceptGearMeshCompoundHarmonicAnalysis",
    "ConceptGearSetCompoundHarmonicAnalysis",
    "ConicalGearCompoundHarmonicAnalysis",
    "ConicalGearMeshCompoundHarmonicAnalysis",
    "ConicalGearSetCompoundHarmonicAnalysis",
    "ConnectionCompoundHarmonicAnalysis",
    "ConnectorCompoundHarmonicAnalysis",
    "CouplingCompoundHarmonicAnalysis",
    "CouplingConnectionCompoundHarmonicAnalysis",
    "CouplingHalfCompoundHarmonicAnalysis",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
    "CVTCompoundHarmonicAnalysis",
    "CVTPulleyCompoundHarmonicAnalysis",
    "CycloidalAssemblyCompoundHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    "CycloidalDiscCompoundHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis",
    "CylindricalGearCompoundHarmonicAnalysis",
    "CylindricalGearMeshCompoundHarmonicAnalysis",
    "CylindricalGearSetCompoundHarmonicAnalysis",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
    "DatumCompoundHarmonicAnalysis",
    "ExternalCADModelCompoundHarmonicAnalysis",
    "FaceGearCompoundHarmonicAnalysis",
    "FaceGearMeshCompoundHarmonicAnalysis",
    "FaceGearSetCompoundHarmonicAnalysis",
    "FEPartCompoundHarmonicAnalysis",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
    "GearCompoundHarmonicAnalysis",
    "GearMeshCompoundHarmonicAnalysis",
    "GearSetCompoundHarmonicAnalysis",
    "GuideDxfModelCompoundHarmonicAnalysis",
    "HypoidGearCompoundHarmonicAnalysis",
    "HypoidGearMeshCompoundHarmonicAnalysis",
    "HypoidGearSetCompoundHarmonicAnalysis",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    "MassDiscCompoundHarmonicAnalysis",
    "MeasurementComponentCompoundHarmonicAnalysis",
    "MountableComponentCompoundHarmonicAnalysis",
    "OilSealCompoundHarmonicAnalysis",
    "PartCompoundHarmonicAnalysis",
    "PartToPartShearCouplingCompoundHarmonicAnalysis",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysis",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
    "PlanetCarrierCompoundHarmonicAnalysis",
    "PointLoadCompoundHarmonicAnalysis",
    "PowerLoadCompoundHarmonicAnalysis",
    "PulleyCompoundHarmonicAnalysis",
    "RingPinsCompoundHarmonicAnalysis",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
    "RollingRingAssemblyCompoundHarmonicAnalysis",
    "RollingRingCompoundHarmonicAnalysis",
    "RollingRingConnectionCompoundHarmonicAnalysis",
    "RootAssemblyCompoundHarmonicAnalysis",
    "ShaftCompoundHarmonicAnalysis",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
    "SpiralBevelGearCompoundHarmonicAnalysis",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
    "SpiralBevelGearSetCompoundHarmonicAnalysis",
    "SpringDamperCompoundHarmonicAnalysis",
    "SpringDamperConnectionCompoundHarmonicAnalysis",
    "SpringDamperHalfCompoundHarmonicAnalysis",
    "StraightBevelDiffGearCompoundHarmonicAnalysis",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
    "StraightBevelGearCompoundHarmonicAnalysis",
    "StraightBevelGearMeshCompoundHarmonicAnalysis",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
    "SynchroniserCompoundHarmonicAnalysis",
    "SynchroniserHalfCompoundHarmonicAnalysis",
    "SynchroniserPartCompoundHarmonicAnalysis",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
    "TorqueConverterCompoundHarmonicAnalysis",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
    "UnbalancedMassCompoundHarmonicAnalysis",
    "VirtualComponentCompoundHarmonicAnalysis",
    "WormGearCompoundHarmonicAnalysis",
    "WormGearMeshCompoundHarmonicAnalysis",
    "WormGearSetCompoundHarmonicAnalysis",
    "ZerolBevelGearCompoundHarmonicAnalysis",
    "ZerolBevelGearMeshCompoundHarmonicAnalysis",
    "ZerolBevelGearSetCompoundHarmonicAnalysis",
)
