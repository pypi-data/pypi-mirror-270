"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2874 import AbstractAssemblyCompoundSystemDeflection
    from ._2875 import AbstractShaftCompoundSystemDeflection
    from ._2876 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2877 import (
        AbstractShaftToMountableComponentConnectionCompoundSystemDeflection,
    )
    from ._2878 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2879 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2880 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2881 import AssemblyCompoundSystemDeflection
    from ._2882 import BearingCompoundSystemDeflection
    from ._2883 import BeltConnectionCompoundSystemDeflection
    from ._2884 import BeltDriveCompoundSystemDeflection
    from ._2885 import BevelDifferentialGearCompoundSystemDeflection
    from ._2886 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2887 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2888 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2889 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2890 import BevelGearCompoundSystemDeflection
    from ._2891 import BevelGearMeshCompoundSystemDeflection
    from ._2892 import BevelGearSetCompoundSystemDeflection
    from ._2893 import BoltCompoundSystemDeflection
    from ._2894 import BoltedJointCompoundSystemDeflection
    from ._2895 import ClutchCompoundSystemDeflection
    from ._2896 import ClutchConnectionCompoundSystemDeflection
    from ._2897 import ClutchHalfCompoundSystemDeflection
    from ._2898 import CoaxialConnectionCompoundSystemDeflection
    from ._2899 import ComponentCompoundSystemDeflection
    from ._2900 import ConceptCouplingCompoundSystemDeflection
    from ._2901 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2902 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2903 import ConceptGearCompoundSystemDeflection
    from ._2904 import ConceptGearMeshCompoundSystemDeflection
    from ._2905 import ConceptGearSetCompoundSystemDeflection
    from ._2906 import ConicalGearCompoundSystemDeflection
    from ._2907 import ConicalGearMeshCompoundSystemDeflection
    from ._2908 import ConicalGearSetCompoundSystemDeflection
    from ._2909 import ConnectionCompoundSystemDeflection
    from ._2910 import ConnectorCompoundSystemDeflection
    from ._2911 import CouplingCompoundSystemDeflection
    from ._2912 import CouplingConnectionCompoundSystemDeflection
    from ._2913 import CouplingHalfCompoundSystemDeflection
    from ._2914 import CVTBeltConnectionCompoundSystemDeflection
    from ._2915 import CVTCompoundSystemDeflection
    from ._2916 import CVTPulleyCompoundSystemDeflection
    from ._2917 import CycloidalAssemblyCompoundSystemDeflection
    from ._2918 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2919 import CycloidalDiscCompoundSystemDeflection
    from ._2920 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2921 import CylindricalGearCompoundSystemDeflection
    from ._2922 import CylindricalGearMeshCompoundSystemDeflection
    from ._2923 import CylindricalGearSetCompoundSystemDeflection
    from ._2924 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2925 import DatumCompoundSystemDeflection
    from ._2926 import DutyCycleEfficiencyResults
    from ._2927 import ExternalCADModelCompoundSystemDeflection
    from ._2928 import FaceGearCompoundSystemDeflection
    from ._2929 import FaceGearMeshCompoundSystemDeflection
    from ._2930 import FaceGearSetCompoundSystemDeflection
    from ._2931 import FEPartCompoundSystemDeflection
    from ._2932 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2933 import GearCompoundSystemDeflection
    from ._2934 import GearMeshCompoundSystemDeflection
    from ._2935 import GearSetCompoundSystemDeflection
    from ._2936 import GuideDxfModelCompoundSystemDeflection
    from ._2937 import HypoidGearCompoundSystemDeflection
    from ._2938 import HypoidGearMeshCompoundSystemDeflection
    from ._2939 import HypoidGearSetCompoundSystemDeflection
    from ._2940 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2941 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2942 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2943 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2944 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2945 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2946 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2947 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2948 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection,
    )
    from ._2949 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection,
    )
    from ._2950 import MassDiscCompoundSystemDeflection
    from ._2951 import MeasurementComponentCompoundSystemDeflection
    from ._2952 import MountableComponentCompoundSystemDeflection
    from ._2953 import OilSealCompoundSystemDeflection
    from ._2954 import PartCompoundSystemDeflection
    from ._2955 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2956 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2957 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2958 import PlanetaryConnectionCompoundSystemDeflection
    from ._2959 import PlanetaryGearSetCompoundSystemDeflection
    from ._2960 import PlanetCarrierCompoundSystemDeflection
    from ._2961 import PointLoadCompoundSystemDeflection
    from ._2962 import PowerLoadCompoundSystemDeflection
    from ._2963 import PulleyCompoundSystemDeflection
    from ._2964 import RingPinsCompoundSystemDeflection
    from ._2965 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2966 import RollingRingAssemblyCompoundSystemDeflection
    from ._2967 import RollingRingCompoundSystemDeflection
    from ._2968 import RollingRingConnectionCompoundSystemDeflection
    from ._2969 import RootAssemblyCompoundSystemDeflection
    from ._2970 import ShaftCompoundSystemDeflection
    from ._2971 import ShaftDutyCycleSystemDeflection
    from ._2972 import ShaftHubConnectionCompoundSystemDeflection
    from ._2973 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2974 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2975 import SpiralBevelGearCompoundSystemDeflection
    from ._2976 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2977 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2978 import SpringDamperCompoundSystemDeflection
    from ._2979 import SpringDamperConnectionCompoundSystemDeflection
    from ._2980 import SpringDamperHalfCompoundSystemDeflection
    from ._2981 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2982 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2983 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2984 import StraightBevelGearCompoundSystemDeflection
    from ._2985 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2986 import StraightBevelGearSetCompoundSystemDeflection
    from ._2987 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2988 import StraightBevelSunGearCompoundSystemDeflection
    from ._2989 import SynchroniserCompoundSystemDeflection
    from ._2990 import SynchroniserHalfCompoundSystemDeflection
    from ._2991 import SynchroniserPartCompoundSystemDeflection
    from ._2992 import SynchroniserSleeveCompoundSystemDeflection
    from ._2993 import TorqueConverterCompoundSystemDeflection
    from ._2994 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2995 import TorqueConverterPumpCompoundSystemDeflection
    from ._2996 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2997 import UnbalancedMassCompoundSystemDeflection
    from ._2998 import VirtualComponentCompoundSystemDeflection
    from ._2999 import WormGearCompoundSystemDeflection
    from ._3000 import WormGearMeshCompoundSystemDeflection
    from ._3001 import WormGearSetCompoundSystemDeflection
    from ._3002 import ZerolBevelGearCompoundSystemDeflection
    from ._3003 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._3004 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        "_2874": ["AbstractAssemblyCompoundSystemDeflection"],
        "_2875": ["AbstractShaftCompoundSystemDeflection"],
        "_2876": ["AbstractShaftOrHousingCompoundSystemDeflection"],
        "_2877": [
            "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ],
        "_2878": ["AGMAGleasonConicalGearCompoundSystemDeflection"],
        "_2879": ["AGMAGleasonConicalGearMeshCompoundSystemDeflection"],
        "_2880": ["AGMAGleasonConicalGearSetCompoundSystemDeflection"],
        "_2881": ["AssemblyCompoundSystemDeflection"],
        "_2882": ["BearingCompoundSystemDeflection"],
        "_2883": ["BeltConnectionCompoundSystemDeflection"],
        "_2884": ["BeltDriveCompoundSystemDeflection"],
        "_2885": ["BevelDifferentialGearCompoundSystemDeflection"],
        "_2886": ["BevelDifferentialGearMeshCompoundSystemDeflection"],
        "_2887": ["BevelDifferentialGearSetCompoundSystemDeflection"],
        "_2888": ["BevelDifferentialPlanetGearCompoundSystemDeflection"],
        "_2889": ["BevelDifferentialSunGearCompoundSystemDeflection"],
        "_2890": ["BevelGearCompoundSystemDeflection"],
        "_2891": ["BevelGearMeshCompoundSystemDeflection"],
        "_2892": ["BevelGearSetCompoundSystemDeflection"],
        "_2893": ["BoltCompoundSystemDeflection"],
        "_2894": ["BoltedJointCompoundSystemDeflection"],
        "_2895": ["ClutchCompoundSystemDeflection"],
        "_2896": ["ClutchConnectionCompoundSystemDeflection"],
        "_2897": ["ClutchHalfCompoundSystemDeflection"],
        "_2898": ["CoaxialConnectionCompoundSystemDeflection"],
        "_2899": ["ComponentCompoundSystemDeflection"],
        "_2900": ["ConceptCouplingCompoundSystemDeflection"],
        "_2901": ["ConceptCouplingConnectionCompoundSystemDeflection"],
        "_2902": ["ConceptCouplingHalfCompoundSystemDeflection"],
        "_2903": ["ConceptGearCompoundSystemDeflection"],
        "_2904": ["ConceptGearMeshCompoundSystemDeflection"],
        "_2905": ["ConceptGearSetCompoundSystemDeflection"],
        "_2906": ["ConicalGearCompoundSystemDeflection"],
        "_2907": ["ConicalGearMeshCompoundSystemDeflection"],
        "_2908": ["ConicalGearSetCompoundSystemDeflection"],
        "_2909": ["ConnectionCompoundSystemDeflection"],
        "_2910": ["ConnectorCompoundSystemDeflection"],
        "_2911": ["CouplingCompoundSystemDeflection"],
        "_2912": ["CouplingConnectionCompoundSystemDeflection"],
        "_2913": ["CouplingHalfCompoundSystemDeflection"],
        "_2914": ["CVTBeltConnectionCompoundSystemDeflection"],
        "_2915": ["CVTCompoundSystemDeflection"],
        "_2916": ["CVTPulleyCompoundSystemDeflection"],
        "_2917": ["CycloidalAssemblyCompoundSystemDeflection"],
        "_2918": ["CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"],
        "_2919": ["CycloidalDiscCompoundSystemDeflection"],
        "_2920": ["CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"],
        "_2921": ["CylindricalGearCompoundSystemDeflection"],
        "_2922": ["CylindricalGearMeshCompoundSystemDeflection"],
        "_2923": ["CylindricalGearSetCompoundSystemDeflection"],
        "_2924": ["CylindricalPlanetGearCompoundSystemDeflection"],
        "_2925": ["DatumCompoundSystemDeflection"],
        "_2926": ["DutyCycleEfficiencyResults"],
        "_2927": ["ExternalCADModelCompoundSystemDeflection"],
        "_2928": ["FaceGearCompoundSystemDeflection"],
        "_2929": ["FaceGearMeshCompoundSystemDeflection"],
        "_2930": ["FaceGearSetCompoundSystemDeflection"],
        "_2931": ["FEPartCompoundSystemDeflection"],
        "_2932": ["FlexiblePinAssemblyCompoundSystemDeflection"],
        "_2933": ["GearCompoundSystemDeflection"],
        "_2934": ["GearMeshCompoundSystemDeflection"],
        "_2935": ["GearSetCompoundSystemDeflection"],
        "_2936": ["GuideDxfModelCompoundSystemDeflection"],
        "_2937": ["HypoidGearCompoundSystemDeflection"],
        "_2938": ["HypoidGearMeshCompoundSystemDeflection"],
        "_2939": ["HypoidGearSetCompoundSystemDeflection"],
        "_2940": ["InterMountableComponentConnectionCompoundSystemDeflection"],
        "_2941": ["KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"],
        "_2942": ["KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"],
        "_2943": ["KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"],
        "_2944": ["KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"],
        "_2945": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"],
        "_2946": ["KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection"],
        "_2947": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"],
        "_2948": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ],
        "_2949": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"],
        "_2950": ["MassDiscCompoundSystemDeflection"],
        "_2951": ["MeasurementComponentCompoundSystemDeflection"],
        "_2952": ["MountableComponentCompoundSystemDeflection"],
        "_2953": ["OilSealCompoundSystemDeflection"],
        "_2954": ["PartCompoundSystemDeflection"],
        "_2955": ["PartToPartShearCouplingCompoundSystemDeflection"],
        "_2956": ["PartToPartShearCouplingConnectionCompoundSystemDeflection"],
        "_2957": ["PartToPartShearCouplingHalfCompoundSystemDeflection"],
        "_2958": ["PlanetaryConnectionCompoundSystemDeflection"],
        "_2959": ["PlanetaryGearSetCompoundSystemDeflection"],
        "_2960": ["PlanetCarrierCompoundSystemDeflection"],
        "_2961": ["PointLoadCompoundSystemDeflection"],
        "_2962": ["PowerLoadCompoundSystemDeflection"],
        "_2963": ["PulleyCompoundSystemDeflection"],
        "_2964": ["RingPinsCompoundSystemDeflection"],
        "_2965": ["RingPinsToDiscConnectionCompoundSystemDeflection"],
        "_2966": ["RollingRingAssemblyCompoundSystemDeflection"],
        "_2967": ["RollingRingCompoundSystemDeflection"],
        "_2968": ["RollingRingConnectionCompoundSystemDeflection"],
        "_2969": ["RootAssemblyCompoundSystemDeflection"],
        "_2970": ["ShaftCompoundSystemDeflection"],
        "_2971": ["ShaftDutyCycleSystemDeflection"],
        "_2972": ["ShaftHubConnectionCompoundSystemDeflection"],
        "_2973": ["ShaftToMountableComponentConnectionCompoundSystemDeflection"],
        "_2974": ["SpecialisedAssemblyCompoundSystemDeflection"],
        "_2975": ["SpiralBevelGearCompoundSystemDeflection"],
        "_2976": ["SpiralBevelGearMeshCompoundSystemDeflection"],
        "_2977": ["SpiralBevelGearSetCompoundSystemDeflection"],
        "_2978": ["SpringDamperCompoundSystemDeflection"],
        "_2979": ["SpringDamperConnectionCompoundSystemDeflection"],
        "_2980": ["SpringDamperHalfCompoundSystemDeflection"],
        "_2981": ["StraightBevelDiffGearCompoundSystemDeflection"],
        "_2982": ["StraightBevelDiffGearMeshCompoundSystemDeflection"],
        "_2983": ["StraightBevelDiffGearSetCompoundSystemDeflection"],
        "_2984": ["StraightBevelGearCompoundSystemDeflection"],
        "_2985": ["StraightBevelGearMeshCompoundSystemDeflection"],
        "_2986": ["StraightBevelGearSetCompoundSystemDeflection"],
        "_2987": ["StraightBevelPlanetGearCompoundSystemDeflection"],
        "_2988": ["StraightBevelSunGearCompoundSystemDeflection"],
        "_2989": ["SynchroniserCompoundSystemDeflection"],
        "_2990": ["SynchroniserHalfCompoundSystemDeflection"],
        "_2991": ["SynchroniserPartCompoundSystemDeflection"],
        "_2992": ["SynchroniserSleeveCompoundSystemDeflection"],
        "_2993": ["TorqueConverterCompoundSystemDeflection"],
        "_2994": ["TorqueConverterConnectionCompoundSystemDeflection"],
        "_2995": ["TorqueConverterPumpCompoundSystemDeflection"],
        "_2996": ["TorqueConverterTurbineCompoundSystemDeflection"],
        "_2997": ["UnbalancedMassCompoundSystemDeflection"],
        "_2998": ["VirtualComponentCompoundSystemDeflection"],
        "_2999": ["WormGearCompoundSystemDeflection"],
        "_3000": ["WormGearMeshCompoundSystemDeflection"],
        "_3001": ["WormGearSetCompoundSystemDeflection"],
        "_3002": ["ZerolBevelGearCompoundSystemDeflection"],
        "_3003": ["ZerolBevelGearMeshCompoundSystemDeflection"],
        "_3004": ["ZerolBevelGearSetCompoundSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSystemDeflection",
    "AbstractShaftCompoundSystemDeflection",
    "AbstractShaftOrHousingCompoundSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
    "AssemblyCompoundSystemDeflection",
    "BearingCompoundSystemDeflection",
    "BeltConnectionCompoundSystemDeflection",
    "BeltDriveCompoundSystemDeflection",
    "BevelDifferentialGearCompoundSystemDeflection",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
    "BevelDifferentialGearSetCompoundSystemDeflection",
    "BevelDifferentialPlanetGearCompoundSystemDeflection",
    "BevelDifferentialSunGearCompoundSystemDeflection",
    "BevelGearCompoundSystemDeflection",
    "BevelGearMeshCompoundSystemDeflection",
    "BevelGearSetCompoundSystemDeflection",
    "BoltCompoundSystemDeflection",
    "BoltedJointCompoundSystemDeflection",
    "ClutchCompoundSystemDeflection",
    "ClutchConnectionCompoundSystemDeflection",
    "ClutchHalfCompoundSystemDeflection",
    "CoaxialConnectionCompoundSystemDeflection",
    "ComponentCompoundSystemDeflection",
    "ConceptCouplingCompoundSystemDeflection",
    "ConceptCouplingConnectionCompoundSystemDeflection",
    "ConceptCouplingHalfCompoundSystemDeflection",
    "ConceptGearCompoundSystemDeflection",
    "ConceptGearMeshCompoundSystemDeflection",
    "ConceptGearSetCompoundSystemDeflection",
    "ConicalGearCompoundSystemDeflection",
    "ConicalGearMeshCompoundSystemDeflection",
    "ConicalGearSetCompoundSystemDeflection",
    "ConnectionCompoundSystemDeflection",
    "ConnectorCompoundSystemDeflection",
    "CouplingCompoundSystemDeflection",
    "CouplingConnectionCompoundSystemDeflection",
    "CouplingHalfCompoundSystemDeflection",
    "CVTBeltConnectionCompoundSystemDeflection",
    "CVTCompoundSystemDeflection",
    "CVTPulleyCompoundSystemDeflection",
    "CycloidalAssemblyCompoundSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    "CycloidalDiscCompoundSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    "CylindricalGearCompoundSystemDeflection",
    "CylindricalGearMeshCompoundSystemDeflection",
    "CylindricalGearSetCompoundSystemDeflection",
    "CylindricalPlanetGearCompoundSystemDeflection",
    "DatumCompoundSystemDeflection",
    "DutyCycleEfficiencyResults",
    "ExternalCADModelCompoundSystemDeflection",
    "FaceGearCompoundSystemDeflection",
    "FaceGearMeshCompoundSystemDeflection",
    "FaceGearSetCompoundSystemDeflection",
    "FEPartCompoundSystemDeflection",
    "FlexiblePinAssemblyCompoundSystemDeflection",
    "GearCompoundSystemDeflection",
    "GearMeshCompoundSystemDeflection",
    "GearSetCompoundSystemDeflection",
    "GuideDxfModelCompoundSystemDeflection",
    "HypoidGearCompoundSystemDeflection",
    "HypoidGearMeshCompoundSystemDeflection",
    "HypoidGearSetCompoundSystemDeflection",
    "InterMountableComponentConnectionCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    "MassDiscCompoundSystemDeflection",
    "MeasurementComponentCompoundSystemDeflection",
    "MountableComponentCompoundSystemDeflection",
    "OilSealCompoundSystemDeflection",
    "PartCompoundSystemDeflection",
    "PartToPartShearCouplingCompoundSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundSystemDeflection",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
    "PlanetaryConnectionCompoundSystemDeflection",
    "PlanetaryGearSetCompoundSystemDeflection",
    "PlanetCarrierCompoundSystemDeflection",
    "PointLoadCompoundSystemDeflection",
    "PowerLoadCompoundSystemDeflection",
    "PulleyCompoundSystemDeflection",
    "RingPinsCompoundSystemDeflection",
    "RingPinsToDiscConnectionCompoundSystemDeflection",
    "RollingRingAssemblyCompoundSystemDeflection",
    "RollingRingCompoundSystemDeflection",
    "RollingRingConnectionCompoundSystemDeflection",
    "RootAssemblyCompoundSystemDeflection",
    "ShaftCompoundSystemDeflection",
    "ShaftDutyCycleSystemDeflection",
    "ShaftHubConnectionCompoundSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
    "SpecialisedAssemblyCompoundSystemDeflection",
    "SpiralBevelGearCompoundSystemDeflection",
    "SpiralBevelGearMeshCompoundSystemDeflection",
    "SpiralBevelGearSetCompoundSystemDeflection",
    "SpringDamperCompoundSystemDeflection",
    "SpringDamperConnectionCompoundSystemDeflection",
    "SpringDamperHalfCompoundSystemDeflection",
    "StraightBevelDiffGearCompoundSystemDeflection",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
    "StraightBevelGearCompoundSystemDeflection",
    "StraightBevelGearMeshCompoundSystemDeflection",
    "StraightBevelGearSetCompoundSystemDeflection",
    "StraightBevelPlanetGearCompoundSystemDeflection",
    "StraightBevelSunGearCompoundSystemDeflection",
    "SynchroniserCompoundSystemDeflection",
    "SynchroniserHalfCompoundSystemDeflection",
    "SynchroniserPartCompoundSystemDeflection",
    "SynchroniserSleeveCompoundSystemDeflection",
    "TorqueConverterCompoundSystemDeflection",
    "TorqueConverterConnectionCompoundSystemDeflection",
    "TorqueConverterPumpCompoundSystemDeflection",
    "TorqueConverterTurbineCompoundSystemDeflection",
    "UnbalancedMassCompoundSystemDeflection",
    "VirtualComponentCompoundSystemDeflection",
    "WormGearCompoundSystemDeflection",
    "WormGearMeshCompoundSystemDeflection",
    "WormGearSetCompoundSystemDeflection",
    "ZerolBevelGearCompoundSystemDeflection",
    "ZerolBevelGearMeshCompoundSystemDeflection",
    "ZerolBevelGearSetCompoundSystemDeflection",
)
