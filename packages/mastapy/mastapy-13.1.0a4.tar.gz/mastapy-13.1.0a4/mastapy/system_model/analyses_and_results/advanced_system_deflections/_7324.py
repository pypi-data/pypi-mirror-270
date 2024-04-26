"""ComponentAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7381
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7297,
        _7298,
        _7303,
        _7307,
        _7310,
        _7313,
        _7314,
        _7315,
        _7318,
        _7322,
        _7327,
        _7328,
        _7331,
        _7335,
        _7339,
        _7342,
        _7344,
        _7347,
        _7351,
        _7352,
        _7353,
        _7354,
        _7357,
        _7359,
        _7362,
        _7363,
        _7367,
        _7370,
        _7373,
        _7377,
        _7378,
        _7379,
        _7380,
        _7384,
        _7387,
        _7388,
        _7389,
        _7390,
        _7391,
        _7393,
        _7397,
        _7398,
        _7401,
        _7406,
        _7407,
        _7410,
        _7413,
        _7414,
        _7416,
        _7417,
        _7418,
        _7421,
        _7422,
        _7424,
        _7425,
        _7426,
        _7429,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ComponentAdvancedSystemDeflection")


class ComponentAdvancedSystemDeflection(_7381.PartAdvancedSystemDeflection):
    """ComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentAdvancedSystemDeflection")

    class _Cast_ComponentAdvancedSystemDeflection:
        """Special nested class for casting ComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
            parent: "ComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7297.AbstractShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7298.AbstractShaftOrHousingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(
                _7298.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7303.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(
                _7303.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bearing_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7307.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.BearingAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7310.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(
                _7310.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7313.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(
                _7313.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7314.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(
                _7314.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7315.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.BevelGearAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7318.BoltAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7318,
            )

            return self._parent._cast(_7318.BoltAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7322.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7327.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7328.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7331.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.ConicalGearAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7335.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7339.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7342.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(_7342.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7344.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7347.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7351.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7352.DatumAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7353.ExternalCADModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7354.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.FaceGearAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7357.FEPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.FEPartAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7359.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.GearAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7362.GuideDxfModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7363.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(
                _7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(
                _7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7377.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7378.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7380.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7384.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planet_carrier_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7387.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7388.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7389.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7390.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7391.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7393.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.RollingRingAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7397.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7398.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7401.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7406.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(_7406.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7407.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(
                _7407.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7410.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7413.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(
                _7413.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7414.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7414,
            )

            return self._parent._cast(
                _7414.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7416.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7416,
            )

            return self._parent._cast(_7416.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7417.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7417,
            )

            return self._parent._cast(_7417.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7418.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7418,
            )

            return self._parent._cast(_7418.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7421.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7421,
            )

            return self._parent._cast(_7421.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7422.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7422,
            )

            return self._parent._cast(
                _7422.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7424.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7424,
            )

            return self._parent._cast(_7424.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7425.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7425,
            )

            return self._parent._cast(_7425.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7426.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7426,
            )

            return self._parent._cast(_7426.WormGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "_7429.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7429,
            )

            return self._parent._cast(_7429.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
        ) -> "ComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def component_design(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentAdvancedSystemDeflection._Cast_ComponentAdvancedSystemDeflection":
        return self._Cast_ComponentAdvancedSystemDeflection(self)
