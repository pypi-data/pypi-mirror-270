"""ComponentCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4545,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4344
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4467,
        _4468,
        _4470,
        _4474,
        _4477,
        _4480,
        _4481,
        _4482,
        _4485,
        _4489,
        _4494,
        _4495,
        _4498,
        _4502,
        _4505,
        _4508,
        _4511,
        _4513,
        _4516,
        _4517,
        _4518,
        _4519,
        _4522,
        _4524,
        _4527,
        _4528,
        _4532,
        _4535,
        _4538,
        _4541,
        _4542,
        _4543,
        _4544,
        _4548,
        _4551,
        _4552,
        _4553,
        _4554,
        _4555,
        _4558,
        _4561,
        _4562,
        _4565,
        _4570,
        _4571,
        _4574,
        _4577,
        _4578,
        _4580,
        _4581,
        _4582,
        _4585,
        _4586,
        _4587,
        _4588,
        _4589,
        _4592,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ComponentCompoundParametricStudyTool")


class ComponentCompoundParametricStudyTool(_4545.PartCompoundParametricStudyTool):
    """ComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundParametricStudyTool")

    class _Cast_ComponentCompoundParametricStudyTool:
        """Special nested class for casting ComponentCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
            parent: "ComponentCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4545.PartCompoundParametricStudyTool":
            return self._parent._cast(_4545.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4467.AbstractShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(_4467.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4468.AbstractShaftOrHousingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(
                _4468.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4470.AGMAGleasonConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(
                _4470.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def bearing_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4474.BearingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.BearingCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4477.BevelDifferentialGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(
                _4477.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4480.BevelDifferentialPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(
                _4480.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4481.BevelDifferentialSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(
                _4481.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4482.BevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.BevelGearCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4485.BoltCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.BoltCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4489.ClutchHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(_4489.ClutchHalfCompoundParametricStudyTool)

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4494.ConceptCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(
                _4494.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4495.ConceptGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.ConceptGearCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4498.ConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.ConicalGearCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4502.ConnectorCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4505.CouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4508.CVTPulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(_4508.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4511.CycloidalDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(_4511.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4513.CylindricalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(_4513.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4516.CylindricalPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4517.DatumCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(_4517.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4518.ExternalCADModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4519.FaceGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(_4519.FaceGearCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4522.FEPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.FEPartCompoundParametricStudyTool)

        @property
        def gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4524.GearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(_4524.GearCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4527.GuideDxfModelCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4528.HypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.HypoidGearCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(
                _4532.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4535.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(
                _4535.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4538.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(
                _4538.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4541.MassDiscCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(_4541.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4542.MeasurementComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(
                _4542.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4543.MountableComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4544.OilSealCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(_4544.OilSealCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4548.PartToPartShearCouplingHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4551.PlanetCarrierCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(_4551.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4552.PointLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(_4552.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4553.PowerLoadCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(_4553.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4554.PulleyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(_4554.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4555.RingPinsCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(_4555.RingPinsCompoundParametricStudyTool)

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4558.RollingRingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(_4558.RollingRingCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4561.ShaftCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(_4561.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4562.ShaftHubConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4565.SpiralBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4570.SpringDamperHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(_4570.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4571.StraightBevelDiffGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4574.StraightBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4574,
            )

            return self._parent._cast(
                _4574.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4577.StraightBevelPlanetGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4577,
            )

            return self._parent._cast(
                _4577.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4578.StraightBevelSunGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4578,
            )

            return self._parent._cast(
                _4578.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4580.SynchroniserHalfCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4580,
            )

            return self._parent._cast(_4580.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4581.SynchroniserPartCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4581,
            )

            return self._parent._cast(_4581.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4582.SynchroniserSleeveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4582,
            )

            return self._parent._cast(
                _4582.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4585.TorqueConverterPumpCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4585,
            )

            return self._parent._cast(
                _4585.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4586.TorqueConverterTurbineCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4586,
            )

            return self._parent._cast(
                _4586.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4587.UnbalancedMassCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4587,
            )

            return self._parent._cast(_4587.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4588.VirtualComponentCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4588,
            )

            return self._parent._cast(_4588.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4589.WormGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4589,
            )

            return self._parent._cast(_4589.WormGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "_4592.ZerolBevelGearCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4592,
            )

            return self._parent._cast(_4592.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def component_compound_parametric_study_tool(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
        ) -> "ComponentCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "ComponentCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4344.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

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
    ) -> "List[_4344.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

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
    ) -> "ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool":
        return self._Cast_ComponentCompoundParametricStudyTool(self)
