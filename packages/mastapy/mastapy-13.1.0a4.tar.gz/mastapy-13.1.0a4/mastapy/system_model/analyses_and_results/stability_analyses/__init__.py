"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3786 import AbstractAssemblyStabilityAnalysis
    from ._3787 import AbstractShaftOrHousingStabilityAnalysis
    from ._3788 import AbstractShaftStabilityAnalysis
    from ._3789 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3790 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3791 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3792 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3793 import AssemblyStabilityAnalysis
    from ._3794 import BearingStabilityAnalysis
    from ._3795 import BeltConnectionStabilityAnalysis
    from ._3796 import BeltDriveStabilityAnalysis
    from ._3797 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3798 import BevelDifferentialGearSetStabilityAnalysis
    from ._3799 import BevelDifferentialGearStabilityAnalysis
    from ._3800 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3801 import BevelDifferentialSunGearStabilityAnalysis
    from ._3802 import BevelGearMeshStabilityAnalysis
    from ._3803 import BevelGearSetStabilityAnalysis
    from ._3804 import BevelGearStabilityAnalysis
    from ._3805 import BoltedJointStabilityAnalysis
    from ._3806 import BoltStabilityAnalysis
    from ._3807 import ClutchConnectionStabilityAnalysis
    from ._3808 import ClutchHalfStabilityAnalysis
    from ._3809 import ClutchStabilityAnalysis
    from ._3810 import CoaxialConnectionStabilityAnalysis
    from ._3811 import ComponentStabilityAnalysis
    from ._3812 import ConceptCouplingConnectionStabilityAnalysis
    from ._3813 import ConceptCouplingHalfStabilityAnalysis
    from ._3814 import ConceptCouplingStabilityAnalysis
    from ._3815 import ConceptGearMeshStabilityAnalysis
    from ._3816 import ConceptGearSetStabilityAnalysis
    from ._3817 import ConceptGearStabilityAnalysis
    from ._3818 import ConicalGearMeshStabilityAnalysis
    from ._3819 import ConicalGearSetStabilityAnalysis
    from ._3820 import ConicalGearStabilityAnalysis
    from ._3821 import ConnectionStabilityAnalysis
    from ._3822 import ConnectorStabilityAnalysis
    from ._3823 import CouplingConnectionStabilityAnalysis
    from ._3824 import CouplingHalfStabilityAnalysis
    from ._3825 import CouplingStabilityAnalysis
    from ._3826 import CriticalSpeed
    from ._3827 import CVTBeltConnectionStabilityAnalysis
    from ._3828 import CVTPulleyStabilityAnalysis
    from ._3829 import CVTStabilityAnalysis
    from ._3830 import CycloidalAssemblyStabilityAnalysis
    from ._3831 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3832 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3833 import CycloidalDiscStabilityAnalysis
    from ._3834 import CylindricalGearMeshStabilityAnalysis
    from ._3835 import CylindricalGearSetStabilityAnalysis
    from ._3836 import CylindricalGearStabilityAnalysis
    from ._3837 import CylindricalPlanetGearStabilityAnalysis
    from ._3838 import DatumStabilityAnalysis
    from ._3839 import DynamicModelForStabilityAnalysis
    from ._3840 import ExternalCADModelStabilityAnalysis
    from ._3841 import FaceGearMeshStabilityAnalysis
    from ._3842 import FaceGearSetStabilityAnalysis
    from ._3843 import FaceGearStabilityAnalysis
    from ._3844 import FEPartStabilityAnalysis
    from ._3845 import FlexiblePinAssemblyStabilityAnalysis
    from ._3846 import GearMeshStabilityAnalysis
    from ._3847 import GearSetStabilityAnalysis
    from ._3848 import GearStabilityAnalysis
    from ._3849 import GuideDxfModelStabilityAnalysis
    from ._3850 import HypoidGearMeshStabilityAnalysis
    from ._3851 import HypoidGearSetStabilityAnalysis
    from ._3852 import HypoidGearStabilityAnalysis
    from ._3853 import InterMountableComponentConnectionStabilityAnalysis
    from ._3854 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3855 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3856 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3857 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3858 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3859 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3860 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3861 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3862 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3863 import MassDiscStabilityAnalysis
    from ._3864 import MeasurementComponentStabilityAnalysis
    from ._3865 import MountableComponentStabilityAnalysis
    from ._3866 import OilSealStabilityAnalysis
    from ._3867 import PartStabilityAnalysis
    from ._3868 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3869 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3870 import PartToPartShearCouplingStabilityAnalysis
    from ._3871 import PlanetaryConnectionStabilityAnalysis
    from ._3872 import PlanetaryGearSetStabilityAnalysis
    from ._3873 import PlanetCarrierStabilityAnalysis
    from ._3874 import PointLoadStabilityAnalysis
    from ._3875 import PowerLoadStabilityAnalysis
    from ._3876 import PulleyStabilityAnalysis
    from ._3877 import RingPinsStabilityAnalysis
    from ._3878 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3879 import RollingRingAssemblyStabilityAnalysis
    from ._3880 import RollingRingConnectionStabilityAnalysis
    from ._3881 import RollingRingStabilityAnalysis
    from ._3882 import RootAssemblyStabilityAnalysis
    from ._3883 import ShaftHubConnectionStabilityAnalysis
    from ._3884 import ShaftStabilityAnalysis
    from ._3885 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3886 import SpecialisedAssemblyStabilityAnalysis
    from ._3887 import SpiralBevelGearMeshStabilityAnalysis
    from ._3888 import SpiralBevelGearSetStabilityAnalysis
    from ._3889 import SpiralBevelGearStabilityAnalysis
    from ._3890 import SpringDamperConnectionStabilityAnalysis
    from ._3891 import SpringDamperHalfStabilityAnalysis
    from ._3892 import SpringDamperStabilityAnalysis
    from ._3893 import StabilityAnalysis
    from ._3894 import StabilityAnalysisDrawStyle
    from ._3895 import StabilityAnalysisOptions
    from ._3896 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3897 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3898 import StraightBevelDiffGearStabilityAnalysis
    from ._3899 import StraightBevelGearMeshStabilityAnalysis
    from ._3900 import StraightBevelGearSetStabilityAnalysis
    from ._3901 import StraightBevelGearStabilityAnalysis
    from ._3902 import StraightBevelPlanetGearStabilityAnalysis
    from ._3903 import StraightBevelSunGearStabilityAnalysis
    from ._3904 import SynchroniserHalfStabilityAnalysis
    from ._3905 import SynchroniserPartStabilityAnalysis
    from ._3906 import SynchroniserSleeveStabilityAnalysis
    from ._3907 import SynchroniserStabilityAnalysis
    from ._3908 import TorqueConverterConnectionStabilityAnalysis
    from ._3909 import TorqueConverterPumpStabilityAnalysis
    from ._3910 import TorqueConverterStabilityAnalysis
    from ._3911 import TorqueConverterTurbineStabilityAnalysis
    from ._3912 import UnbalancedMassStabilityAnalysis
    from ._3913 import VirtualComponentStabilityAnalysis
    from ._3914 import WormGearMeshStabilityAnalysis
    from ._3915 import WormGearSetStabilityAnalysis
    from ._3916 import WormGearStabilityAnalysis
    from ._3917 import ZerolBevelGearMeshStabilityAnalysis
    from ._3918 import ZerolBevelGearSetStabilityAnalysis
    from ._3919 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        "_3786": ["AbstractAssemblyStabilityAnalysis"],
        "_3787": ["AbstractShaftOrHousingStabilityAnalysis"],
        "_3788": ["AbstractShaftStabilityAnalysis"],
        "_3789": ["AbstractShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3790": ["AGMAGleasonConicalGearMeshStabilityAnalysis"],
        "_3791": ["AGMAGleasonConicalGearSetStabilityAnalysis"],
        "_3792": ["AGMAGleasonConicalGearStabilityAnalysis"],
        "_3793": ["AssemblyStabilityAnalysis"],
        "_3794": ["BearingStabilityAnalysis"],
        "_3795": ["BeltConnectionStabilityAnalysis"],
        "_3796": ["BeltDriveStabilityAnalysis"],
        "_3797": ["BevelDifferentialGearMeshStabilityAnalysis"],
        "_3798": ["BevelDifferentialGearSetStabilityAnalysis"],
        "_3799": ["BevelDifferentialGearStabilityAnalysis"],
        "_3800": ["BevelDifferentialPlanetGearStabilityAnalysis"],
        "_3801": ["BevelDifferentialSunGearStabilityAnalysis"],
        "_3802": ["BevelGearMeshStabilityAnalysis"],
        "_3803": ["BevelGearSetStabilityAnalysis"],
        "_3804": ["BevelGearStabilityAnalysis"],
        "_3805": ["BoltedJointStabilityAnalysis"],
        "_3806": ["BoltStabilityAnalysis"],
        "_3807": ["ClutchConnectionStabilityAnalysis"],
        "_3808": ["ClutchHalfStabilityAnalysis"],
        "_3809": ["ClutchStabilityAnalysis"],
        "_3810": ["CoaxialConnectionStabilityAnalysis"],
        "_3811": ["ComponentStabilityAnalysis"],
        "_3812": ["ConceptCouplingConnectionStabilityAnalysis"],
        "_3813": ["ConceptCouplingHalfStabilityAnalysis"],
        "_3814": ["ConceptCouplingStabilityAnalysis"],
        "_3815": ["ConceptGearMeshStabilityAnalysis"],
        "_3816": ["ConceptGearSetStabilityAnalysis"],
        "_3817": ["ConceptGearStabilityAnalysis"],
        "_3818": ["ConicalGearMeshStabilityAnalysis"],
        "_3819": ["ConicalGearSetStabilityAnalysis"],
        "_3820": ["ConicalGearStabilityAnalysis"],
        "_3821": ["ConnectionStabilityAnalysis"],
        "_3822": ["ConnectorStabilityAnalysis"],
        "_3823": ["CouplingConnectionStabilityAnalysis"],
        "_3824": ["CouplingHalfStabilityAnalysis"],
        "_3825": ["CouplingStabilityAnalysis"],
        "_3826": ["CriticalSpeed"],
        "_3827": ["CVTBeltConnectionStabilityAnalysis"],
        "_3828": ["CVTPulleyStabilityAnalysis"],
        "_3829": ["CVTStabilityAnalysis"],
        "_3830": ["CycloidalAssemblyStabilityAnalysis"],
        "_3831": ["CycloidalDiscCentralBearingConnectionStabilityAnalysis"],
        "_3832": ["CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"],
        "_3833": ["CycloidalDiscStabilityAnalysis"],
        "_3834": ["CylindricalGearMeshStabilityAnalysis"],
        "_3835": ["CylindricalGearSetStabilityAnalysis"],
        "_3836": ["CylindricalGearStabilityAnalysis"],
        "_3837": ["CylindricalPlanetGearStabilityAnalysis"],
        "_3838": ["DatumStabilityAnalysis"],
        "_3839": ["DynamicModelForStabilityAnalysis"],
        "_3840": ["ExternalCADModelStabilityAnalysis"],
        "_3841": ["FaceGearMeshStabilityAnalysis"],
        "_3842": ["FaceGearSetStabilityAnalysis"],
        "_3843": ["FaceGearStabilityAnalysis"],
        "_3844": ["FEPartStabilityAnalysis"],
        "_3845": ["FlexiblePinAssemblyStabilityAnalysis"],
        "_3846": ["GearMeshStabilityAnalysis"],
        "_3847": ["GearSetStabilityAnalysis"],
        "_3848": ["GearStabilityAnalysis"],
        "_3849": ["GuideDxfModelStabilityAnalysis"],
        "_3850": ["HypoidGearMeshStabilityAnalysis"],
        "_3851": ["HypoidGearSetStabilityAnalysis"],
        "_3852": ["HypoidGearStabilityAnalysis"],
        "_3853": ["InterMountableComponentConnectionStabilityAnalysis"],
        "_3854": ["KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"],
        "_3855": ["KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"],
        "_3856": ["KlingelnbergCycloPalloidConicalGearStabilityAnalysis"],
        "_3857": ["KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"],
        "_3858": ["KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis"],
        "_3859": ["KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"],
        "_3860": ["KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"],
        "_3861": ["KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"],
        "_3862": ["KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"],
        "_3863": ["MassDiscStabilityAnalysis"],
        "_3864": ["MeasurementComponentStabilityAnalysis"],
        "_3865": ["MountableComponentStabilityAnalysis"],
        "_3866": ["OilSealStabilityAnalysis"],
        "_3867": ["PartStabilityAnalysis"],
        "_3868": ["PartToPartShearCouplingConnectionStabilityAnalysis"],
        "_3869": ["PartToPartShearCouplingHalfStabilityAnalysis"],
        "_3870": ["PartToPartShearCouplingStabilityAnalysis"],
        "_3871": ["PlanetaryConnectionStabilityAnalysis"],
        "_3872": ["PlanetaryGearSetStabilityAnalysis"],
        "_3873": ["PlanetCarrierStabilityAnalysis"],
        "_3874": ["PointLoadStabilityAnalysis"],
        "_3875": ["PowerLoadStabilityAnalysis"],
        "_3876": ["PulleyStabilityAnalysis"],
        "_3877": ["RingPinsStabilityAnalysis"],
        "_3878": ["RingPinsToDiscConnectionStabilityAnalysis"],
        "_3879": ["RollingRingAssemblyStabilityAnalysis"],
        "_3880": ["RollingRingConnectionStabilityAnalysis"],
        "_3881": ["RollingRingStabilityAnalysis"],
        "_3882": ["RootAssemblyStabilityAnalysis"],
        "_3883": ["ShaftHubConnectionStabilityAnalysis"],
        "_3884": ["ShaftStabilityAnalysis"],
        "_3885": ["ShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3886": ["SpecialisedAssemblyStabilityAnalysis"],
        "_3887": ["SpiralBevelGearMeshStabilityAnalysis"],
        "_3888": ["SpiralBevelGearSetStabilityAnalysis"],
        "_3889": ["SpiralBevelGearStabilityAnalysis"],
        "_3890": ["SpringDamperConnectionStabilityAnalysis"],
        "_3891": ["SpringDamperHalfStabilityAnalysis"],
        "_3892": ["SpringDamperStabilityAnalysis"],
        "_3893": ["StabilityAnalysis"],
        "_3894": ["StabilityAnalysisDrawStyle"],
        "_3895": ["StabilityAnalysisOptions"],
        "_3896": ["StraightBevelDiffGearMeshStabilityAnalysis"],
        "_3897": ["StraightBevelDiffGearSetStabilityAnalysis"],
        "_3898": ["StraightBevelDiffGearStabilityAnalysis"],
        "_3899": ["StraightBevelGearMeshStabilityAnalysis"],
        "_3900": ["StraightBevelGearSetStabilityAnalysis"],
        "_3901": ["StraightBevelGearStabilityAnalysis"],
        "_3902": ["StraightBevelPlanetGearStabilityAnalysis"],
        "_3903": ["StraightBevelSunGearStabilityAnalysis"],
        "_3904": ["SynchroniserHalfStabilityAnalysis"],
        "_3905": ["SynchroniserPartStabilityAnalysis"],
        "_3906": ["SynchroniserSleeveStabilityAnalysis"],
        "_3907": ["SynchroniserStabilityAnalysis"],
        "_3908": ["TorqueConverterConnectionStabilityAnalysis"],
        "_3909": ["TorqueConverterPumpStabilityAnalysis"],
        "_3910": ["TorqueConverterStabilityAnalysis"],
        "_3911": ["TorqueConverterTurbineStabilityAnalysis"],
        "_3912": ["UnbalancedMassStabilityAnalysis"],
        "_3913": ["VirtualComponentStabilityAnalysis"],
        "_3914": ["WormGearMeshStabilityAnalysis"],
        "_3915": ["WormGearSetStabilityAnalysis"],
        "_3916": ["WormGearStabilityAnalysis"],
        "_3917": ["ZerolBevelGearMeshStabilityAnalysis"],
        "_3918": ["ZerolBevelGearSetStabilityAnalysis"],
        "_3919": ["ZerolBevelGearStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStabilityAnalysis",
    "AbstractShaftOrHousingStabilityAnalysis",
    "AbstractShaftStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
    "AGMAGleasonConicalGearStabilityAnalysis",
    "AssemblyStabilityAnalysis",
    "BearingStabilityAnalysis",
    "BeltConnectionStabilityAnalysis",
    "BeltDriveStabilityAnalysis",
    "BevelDifferentialGearMeshStabilityAnalysis",
    "BevelDifferentialGearSetStabilityAnalysis",
    "BevelDifferentialGearStabilityAnalysis",
    "BevelDifferentialPlanetGearStabilityAnalysis",
    "BevelDifferentialSunGearStabilityAnalysis",
    "BevelGearMeshStabilityAnalysis",
    "BevelGearSetStabilityAnalysis",
    "BevelGearStabilityAnalysis",
    "BoltedJointStabilityAnalysis",
    "BoltStabilityAnalysis",
    "ClutchConnectionStabilityAnalysis",
    "ClutchHalfStabilityAnalysis",
    "ClutchStabilityAnalysis",
    "CoaxialConnectionStabilityAnalysis",
    "ComponentStabilityAnalysis",
    "ConceptCouplingConnectionStabilityAnalysis",
    "ConceptCouplingHalfStabilityAnalysis",
    "ConceptCouplingStabilityAnalysis",
    "ConceptGearMeshStabilityAnalysis",
    "ConceptGearSetStabilityAnalysis",
    "ConceptGearStabilityAnalysis",
    "ConicalGearMeshStabilityAnalysis",
    "ConicalGearSetStabilityAnalysis",
    "ConicalGearStabilityAnalysis",
    "ConnectionStabilityAnalysis",
    "ConnectorStabilityAnalysis",
    "CouplingConnectionStabilityAnalysis",
    "CouplingHalfStabilityAnalysis",
    "CouplingStabilityAnalysis",
    "CriticalSpeed",
    "CVTBeltConnectionStabilityAnalysis",
    "CVTPulleyStabilityAnalysis",
    "CVTStabilityAnalysis",
    "CycloidalAssemblyStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    "CycloidalDiscStabilityAnalysis",
    "CylindricalGearMeshStabilityAnalysis",
    "CylindricalGearSetStabilityAnalysis",
    "CylindricalGearStabilityAnalysis",
    "CylindricalPlanetGearStabilityAnalysis",
    "DatumStabilityAnalysis",
    "DynamicModelForStabilityAnalysis",
    "ExternalCADModelStabilityAnalysis",
    "FaceGearMeshStabilityAnalysis",
    "FaceGearSetStabilityAnalysis",
    "FaceGearStabilityAnalysis",
    "FEPartStabilityAnalysis",
    "FlexiblePinAssemblyStabilityAnalysis",
    "GearMeshStabilityAnalysis",
    "GearSetStabilityAnalysis",
    "GearStabilityAnalysis",
    "GuideDxfModelStabilityAnalysis",
    "HypoidGearMeshStabilityAnalysis",
    "HypoidGearSetStabilityAnalysis",
    "HypoidGearStabilityAnalysis",
    "InterMountableComponentConnectionStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    "MassDiscStabilityAnalysis",
    "MeasurementComponentStabilityAnalysis",
    "MountableComponentStabilityAnalysis",
    "OilSealStabilityAnalysis",
    "PartStabilityAnalysis",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
    "PartToPartShearCouplingHalfStabilityAnalysis",
    "PartToPartShearCouplingStabilityAnalysis",
    "PlanetaryConnectionStabilityAnalysis",
    "PlanetaryGearSetStabilityAnalysis",
    "PlanetCarrierStabilityAnalysis",
    "PointLoadStabilityAnalysis",
    "PowerLoadStabilityAnalysis",
    "PulleyStabilityAnalysis",
    "RingPinsStabilityAnalysis",
    "RingPinsToDiscConnectionStabilityAnalysis",
    "RollingRingAssemblyStabilityAnalysis",
    "RollingRingConnectionStabilityAnalysis",
    "RollingRingStabilityAnalysis",
    "RootAssemblyStabilityAnalysis",
    "ShaftHubConnectionStabilityAnalysis",
    "ShaftStabilityAnalysis",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
    "SpecialisedAssemblyStabilityAnalysis",
    "SpiralBevelGearMeshStabilityAnalysis",
    "SpiralBevelGearSetStabilityAnalysis",
    "SpiralBevelGearStabilityAnalysis",
    "SpringDamperConnectionStabilityAnalysis",
    "SpringDamperHalfStabilityAnalysis",
    "SpringDamperStabilityAnalysis",
    "StabilityAnalysis",
    "StabilityAnalysisDrawStyle",
    "StabilityAnalysisOptions",
    "StraightBevelDiffGearMeshStabilityAnalysis",
    "StraightBevelDiffGearSetStabilityAnalysis",
    "StraightBevelDiffGearStabilityAnalysis",
    "StraightBevelGearMeshStabilityAnalysis",
    "StraightBevelGearSetStabilityAnalysis",
    "StraightBevelGearStabilityAnalysis",
    "StraightBevelPlanetGearStabilityAnalysis",
    "StraightBevelSunGearStabilityAnalysis",
    "SynchroniserHalfStabilityAnalysis",
    "SynchroniserPartStabilityAnalysis",
    "SynchroniserSleeveStabilityAnalysis",
    "SynchroniserStabilityAnalysis",
    "TorqueConverterConnectionStabilityAnalysis",
    "TorqueConverterPumpStabilityAnalysis",
    "TorqueConverterStabilityAnalysis",
    "TorqueConverterTurbineStabilityAnalysis",
    "UnbalancedMassStabilityAnalysis",
    "VirtualComponentStabilityAnalysis",
    "WormGearMeshStabilityAnalysis",
    "WormGearSetStabilityAnalysis",
    "WormGearStabilityAnalysis",
    "ZerolBevelGearMeshStabilityAnalysis",
    "ZerolBevelGearSetStabilityAnalysis",
    "ZerolBevelGearStabilityAnalysis",
)
