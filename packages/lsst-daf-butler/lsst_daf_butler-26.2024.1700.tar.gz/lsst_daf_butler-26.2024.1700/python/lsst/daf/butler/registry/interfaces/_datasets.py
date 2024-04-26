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

from ... import ddl

__all__ = ("DatasetRecordStorageManager", "DatasetRecordStorage")

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator, Mapping, Sequence, Set
from typing import TYPE_CHECKING, Any

from lsst.daf.relation import Relation

from ..._dataset_ref import DatasetId, DatasetIdGenEnum, DatasetRef
from ..._dataset_type import DatasetType
from ..._exceptions import MissingDatasetTypeError
from ..._timespan import Timespan
from ...dimensions import DataCoordinate
from ._versioning import VersionedExtension, VersionTuple

if TYPE_CHECKING:
    from ...direct_query_driver import QueryJoiner  # new query system, server+direct only
    from .._caching_context import CachingContext
    from .._collection_summary import CollectionSummary
    from ..queries import SqlQueryContext  # old registry query system
    from ._collections import CollectionManager, CollectionRecord, RunRecord
    from ._database import Database, StaticTablesContext
    from ._dimensions import DimensionRecordStorageManager


class DatasetRecordStorage(ABC):
    """An interface that manages the records associated with a particular
    `DatasetType`.

    Parameters
    ----------
    datasetType : `DatasetType`
        Dataset type whose records this object manages.
    """

    def __init__(self, datasetType: DatasetType):
        self.datasetType = datasetType

    @abstractmethod
    def insert(
        self,
        run: RunRecord,
        dataIds: Iterable[DataCoordinate],
        idGenerationMode: DatasetIdGenEnum = DatasetIdGenEnum.UNIQUE,
    ) -> Iterator[DatasetRef]:
        """Insert one or more dataset entries into the database.

        Parameters
        ----------
        run : `RunRecord`
            The record object describing the `~CollectionType.RUN` collection
            this dataset will be associated with.
        dataIds : `~collections.abc.Iterable` [ `DataCoordinate` ]
            Expanded data IDs (`DataCoordinate` instances) for the
            datasets to be added.   The dimensions of all data IDs must be the
            same as ``self.datasetType.dimensions``.
        idGenerationMode : `DatasetIdGenEnum`
            With `UNIQUE` each new dataset is inserted with its new unique ID.
            With non-`UNIQUE` mode ID is computed from some combination of
            dataset type, dataId, and run collection name; if the same ID is
            already in the database then new record is not inserted.

        Returns
        -------
        datasets : `~collections.abc.Iterable` [ `DatasetRef` ]
            References to the inserted datasets.
        """
        raise NotImplementedError()

    @abstractmethod
    def import_(
        self,
        run: RunRecord,
        datasets: Iterable[DatasetRef],
    ) -> Iterator[DatasetRef]:
        """Insert one or more dataset entries into the database.

        Parameters
        ----------
        run : `RunRecord`
            The record object describing the `~CollectionType.RUN` collection
            this dataset will be associated with.
        datasets : `~collections.abc.Iterable` of `DatasetRef`
            Datasets to be inserted.  Datasets can specify ``id`` attribute
            which will be used for inserted datasets. All dataset IDs must
            have the same type (`int` or `uuid.UUID`), if type of dataset IDs
            does not match type supported by this class then IDs will be
            ignored and new IDs will be generated by backend.

        Returns
        -------
        datasets : `~collections.abc.Iterable` [ `DatasetRef` ]
            References to the inserted or existing datasets.

        Notes
        -----
        The ``datasetType`` and ``run`` attributes of datasets are supposed to
        be identical across all datasets but this is not checked and it should
        be enforced by higher level registry code. This method does not need
        to use those attributes from datasets, only ``dataId`` and ``id`` are
        relevant.
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self, datasets: Iterable[DatasetRef]) -> None:
        """Fully delete the given datasets from the registry.

        Parameters
        ----------
        datasets : `~collections.abc.Iterable` [ `DatasetRef` ]
            Datasets to be deleted.  All datasets must be resolved and have
            the same `DatasetType` as ``self``.

        Raises
        ------
        AmbiguousDatasetError
            Raised if any of the given `DatasetRef` instances is unresolved.
        """
        raise NotImplementedError()

    @abstractmethod
    def associate(self, collection: CollectionRecord, datasets: Iterable[DatasetRef]) -> None:
        """Associate one or more datasets with a collection.

        Parameters
        ----------
        collection : `CollectionRecord`
            The record object describing the collection.  ``collection.type``
            must be `~CollectionType.TAGGED`.
        datasets : `~collections.abc.Iterable` [ `DatasetRef` ]
            Datasets to be associated.  All datasets must be resolved and have
            the same `DatasetType` as ``self``.

        Raises
        ------
        AmbiguousDatasetError
            Raised if any of the given `DatasetRef` instances is unresolved.

        Notes
        -----
        Associating a dataset with into collection that already contains a
        different dataset with the same `DatasetType` and data ID will remove
        the existing dataset from that collection.

        Associating the same dataset into a collection multiple times is a
        no-op, but is still not permitted on read-only databases.
        """
        raise NotImplementedError()

    @abstractmethod
    def disassociate(self, collection: CollectionRecord, datasets: Iterable[DatasetRef]) -> None:
        """Remove one or more datasets from a collection.

        Parameters
        ----------
        collection : `CollectionRecord`
            The record object describing the collection.  ``collection.type``
            must be `~CollectionType.TAGGED`.
        datasets : `~collections.abc.Iterable` [ `DatasetRef` ]
            Datasets to be disassociated.  All datasets must be resolved and
            have the same `DatasetType` as ``self``.

        Raises
        ------
        AmbiguousDatasetError
            Raised if any of the given `DatasetRef` instances is unresolved.
        """
        raise NotImplementedError()

    @abstractmethod
    def certify(
        self,
        collection: CollectionRecord,
        datasets: Iterable[DatasetRef],
        timespan: Timespan,
        context: SqlQueryContext,
    ) -> None:
        """Associate one or more datasets with a calibration collection and a
        validity range within it.

        Parameters
        ----------
        collection : `CollectionRecord`
            The record object describing the collection.  ``collection.type``
            must be `~CollectionType.CALIBRATION`.
        datasets : `~collections.abc.Iterable` [ `DatasetRef` ]
            Datasets to be associated.  All datasets must be resolved and have
            the same `DatasetType` as ``self``.
        timespan : `Timespan`
            The validity range for these datasets within the collection.
        context : `SqlQueryContext`
            The object that manages database connections, temporary tables and
            relation engines for this query.

        Raises
        ------
        AmbiguousDatasetError
            Raised if any of the given `DatasetRef` instances is unresolved.
        ConflictingDefinitionError
            Raised if the collection already contains a different dataset with
            the same `DatasetType` and data ID and an overlapping validity
            range.
        CollectionTypeError
            Raised if
            ``collection.type is not CollectionType.CALIBRATION`` or if
            ``self.datasetType.isCalibration() is False``.
        """
        raise NotImplementedError()

    @abstractmethod
    def decertify(
        self,
        collection: CollectionRecord,
        timespan: Timespan,
        *,
        dataIds: Iterable[DataCoordinate] | None = None,
        context: SqlQueryContext,
    ) -> None:
        """Remove or adjust datasets to clear a validity range within a
        calibration collection.

        Parameters
        ----------
        collection : `CollectionRecord`
            The record object describing the collection.  ``collection.type``
            must be `~CollectionType.CALIBRATION`.
        timespan : `Timespan`
            The validity range to remove datasets from within the collection.
            Datasets that overlap this range but are not contained by it will
            have their validity ranges adjusted to not overlap it, which may
            split a single dataset validity range into two.
        dataIds : `~collections.abc.Iterable` [ `DataCoordinate` ], optional
            Data IDs that should be decertified within the given validity range
            If `None`, all data IDs for ``self.datasetType`` will be
            decertified.
        context : `SqlQueryContext`
            The object that manages database connections, temporary tables and
            relation engines for this query.

        Raises
        ------
        CollectionTypeError
            Raised if ``collection.type is not CollectionType.CALIBRATION``.
        """
        raise NotImplementedError()

    @abstractmethod
    def make_relation(
        self,
        *collections: CollectionRecord,
        columns: Set[str],
        context: SqlQueryContext,
    ) -> Relation:
        """Return a `sql.Relation` that represents a query for for this
        `DatasetType` in one or more collections.

        Parameters
        ----------
        *collections : `CollectionRecord`
            The record object(s) describing the collection(s) to query.  May
            not be of type `CollectionType.CHAINED`.  If multiple collections
            are passed, the query will search all of them in an unspecified
            order, and all collections must have the same type.  Must include
            at least one collection.
        columns : `~collections.abc.Set` [ `str` ]
            Columns to include in the relation.  See `Query.find_datasets` for
            most options, but this method supports one more:

            - ``rank``: a calculated integer column holding the index of the
              collection the dataset was found in, within the ``collections``
              sequence given.
        context : `SqlQueryContext`
            The object that manages database connections, temporary tables and
            relation engines for this query.

        Returns
        -------
        relation : `~lsst.daf.relation.Relation`
            Representation of the query.
        """
        raise NotImplementedError()

    @abstractmethod
    def make_query_joiner(self, collections: Sequence[CollectionRecord], fields: Set[str]) -> QueryJoiner:
        """Make a `..direct_query_driver.QueryJoiner` that represents a search
        for datasets of this type.

        Parameters
        ----------
        collections : `~collections.abc.Sequence` [ `CollectionRecord` ]
            Collections to search, in order, after filtering out collections
            with no datasets of this type via collection summaries.
        fields : `~collections.abc.Set` [ `str` ]
            Names of fields to make available in the joiner.  Options include:

            - ``dataset_id`` (UUID)
            - ``run` (collection name, `str`)
            - ``collection`` (collection name, `str`)
            - ``collection_key`` (collection primary key, manager-dependent)
            - ``timespan`` (validity range, or unbounded for non-calibrations)
            - ``ingest_date`` (time dataset was ingested into repository)

            Dimension keys for the dataset type's required dimensions are
            always included.

        Returns
        -------
        joiner : `..direct_query_driver.QueryJoiner`
            A query-construction object representing a table or subquery.  If
            ``fields`` is empty or ``len(collections) <= 1``, this is
            guaranteed to have rows that are unique over dimension keys.
        """
        raise NotImplementedError()

    datasetType: DatasetType
    """Dataset type whose records this object manages (`DatasetType`).
    """


class DatasetRecordStorageManager(VersionedExtension):
    """An interface that manages the tables that describe datasets.

    `DatasetRecordStorageManager` primarily serves as a container and factory
    for `DatasetRecordStorage` instances, which each provide access to the
    records for a different `DatasetType`.

    Parameters
    ----------
    registry_schema_version : `VersionTuple` or `None`, optional
        Version of registry schema.
    """

    def __init__(self, *, registry_schema_version: VersionTuple | None = None) -> None:
        super().__init__(registry_schema_version=registry_schema_version)

    @abstractmethod
    def clone(
        self,
        *,
        db: Database,
        collections: CollectionManager,
        dimensions: DimensionRecordStorageManager,
        caching_context: CachingContext,
    ) -> DatasetRecordStorageManager:
        """Make an independent copy of this manager instance bound to new
        instances of `Database` and other managers.

        Parameters
        ----------
        db : `Database`
            New `Database` object to use when instantiating the manager.
        collections : `CollectionManager`
            New `CollectionManager` object to use when instantiating the
            manager.
        dimensions : `DimensionRecordStorageManager`
            New `DimensionRecordStorageManager` object to use when
            instantiating the manager.
        caching_context : `CachingContext`
            New `CachingContext` object to use when instantiating the manager.

        Returns
        -------
        instance : `DatasetRecordStorageManager`
            New manager instance with the same configuration as this instance,
            but bound to a new Database object.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def initialize(
        cls,
        db: Database,
        context: StaticTablesContext,
        *,
        collections: CollectionManager,
        dimensions: DimensionRecordStorageManager,
        caching_context: CachingContext,
        registry_schema_version: VersionTuple | None = None,
    ) -> DatasetRecordStorageManager:
        """Construct an instance of the manager.

        Parameters
        ----------
        db : `Database`
            Interface to the underlying database engine and namespace.
        context : `StaticTablesContext`
            Context object obtained from `Database.declareStaticTables`; used
            to declare any tables that should always be present.
        collections : `CollectionManager`
            Manager object for the collections in this `Registry`.
        dimensions : `DimensionRecordStorageManager`
            Manager object for the dimensions in this `Registry`.
        caching_context : `CachingContext`
            Object controlling caching of information returned by managers.
        registry_schema_version : `VersionTuple` or `None`
            Schema version of this extension as defined in registry.

        Returns
        -------
        manager : `DatasetRecordStorageManager`
            An instance of a concrete `DatasetRecordStorageManager` subclass.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def getIdColumnType(cls) -> type:
        """Return type used for columns storing dataset IDs.

        This type is used for columns storing `DatasetRef.id` values, usually
        a `type` subclass provided by SQLAlchemy.

        Returns
        -------
        dtype : `type`
            Type used for dataset identification in database.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def supportsIdGenerationMode(cls, mode: DatasetIdGenEnum) -> bool:
        """Test whether the given dataset ID generation mode is supported by
        `insert`.

        Parameters
        ----------
        mode : `DatasetIdGenEnum`
            Enum value for the mode to test.

        Returns
        -------
        supported : `bool`
            Whether the given mode is supported.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def addDatasetForeignKey(
        cls,
        tableSpec: ddl.TableSpec,
        *,
        name: str = "dataset",
        constraint: bool = True,
        onDelete: str | None = None,
        **kwargs: Any,
    ) -> ddl.FieldSpec:
        """Add a foreign key (field and constraint) referencing the dataset
        table.

        Parameters
        ----------
        tableSpec : `ddl.TableSpec`
            Specification for the table that should reference the dataset
            table.  Will be modified in place.
        name : `str`, optional
            A name to use for the prefix of the new field; the full name is
            ``{name}_id``.
        constraint : `bool`, optional
            If `False` (`True` is default), add a field that can be joined to
            the dataset primary key, but do not add a foreign key constraint.
        onDelete : `str`, optional
            One of "CASCADE" or "SET NULL", indicating what should happen to
            the referencing row if the collection row is deleted.  `None`
            indicates that this should be an integrity error.
        **kwargs
            Additional keyword arguments are forwarded to the `ddl.FieldSpec`
            constructor (only the ``name`` and ``dtype`` arguments are
            otherwise provided).

        Returns
        -------
        idSpec : `ddl.FieldSpec`
            Specification for the ID field.
        """
        raise NotImplementedError()

    @abstractmethod
    def refresh(self) -> None:
        """Ensure all other operations on this manager are aware of any
        dataset types that may have been registered by other clients since
        it was initialized or last refreshed.
        """
        raise NotImplementedError()

    def __getitem__(self, name: str) -> DatasetRecordStorage:
        """Return the object that provides access to the records associated
        with the given `DatasetType` name.

        This is simply a convenience wrapper for `find` that raises `KeyError`
        when the dataset type is not found.

        Returns
        -------
        records : `DatasetRecordStorage`
            The object representing the records for the given dataset type.

        Raises
        ------
        KeyError
            Raised if there is no dataset type with the given name.

        Notes
        -----
        Dataset types registered by another client of the same repository since
        the last call to `initialize` or `refresh` may not be found.
        """
        result = self.find(name)
        if result is None:
            raise MissingDatasetTypeError(f"Dataset type with name '{name}' not found.")
        return result

    @abstractmethod
    def find(self, name: str) -> DatasetRecordStorage | None:
        """Return an object that provides access to the records associated with
        the given `DatasetType` name, if one exists.

        Parameters
        ----------
        name : `str`
            Name of the dataset type.

        Returns
        -------
        records : `DatasetRecordStorage` or `None`
            The object representing the records for the given dataset type, or
            `None` if there are no records for that dataset type.

        Notes
        -----
        Dataset types registered by another client of the same repository since
        the last call to `initialize` or `refresh` may not be found.
        """
        raise NotImplementedError()

    @abstractmethod
    def register(self, datasetType: DatasetType) -> bool:
        """Ensure that this `Registry` can hold records for the given
        `DatasetType`, creating new tables as necessary.

        Parameters
        ----------
        datasetType : `DatasetType`
            Dataset type for which a table should created (as necessary) and
            an associated `DatasetRecordStorage` returned.

        Returns
        -------
        inserted : `bool`
            `True` if the dataset type did not exist in the registry before.

        Notes
        -----
        This operation may not be invoked within a `Database.transaction`
        context.
        """
        raise NotImplementedError()

    @abstractmethod
    def remove(self, name: str) -> None:
        """Remove the dataset type.

        Parameters
        ----------
        name : `str`
            Name of the dataset type.
        """
        raise NotImplementedError()

    @abstractmethod
    def resolve_wildcard(
        self,
        expression: Any,
        missing: list[str] | None = None,
        explicit_only: bool = False,
    ) -> list[DatasetType]:
        """Resolve a dataset type wildcard expression.

        Parameters
        ----------
        expression : `~typing.Any`
            Expression to resolve.  Will be passed to
            `DatasetTypeWildcard.from_expression`.
        missing : `list` of `str`, optional
            String dataset type names that were explicitly given (i.e. not
            regular expression patterns) but not found will be appended to this
            list, if it is provided.
        explicit_only : `bool`, optional
            If `True`, require explicit `DatasetType` instances or `str` names,
            with `re.Pattern` instances deprecated and ``...`` prohibited.

        Returns
        -------
        dataset_types : `list` [ `DatasetType` ]
            A list of resolved dataset types.
        """
        raise NotImplementedError()

    @abstractmethod
    def getDatasetRef(self, id: DatasetId) -> DatasetRef | None:
        """Return a `DatasetRef` for the given dataset primary key
        value.

        Parameters
        ----------
        id : `DatasetId`
            Primary key value for the dataset.

        Returns
        -------
        ref : `DatasetRef` or `None`
            Object representing the dataset, or `None` if no dataset with the
            given primary key values exists in this layer.
        """
        raise NotImplementedError()

    @abstractmethod
    def getCollectionSummary(self, collection: CollectionRecord) -> CollectionSummary:
        """Return a summary for the given collection.

        Parameters
        ----------
        collection : `CollectionRecord`
            Record describing the collection for which a summary is to be
            retrieved.

        Returns
        -------
        summary : `CollectionSummary`
            Summary of the dataset types and governor dimension values in
            this collection.
        """
        raise NotImplementedError()

    @abstractmethod
    def fetch_summaries(
        self, collections: Iterable[CollectionRecord], dataset_types: Iterable[DatasetType] | None = None
    ) -> Mapping[Any, CollectionSummary]:
        """Fetch collection summaries given their names and dataset types.

        Parameters
        ----------
        collections : `~collections.abc.Iterable` [`CollectionRecord`]
            Collection records to query.
        dataset_types : `~collections.abc.Iterable` [`DatasetType`] or `None`
            Dataset types to include into returned summaries. If `None` then
            all dataset types will be included.

        Returns
        -------
        summaries : `~collections.abc.Mapping` [`Any`, `CollectionSummary`]
            Collection summaries indexed by collection record key. This mapping
            will also contain all nested non-chained collections of the chained
            collections.
        """
        raise NotImplementedError()

    @abstractmethod
    def ingest_date_dtype(self) -> type:
        """Return type of the ``ingest_date`` column."""
        raise NotImplementedError()
