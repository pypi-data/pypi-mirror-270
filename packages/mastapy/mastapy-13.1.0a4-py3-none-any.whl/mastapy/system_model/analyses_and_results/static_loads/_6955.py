"""PartLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6924, _6831
from mastapy.system_model.analyses_and_results import _2680
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2486
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6832,
        _6833,
        _6834,
        _6835,
        _6840,
        _6842,
        _6845,
        _6846,
        _6848,
        _6849,
        _6851,
        _6852,
        _6853,
        _6854,
        _6856,
        _6857,
        _6858,
        _6860,
        _6861,
        _6864,
        _6866,
        _6867,
        _6868,
        _6870,
        _6871,
        _6875,
        _6877,
        _6879,
        _6880,
        _6882,
        _6883,
        _6884,
        _6886,
        _6888,
        _6892,
        _6893,
        _6896,
        _6910,
        _6911,
        _6913,
        _6914,
        _6915,
        _6917,
        _6922,
        _6923,
        _6932,
        _6934,
        _6939,
        _6941,
        _6942,
        _6944,
        _6945,
        _6947,
        _6948,
        _6949,
        _6951,
        _6953,
        _6957,
        _6958,
        _6960,
        _6962,
        _6965,
        _6966,
        _6967,
        _6970,
        _6972,
        _6974,
        _6975,
        _6976,
        _6977,
        _6979,
        _6980,
        _6982,
        _6984,
        _6985,
        _6986,
        _6988,
        _6989,
        _6991,
        _6992,
        _6993,
        _6994,
        _6995,
        _6996,
        _6997,
        _7000,
        _7001,
        _7002,
        _7007,
        _7008,
        _7009,
        _7011,
        _7012,
        _7014,
    )
    from mastapy.electric_machines.harmonic_load_data import _1392
    from mastapy.system_model.analyses_and_results import _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartLoadCase",)


Self = TypeVar("Self", bound="PartLoadCase")


class PartLoadCase(_2680.PartAnalysis):
    """PartLoadCase

    This is a mastapy class.
    """

    TYPE = _PART_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartLoadCase")

    class _Cast_PartLoadCase:
        """Special nested class for casting PartLoadCase to subclasses."""

        def __init__(self: "PartLoadCase._Cast_PartLoadCase", parent: "PartLoadCase"):
            self._parent = parent

        @property
        def part_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2680.PartAnalysis":
            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def abstract_shaft_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6834.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6835.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6840.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AGMAGleasonConicalGearLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6842.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6845.AssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.AssemblyLoadCase)

        @property
        def bearing_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6846.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.BearingLoadCase)

        @property
        def belt_drive_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6848.BeltDriveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6849.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6851.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6852.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6853.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6854.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.BevelGearLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6856.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6857.BoltedJointLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.BoltedJointLoadCase)

        @property
        def bolt_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6858.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6860.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.ClutchHalfLoadCase)

        @property
        def clutch_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6861.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6861

            return self._parent._cast(_6861.ClutchLoadCase)

        @property
        def component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6866.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConceptCouplingHalfLoadCase)

        @property
        def concept_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6867.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6867

            return self._parent._cast(_6867.ConceptCouplingLoadCase)

        @property
        def concept_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6868.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConceptGearLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6870.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.ConceptGearSetLoadCase)

        @property
        def conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6871.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConicalGearLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6875.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ConicalGearSetLoadCase)

        @property
        def connector_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6877.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6877

            return self._parent._cast(_6877.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6879.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6879

            return self._parent._cast(_6879.CouplingHalfLoadCase)

        @property
        def coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6880.CouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6880

            return self._parent._cast(_6880.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6882.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.CVTLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6883.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.CVTPulleyLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6884.CycloidalAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6884

            return self._parent._cast(_6884.CycloidalAssemblyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6886.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6888.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.CylindricalGearLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6892.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.CylindricalGearSetLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6893.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6896.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6896

            return self._parent._cast(_6896.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6910.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6911.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.FaceGearLoadCase)

        @property
        def face_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6913.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.FaceGearSetLoadCase)

        @property
        def fe_part_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6914.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.FEPartLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6915.FlexiblePinAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.FlexiblePinAssemblyLoadCase)

        @property
        def gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6917.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(_6917.GearLoadCase)

        @property
        def gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6922.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(_6922.GearSetLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6923.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(_6923.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6932.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.HypoidGearLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6934.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(
                _6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(
                _6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6947.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(
                _6947.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6948.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6949.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6953.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6957.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.PartToPartShearCouplingHalfLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6958.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6960.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.PlanetaryGearSetLoadCase)

        @property
        def planet_carrier_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6962.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6965.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6966.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6967.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6970.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.RingPinsLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6972.RollingRingAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.RollingRingAssemblyLoadCase)

        @property
        def rolling_ring_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6974.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.RollingRingLoadCase)

        @property
        def root_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6975.RootAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.RootAssemblyLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6976.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6977.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.ShaftLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6979.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6979

            return self._parent._cast(_6979.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6980.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.SpiralBevelGearLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6982.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6984.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.SpringDamperHalfLoadCase)

        @property
        def spring_damper_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6985.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6986.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6988.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6989.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.StraightBevelGearLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6991.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.StraightBevelGearSetLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6992.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6993.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6994.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.SynchroniserHalfLoadCase)

        @property
        def synchroniser_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6995.SynchroniserLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.SynchroniserLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6996.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_6997.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7000.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7000

            return self._parent._cast(_7000.TorqueConverterLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7001.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7001

            return self._parent._cast(_7001.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7002.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7002

            return self._parent._cast(_7002.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7007.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7008.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7008

            return self._parent._cast(_7008.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7009.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.WormGearLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7011.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7011

            return self._parent._cast(_7011.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7012.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7012

            return self._parent._cast(_7012.ZerolBevelGearLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "PartLoadCase._Cast_PartLoadCase",
        ) -> "_7014.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7014

            return self._parent._cast(_7014.ZerolBevelGearSetLoadCase)

        @property
        def part_load_case(self: "PartLoadCase._Cast_PartLoadCase") -> "PartLoadCase":
            return self._parent

        def __getattr__(self: "PartLoadCase._Cast_PartLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def harmonic_excitation_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType]"""
        temp = self.wrapped.HarmonicExcitationType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @harmonic_excitation_type.setter
    @enforce_parameter_types
    def harmonic_excitation_type(self: Self, value: "_6924.HarmonicExcitationType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HarmonicExcitationType = value

    @property
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = (
            self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "_6831.StaticLoadCase"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            value
        )

    @property
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp
        )

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: Self, value: "bool"
    ):
        self.wrapped.UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp = (
            bool(value) if value is not None else False
        )

    @property
    def component_design(self: Self) -> "_2486.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_load_case(self: Self) -> "_6831.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6832.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_this_load_case(self: Self):
        """Method does not return."""
        self.wrapped.ClearUserSpecifiedExcitationDataForThisLoadCase()

    def get_harmonic_load_data_for_import(self: Self) -> "_1392.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartLoadCase._Cast_PartLoadCase":
        return self._Cast_PartLoadCase(self)
