"""PartCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PartCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3867
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3920,
        _3921,
        _3922,
        _3924,
        _3926,
        _3927,
        _3928,
        _3930,
        _3931,
        _3933,
        _3934,
        _3935,
        _3936,
        _3938,
        _3939,
        _3940,
        _3941,
        _3943,
        _3945,
        _3946,
        _3948,
        _3949,
        _3951,
        _3952,
        _3954,
        _3956,
        _3957,
        _3959,
        _3961,
        _3962,
        _3963,
        _3965,
        _3967,
        _3969,
        _3970,
        _3971,
        _3972,
        _3973,
        _3975,
        _3976,
        _3977,
        _3978,
        _3980,
        _3981,
        _3982,
        _3984,
        _3986,
        _3988,
        _3989,
        _3991,
        _3992,
        _3994,
        _3995,
        _3996,
        _3997,
        _3998,
        _4000,
        _4002,
        _4004,
        _4005,
        _4006,
        _4007,
        _4008,
        _4009,
        _4011,
        _4012,
        _4014,
        _4015,
        _4016,
        _4018,
        _4019,
        _4021,
        _4022,
        _4024,
        _4025,
        _4027,
        _4028,
        _4030,
        _4031,
        _4032,
        _4033,
        _4034,
        _4035,
        _4036,
        _4037,
        _4039,
        _4040,
        _4041,
        _4042,
        _4043,
        _4045,
        _4046,
        _4048,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PartCompoundStabilityAnalysis")


class PartCompoundStabilityAnalysis(_7572.PartCompoundAnalysis):
    """PartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundStabilityAnalysis")

    class _Cast_PartCompoundStabilityAnalysis:
        """Special nested class for casting PartCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
            parent: "PartCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3921.AbstractShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(_3921.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3922.AbstractShaftOrHousingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(
                _3922.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3924.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(
                _3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3927.AssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3928.BearingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.BearingCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3930.BeltDriveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3931.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(
                _3931.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3933.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3934.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(
                _3934.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3935.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(
                _3935.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3936.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3938.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3939.BoltCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3940.BoltedJointCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3941.ClutchCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(_3941.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3943.ClutchHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ClutchHalfCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3946.ConceptCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3948.ConceptCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(
                _3948.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3949.ConceptGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3951.ConceptGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3952.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3954.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3956.ConnectorCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3957.CouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3959.CouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3961.CVTCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(_3961.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3962.CVTPulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(_3962.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3963.CycloidalAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(_3963.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3965.CycloidalDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(_3965.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3967.CylindricalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(_3967.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3969.CylindricalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(_3969.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3970.CylindricalPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3971.DatumCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(_3971.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3972.ExternalCADModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3973.FaceGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3975.FaceGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(_3975.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3976.FEPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3977.FlexiblePinAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(
                _3977.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3978.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.GearCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3981.GuideDxfModelCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3982.HypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3984.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3986.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(
                _3986.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3989.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(
                _3989.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3991.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(
                _3991.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3992.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> (
            "_3994.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3995.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3996.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(
                _3996.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3997.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_3998.OilSealCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4000.PartToPartShearCouplingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4002.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(
                _4002.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4004.PlanetaryGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(_4004.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4005.PlanetCarrierCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(_4005.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4006.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(_4006.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4007.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4008.PulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4009.RingPinsCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4011.RollingRingAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(
                _4011.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4012.RollingRingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.RollingRingCompoundStabilityAnalysis)

        @property
        def root_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4014.RootAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(_4014.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4015.ShaftCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4016.ShaftHubConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4019.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4021.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4022.SpringDamperCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4024.SpringDamperHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4025.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(
                _4025.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4028.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4028,
            )

            return self._parent._cast(_4028.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4030.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(
                _4030.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4031.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4031,
            )

            return self._parent._cast(
                _4031.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4032.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4032,
            )

            return self._parent._cast(
                _4032.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4033.SynchroniserCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4033,
            )

            return self._parent._cast(_4033.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4034.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4034,
            )

            return self._parent._cast(_4034.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4035.SynchroniserPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4035,
            )

            return self._parent._cast(_4035.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4036.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4036,
            )

            return self._parent._cast(_4036.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4037.TorqueConverterCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4037,
            )

            return self._parent._cast(_4037.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4039.TorqueConverterPumpCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4039,
            )

            return self._parent._cast(
                _4039.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4040.TorqueConverterTurbineCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4040,
            )

            return self._parent._cast(
                _4040.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4041.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4041,
            )

            return self._parent._cast(_4041.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4042.VirtualComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4042,
            )

            return self._parent._cast(_4042.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4043.WormGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4043,
            )

            return self._parent._cast(_4043.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4045.WormGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4045,
            )

            return self._parent._cast(_4045.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4046.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4046,
            )

            return self._parent._cast(_4046.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "_4048.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4048,
            )

            return self._parent._cast(_4048.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
        ) -> "PartCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_3867.PartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3867.PartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PartStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundStabilityAnalysis._Cast_PartCompoundStabilityAnalysis":
        return self._Cast_PartCompoundStabilityAnalysis(self)
