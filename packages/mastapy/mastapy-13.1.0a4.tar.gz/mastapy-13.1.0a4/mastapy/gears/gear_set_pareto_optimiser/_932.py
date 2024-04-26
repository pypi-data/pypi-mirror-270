"""ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE = (
    python_net_import(
        "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
        "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    )
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1564, _1552
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",)


Self = TypeVar(
    "Self", bound="ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"
)


class ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase(
    _934.ParetoCylindricalRatingOptimisationStrategyDatabase
):
    """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _PARETO_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_OPTIMISATION_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    )

    class _Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase:
        """Special nested class for casting ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase to subclasses."""

        def __init__(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
            parent: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ):
            self._parent = parent

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_934.ParetoCylindricalRatingOptimisationStrategyDatabase":
            return self._parent._cast(
                _934.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1564.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1564

            return self._parent._cast(_1564.ParetoOptimisationStrategyDatabase)

        @property
        def design_space_search_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1552.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1843.NamedDatabase":
            pass

            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
        ) -> "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
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
        instance_to_wrap: "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
        return self._Cast_ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase(
            self
        )
