"""ParetoSpiralBevelGearSetOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_SPIRAL_BEVEL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1564, _1552
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("ParetoSpiralBevelGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoSpiralBevelGearSetOptimisationStrategyDatabase")


class ParetoSpiralBevelGearSetOptimisationStrategyDatabase(
    _931.ParetoConicalRatingOptimisationStrategyDatabase
):
    """ParetoSpiralBevelGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_SPIRAL_BEVEL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoSpiralBevelGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
            parent: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "_931.ParetoConicalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _931.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1564.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1564

            return self._parent._cast(_1564.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1552.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1843.NamedDatabase":
            pass

            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
        ) -> "ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoSpiralBevelGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoSpiralBevelGearSetOptimisationStrategyDatabase._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoSpiralBevelGearSetOptimisationStrategyDatabase(self)
