"""ParetoCylindricalGearSetOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1564, _1552
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("ParetoCylindricalGearSetOptimisationStrategyDatabase",)


Self = TypeVar("Self", bound="ParetoCylindricalGearSetOptimisationStrategyDatabase")


class ParetoCylindricalGearSetOptimisationStrategyDatabase(
    _934.ParetoCylindricalRatingOptimisationStrategyDatabase
):
    """ParetoCylindricalGearSetOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase"
    )

    class _Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
            parent: "ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_934.ParetoCylindricalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _934.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1564.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1564

            return self._parent._cast(_1564.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1552.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1843.NamedDatabase":
            pass

            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
        ) -> "ParetoCylindricalGearSetOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoCylindricalGearSetOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoCylindricalGearSetOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase":
        return self._Cast_ParetoCylindricalGearSetOptimisationStrategyDatabase(self)
