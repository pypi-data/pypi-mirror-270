"""AbstractAssemblyCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4545,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AbstractAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4472,
        _4473,
        _4476,
        _4479,
        _4484,
        _4486,
        _4487,
        _4492,
        _4497,
        _4500,
        _4503,
        _4507,
        _4509,
        _4515,
        _4521,
        _4523,
        _4526,
        _4530,
        _4534,
        _4537,
        _4540,
        _4546,
        _4550,
        _4557,
        _4560,
        _4564,
        _4567,
        _4568,
        _4573,
        _4576,
        _4579,
        _4583,
        _4591,
        _4594,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundParametricStudyTool")


class AbstractAssemblyCompoundParametricStudyTool(
    _4545.PartCompoundParametricStudyTool
):
    """AbstractAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundParametricStudyTool"
    )

    class _Cast_AbstractAssemblyCompoundParametricStudyTool:
        """Special nested class for casting AbstractAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
            parent: "AbstractAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4472.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(
                _4472.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4473.AssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.AssemblyCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4476.BeltDriveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4479.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(
                _4479.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4484.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4486.BoltedJointCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4487.ClutchCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(_4487.ClutchCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4492.ConceptCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(_4492.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4497.ConceptGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4500.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.ConicalGearSetCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4503.CouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.CouplingCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4507.CVTCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.CVTCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4509.CycloidalAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(
                _4509.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4515.CylindricalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4521.FaceGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.FaceGearSetCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4523.FlexiblePinAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4526.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(_4526.GearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4530.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4534.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(
                _4534.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4537.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(
                _4537.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4540.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4546.PartToPartShearCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4550.PlanetaryGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(_4550.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4557.RollingRingAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(
                _4557.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4560.RootAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.RootAssemblyCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4564.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(
                _4564.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4567.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(
                _4567.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4568.SpringDamperCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.SpringDamperCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4573.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(
                _4573.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4576.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4576,
            )

            return self._parent._cast(
                _4576.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4579.SynchroniserCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4579,
            )

            return self._parent._cast(_4579.SynchroniserCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4583.TorqueConverterCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4583,
            )

            return self._parent._cast(_4583.TorqueConverterCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4591.WormGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4591,
            )

            return self._parent._cast(_4591.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4594.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4594,
            )

            return self._parent._cast(
                _4594.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "AbstractAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4319.AbstractAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4319.AbstractAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool":
        return self._Cast_AbstractAssemblyCompoundParametricStudyTool(self)
