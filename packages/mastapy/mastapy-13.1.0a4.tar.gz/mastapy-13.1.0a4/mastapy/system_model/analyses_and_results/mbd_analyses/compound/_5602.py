"""CylindricalGearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CylindricalGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5451
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5605,
        _5632,
        _5580,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearCompoundMultibodyDynamicsAnalysis")


class CylindricalGearCompoundMultibodyDynamicsAnalysis(
    _5613.GearCompoundMultibodyDynamicsAnalysis
):
    """CylindricalGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
            parent: "CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.GearCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5613.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "_5605.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
        ) -> "CylindricalGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CylindricalGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5451.CylindricalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.CylindricalGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5451.CylindricalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalGearCompoundMultibodyDynamicsAnalysis(self)
