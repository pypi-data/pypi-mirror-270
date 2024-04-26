# This file is part of daf_butler.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This software is dual licensed under the GNU General Public License and also
# under a 3-clause BSD license. Recipients may choose which of these licenses
# to use; please see the files gpl-3.0.txt and/or bsd_license.txt,
# respectively.  If you choose the GPL option then the following text applies
# (but note that there is still no warranty even if you opt for BSD instead):
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

__all__ = (
    "convert_where_args",
    "convert_order_by_args",
)

import itertools
from collections.abc import Mapping, Set
from typing import Any, cast

from .._exceptions import InvalidQueryError
from ..dimensions import DataCoordinate, DataId, Dimension, DimensionGroup
from .expression_factory import ExpressionFactory, ExpressionProxy
from .tree import (
    DATASET_FIELD_NAMES,
    ColumnExpression,
    DatasetFieldName,
    DatasetFieldReference,
    DimensionFieldReference,
    DimensionKeyReference,
    OrderExpression,
    Predicate,
    Reversed,
    UnaryExpression,
    make_column_literal,
    validate_order_expression,
)


def convert_where_args(
    dimensions: DimensionGroup,
    datasets: Set[str],
    *args: str | Predicate | DataId,
    bind: Mapping[str, Any] | None = None,
    **kwargs: Any,
) -> Predicate:
    """Convert ``where`` arguments to a sequence of column expressions.

    Parameters
    ----------
    dimensions : `DimensionGroup`
        Dimensions already present in the query this filter is being applied
        to.  Returned predicates may reference dimensions outside this set.
    datasets : `~collections.abc.Set` [ `str` ]
        Dataset types already present in the query this filter is being applied
        to.  Returned predicates may reference datasets outside this set; this
        may be an error at a higher level, but it is not necessarily checked
        here.
    *args : `str`, `Predicate`, `DataCoordinate`, or `~collections.abc.Mapping`
        Expressions to convert into predicates.
    bind : `~collections.abc.Mapping`, optional
        Mapping from identifier to literal value used when parsing string
        expressions.
    **kwargs : `object`
        Additional data ID key-value pairs.

    Returns
    -------
    predicate : `Predicate`
        Standardized predicate object.

    Notes
    -----
    Data ID values are not checked for consistency; they are extracted from
    args and then kwargs and combined, with later extractions taking
    precedence.
    """
    result = Predicate.from_bool(True)
    data_id_dict: dict[str, Any] = {}
    for arg in args:
        match arg:
            case str():
                raise NotImplementedError("TODO: plug in registry.queries.expressions.parser")
            case Predicate():
                result = result.logical_and(arg)
            case DataCoordinate():
                data_id_dict.update(arg.mapping)
            case _:
                data_id_dict.update(arg)
    data_id_dict.update(kwargs)
    for k, v in data_id_dict.items():
        result = result.logical_and(
            Predicate.compare(
                DimensionKeyReference.model_construct(dimension=dimensions.universe.dimensions[k]),
                "==",
                make_column_literal(v),
            )
        )
    return result


def convert_order_by_args(
    dimensions: DimensionGroup, datasets: Set[str], *args: str | OrderExpression | ExpressionProxy
) -> tuple[OrderExpression, ...]:
    """Convert ``order_by`` arguments to a sequence of column expressions.

    Parameters
    ----------
    dimensions : `DimensionGroup`
        Dimensions already present in the query whose rows are being sorted.
        Returned expressions may reference dimensions outside this set; this
        may be an error at a higher level, but it is not necessarily checked
        here.
    datasets : `~collections.abc.Set` [ `str` ]
        Dataset types already present in the query whose rows are being sorted.
        Returned expressions may reference datasets outside this set; this may
        be an error at a higher level, but it is not necessarily checked here.
    *args : `OrderExpression`, `str`, or `ExpressionObject`
        Expression or column names to sort by.

    Returns
    -------
    expressions : `tuple` [ `OrderExpression`, ... ]
        Standardized expression objects.
    """
    result: list[OrderExpression] = []
    for arg in args:
        match arg:
            case str():
                reverse = False
                if arg.startswith("-"):
                    reverse = True
                    arg = arg[1:]
                arg = interpret_identifier(dimensions, datasets, arg, {})
                if reverse:
                    arg = Reversed(operand=arg)
            case ExpressionProxy():
                arg = ExpressionFactory.unwrap(arg)
        if not hasattr(arg, "expression_type"):
            raise TypeError(f"Unrecognized order-by argument: {arg!r}.")
        result.append(validate_order_expression(arg))
    return tuple(result)


