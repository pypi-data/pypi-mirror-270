"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6830 import LoadCase
    from ._6831 import StaticLoadCase
    from ._6832 import TimeSeriesLoadCase
    from ._6833 import AbstractAssemblyLoadCase
    from ._6834 import AbstractShaftLoadCase
    from ._6835 import AbstractShaftOrHousingLoadCase
    from ._6836 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6837 import AdditionalAccelerationOptions
    from ._6838 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6839 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6840 import AGMAGleasonConicalGearLoadCase
    from ._6841 import AGMAGleasonConicalGearMeshLoadCase
    from ._6842 import AGMAGleasonConicalGearSetLoadCase
    from ._6843 import AllRingPinsManufacturingError
    from ._6844 import AnalysisType
    from ._6845 import AssemblyLoadCase
    from ._6846 import BearingLoadCase
    from ._6847 import BeltConnectionLoadCase
    from ._6848 import BeltDriveLoadCase
    from ._6849 import BevelDifferentialGearLoadCase
    from ._6850 import BevelDifferentialGearMeshLoadCase
    from ._6851 import BevelDifferentialGearSetLoadCase
    from ._6852 import BevelDifferentialPlanetGearLoadCase
    from ._6853 import BevelDifferentialSunGearLoadCase
    from ._6854 import BevelGearLoadCase
    from ._6855 import BevelGearMeshLoadCase
    from ._6856 import BevelGearSetLoadCase
    from ._6857 import BoltedJointLoadCase
    from ._6858 import BoltLoadCase
    from ._6859 import ClutchConnectionLoadCase
    from ._6860 import ClutchHalfLoadCase
    from ._6861 import ClutchLoadCase
    from ._6862 import CMSElementFaceGroupWithSelectionOption
    from ._6863 import CoaxialConnectionLoadCase
    from ._6864 import ComponentLoadCase
    from ._6865 import ConceptCouplingConnectionLoadCase
    from ._6866 import ConceptCouplingHalfLoadCase
    from ._6867 import ConceptCouplingLoadCase
    from ._6868 import ConceptGearLoadCase
    from ._6869 import ConceptGearMeshLoadCase
    from ._6870 import ConceptGearSetLoadCase
    from ._6871 import ConicalGearLoadCase
    from ._6872 import ConicalGearManufactureError
    from ._6873 import ConicalGearMeshLoadCase
    from ._6874 import ConicalGearSetHarmonicLoadData
    from ._6875 import ConicalGearSetLoadCase
    from ._6876 import ConnectionLoadCase
    from ._6877 import ConnectorLoadCase
    from ._6878 import CouplingConnectionLoadCase
    from ._6879 import CouplingHalfLoadCase
    from ._6880 import CouplingLoadCase
    from ._6881 import CVTBeltConnectionLoadCase
    from ._6882 import CVTLoadCase
    from ._6883 import CVTPulleyLoadCase
    from ._6884 import CycloidalAssemblyLoadCase
    from ._6885 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6886 import CycloidalDiscLoadCase
    from ._6887 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6888 import CylindricalGearLoadCase
    from ._6889 import CylindricalGearManufactureError
    from ._6890 import CylindricalGearMeshLoadCase
    from ._6891 import CylindricalGearSetHarmonicLoadData
    from ._6892 import CylindricalGearSetLoadCase
    from ._6893 import CylindricalPlanetGearLoadCase
    from ._6894 import DataFromMotorPackagePerMeanTorque
    from ._6895 import DataFromMotorPackagePerSpeed
    from ._6896 import DatumLoadCase
    from ._6897 import ElectricMachineDataImportType
    from ._6898 import ElectricMachineHarmonicLoadData
    from ._6899 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6900 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6901 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6902 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6903 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6904 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6905 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6906 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6907 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6908 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6909 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6910 import ExternalCADModelLoadCase
    from ._6911 import FaceGearLoadCase
    from ._6912 import FaceGearMeshLoadCase
    from ._6913 import FaceGearSetLoadCase
    from ._6914 import FEPartLoadCase
    from ._6915 import FlexiblePinAssemblyLoadCase
    from ._6916 import ForceAndTorqueScalingFactor
    from ._6917 import GearLoadCase
    from ._6918 import GearManufactureError
    from ._6919 import GearMeshLoadCase
    from ._6920 import GearMeshTEOrderType
    from ._6921 import GearSetHarmonicLoadData
    from ._6922 import GearSetLoadCase
    from ._6923 import GuideDxfModelLoadCase
    from ._6924 import HarmonicExcitationType
    from ._6925 import HarmonicLoadDataCSVImport
    from ._6926 import HarmonicLoadDataExcelImport
    from ._6927 import HarmonicLoadDataFluxImport
    from ._6928 import HarmonicLoadDataImportBase
    from ._6929 import HarmonicLoadDataImportFromMotorPackages
    from ._6930 import HarmonicLoadDataJMAGImport
    from ._6931 import HarmonicLoadDataMotorCADImport
    from ._6932 import HypoidGearLoadCase
    from ._6933 import HypoidGearMeshLoadCase
    from ._6934 import HypoidGearSetLoadCase
    from ._6935 import ImportType
    from ._6936 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6937 import InnerDiameterReference
    from ._6938 import InterMountableComponentConnectionLoadCase
    from ._6939 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6940 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6941 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6942 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6943 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6944 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6945 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6946 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6947 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6948 import MassDiscLoadCase
    from ._6949 import MeasurementComponentLoadCase
    from ._6950 import MeshStiffnessSource
    from ._6951 import MountableComponentLoadCase
    from ._6952 import NamedSpeed
    from ._6953 import OilSealLoadCase
    from ._6954 import ParametricStudyType
    from ._6955 import PartLoadCase
    from ._6956 import PartToPartShearCouplingConnectionLoadCase
    from ._6957 import PartToPartShearCouplingHalfLoadCase
    from ._6958 import PartToPartShearCouplingLoadCase
    from ._6959 import PlanetaryConnectionLoadCase
    from ._6960 import PlanetaryGearSetLoadCase
    from ._6961 import PlanetarySocketManufactureError
    from ._6962 import PlanetCarrierLoadCase
    from ._6963 import PlanetManufactureError
    from ._6964 import PointLoadHarmonicLoadData
    from ._6965 import PointLoadLoadCase
    from ._6966 import PowerLoadLoadCase
    from ._6967 import PulleyLoadCase
    from ._6968 import ResetMicroGeometryOptions
    from ._6969 import RingPinManufacturingError
    from ._6970 import RingPinsLoadCase
    from ._6971 import RingPinsToDiscConnectionLoadCase
    from ._6972 import RollingRingAssemblyLoadCase
    from ._6973 import RollingRingConnectionLoadCase
    from ._6974 import RollingRingLoadCase
    from ._6975 import RootAssemblyLoadCase
    from ._6976 import ShaftHubConnectionLoadCase
    from ._6977 import ShaftLoadCase
    from ._6978 import ShaftToMountableComponentConnectionLoadCase
    from ._6979 import SpecialisedAssemblyLoadCase
    from ._6980 import SpiralBevelGearLoadCase
    from ._6981 import SpiralBevelGearMeshLoadCase
    from ._6982 import SpiralBevelGearSetLoadCase
    from ._6983 import SpringDamperConnectionLoadCase
    from ._6984 import SpringDamperHalfLoadCase
    from ._6985 import SpringDamperLoadCase
    from ._6986 import StraightBevelDiffGearLoadCase
    from ._6987 import StraightBevelDiffGearMeshLoadCase
    from ._6988 import StraightBevelDiffGearSetLoadCase
    from ._6989 import StraightBevelGearLoadCase
    from ._6990 import StraightBevelGearMeshLoadCase
    from ._6991 import StraightBevelGearSetLoadCase
    from ._6992 import StraightBevelPlanetGearLoadCase
    from ._6993 import StraightBevelSunGearLoadCase
    from ._6994 import SynchroniserHalfLoadCase
    from ._6995 import SynchroniserLoadCase
    from ._6996 import SynchroniserPartLoadCase
    from ._6997 import SynchroniserSleeveLoadCase
    from ._6998 import TEExcitationType
    from ._6999 import TorqueConverterConnectionLoadCase
    from ._7000 import TorqueConverterLoadCase
    from ._7001 import TorqueConverterPumpLoadCase
    from ._7002 import TorqueConverterTurbineLoadCase
    from ._7003 import TorqueRippleInputType
    from ._7004 import TorqueSpecificationForSystemDeflection
    from ._7005 import TransmissionEfficiencySettings
    from ._7006 import UnbalancedMassHarmonicLoadData
    from ._7007 import UnbalancedMassLoadCase
    from ._7008 import VirtualComponentLoadCase
    from ._7009 import WormGearLoadCase
    from ._7010 import WormGearMeshLoadCase
    from ._7011 import WormGearSetLoadCase
    from ._7012 import ZerolBevelGearLoadCase
    from ._7013 import ZerolBevelGearMeshLoadCase
    from ._7014 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6830": ["LoadCase"],
        "_6831": ["StaticLoadCase"],
        "_6832": ["TimeSeriesLoadCase"],
        "_6833": ["AbstractAssemblyLoadCase"],
        "_6834": ["AbstractShaftLoadCase"],
        "_6835": ["AbstractShaftOrHousingLoadCase"],
        "_6836": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6837": ["AdditionalAccelerationOptions"],
        "_6838": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6839": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6840": ["AGMAGleasonConicalGearLoadCase"],
        "_6841": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6842": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6843": ["AllRingPinsManufacturingError"],
        "_6844": ["AnalysisType"],
        "_6845": ["AssemblyLoadCase"],
        "_6846": ["BearingLoadCase"],
        "_6847": ["BeltConnectionLoadCase"],
        "_6848": ["BeltDriveLoadCase"],
        "_6849": ["BevelDifferentialGearLoadCase"],
        "_6850": ["BevelDifferentialGearMeshLoadCase"],
        "_6851": ["BevelDifferentialGearSetLoadCase"],
        "_6852": ["BevelDifferentialPlanetGearLoadCase"],
        "_6853": ["BevelDifferentialSunGearLoadCase"],
        "_6854": ["BevelGearLoadCase"],
        "_6855": ["BevelGearMeshLoadCase"],
        "_6856": ["BevelGearSetLoadCase"],
        "_6857": ["BoltedJointLoadCase"],
        "_6858": ["BoltLoadCase"],
        "_6859": ["ClutchConnectionLoadCase"],
        "_6860": ["ClutchHalfLoadCase"],
        "_6861": ["ClutchLoadCase"],
        "_6862": ["CMSElementFaceGroupWithSelectionOption"],
        "_6863": ["CoaxialConnectionLoadCase"],
        "_6864": ["ComponentLoadCase"],
        "_6865": ["ConceptCouplingConnectionLoadCase"],
        "_6866": ["ConceptCouplingHalfLoadCase"],
        "_6867": ["ConceptCouplingLoadCase"],
        "_6868": ["ConceptGearLoadCase"],
        "_6869": ["ConceptGearMeshLoadCase"],
        "_6870": ["ConceptGearSetLoadCase"],
        "_6871": ["ConicalGearLoadCase"],
        "_6872": ["ConicalGearManufactureError"],
        "_6873": ["ConicalGearMeshLoadCase"],
        "_6874": ["ConicalGearSetHarmonicLoadData"],
        "_6875": ["ConicalGearSetLoadCase"],
        "_6876": ["ConnectionLoadCase"],
        "_6877": ["ConnectorLoadCase"],
        "_6878": ["CouplingConnectionLoadCase"],
        "_6879": ["CouplingHalfLoadCase"],
        "_6880": ["CouplingLoadCase"],
        "_6881": ["CVTBeltConnectionLoadCase"],
        "_6882": ["CVTLoadCase"],
        "_6883": ["CVTPulleyLoadCase"],
        "_6884": ["CycloidalAssemblyLoadCase"],
        "_6885": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6886": ["CycloidalDiscLoadCase"],
        "_6887": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6888": ["CylindricalGearLoadCase"],
        "_6889": ["CylindricalGearManufactureError"],
        "_6890": ["CylindricalGearMeshLoadCase"],
        "_6891": ["CylindricalGearSetHarmonicLoadData"],
        "_6892": ["CylindricalGearSetLoadCase"],
        "_6893": ["CylindricalPlanetGearLoadCase"],
        "_6894": ["DataFromMotorPackagePerMeanTorque"],
        "_6895": ["DataFromMotorPackagePerSpeed"],
        "_6896": ["DatumLoadCase"],
        "_6897": ["ElectricMachineDataImportType"],
        "_6898": ["ElectricMachineHarmonicLoadData"],
        "_6899": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6900": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6901": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6902": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6903": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6904": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6905": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6906": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6907": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6908": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6909": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6910": ["ExternalCADModelLoadCase"],
        "_6911": ["FaceGearLoadCase"],
        "_6912": ["FaceGearMeshLoadCase"],
        "_6913": ["FaceGearSetLoadCase"],
        "_6914": ["FEPartLoadCase"],
        "_6915": ["FlexiblePinAssemblyLoadCase"],
        "_6916": ["ForceAndTorqueScalingFactor"],
        "_6917": ["GearLoadCase"],
        "_6918": ["GearManufactureError"],
        "_6919": ["GearMeshLoadCase"],
        "_6920": ["GearMeshTEOrderType"],
        "_6921": ["GearSetHarmonicLoadData"],
        "_6922": ["GearSetLoadCase"],
        "_6923": ["GuideDxfModelLoadCase"],
        "_6924": ["HarmonicExcitationType"],
        "_6925": ["HarmonicLoadDataCSVImport"],
        "_6926": ["HarmonicLoadDataExcelImport"],
        "_6927": ["HarmonicLoadDataFluxImport"],
        "_6928": ["HarmonicLoadDataImportBase"],
        "_6929": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6930": ["HarmonicLoadDataJMAGImport"],
        "_6931": ["HarmonicLoadDataMotorCADImport"],
        "_6932": ["HypoidGearLoadCase"],
        "_6933": ["HypoidGearMeshLoadCase"],
        "_6934": ["HypoidGearSetLoadCase"],
        "_6935": ["ImportType"],
        "_6936": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6937": ["InnerDiameterReference"],
        "_6938": ["InterMountableComponentConnectionLoadCase"],
        "_6939": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6940": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6941": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6942": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6943": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6944": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6945": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6946": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6947": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6948": ["MassDiscLoadCase"],
        "_6949": ["MeasurementComponentLoadCase"],
        "_6950": ["MeshStiffnessSource"],
        "_6951": ["MountableComponentLoadCase"],
        "_6952": ["NamedSpeed"],
        "_6953": ["OilSealLoadCase"],
        "_6954": ["ParametricStudyType"],
        "_6955": ["PartLoadCase"],
        "_6956": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6957": ["PartToPartShearCouplingHalfLoadCase"],
        "_6958": ["PartToPartShearCouplingLoadCase"],
        "_6959": ["PlanetaryConnectionLoadCase"],
        "_6960": ["PlanetaryGearSetLoadCase"],
        "_6961": ["PlanetarySocketManufactureError"],
        "_6962": ["PlanetCarrierLoadCase"],
        "_6963": ["PlanetManufactureError"],
        "_6964": ["PointLoadHarmonicLoadData"],
        "_6965": ["PointLoadLoadCase"],
        "_6966": ["PowerLoadLoadCase"],
        "_6967": ["PulleyLoadCase"],
        "_6968": ["ResetMicroGeometryOptions"],
        "_6969": ["RingPinManufacturingError"],
        "_6970": ["RingPinsLoadCase"],
        "_6971": ["RingPinsToDiscConnectionLoadCase"],
        "_6972": ["RollingRingAssemblyLoadCase"],
        "_6973": ["RollingRingConnectionLoadCase"],
        "_6974": ["RollingRingLoadCase"],
        "_6975": ["RootAssemblyLoadCase"],
        "_6976": ["ShaftHubConnectionLoadCase"],
        "_6977": ["ShaftLoadCase"],
        "_6978": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6979": ["SpecialisedAssemblyLoadCase"],
        "_6980": ["SpiralBevelGearLoadCase"],
        "_6981": ["SpiralBevelGearMeshLoadCase"],
        "_6982": ["SpiralBevelGearSetLoadCase"],
        "_6983": ["SpringDamperConnectionLoadCase"],
        "_6984": ["SpringDamperHalfLoadCase"],
        "_6985": ["SpringDamperLoadCase"],
        "_6986": ["StraightBevelDiffGearLoadCase"],
        "_6987": ["StraightBevelDiffGearMeshLoadCase"],
        "_6988": ["StraightBevelDiffGearSetLoadCase"],
        "_6989": ["StraightBevelGearLoadCase"],
        "_6990": ["StraightBevelGearMeshLoadCase"],
        "_6991": ["StraightBevelGearSetLoadCase"],
        "_6992": ["StraightBevelPlanetGearLoadCase"],
        "_6993": ["StraightBevelSunGearLoadCase"],
        "_6994": ["SynchroniserHalfLoadCase"],
        "_6995": ["SynchroniserLoadCase"],
        "_6996": ["SynchroniserPartLoadCase"],
        "_6997": ["SynchroniserSleeveLoadCase"],
        "_6998": ["TEExcitationType"],
        "_6999": ["TorqueConverterConnectionLoadCase"],
        "_7000": ["TorqueConverterLoadCase"],
        "_7001": ["TorqueConverterPumpLoadCase"],
        "_7002": ["TorqueConverterTurbineLoadCase"],
        "_7003": ["TorqueRippleInputType"],
        "_7004": ["TorqueSpecificationForSystemDeflection"],
        "_7005": ["TransmissionEfficiencySettings"],
        "_7006": ["UnbalancedMassHarmonicLoadData"],
        "_7007": ["UnbalancedMassLoadCase"],
        "_7008": ["VirtualComponentLoadCase"],
        "_7009": ["WormGearLoadCase"],
        "_7010": ["WormGearMeshLoadCase"],
        "_7011": ["WormGearSetLoadCase"],
        "_7012": ["ZerolBevelGearLoadCase"],
        "_7013": ["ZerolBevelGearMeshLoadCase"],
        "_7014": ["ZerolBevelGearSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LoadCase",
    "StaticLoadCase",
    "TimeSeriesLoadCase",
    "AbstractAssemblyLoadCase",
    "AbstractShaftLoadCase",
    "AbstractShaftOrHousingLoadCase",
    "AbstractShaftToMountableComponentConnectionLoadCase",
    "AdditionalAccelerationOptions",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    "AdvancedTimeSteppingAnalysisForModulationType",
    "AGMAGleasonConicalGearLoadCase",
    "AGMAGleasonConicalGearMeshLoadCase",
    "AGMAGleasonConicalGearSetLoadCase",
    "AllRingPinsManufacturingError",
    "AnalysisType",
    "AssemblyLoadCase",
    "BearingLoadCase",
    "BeltConnectionLoadCase",
    "BeltDriveLoadCase",
    "BevelDifferentialGearLoadCase",
    "BevelDifferentialGearMeshLoadCase",
    "BevelDifferentialGearSetLoadCase",
    "BevelDifferentialPlanetGearLoadCase",
    "BevelDifferentialSunGearLoadCase",
    "BevelGearLoadCase",
    "BevelGearMeshLoadCase",
    "BevelGearSetLoadCase",
    "BoltedJointLoadCase",
    "BoltLoadCase",
    "ClutchConnectionLoadCase",
    "ClutchHalfLoadCase",
    "ClutchLoadCase",
    "CMSElementFaceGroupWithSelectionOption",
    "CoaxialConnectionLoadCase",
    "ComponentLoadCase",
    "ConceptCouplingConnectionLoadCase",
    "ConceptCouplingHalfLoadCase",
    "ConceptCouplingLoadCase",
    "ConceptGearLoadCase",
    "ConceptGearMeshLoadCase",
    "ConceptGearSetLoadCase",
    "ConicalGearLoadCase",
    "ConicalGearManufactureError",
    "ConicalGearMeshLoadCase",
    "ConicalGearSetHarmonicLoadData",
    "ConicalGearSetLoadCase",
    "ConnectionLoadCase",
    "ConnectorLoadCase",
    "CouplingConnectionLoadCase",
    "CouplingHalfLoadCase",
    "CouplingLoadCase",
    "CVTBeltConnectionLoadCase",
    "CVTLoadCase",
    "CVTPulleyLoadCase",
    "CycloidalAssemblyLoadCase",
    "CycloidalDiscCentralBearingConnectionLoadCase",
    "CycloidalDiscLoadCase",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
    "CylindricalGearLoadCase",
    "CylindricalGearManufactureError",
    "CylindricalGearMeshLoadCase",
    "CylindricalGearSetHarmonicLoadData",
    "CylindricalGearSetLoadCase",
    "CylindricalPlanetGearLoadCase",
    "DataFromMotorPackagePerMeanTorque",
    "DataFromMotorPackagePerSpeed",
    "DatumLoadCase",
    "ElectricMachineDataImportType",
    "ElectricMachineHarmonicLoadData",
    "ElectricMachineHarmonicLoadDataFromExcel",
    "ElectricMachineHarmonicLoadDataFromFlux",
    "ElectricMachineHarmonicLoadDataFromJMAG",
    "ElectricMachineHarmonicLoadDataFromMASTA",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
    "ElectricMachineHarmonicLoadExcelImportOptions",
    "ElectricMachineHarmonicLoadFluxImportOptions",
    "ElectricMachineHarmonicLoadImportOptionsBase",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
    "ExternalCADModelLoadCase",
    "FaceGearLoadCase",
    "FaceGearMeshLoadCase",
    "FaceGearSetLoadCase",
    "FEPartLoadCase",
    "FlexiblePinAssemblyLoadCase",
    "ForceAndTorqueScalingFactor",
    "GearLoadCase",
    "GearManufactureError",
    "GearMeshLoadCase",
    "GearMeshTEOrderType",
    "GearSetHarmonicLoadData",
    "GearSetLoadCase",
    "GuideDxfModelLoadCase",
    "HarmonicExcitationType",
    "HarmonicLoadDataCSVImport",
    "HarmonicLoadDataExcelImport",
    "HarmonicLoadDataFluxImport",
    "HarmonicLoadDataImportBase",
    "HarmonicLoadDataImportFromMotorPackages",
    "HarmonicLoadDataJMAGImport",
    "HarmonicLoadDataMotorCADImport",
    "HypoidGearLoadCase",
    "HypoidGearMeshLoadCase",
    "HypoidGearSetLoadCase",
    "ImportType",
    "InformationAtRingPinToDiscContactPointFromGeometry",
    "InnerDiameterReference",
    "InterMountableComponentConnectionLoadCase",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    "MassDiscLoadCase",
    "MeasurementComponentLoadCase",
    "MeshStiffnessSource",
    "MountableComponentLoadCase",
    "NamedSpeed",
    "OilSealLoadCase",
    "ParametricStudyType",
    "PartLoadCase",
    "PartToPartShearCouplingConnectionLoadCase",
    "PartToPartShearCouplingHalfLoadCase",
    "PartToPartShearCouplingLoadCase",
    "PlanetaryConnectionLoadCase",
    "PlanetaryGearSetLoadCase",
    "PlanetarySocketManufactureError",
    "PlanetCarrierLoadCase",
    "PlanetManufactureError",
    "PointLoadHarmonicLoadData",
    "PointLoadLoadCase",
    "PowerLoadLoadCase",
    "PulleyLoadCase",
    "ResetMicroGeometryOptions",
    "RingPinManufacturingError",
    "RingPinsLoadCase",
    "RingPinsToDiscConnectionLoadCase",
    "RollingRingAssemblyLoadCase",
    "RollingRingConnectionLoadCase",
    "RollingRingLoadCase",
    "RootAssemblyLoadCase",
    "ShaftHubConnectionLoadCase",
    "ShaftLoadCase",
    "ShaftToMountableComponentConnectionLoadCase",
    "SpecialisedAssemblyLoadCase",
    "SpiralBevelGearLoadCase",
    "SpiralBevelGearMeshLoadCase",
    "SpiralBevelGearSetLoadCase",
    "SpringDamperConnectionLoadCase",
    "SpringDamperHalfLoadCase",
    "SpringDamperLoadCase",
    "StraightBevelDiffGearLoadCase",
    "StraightBevelDiffGearMeshLoadCase",
    "StraightBevelDiffGearSetLoadCase",
    "StraightBevelGearLoadCase",
    "StraightBevelGearMeshLoadCase",
    "StraightBevelGearSetLoadCase",
    "StraightBevelPlanetGearLoadCase",
    "StraightBevelSunGearLoadCase",
    "SynchroniserHalfLoadCase",
    "SynchroniserLoadCase",
    "SynchroniserPartLoadCase",
    "SynchroniserSleeveLoadCase",
    "TEExcitationType",
    "TorqueConverterConnectionLoadCase",
    "TorqueConverterLoadCase",
    "TorqueConverterPumpLoadCase",
    "TorqueConverterTurbineLoadCase",
    "TorqueRippleInputType",
    "TorqueSpecificationForSystemDeflection",
    "TransmissionEfficiencySettings",
    "UnbalancedMassHarmonicLoadData",
    "UnbalancedMassLoadCase",
    "VirtualComponentLoadCase",
    "WormGearLoadCase",
    "WormGearMeshLoadCase",
    "WormGearSetLoadCase",
    "ZerolBevelGearLoadCase",
    "ZerolBevelGearMeshLoadCase",
    "ZerolBevelGearSetLoadCase",
)
