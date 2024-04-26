"""NamedDatabaseItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DATABASE_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Databases", "NamedDatabaseItem"
)

if TYPE_CHECKING:
    from mastapy.utility import _1595
    from mastapy.utility.databases import _1845
    from mastapy.shafts import _24, _40, _43
    from mastapy.nodal_analysis import _50
    from mastapy.materials import _252, _274, _276, _280
    from mastapy.gears import _349
    from mastapy.gears.rating.cylindrical import _461, _477
    from mastapy.gears.materials import (
        _590,
        _592,
        _594,
        _598,
        _601,
        _604,
        _605,
        _608,
        _610,
        _613,
    )
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _713,
        _714,
        _715,
        _716,
        _717,
        _719,
        _720,
        _721,
        _722,
        _725,
    )
    from mastapy.gears.manufacturing.bevel import _806
    from mastapy.gears.gear_designs import _949, _951, _954
    from mastapy.gears.gear_designs.cylindrical import _1022, _1030
    from mastapy.electric_machines import _1295, _1313, _1326
    from mastapy.detailed_rigid_connectors.splines import _1428
    from mastapy.cycloidal import _1468, _1475
    from mastapy.bolts import _1478, _1480, _1482
    from mastapy.math_utility.optimisation import _1561
    from mastapy.bearings import _1898
    from mastapy.bearings.bearing_results.rolling import _1992
    from mastapy.system_model.optimization import _2244, _2247, _2252, _2253
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2581


__docformat__ = "restructuredtext en"
__all__ = ("NamedDatabaseItem",)


Self = TypeVar("Self", bound="NamedDatabaseItem")


class NamedDatabaseItem(_0.APIBase):
    """NamedDatabaseItem

    This is a mastapy class.
    """

    TYPE = _NAMED_DATABASE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NamedDatabaseItem")

    class _Cast_NamedDatabaseItem:
        """Special nested class for casting NamedDatabaseItem to subclasses."""

        def __init__(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
            parent: "NamedDatabaseItem",
        ):
            self._parent = parent

        @property
        def shaft_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_24.ShaftMaterial":
            from mastapy.shafts import _24

            return self._parent._cast(_24.ShaftMaterial)

        @property
        def shaft_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_40.ShaftSettingsItem":
            from mastapy.shafts import _40

            return self._parent._cast(_40.ShaftSettingsItem)

        @property
        def simple_shaft_definition(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_43.SimpleShaftDefinition":
            from mastapy.shafts import _43

            return self._parent._cast(_43.SimpleShaftDefinition)

        @property
        def analysis_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_50.AnalysisSettingsItem":
            from mastapy.nodal_analysis import _50

            return self._parent._cast(_50.AnalysisSettingsItem)

        @property
        def bearing_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_252.BearingMaterial":
            from mastapy.materials import _252

            return self._parent._cast(_252.BearingMaterial)

        @property
        def lubrication_detail(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_274.LubricationDetail":
            from mastapy.materials import _274

            return self._parent._cast(_274.LubricationDetail)

        @property
        def material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_276.Material":
            from mastapy.materials import _276

            return self._parent._cast(_276.Material)

        @property
        def materials_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_280.MaterialsSettingsItem":
            from mastapy.materials import _280

            return self._parent._cast(_280.MaterialsSettingsItem)

        @property
        def pocketing_power_loss_coefficients(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_349.PocketingPowerLossCoefficients":
            from mastapy.gears import _349

            return self._parent._cast(_349.PocketingPowerLossCoefficients)

        @property
        def cylindrical_gear_design_and_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_461.CylindricalGearDesignAndRatingSettingsItem":
            from mastapy.gears.rating.cylindrical import _461

            return self._parent._cast(_461.CylindricalGearDesignAndRatingSettingsItem)

        @property
        def cylindrical_plastic_gear_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_477.CylindricalPlasticGearRatingSettingsItem":
            from mastapy.gears.rating.cylindrical import _477

            return self._parent._cast(_477.CylindricalPlasticGearRatingSettingsItem)

        @property
        def agma_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_590.AGMACylindricalGearMaterial":
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_592.BevelGearISOMaterial":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.BevelGearISOMaterial)

        @property
        def bevel_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_594.BevelGearMaterial":
            from mastapy.gears.materials import _594

            return self._parent._cast(_594.BevelGearMaterial)

        @property
        def cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_598.CylindricalGearMaterial":
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.CylindricalGearMaterial)

        @property
        def gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_601.GearMaterial":
            from mastapy.gears.materials import _601

            return self._parent._cast(_601.GearMaterial)

        @property
        def iso_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_604.ISOCylindricalGearMaterial":
            from mastapy.gears.materials import _604

            return self._parent._cast(_604.ISOCylindricalGearMaterial)

        @property
        def isotr1417912001_coefficient_of_friction_constants(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_605.ISOTR1417912001CoefficientOfFrictionConstants":
            from mastapy.gears.materials import _605

            return self._parent._cast(
                _605.ISOTR1417912001CoefficientOfFrictionConstants
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_608.KlingelnbergCycloPalloidConicalGearMaterial":
            from mastapy.gears.materials import _608

            return self._parent._cast(_608.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_610.PlasticCylindricalGearMaterial":
            from mastapy.gears.materials import _610

            return self._parent._cast(_610.PlasticCylindricalGearMaterial)

        @property
        def raw_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_613.RawMaterial":
            from mastapy.gears.materials import _613

            return self._parent._cast(_613.RawMaterial)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_713.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearAbstractCutterDesign)

        @property
        def cylindrical_gear_form_grinding_wheel(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_714.CylindricalGearFormGrindingWheel":
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_715.CylindricalGearGrindingWorm":
            from mastapy.gears.manufacturing.cylindrical.cutters import _715

            return self._parent._cast(_715.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_716.CylindricalGearHobDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_717.CylindricalGearPlungeShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_719.CylindricalGearRackDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _719

            return self._parent._cast(_719.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_720.CylindricalGearRealCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _720

            return self._parent._cast(_720.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_721.CylindricalGearShaper":
            from mastapy.gears.manufacturing.cylindrical.cutters import _721

            return self._parent._cast(_721.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_722.CylindricalGearShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _722

            return self._parent._cast(_722.CylindricalGearShaver)

        @property
        def involute_cutter_design(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_725.InvoluteCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _725

            return self._parent._cast(_725.InvoluteCutterDesign)

        @property
        def manufacturing_machine(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_806.ManufacturingMachine":
            from mastapy.gears.manufacturing.bevel import _806

            return self._parent._cast(_806.ManufacturingMachine)

        @property
        def bevel_hypoid_gear_design_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_949.BevelHypoidGearDesignSettingsItem":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.BevelHypoidGearDesignSettingsItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_951.BevelHypoidGearRatingSettingsItem":
            from mastapy.gears.gear_designs import _951

            return self._parent._cast(_951.BevelHypoidGearRatingSettingsItem)

        @property
        def design_constraints_collection(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_954.DesignConstraintsCollection":
            from mastapy.gears.gear_designs import _954

            return self._parent._cast(_954.DesignConstraintsCollection)

        @property
        def cylindrical_gear_design_constraints(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1022.CylindricalGearDesignConstraints":
            from mastapy.gears.gear_designs.cylindrical import _1022

            return self._parent._cast(_1022.CylindricalGearDesignConstraints)

        @property
        def cylindrical_gear_micro_geometry_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1030.CylindricalGearMicroGeometrySettingsItem":
            from mastapy.gears.gear_designs.cylindrical import _1030

            return self._parent._cast(_1030.CylindricalGearMicroGeometrySettingsItem)

        @property
        def magnet_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1295.MagnetMaterial":
            from mastapy.electric_machines import _1295

            return self._parent._cast(_1295.MagnetMaterial)

        @property
        def stator_rotor_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1313.StatorRotorMaterial":
            from mastapy.electric_machines import _1313

            return self._parent._cast(_1313.StatorRotorMaterial)

        @property
        def winding_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1326.WindingMaterial":
            from mastapy.electric_machines import _1326

            return self._parent._cast(_1326.WindingMaterial)

        @property
        def spline_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1428.SplineMaterial":
            from mastapy.detailed_rigid_connectors.splines import _1428

            return self._parent._cast(_1428.SplineMaterial)

        @property
        def cycloidal_disc_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1468.CycloidalDiscMaterial":
            from mastapy.cycloidal import _1468

            return self._parent._cast(_1468.CycloidalDiscMaterial)

        @property
        def ring_pins_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1475.RingPinsMaterial":
            from mastapy.cycloidal import _1475

            return self._parent._cast(_1475.RingPinsMaterial)

        @property
        def bolted_joint_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1478.BoltedJointMaterial":
            from mastapy.bolts import _1478

            return self._parent._cast(_1478.BoltedJointMaterial)

        @property
        def bolt_geometry(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1480.BoltGeometry":
            from mastapy.bolts import _1480

            return self._parent._cast(_1480.BoltGeometry)

        @property
        def bolt_material(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1482.BoltMaterial":
            from mastapy.bolts import _1482

            return self._parent._cast(_1482.BoltMaterial)

        @property
        def pareto_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1561.ParetoOptimisationStrategy":
            from mastapy.math_utility.optimisation import _1561

            return self._parent._cast(_1561.ParetoOptimisationStrategy)

        @property
        def bearing_settings_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1898.BearingSettingsItem":
            from mastapy.bearings import _1898

            return self._parent._cast(_1898.BearingSettingsItem)

        @property
        def iso14179_settings(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_1992.ISO14179Settings":
            from mastapy.bearings.bearing_results.rolling import _1992

            return self._parent._cast(_1992.ISO14179Settings)

        @property
        def conical_gear_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2244.ConicalGearOptimisationStrategy":
            from mastapy.system_model.optimization import _2244

            return self._parent._cast(_2244.ConicalGearOptimisationStrategy)

        @property
        def cylindrical_gear_optimisation_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2247.CylindricalGearOptimisationStrategy":
            from mastapy.system_model.optimization import _2247

            return self._parent._cast(_2247.CylindricalGearOptimisationStrategy)

        @property
        def optimization_strategy(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2252.OptimizationStrategy":
            from mastapy.system_model.optimization import _2252

            return self._parent._cast(_2252.OptimizationStrategy)

        @property
        def optimization_strategy_base(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2253.OptimizationStrategyBase":
            from mastapy.system_model.optimization import _2253

            return self._parent._cast(_2253.OptimizationStrategyBase)

        @property
        def supercharger_rotor_set(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "_2581.SuperchargerRotorSet":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2581,
            )

            return self._parent._cast(_2581.SuperchargerRotorSet)

        @property
        def named_database_item(
            self: "NamedDatabaseItem._Cast_NamedDatabaseItem",
        ) -> "NamedDatabaseItem":
            return self._parent

        def __getattr__(self: "NamedDatabaseItem._Cast_NamedDatabaseItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NamedDatabaseItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def no_history(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NoHistory

        if temp is None:
            return ""

        return temp

    @property
    def history(self: Self) -> "_1595.FileHistory":
        """mastapy.utility.FileHistory

        Note:
            This property is readonly.
        """
        temp = self.wrapped.History

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def database_key(self: Self) -> "_1845.NamedKey":
        """mastapy.utility.databases.NamedKey"""
        temp = self.wrapped.DatabaseKey

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @database_key.setter
    @enforce_parameter_types
    def database_key(self: Self, value: "_1845.NamedKey"):
        self.wrapped.DatabaseKey = value.wrapped

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "NamedDatabaseItem._Cast_NamedDatabaseItem":
        return self._Cast_NamedDatabaseItem(self)
