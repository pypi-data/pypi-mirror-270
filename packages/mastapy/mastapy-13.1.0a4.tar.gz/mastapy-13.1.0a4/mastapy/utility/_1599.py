"""IndependentReportablePropertiesBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_REPORTABLE_PROPERTIES_BASE = python_net_import(
    "SMT.MastaAPI.Utility", "IndependentReportablePropertiesBase"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _305
    from mastapy.geometry import _316
    from mastapy.gears import _353
    from mastapy.gears.gear_designs.cylindrical import (
        _1028,
        _1059,
        _1067,
        _1068,
        _1071,
        _1072,
        _1080,
        _1088,
        _1090,
        _1094,
        _1098,
    )
    from mastapy.electric_machines import _1271
    from mastapy.electric_machines.load_cases_and_analyses import _1389
    from mastapy.math_utility.measured_data import _1578, _1579, _1580
    from mastapy.bearings.tolerances import _1935
    from mastapy.bearings.bearing_results import _1963
    from mastapy.bearings.bearing_results.rolling import _1994, _2088
    from mastapy.system_model.analyses_and_results.static_loads import _6837


__docformat__ = "restructuredtext en"
__all__ = ("IndependentReportablePropertiesBase",)


Self = TypeVar("Self", bound="IndependentReportablePropertiesBase")
T = TypeVar("T", bound="IndependentReportablePropertiesBase")


class IndependentReportablePropertiesBase(_0.APIBase, Generic[T]):
    """IndependentReportablePropertiesBase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _INDEPENDENT_REPORTABLE_PROPERTIES_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentReportablePropertiesBase")

    class _Cast_IndependentReportablePropertiesBase:
        """Special nested class for casting IndependentReportablePropertiesBase to subclasses."""

        def __init__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
            parent: "IndependentReportablePropertiesBase",
        ):
            self._parent = parent

        @property
        def oil_pump_detail(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_305.OilPumpDetail":
            from mastapy.materials.efficiency import _305

            return self._parent._cast(_305.OilPumpDetail)

        @property
        def packaging_limits(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_316.PackagingLimits":
            from mastapy.geometry import _316

            return self._parent._cast(_316.PackagingLimits)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_353.SpecificationForTheEffectOfOilKinematicViscosity":
            from mastapy.gears import _353

            return self._parent._cast(
                _353.SpecificationForTheEffectOfOilKinematicViscosity
            )

        @property
        def cylindrical_gear_micro_geometry_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1028.CylindricalGearMicroGeometrySettings":
            from mastapy.gears.gear_designs.cylindrical import _1028

            return self._parent._cast(_1028.CylindricalGearMicroGeometrySettings)

        @property
        def hardened_material_properties(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1059.HardenedMaterialProperties":
            from mastapy.gears.gear_designs.cylindrical import _1059

            return self._parent._cast(_1059.HardenedMaterialProperties)

        @property
        def ltca_load_case_modifiable_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1067.LTCALoadCaseModifiableSettings":
            from mastapy.gears.gear_designs.cylindrical import _1067

            return self._parent._cast(_1067.LTCALoadCaseModifiableSettings)

        @property
        def ltca_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1068.LTCASettings":
            from mastapy.gears.gear_designs.cylindrical import _1068

            return self._parent._cast(_1068.LTCASettings)

        @property
        def micropitting(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1071.Micropitting":
            from mastapy.gears.gear_designs.cylindrical import _1071

            return self._parent._cast(_1071.Micropitting)

        @property
        def muller_residual_stress_definition(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1072.MullerResidualStressDefinition":
            from mastapy.gears.gear_designs.cylindrical import _1072

            return self._parent._cast(_1072.MullerResidualStressDefinition)

        @property
        def scuffing(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1080.Scuffing":
            from mastapy.gears.gear_designs.cylindrical import _1080

            return self._parent._cast(_1080.Scuffing)

        @property
        def surface_roughness(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1088.SurfaceRoughness":
            from mastapy.gears.gear_designs.cylindrical import _1088

            return self._parent._cast(_1088.SurfaceRoughness)

        @property
        def tiff_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1090.TiffAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1090

            return self._parent._cast(_1090.TiffAnalysisSettings)

        @property
        def tooth_flank_fracture_analysis_settings(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1094.ToothFlankFractureAnalysisSettings":
            from mastapy.gears.gear_designs.cylindrical import _1094

            return self._parent._cast(_1094.ToothFlankFractureAnalysisSettings)

        @property
        def usage(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1098.Usage":
            from mastapy.gears.gear_designs.cylindrical import _1098

            return self._parent._cast(_1098.Usage)

        @property
        def eccentricity(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1271.Eccentricity":
            from mastapy.electric_machines import _1271

            return self._parent._cast(_1271.Eccentricity)

        @property
        def temperatures(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1389.Temperatures":
            from mastapy.electric_machines.load_cases_and_analyses import _1389

            return self._parent._cast(_1389.Temperatures)

        @property
        def lookup_table_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1578.LookupTableBase":
            from mastapy.math_utility.measured_data import _1578

            return self._parent._cast(_1578.LookupTableBase)

        @property
        def onedimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1579.OnedimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1579

            return self._parent._cast(_1579.OnedimensionalFunctionLookupTable)

        @property
        def twodimensional_function_lookup_table(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1580.TwodimensionalFunctionLookupTable":
            from mastapy.math_utility.measured_data import _1580

            return self._parent._cast(_1580.TwodimensionalFunctionLookupTable)

        @property
        def roundness_specification(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1935.RoundnessSpecification":
            from mastapy.bearings.tolerances import _1935

            return self._parent._cast(_1935.RoundnessSpecification)

        @property
        def equivalent_load_factors(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1963.EquivalentLoadFactors":
            from mastapy.bearings.bearing_results import _1963

            return self._parent._cast(_1963.EquivalentLoadFactors)

        @property
        def iso14179_settings_per_bearing_type(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_1994.ISO14179SettingsPerBearingType":
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(_1994.ISO14179SettingsPerBearingType)

        @property
        def rolling_bearing_friction_coefficients(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_2088.RollingBearingFrictionCoefficients":
            from mastapy.bearings.bearing_results.rolling import _2088

            return self._parent._cast(_2088.RollingBearingFrictionCoefficients)

        @property
        def additional_acceleration_options(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "_6837.AdditionalAccelerationOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.AdditionalAccelerationOptions)

        @property
        def independent_reportable_properties_base(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
        ) -> "IndependentReportablePropertiesBase":
            return self._parent

        def __getattr__(
            self: "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "IndependentReportablePropertiesBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "IndependentReportablePropertiesBase._Cast_IndependentReportablePropertiesBase"
    ):
        return self._Cast_IndependentReportablePropertiesBase(self)
