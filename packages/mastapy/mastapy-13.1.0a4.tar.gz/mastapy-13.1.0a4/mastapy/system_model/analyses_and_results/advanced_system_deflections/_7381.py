"""PartAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PartAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7300,
        _7296,
        _7297,
        _7298,
        _7303,
        _7305,
        _7306,
        _7307,
        _7309,
        _7310,
        _7312,
        _7313,
        _7314,
        _7315,
        _7317,
        _7318,
        _7319,
        _7320,
        _7322,
        _7324,
        _7325,
        _7327,
        _7328,
        _7330,
        _7331,
        _7333,
        _7335,
        _7337,
        _7339,
        _7340,
        _7342,
        _7343,
        _7344,
        _7347,
        _7349,
        _7351,
        _7352,
        _7353,
        _7354,
        _7356,
        _7357,
        _7358,
        _7359,
        _7361,
        _7362,
        _7363,
        _7365,
        _7367,
        _7369,
        _7370,
        _7372,
        _7373,
        _7375,
        _7377,
        _7378,
        _7379,
        _7380,
        _7382,
        _7384,
        _7386,
        _7387,
        _7388,
        _7389,
        _7390,
        _7391,
        _7393,
        _7394,
        _7396,
        _7397,
        _7398,
        _7400,
        _7401,
        _7403,
        _7404,
        _7406,
        _7407,
        _7409,
        _7410,
        _7412,
        _7413,
        _7414,
        _7415,
        _7416,
        _7417,
        _7418,
        _7419,
        _7421,
        _7422,
        _7424,
        _7425,
        _7426,
        _7428,
        _7429,
        _7431,
    )
    from mastapy.system_model.part_model import _2486
    from mastapy.math_utility.convergence import _1588
    from mastapy.system_model.drawing import _2262
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PartAdvancedSystemDeflection")


class PartAdvancedSystemDeflection(_7574.PartStaticLoadAnalysisCase):
    """PartAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartAdvancedSystemDeflection")

    class _Cast_PartAdvancedSystemDeflection:
        """Special nested class for casting PartAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
            parent: "PartAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7297.AbstractShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7298.AbstractShaftOrHousingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(
                _7298.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7303.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(
                _7303.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(
                _7305.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7306.AssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7306,
            )

            return self._parent._cast(_7306.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7307.BearingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7309.BeltDriveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7310.BevelDifferentialGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7310,
            )

            return self._parent._cast(
                _7310.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7312.BevelDifferentialGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(
                _7312.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7313.BevelDifferentialPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(
                _7313.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7314.BevelDifferentialSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(
                _7314.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7315.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7317.BevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7318.BoltAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7318,
            )

            return self._parent._cast(_7318.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7319.BoltedJointAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(_7319.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7320.ClutchAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7322.ClutchHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7322,
            )

            return self._parent._cast(_7322.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7325.ConceptCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(_7325.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7327.ConceptCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7328.ConceptGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7330.ConceptGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7331.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7333.ConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7335.ConnectorAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7337.CouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7339.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7340.CVTAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7340,
            )

            return self._parent._cast(_7340.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7342.CVTPulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(_7342.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7343.CycloidalAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(_7343.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7344.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7347.CylindricalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(_7347.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7349.CylindricalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(_7349.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7351.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7352.DatumAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7353.ExternalCADModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7354.FaceGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7356.FaceGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(_7356.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7357.FEPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7358.FlexiblePinAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(_7358.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7359.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7361.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7362.GuideDxfModelAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7363.HypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7365.HypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(
                _7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7369,
            )

            return self._parent._cast(
                _7369.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(
                _7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(
                _7372.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(
                _7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(
                _7375.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7377.MassDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7378.MeasurementComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7380.OilSealAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7382.PartToPartShearCouplingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7384.PartToPartShearCouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(
                _7384.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7386.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7387.PlanetCarrierAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7388.PointLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7389.PowerLoadAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7390.PulleyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7391.RingPinsAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7393.RollingRingAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7394.RollingRingAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(_7394.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7396.RootAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(_7396.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7397.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7398.ShaftHubConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7401.SpiralBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7403.SpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7404.SpringDamperAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7404,
            )

            return self._parent._cast(_7404.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7406.SpringDamperHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7406,
            )

            return self._parent._cast(_7406.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7407.StraightBevelDiffGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7407,
            )

            return self._parent._cast(
                _7407.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7409.StraightBevelDiffGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7409,
            )

            return self._parent._cast(
                _7409.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7410.StraightBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7410,
            )

            return self._parent._cast(_7410.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7412.StraightBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7412,
            )

            return self._parent._cast(
                _7412.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7413.StraightBevelPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7413,
            )

            return self._parent._cast(
                _7413.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7414.StraightBevelSunGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7414,
            )

            return self._parent._cast(
                _7414.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7415.SynchroniserAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7415,
            )

            return self._parent._cast(_7415.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7416.SynchroniserHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7416,
            )

            return self._parent._cast(_7416.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7417.SynchroniserPartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7417,
            )

            return self._parent._cast(_7417.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7418.SynchroniserSleeveAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7418,
            )

            return self._parent._cast(_7418.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7419.TorqueConverterAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7419,
            )

            return self._parent._cast(_7419.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7421.TorqueConverterPumpAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7421,
            )

            return self._parent._cast(_7421.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7422.TorqueConverterTurbineAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7422,
            )

            return self._parent._cast(
                _7422.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7424.UnbalancedMassAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7424,
            )

            return self._parent._cast(_7424.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7425.VirtualComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7425,
            )

            return self._parent._cast(_7425.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7426.WormGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7426,
            )

            return self._parent._cast(_7426.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7428.WormGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7428,
            )

            return self._parent._cast(_7428.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7429.ZerolBevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7429,
            )

            return self._parent._cast(_7429.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "_7431.ZerolBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7431,
            )

            return self._parent._cast(_7431.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
        ) -> "PartAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection(self: Self) -> "_7300.AdvancedSystemDeflection":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.AdvancedSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def data_logger(self: Self) -> "_1588.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2262.AdvancedSystemDeflectionViewable":
        """mastapy.system_model.drawing.AdvancedSystemDeflectionViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection":
        return self._Cast_PartAdvancedSystemDeflection(self)
