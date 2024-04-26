"""MountableComponentAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7062,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.system_deflections import _2805
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7040,
        _7045,
        _7048,
        _7051,
        _7052,
        _7053,
        _7060,
        _7065,
        _7066,
        _7069,
        _7073,
        _7076,
        _7079,
        _7084,
        _7087,
        _7090,
        _7095,
        _7100,
        _7104,
        _7107,
        _7110,
        _7113,
        _7114,
        _7116,
        _7120,
        _7123,
        _7124,
        _7125,
        _7126,
        _7127,
        _7129,
        _7134,
        _7137,
        _7142,
        _7143,
        _7146,
        _7149,
        _7150,
        _7152,
        _7153,
        _7154,
        _7157,
        _7158,
        _7159,
        _7160,
        _7161,
        _7164,
        _7117,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MountableComponentAdvancedTimeSteppingAnalysisForModulation"
)


class MountableComponentAdvancedTimeSteppingAnalysisForModulation(
    _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """MountableComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MountableComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
            parent: "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7062.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7062.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7117.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.BearingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7051.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7060.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7065.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7066.ConceptGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7073.ConnectorAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7084.CylindricalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7087.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7090.FaceGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7095.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7100.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7104.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7107.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7113.MassDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7114.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7116.OilSealAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7120.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7123.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7124.PointLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7125.PowerLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.PulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7127.RingPinsAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7129.RollingRingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7134.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7142.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7142,
            )

            return self._parent._cast(
                _7142.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7143,
            )

            return self._parent._cast(
                _7143.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7146,
            )

            return self._parent._cast(
                _7146.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7149,
            )

            return self._parent._cast(
                _7149.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7150,
            )

            return self._parent._cast(
                _7150.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7152.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7152,
            )

            return self._parent._cast(
                _7152.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7153.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7153,
            )

            return self._parent._cast(
                _7153.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7154.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7154,
            )

            return self._parent._cast(
                _7154.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7157.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7157,
            )

            return self._parent._cast(
                _7157.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7158.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7158,
            )

            return self._parent._cast(
                _7158.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7159.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7159,
            )

            return self._parent._cast(
                _7159.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7160.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7160,
            )

            return self._parent._cast(
                _7160.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7161.WormGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7161,
            )

            return self._parent._cast(
                _7161.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7164,
            )

            return self._parent._cast(
                _7164.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "MountableComponentAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2805.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation(
            self
        )