def interpret_identifier(
    dimensions: DimensionGroup, datasets: Set[str], identifier: str, bind: Mapping[str, Any]
) -> ColumnExpression:
    """Associate an identifier in a ``where`` or ``order_by`` expression with
    a query column or bind literal.

    Parameters
    ----------
    dimensions : `DimensionGroup`
        Dimensions already present in the query this filter is being applied
        to.  Returned expressions may reference dimensions outside this set.
    datasets : `~collections.abc.Set` [ `str` ]
        Dataset types already present in the query this filter is being applied
        to.  Returned expressions may reference datasets outside this set.
    identifier : `str`
        String identifier to process.
    bind : `~collections.abc.Mapping` [ `str`, `object` ]
        Dictionary of bind literals to match identifiers against first.

    Returns
    -------
    expression : `ColumnExpression`
        Column expression corresponding to the identifier.
    """
    if identifier in bind:
        return make_column_literal(bind[identifier])
    terms = identifier.split(".")
    match len(terms):
        case 1:
            if identifier in dimensions.universe.dimensions:
                return DimensionKeyReference.model_construct(
                    dimension=dimensions.universe.dimensions[identifier]
                )
            # This is an unqualified reference to a field of a dimension
            # element or datasets; this is okay if it's unambiguous.
            element_matches: set[str] = set()
            for element_name in dimensions.elements:
                element = dimensions.universe[element_name]
                if identifier in element.schema.names:
                    element_matches.add(element_name)
            if identifier in DATASET_FIELD_NAMES:
                dataset_matches = set(datasets)
            else:
                dataset_matches = set()
            if len(element_matches) + len(dataset_matches) > 1:
                match_str = ", ".join(
                    f"'{x}.{identifier}'" for x in sorted(itertools.chain(element_matches, dataset_matches))
                )
                raise InvalidQueryError(
                    f"Ambiguous identifier {identifier!r} matches multiple fields: {match_str}."
                )
            elif element_matches:
                element = dimensions.universe[element_matches.pop()]
                return DimensionFieldReference.model_construct(element=element, field=identifier)
            elif dataset_matches:
                return DatasetFieldReference.model_construct(
                    dataset_type=dataset_matches.pop(), field=cast(DatasetFieldName, identifier)
                )
        case 2:
            first, second = terms
            if first in dimensions.universe.elements.names:
                element = dimensions.universe[first]
                if second in element.schema.dimensions.names:
                    if isinstance(element, Dimension) and second == element.primary_key.name:
                        # Identifier is something like "visit.id" which we want
                        # to interpret the same way as just "visit".
                        return DimensionKeyReference.model_construct(dimension=element)
                    else:
                        # Identifier is something like "visit.instrument",
                        # which we want to interpret the same way as just
                        # "instrument".
                        dimension = dimensions.universe.dimensions[second]
                        return DimensionKeyReference.model_construct(dimension=dimension)
                elif second in element.schema.remainder.names:
                    return DimensionFieldReference.model_construct(element=element, field=second)
                else:
                    raise InvalidQueryError(f"Unrecognized field {second!r} for {first}.")
            elif second in DATASET_FIELD_NAMES:
                # We just assume the dataset type is okay; it's the job of
                # higher-level code to complain otherwise.
                return DatasetFieldReference.model_construct(
                    dataset_type=first, field=cast(DatasetFieldName, second)
                )
            if first == "timespan":
                base = interpret_identifier(dimensions, datasets, "timespan", bind)
                if second == "begin":
                    return UnaryExpression(operand=base, operator="begin_of")
                if second == "end":
                    return UnaryExpression(operand=base, operator="end_of")
            elif first in datasets:
                raise InvalidQueryError(
                    f"Identifier {identifier!r} references dataset type {first!r} but field "
                    f"{second!r} is not valid for datasets."
                )
        case 3:
            base = interpret_identifier(dimensions, datasets, ".".join(terms[:2]), bind)
            if terms[2] == "begin":
                return UnaryExpression(operand=base, operator="begin_of")
            if terms[2] == "end":
                return UnaryExpression(operand=base, operator="end_of")
    raise InvalidQueryError(f"Unrecognized identifier {identifier!r}.")
