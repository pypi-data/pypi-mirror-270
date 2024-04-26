"""Database"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "Database")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1841, _1843, _1846
    from mastapy.shafts import _25, _39
    from mastapy.nodal_analysis import _49
    from mastapy.materials import _253, _256, _275, _277, _279
    from mastapy.gears import _350
    from mastapy.gears.rating.cylindrical import _460, _476
    from mastapy.gears.materials import (
        _591,
        _593,
        _595,
        _596,
        _597,
        _599,
        _600,
        _602,
        _606,
        _607,
        _614,
    )
    from mastapy.gears.manufacturing.cylindrical import _617, _622, _633
    from mastapy.gears.manufacturing.cylindrical.cutters import _712, _718, _723, _724
    from mastapy.gears.manufacturing.bevel import _807
    from mastapy.gears.gear_set_pareto_optimiser import (
        _926,
        _928,
        _929,
        _931,
        _932,
        _933,
        _934,
        _935,
        _936,
        _937,
        _938,
        _939,
        _941,
        _942,
        _943,
        _944,
    )
    from mastapy.gears.gear_designs import _948, _950, _953
    from mastapy.gears.gear_designs.cylindrical import _1023, _1029
    from mastapy.electric_machines import _1296, _1314, _1327
    from mastapy.cycloidal import _1469, _1476
    from mastapy.bolts import _1479, _1481, _1483, _1488
    from mastapy.math_utility.optimisation import _1552, _1564
    from mastapy.bearings import _1897, _1910
    from mastapy.bearings.bearing_results.rolling import _1993
    from mastapy.system_model.optimization import _2246, _2254
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2582


__docformat__ = "restructuredtext en"
__all__ = ("Database",)


Self = TypeVar("Self", bound="Database")
TKey = TypeVar("TKey", bound="_1841.DatabaseKey")
TValue = TypeVar("TValue", bound="_0.APIBase")


class Database(_0.APIBase, Generic[TKey, TValue]):
    """Database

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Database")

    class _Cast_Database:
        """Special nested class for casting Database to subclasses."""

        def __init__(self: "Database._Cast_Database", parent: "Database"):
            self._parent = parent

        @property
        def shaft_material_database(
            self: "Database._Cast_Database",
        ) -> "_25.ShaftMaterialDatabase":
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(
            self: "Database._Cast_Database",
        ) -> "_39.ShaftSettingsDatabase":
            from mastapy.shafts import _39

            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(
            self: "Database._Cast_Database",
        ) -> "_49.AnalysisSettingsDatabase":
            from mastapy.nodal_analysis import _49

            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(
            self: "Database._Cast_Database",
        ) -> "_253.BearingMaterialDatabase":
            from mastapy.materials import _253

            return self._parent._cast(_253.BearingMaterialDatabase)

        @property
        def component_material_database(
            self: "Database._Cast_Database",
        ) -> "_256.ComponentMaterialDatabase":
            from mastapy.materials import _256

            return self._parent._cast(_256.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(
            self: "Database._Cast_Database",
        ) -> "_275.LubricationDetailDatabase":
            from mastapy.materials import _275

            return self._parent._cast(_275.LubricationDetailDatabase)

        @property
        def material_database(
            self: "Database._Cast_Database",
        ) -> "_277.MaterialDatabase":
            from mastapy.materials import _277

            return self._parent._cast(_277.MaterialDatabase)

        @property
        def materials_settings_database(
            self: "Database._Cast_Database",
        ) -> "_279.MaterialsSettingsDatabase":
            from mastapy.materials import _279

            return self._parent._cast(_279.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(
            self: "Database._Cast_Database",
        ) -> "_350.PocketingPowerLossCoefficientsDatabase":
            from mastapy.gears import _350

            return self._parent._cast(_350.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "Database._Cast_Database",
        ) -> "_460.CylindricalGearDesignAndRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _460

            return self._parent._cast(
                _460.CylindricalGearDesignAndRatingSettingsDatabase
            )

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "Database._Cast_Database",
        ) -> "_476.CylindricalPlasticGearRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _476

            return self._parent._cast(_476.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "Database._Cast_Database",
        ) -> "_591.BevelGearAbstractMaterialDatabase":
            from mastapy.gears.materials import _591

            return self._parent._cast(_591.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "Database._Cast_Database",
        ) -> "_593.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(
            self: "Database._Cast_Database",
        ) -> "_595.BevelGearMaterialDatabase":
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "Database._Cast_Database",
        ) -> "_596.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "Database._Cast_Database",
        ) -> "_597.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _597

            return self._parent._cast(_597.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "Database._Cast_Database",
        ) -> "_599.CylindricalGearMaterialDatabase":
            from mastapy.gears.materials import _599

            return self._parent._cast(_599.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "Database._Cast_Database",
        ) -> "_600.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _600

            return self._parent._cast(_600.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(
            self: "Database._Cast_Database",
        ) -> "_602.GearMaterialDatabase":
            from mastapy.gears.materials import _602

            return self._parent._cast(_602.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "Database._Cast_Database",
        ) -> "_606.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
            from mastapy.gears.materials import _606

            return self._parent._cast(
                _606.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
            )

        @property
        def klingelnberg_conical_gear_material_database(
            self: "Database._Cast_Database",
        ) -> "_607.KlingelnbergConicalGearMaterialDatabase":
            from mastapy.gears.materials import _607

            return self._parent._cast(_607.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(
            self: "Database._Cast_Database",
        ) -> "_614.RawMaterialDatabase":
            from mastapy.gears.materials import _614

            return self._parent._cast(_614.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(
            self: "Database._Cast_Database",
        ) -> "_617.CylindricalCutterDatabase":
            from mastapy.gears.manufacturing.cylindrical import _617

            return self._parent._cast(_617.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(
            self: "Database._Cast_Database",
        ) -> "_622.CylindricalHobDatabase":
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "Database._Cast_Database",
        ) -> "_633.CylindricalShaperDatabase":
            from mastapy.gears.manufacturing.cylindrical import _633

            return self._parent._cast(_633.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "Database._Cast_Database",
        ) -> "_712.CylindricalFormedWheelGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _712

            return self._parent._cast(_712.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "Database._Cast_Database",
        ) -> "_718.CylindricalGearPlungeShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _718

            return self._parent._cast(_718.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "Database._Cast_Database",
        ) -> "_723.CylindricalGearShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _723

            return self._parent._cast(_723.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "Database._Cast_Database",
        ) -> "_724.CylindricalWormGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _724

            return self._parent._cast(_724.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(
            self: "Database._Cast_Database",
        ) -> "_807.ManufacturingMachineDatabase":
            from mastapy.gears.manufacturing.bevel import _807

            return self._parent._cast(_807.ManufacturingMachineDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_926.MicroGeometryDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_928.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_929.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_931.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_932.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_933.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _933

            return self._parent._cast(
                _933.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_934.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_935.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_936.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_937.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(_937.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_938.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _938

            return self._parent._cast(
                _938.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_939.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _939

            return self._parent._cast(
                _939.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_941.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _941

            return self._parent._cast(
                _941.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_942.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _942

            return self._parent._cast(
                _942.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_943.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _943

            return self._parent._cast(
                _943.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_944.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _944

            return self._parent._cast(
                _944.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def bevel_hypoid_gear_design_settings_database(
            self: "Database._Cast_Database",
        ) -> "_948.BevelHypoidGearDesignSettingsDatabase":
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(
            self: "Database._Cast_Database",
        ) -> "_950.BevelHypoidGearRatingSettingsDatabase":
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(
            self: "Database._Cast_Database",
        ) -> "_953.DesignConstraintCollectionDatabase":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "Database._Cast_Database",
        ) -> "_1023.CylindricalGearDesignConstraintsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1023

            return self._parent._cast(_1023.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "Database._Cast_Database",
        ) -> "_1029.CylindricalGearMicroGeometrySettingsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1029

            return self._parent._cast(
                _1029.CylindricalGearMicroGeometrySettingsDatabase
            )

        @property
        def magnet_material_database(
            self: "Database._Cast_Database",
        ) -> "_1296.MagnetMaterialDatabase":
            from mastapy.electric_machines import _1296

            return self._parent._cast(_1296.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "Database._Cast_Database",
        ) -> "_1314.StatorRotorMaterialDatabase":
            from mastapy.electric_machines import _1314

            return self._parent._cast(_1314.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(
            self: "Database._Cast_Database",
        ) -> "_1327.WindingMaterialDatabase":
            from mastapy.electric_machines import _1327

            return self._parent._cast(_1327.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "Database._Cast_Database",
        ) -> "_1469.CycloidalDiscMaterialDatabase":
            from mastapy.cycloidal import _1469

            return self._parent._cast(_1469.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "Database._Cast_Database",
        ) -> "_1476.RingPinsMaterialDatabase":
            from mastapy.cycloidal import _1476

            return self._parent._cast(_1476.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(
            self: "Database._Cast_Database",
        ) -> "_1479.BoltedJointMaterialDatabase":
            from mastapy.bolts import _1479

            return self._parent._cast(_1479.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(
            self: "Database._Cast_Database",
        ) -> "_1481.BoltGeometryDatabase":
            from mastapy.bolts import _1481

            return self._parent._cast(_1481.BoltGeometryDatabase)

        @property
        def bolt_material_database(
            self: "Database._Cast_Database",
        ) -> "_1483.BoltMaterialDatabase":
            from mastapy.bolts import _1483

            return self._parent._cast(_1483.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(
            self: "Database._Cast_Database",
        ) -> "_1488.ClampedSectionMaterialDatabase":
            from mastapy.bolts import _1488

            return self._parent._cast(_1488.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_1552.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.DesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_1564.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1564

            return self._parent._cast(_1564.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(self: "Database._Cast_Database") -> "_1843.NamedDatabase":
            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(self: "Database._Cast_Database") -> "_1846.SQLDatabase":
            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def bearing_settings_database(
            self: "Database._Cast_Database",
        ) -> "_1897.BearingSettingsDatabase":
            from mastapy.bearings import _1897

            return self._parent._cast(_1897.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(
            self: "Database._Cast_Database",
        ) -> "_1910.RollingBearingDatabase":
            from mastapy.bearings import _1910

            return self._parent._cast(_1910.RollingBearingDatabase)

        @property
        def iso14179_settings_database(
            self: "Database._Cast_Database",
        ) -> "_1993.ISO14179SettingsDatabase":
            from mastapy.bearings.bearing_results.rolling import _1993

            return self._parent._cast(_1993.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_2246.ConicalGearOptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2246

            return self._parent._cast(_2246.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(
            self: "Database._Cast_Database",
        ) -> "_2254.OptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2254

            return self._parent._cast(_2254.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(
            self: "Database._Cast_Database",
        ) -> "_2582.SuperchargerRotorSetDatabase":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2582,
            )

            return self._parent._cast(_2582.SuperchargerRotorSetDatabase)

        @property
        def database(self: "Database._Cast_Database") -> "Database":
            return self._parent

        def __getattr__(self: "Database._Cast_Database", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Database.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def count(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Count

        if temp is None:
            return 0

        return temp

    @enforce_parameter_types
    def can_be_removed(self: Self, item: "TValue") -> "bool":
        """bool

        Args:
            item (TValue)
        """
        method_result = self.wrapped.CanBeRemoved(item)
        return method_result

    def get_all_items(self: Self) -> "List[TValue]":
        """List[TValue]"""
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetAllItems())

    @property
    def cast_to(self: Self) -> "Database._Cast_Database":
        return self._Cast_Database(self)
