"""GearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5632
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "GearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5463
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5559,
        _5566,
        _5569,
        _5570,
        _5571,
        _5584,
        _5587,
        _5602,
        _5605,
        _5608,
        _5617,
        _5621,
        _5624,
        _5627,
        _5654,
        _5660,
        _5663,
        _5666,
        _5667,
        _5678,
        _5681,
        _5580,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="GearCompoundMultibodyDynamicsAnalysis")


class GearCompoundMultibodyDynamicsAnalysis(
    _5632.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """GearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_GearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting GearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
            parent: "GearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.MountableComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5632.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(
                _5566.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5569.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5571.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(_5571.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5587.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(
                _5587.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5608.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5621.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5624.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(
                _5624.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5654.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5660.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5660,
            )

            return self._parent._cast(
                _5660.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5663.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5663,
            )

            return self._parent._cast(
                _5663.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5666.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5666,
            )

            return self._parent._cast(
                _5666.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5667.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5667,
            )

            return self._parent._cast(
                _5667.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5678.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5678,
            )

            return self._parent._cast(_5678.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5681.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5681,
            )

            return self._parent._cast(
                _5681.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
        ) -> "GearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "GearCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5463.GearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5463.GearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.GearMultibodyDynamicsAnalysis]

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
    ) -> "GearCompoundMultibodyDynamicsAnalysis._Cast_GearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_GearCompoundMultibodyDynamicsAnalysis(self)
