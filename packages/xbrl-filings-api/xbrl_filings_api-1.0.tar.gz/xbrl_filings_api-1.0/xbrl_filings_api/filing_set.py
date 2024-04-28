"""
Define `FilingSet` class.

This is an extended set type with certain added attributes.

"""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import copy
import sys
from collections.abc import (
    AsyncIterator,
    Collection,
    Iterable,
    Iterator,
    Mapping,
    MutableSet,
    Sequence,
)
from datetime import date, datetime
from pathlib import Path, PurePath
from typing import TYPE_CHECKING, Any, Optional, Union

from xbrl_filings_api import (
    database_processor,
    download_specs_construct,
    downloader,
    options,
)
from xbrl_filings_api.api_resource import APIResource
from xbrl_filings_api.constants import DataAttributeType, FileStringType
from xbrl_filings_api.download_info import DownloadInfo
from xbrl_filings_api.download_item import DownloadItem
from xbrl_filings_api.entity import Entity
from xbrl_filings_api.exceptions import CorruptDownloadError
from xbrl_filings_api.filing import Filing
from xbrl_filings_api.resource_collection import ResourceCollection
from xbrl_filings_api.scope_flag import ScopeFlag
from xbrl_filings_api.validation_message import ValidationMessage

if TYPE_CHECKING and sys.version_info >= (3, 10):
    from types import NotImplementedType

__all__ = ['FilingSet']


class FilingSet:
    r"""Mutable set for `Filing` objects.

    Can be initialized with the single argument being an iterable of
    `Filing` objects. This class provides a similar but broader
    interface as builtin :class:`set` class. All set-like operators and
    methods accept iterables instead of strict sets. This class
    implements a :term:`mutable set` and :pt:`isinstance(filingset,
    collections.abc.MutableSet)` is :pt:`True` (virtual subclass).

    In addition to set functionality it provides certain filing-related
    attributes and methods.

    If working with large sets, in-place operations (e.g. `update`
    method and ``|=`` operator) are recommended over new set operations
    (`union` method and ``|`` operator). See section *Notes*.

    Defines operators ``|``, ``|=``, ``&``, ``&=``, ``-``, ``-=``,
    ``^``, ``^=``, ``<``, ``<=``, ``==``, ``>``, ``>=``, and ``!=``.
    Instead of just set-like objects, the operators accept any iterables
    of Filing objects.

    `Filing` objects, as subclass of `APIResource`, have a custom
    `__hash__() <APIResource.__hash__>` method and their hash is based
    on a tuple of strings 'APIResource',
    `Filing.TYPE <APIResource.TYPE>`, and
    `Filing.api_id <APIResource.api_id>`. This means that equality
    checks (``==`` and ``!=`` operators) and set content uniqueness are
    based on this tuple. For example, when the actual filing object is
    not available, the fastest way to check if a filing with ``api_id``
    '123' is included in the filing set ``fs`` is::

        ('APIResource', Filing.TYPE, '123') in fs

    Same applies for `ResourceCollection` in attributes
    `entities` and `validation_messages`. These collections are,
    however, lazy iterators.

    Notes
    -----
    It is possible to combine filing sets from different queries into a
    single ``FilingSet`` without redundant copies of objects. Due to
    cross-referencing, the operations returning a new set always deep
    copy all objects to the results set. The in-place operations retain
    the objects from the left set but deep copy everything from the
    right set.

    As the operators work on an iterable basis, for example the ``>=``
    operator or `issuperset()` method returns True for a FilingSet and
    any iterable with the same Filings but is undefined if the iterable
    contains any item other than a filing. However, operators ``==`` and
    ``!=`` are never undefined.
    """

    def __init__(self, filings: Optional[Iterable[Filing]] = None) -> None:
        """
        Initialize `FilingSet`.

        Parameters
        ----------
        filings : iterable of Filing, optional
            Initial filings.
        """
        self._filings: set[Filing] = set()
        if filings is not None:
            if isinstance(filings, FilingSet):
                self._filings.update(filings)
            else:
                for filing in filings:
                    if not isinstance(filing, Filing):
                        msg = 'All iterable items must be Filing objects.'
                        raise ValueError(msg)
                    self._filings.add(filing)

        self.entities = ResourceCollection(self, 'entity', Entity)
        """
        Lazy iterator for entity references in filings.

        See documentation for `ResourceCollection` class.
        """

        self.validation_messages = ResourceCollection(
            self, 'validation_messages', ValidationMessage)
        """
        Lazy iterator for validation message references in filings.

        See documentation for `ResourceCollection` class.
        """

    @property
    def columns(self) -> list[str]:
        """List of available columns for filings of this set."""
        flags = ScopeFlag.GET_ONLY_FILINGS
        if self.entities.exist:
            flags = ScopeFlag.GET_ENTITY
        return Filing.get_data_attributes(
            flags=flags,
            filings=self
            )

    def download(
            self,
            files: Union[
                FileStringType,
                Iterable[FileStringType],
                Mapping[FileStringType, DownloadItem]
                ],
            to_dir: Union[str, PurePath, None] = None,
            *,
            stem_pattern: Union[str, None] = None,
            check_corruption: bool = True,
            max_concurrent: Union[int, None] = 5,
            ) -> None:
        """
        Download files according to parameter ``files``.

        The ``files`` parameter accepts three formats::

            fs.download('json', to_dir='dir/path')
            fs.download(['json', 'package'], to_dir='dir/path')
            fs.download({
                    'json': DownloadItem(),
                    'package': DownloadItem(to_dir=other_dir)
                }, to_dir='dir/path')

        The filesystem path of the downloaded file will be saved in the
        `Filing` object attributes ``<file>_download_path`` such as
        ``json_download_path`` for the downloaded JSON file.

        If ``package`` files are requested to be downloaded and
        parameter ``check_corruption`` is :pt:`True`, the downloaded
        package files will be checked through the `package_sha256`
        attribute. If these attribute values do not match the ones
        calculated from the downloaded files, an exception
        :exc:`~xbrl_filings_api.exceptions.CorruptDownloadError` of the
        first corrupt file is raised after all downloads have finished.
        The downloaded files will not be deleted but the filenames will
        be appended with ending ``".corrupt"``. However, attributes
        `Filing.package_download_path` will not store these corrupt
        paths.

        The directories in the path of parameter ``to_dir`` will be
        created if they do not exist. By default, filename is derived
        from download URL. If the file already exists, it will be
        overwritten.

        If download is interrupted, the files will be left with ending
        ``".unfinished"``.

        If no name could be derived from the url attribute, the file
        will be named ``file0001``, ``file0002``, etc. In this case a
        new file is always created.

        Parameter ``stem_pattern`` requires a placeholder ``"/name/"``.
        For example pattern ``/name/_second_try`` will change original
        filename ``743700XJC24THUPK0S03-2022-12-31-fi.xhtml`` into
        ``743700XJC24THUPK0S03-2022-12-31-fi_second_try.xhtml``. Not
        recommended for packages as their names should not be changed.

        HTTP request timeout is defined in `options.timeout_sec`.

        Parameters
        ----------
        files : str or iterable of str or mapping of {str: DownloadItem}
            All of the ``str`` values in annotation are `FileStringType`
            literals. `DownloadItem` attributes override method
            arguments for the file.
        to_dir : path-like, optional
            Directory to save the files. Defaults to working directory.
        stem_pattern : str, optional
            Pattern to add to the filename stems. Placeholder
            ``"/name/"`` is always required.
        check_corruption : bool, default True
            Raise
            :exc:`~xbrl_filings_api.exceptions.CorruptDownloadError` for
            any corrupt ``'package'`` file.
        max_concurrent : int or None, default 5
            Maximum number of simultaneous downloads allowed. Value
            :pt:`None` means unlimited.

        Raises
        ------
        ~xbrl_filings_api.exceptions.CorruptDownloadError
            When attribute `Filing.package_sha256` does not match the
            calculated hash of ``'package'`` file and
            ``check_corruption`` is :pt:`True`.
        requests.HTTPError
            When HTTP status error occurs.
        requests.ConnectionError
            When connection fails.

        See Also
        --------
        Filing.download : For a single filing.
        """
        downloader.validate_stem_pattern(stem_pattern)

        items = []
        for filing in self:
            items.extend(
                download_specs_construct.construct(
                    files, filing, to_dir, stem_pattern,
                    check_corruption=check_corruption,
                    isfilingset=True
                    ))
        results = downloader.download_parallel(
            items,
            max_concurrent=max_concurrent,
            timeout=options.timeout_sec
            )
        for result in results:
            if result.path:
                res_info: DownloadInfo = result.info
                setattr(
                    res_info.obj,
                    f'{res_info.file}_download_path',
                    result.path
                    )
        excs = [
            result.err for result in results
            if isinstance(result.err, Exception)
            ]
        for err_i, err in enumerate(excs):
            if isinstance(err, downloader.CorruptDownloadError):
                # Wrap again with FilingsAPIError subclassed exception
                excs[err_i] = CorruptDownloadError(
                    path=err.path,
                    url=err.url,
                    calculated_hash=err.calculated_hash,
                    expected_hash=err.expected_hash
                    )
        if excs:
            raise excs[0]

    async def download_aiter(
            self,
            files: Union[
                FileStringType,
                Iterable[FileStringType],
                Mapping[FileStringType, DownloadItem]
                ],
            to_dir: Union[str, PurePath, None] = None,
            *,
            stem_pattern: Union[str, None] = None,
            check_corruption: bool = True,
            max_concurrent: Union[int, None] = 5
            ) -> AsyncIterator[downloader.DownloadResult]:
        """
        Download files and yield `DownloadResult` objects.

        The function follows the same logic as method `download()`. See
        documentation.

        Parameters
        ----------
        files : str or iterable of str or mapping of {str: DownloadItem}
            All of the ``str`` values in annotation are `FileStringType`
            literals. `DownloadItem` attributes override method
            arguments for the file.
        to_dir : path-like, optional
            Directory to save the files. Defaults to working directory.
        stem_pattern : str, optional
            Pattern to add to the filename stems. Placeholder
            ``"/name/"`` is always required.
        check_corruption : bool, default True
            Raise
            :exc:`~xbrl_filings_api.exceptions.CorruptDownloadError` for
            any corrupt ``'package'`` file.
        max_concurrent : int or None, default 5
            Maximum number of simultaneous downloads allowed. Value
            :pt:`None` means unlimited.

        Yields
        ------
        DownloadResult
            Contains information on the finished download.

        See Also
        --------
        Filing.download_aiter : For a single filing.
        """
        downloader.validate_stem_pattern(stem_pattern)

        items = []
        for filing in self:
            items.extend(
                download_specs_construct.construct(
                    files, filing, to_dir, stem_pattern,
                    check_corruption=check_corruption,
                    isfilingset=True
                    ))
        dliter = downloader.download_parallel_aiter(
            items,
            max_concurrent=max_concurrent,
            timeout=options.timeout_sec
            )
        async for result in dliter:
            yresult = result
            if yresult.path:
                res_info: DownloadInfo = yresult.info
                setattr(
                    res_info.obj,
                    f'{res_info.file}_download_path',
                    yresult.path
                    )
            orig_err = yresult.err
            if isinstance(orig_err, downloader.CorruptDownloadError):
                # Wrap again with FilingsAPIError subclassed exception
                err = CorruptDownloadError(
                    path=orig_err.path,
                    url=orig_err.url,
                    calculated_hash=orig_err.calculated_hash,
                    expected_hash=orig_err.expected_hash
                    )
                yresult = downloader.DownloadResult(
                    yresult.url, yresult.path, err, yresult.info)
            yield yresult

    def get_pandas_data(
            self, attr_names: Optional[Iterable[str]] = None, *,
            with_entity: bool = False, strip_timezone: bool = True,
            date_as_datetime: bool = True, include_urls : bool = False,
            include_paths : bool = False
            ) -> dict[str, list[DataAttributeType]]:
        """
        Get filings as data for :class:`pandas.DataFrame` constructor.

        A new dataframe can be instantiated by::

            import pandas as pd
            df = pd.DataFrame(data=filingset.get_pandas_data())

        If parameter ``attr_names`` is not given, data attributes
        excluding ones ending ``_date_str`` will be extracted.
        Attributes ending in ``_download_path`` will be extracted only
        if at least one file of this type has been downloaded (and
        ``include_paths`` is :pt:`True`) and `entity_api_id` if there is
        at least one entity object in the set and parameter
        ``with_entity`` is :pt:`False`.

        Parameters
        ----------
        attr_names : iterable of str, optional
            Valid attributes names of `Filing` object or ``entity.``
            prefixed attributes of its `Entity` object.
        with_entity : bool, default False
            When parameter ``attr_names`` is not given, include entity
            attributes to the filing.
        strip_timezone : bool, default True
            Strip timezone information (always UTC) from
            :class:`~datetime.datetime` values.
        date_as_datetime : bool, default True
            Convert :class:`~datetime.date` values to naive
            :class:`~datetime.datetime` to be converted to
            :class:`pandas.datetime64` by pandas.
        include_urls : bool, default False
            When parameter ``attr_names`` is not given, include
            attributes ending ``_url``.
        include_paths : bool, default False
            When parameter ``attr_names`` is not given, include
            attributes ending ``_path``.

        Returns
        -------
        data : dict of {str: list of DataAttributeType}
            Column names are the same as the attributes for resource of
            this type.

        See Also
        --------
        ResourceCollection.get_pandas_data : For other resources.
        """
        data: dict[str, list[DataAttributeType]]
        if attr_names:
            data = {col: [] for col in attr_names}
        else:
            data = {col: [] for col in self.columns}
            if with_entity:
                if 'entity_api_id' in data:
                    del data['entity_api_id']
                ent_cols: dict[str, list[DataAttributeType]] = {
                    f'entity.{col}': [] for col in self.entities.columns}
                data.update(ent_cols)
            if not include_urls:
                url_cols = [col for col in data if col.endswith('_url')]
                for col in url_cols:
                    del data[col]
            if not include_paths:
                path_cols = [col for col in data if col.endswith('_path')]
                for col in path_cols:
                    del data[col]
        for filing in self:
            for col_name in data:
                val: DataAttributeType = None
                if col_name.startswith('entity.'):
                    if filing.entity:
                        val = getattr(filing.entity, col_name[7:])
                else:
                    val = getattr(filing, col_name)
                if strip_timezone and isinstance(val, datetime):
                    val = val.replace(tzinfo=None)
                if (date_as_datetime
                        and isinstance(val, date)
                        and type(val) is not datetime):
                    val = datetime.fromordinal(val.toordinal())
                data[col_name].append(val)
        return data

    def pop_duplicates(
            self, languages: Union[Iterable[str], None] = ['en'], *,
            use_reporting_date: bool = False, all_markets: bool = False
            ) -> FilingSet:
        """
        Pops duplicates of the same enclosure from the set of filings.

        Entities must be available on the `FilingSet`.

        The method searches the ``FilingSet`` and leaves only one filing
        for each group of same `entity_api_id`, `last_end_date` pairs,
        i.e., one filing for each unique enclosure of the same entity
        for the same financial period. If parameter
        ``use_reporting_date`` is :pt:`True`, grouping is based on
        ``entity_api_id``, `reporting_date` instead.

        Some entities report on multiple markets. If all these
        country-specific filings are wished to retain, set parameter
        ``all_markets`` as :pt:`True`. Grouping will then also include
        `country` as the last item.

        The selected filing from the group is chosen primarily on
        ``languages`` parameter values matched on the `Filing.language`
        attribute. Parameter value ``['sv', 'fi']`` thus means that
        Swedish filings are preferred, secondarily Finnish, and lastly
        the ones which have language as :pt:`None`. Value :pt:`None` can
        be used in the iterable as well. Parameter value :pt:`None`
        means no language preference.

        If there are more than one filing for the language match (or
        ``language`` is :pt:`None`), the filings will be ordered based
        on their `filing_index` and the last one is chosen which is
        practically the one with highest filing number part of
        ``filing_index``.

        Parameters
        ----------
        languages : iterable of str or None, default ['en']
            Preferred languages for the retained filing.
        use_reporting_date : bool, default False
            Use `reporting_date` instead of `last_end_date` when
            grouping.
        all_markets : bool, default False
            Append `country` as the last item in grouping.

        Returns
        -------
        FilingSet
            The set of removed filings.
        """
        if not self.entities.exist:
            msg = 'Entities must be available on the FilingSet'
            raise ValueError(msg)
        if languages is None:
            langs = [None]
        else:
            # Expected type Iterable[None] ?
            langs = list(languages) # type: ignore[arg-type]
        if not any(lan is None for lan in langs):
            langs.append(None)

        enclosures: dict[str, set[Filing]] = {}
        for filing in self:
            key = f'{filing.entity_api_id}'
            if use_reporting_date:
                key += f':{filing.reporting_date}'
            else:
                key += f':{filing.last_end_date}'
            if all_markets:
                key += f':{filing.country}'

            if enclosures.get(key):
                enclosures[key].add(filing)
            else:
                enclosures[key] = {filing}

        popped: set[Filing] = set()
        for enc_filings in enclosures.values():
            # Select correct language filing to be retained
            retain_filing: Union[Filing, None] = None
            for lan in langs:
                lang_filings: set[Filing] = set(filter(
                    lambda f: f.language == lan, enc_filings))
                retain_filing = (
                    self._get_last_filing_index_filing(lang_filings))
                if retain_filing:
                    break
            else:
                # Fallback if no preferred language or None matches
                retain_filing = self._get_last_filing_index_filing(enc_filings)
            # Add the rest to be returned and remove popped from self
            for filing in enc_filings:
                if filing is not retain_filing:
                    popped.add(filing)
        # Execute pop
        self.difference_update(popped)
        return FilingSet(popped)

    def to_sqlite(
            self,
            path: Union[str, Path],
            *,
            update: bool = False,
            flags: ScopeFlag = (
                ScopeFlag.GET_ENTITY
                | ScopeFlag.GET_VALIDATION_MESSAGES)
            ) -> None:
        """
        Save set to an SQLite3 database.

        The method has the same signature and follows the same rules as
        the query function :func:`~xbrl_filings_api.query.to_sqlite`
        with the exception of missing all query parameters.

        Flags also default to all tables turned on. If no additional
        information is present in the set, the tables will not be
        created if they do not exist.

        Parameters
        ----------
        path : path-like
            Path to the SQLite database.
        update : bool, default False
            If the database already exists, update it with these
            records. Old records are updated and new ones are added.
        flags : ScopeFlag, default GET_ENTITY | GET_VALIDATION_MESSAGES
            Scope of saving. Flag `GET_ENTITY` will save entity records
            of filings and `GET_VALIDATION_MESSAGES` the validation
            messages.

        Raises
        ------
        FileExistsError
            When ``update`` is :pt:`False` and the intended save path
            for the database is an existing file.
        DatabaseSchemaUnmatchError
            When ``update`` is :pt:`True` and the file contains a
            database whose schema does not match the expected format.
        sqlite3.DatabaseError
            For example when ``update`` is :pt:`True` and the file is
            not a database etc.

        See Also
        --------
        xbrl_filings_api.to_sqlite : Query and save to SQLite.
        """
        ppath = path if isinstance(path, Path) else Path(path)

        data_objs, flags = self._get_data_sets(flags)

        database_processor.sets_to_sqlite(
            flags, ppath, data_objs, update=update)

    def __repr__(self) -> str:
        """
        Return repr with len() of self, entities, validation_messages.

        Values len(`entities`) and len(`validation_messages`) are only
        shown if more than zero are present.
        """
        subreslist = ''
        if self.entities.exist:
            subreslist += f', len(entities)={len(self.entities)}'
        if self.validation_messages.exist:
            subreslist += (
                f', len(validation_messages)={len(self.validation_messages)}')
        return (
            f'{type(self).__name__}('
            f'len(self)={len(self)}{subreslist})'
            )

    def _get_data_sets(
            self, flags: ScopeFlag
            ) -> tuple[dict[str, Collection[APIResource]], ScopeFlag]:
        """Get sets of data objects and disable flags for empty sets."""
        # FilingSet is Collection[APIResource] (dict-item)
        data_objs: dict[str, Collection[APIResource]] = {
            'Filing': self} # type: ignore[dict-item]
        subresources = [
            (
                Entity,
                self.entities,
                ScopeFlag.GET_ENTITY
            ), (
                ValidationMessage,
                self.validation_messages,
                ScopeFlag.GET_VALIDATION_MESSAGES
            )]
        type_obj: type[APIResource]
        obj_set: ResourceCollection
        for type_obj, obj_set, type_flag in subresources:
            if not obj_set.exist:
                flags &= ~type_obj._FILING_FLAG
            elif type_flag in flags:
                data_objs[type_obj.__name__] = obj_set
        if flags == ScopeFlag(0):
            flags = ScopeFlag.GET_ONLY_FILINGS
        return data_objs, flags

    def _get_last_filing_index_filing(
            self, filings: set[Filing]
            ) -> Union[Filing, None]:
        if len(filings) == 0:
            return None
        str_indexes = [
            '' if f.filing_index is None else f.filing_index
            for f in filings
            ]
        max_filing_index = max(str_indexes)
        def filter_filing_index_str(filing: Filing) -> bool:
            ismatch = filing.filing_index == max_filing_index
            if not ismatch and max_filing_index == '':
                ismatch = filing.filing_index is None
            return ismatch
        return next(filter(filter_filing_index_str, filings))

    # Mutable set operations

    def __contains__(self, other: Any) -> int: # noqa: D105 # No docstring
        return other in self._filings

    def __iter__(self) -> Iterator[Filing]: # noqa: D105 # No docstring
        return iter(self._filings)

    def __len__(self) -> int: # noqa: D105 # No docstring
        return len(self._filings)

    def __lt__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]) -> Union[bool, NotImplementedType]:
        val: Union[bool, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            val = self._filings < set(arg_lists[0])
        return val

    def __le__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]) -> Union[bool, NotImplementedType]:
        val: Union[bool, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            val = self._filings <= set(arg_lists[0])
        return val

    def __ge__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]) -> Union[bool, NotImplementedType]:
        val: Union[bool, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            val = self._filings >= set(arg_lists[0])
        return val

    def __gt__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]) -> Union[bool, NotImplementedType]:
        val: Union[bool, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            val = self._filings > set(arg_lists[0])
        return val

    def __eq__( # noqa: D105 # No docstring
            self, other: object) -> bool:
        val: bool = False
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            val = self._filings == set(arg_lists[0])
        return val

    def __ne__(self, other: object) -> bool: # noqa: D105 # No docstring
        return not self.__eq__(other)

    def _hash(self) -> int:
        """Return hash() of frozenset of contained filings."""
        return hash(frozenset(self._filings))

    def clear(self) -> None:
        """Clear the filing set of filings."""
        self._filings.clear()

    def _union(
            self, fs: FilingSet, others: list[list[Filing]],
            *, isedit: bool) -> None:
        if not isedit:
            self._deepcopy_filingset_contents(fs)
        for fs_arg in others:
            for filing in fs_arg:
                fs.add(filing)

    def union(
            self, *others: Iterable[Filing]) -> FilingSet:
        """
        Return union FilingSet and update cross-references.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Returns
        -------
        FilingSet
            A new set which has filings of this set and all ``others``.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters(others)
        fs = FilingSet(self)
        self._union(fs, arg_lists, isedit=False)
        return fs

    def __or__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        new: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            new = FilingSet(self)
            self._union(new, arg_lists, isedit=False)
        return new

    def update(self, *others: Iterable[Filing]) -> None:
        """
        Apply union in self and update cross-references.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters(others)
        self._union(self, arg_lists, isedit=True)

    def __ior__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        val: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            self._union(self, arg_lists, isedit=True)
            val = self
        return val

    def _intersection(
            self, fs: FilingSet, others: list[list[Filing]], *,
            isedit: bool) -> None:
        if not isedit:
            self._deepcopy_filingset_contents(fs)
        id_differs = {filing: True for filing in self}
        for fs_arg in others:
            for filing in fs_arg:
                if filing in id_differs:
                    id_differs[filing] = False
        for filing, differs in id_differs.items():
            if differs:
                fs.remove(filing)

    def intersection(
            self, *others: Iterable[Filing]) -> FilingSet:
        """
        Return intersection FilingSet and update cross-references.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Returns
        -------
        FilingSet
            A new set which has filings common with this set and any set
            in ``others``.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters(others)
        fs = FilingSet(self)
        self._intersection(fs, arg_lists, isedit=False)
        return fs

    def __and__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        new: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            new = FilingSet(self)
            self._intersection(new, arg_lists, isedit=False)
        return new

    def intersection_update(self, *others: Iterable[Filing]) -> None:
        """
        Apply intersection in self and update cross-references.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters(others)
        self._intersection(self, arg_lists, isedit=True)

    def __iand__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        val: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            self._intersection(self, arg_lists, isedit=True)
            val = self
        return val

    def _difference(
            self, fs: FilingSet, others: list[list[Filing]], *,
            isedit: bool) -> None:
        if not isedit:
            self._deepcopy_filingset_contents(fs)
        for fs_arg in others:
            for filing in fs_arg:
                fs.discard(filing)

    def difference(
            self, *others: Iterable[Filing]) -> FilingSet:
        """
        Return difference FilingSet and update cross-references.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Returns
        -------
        FilingSet
            A new set which is this set without filings in all
            ``others``.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters(others)
        fs = FilingSet(self)
        self._difference(fs, arg_lists, isedit=False)
        return fs

    def __sub__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        new: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            new = FilingSet(self)
            self._difference(new, arg_lists, isedit=False)
        return new

    def difference_update(self, *others: Iterable[Filing]) -> None:
        """
        Apply difference to self and update cross-references.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters(others)
        self._difference(self, arg_lists, isedit=True)

    def __isub__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        val: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            self._difference(self, arg_lists, isedit=True)
            val = self
        return val

    def _symmetric_difference(
            self, fs: FilingSet, other: list[Filing], *, isedit: bool
            ) -> None:
        if not isedit:
            self._deepcopy_filingset_contents(fs)
        id_other_differs = {filing: True for filing in other}
        for filing in other:
            if filing in fs:
                fs.discard(filing)
                id_other_differs[filing] = False
        for filing, other_differs in id_other_differs.items():
            if other_differs:
                fs.add(filing)

    def symmetric_difference(
            self, other: Iterable[Filing]) -> FilingSet:
        """
        Return symmetric difference and update cross-references.

        Parameters
        ----------
        other : iterable of Filing
            An iterable of ``Filing`` objects.

        Returns
        -------
        FilingSet
            A new set which has filings in this set or ``other`` but not
            in both.

        Raises
        ------
        ValueError
            When any item in parameter ``other`` is not ``Filing``.
        """
        arg_lists = self._check_arg_iters([other])
        fs = FilingSet(self)
        self._symmetric_difference(fs, arg_lists[0], isedit=False)
        return fs

    def __xor__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        new: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            new = FilingSet(self)
            self._symmetric_difference(new, arg_lists[0], isedit=False)
        return new

    def symmetric_difference_update(self, other: Iterable[Filing]) -> None:
        """
        Apply symmetric difference in self and update cross-refs.

        Parameters
        ----------
        *others : iterable of Filing
            One or more arguments of ``Filing`` iterables.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters([other])
        self._symmetric_difference(self, arg_lists[0], isedit=True)

    def __ixor__( # noqa: D105 # No docstring
            self, other: Iterable[Filing]
            ) -> Union[FilingSet, NotImplementedType]:
        val: Union[FilingSet, NotImplementedType] = NotImplemented
        try:
            arg_lists = self._check_arg_iters([other])
        except (TypeError, ValueError):
            pass
        else:
            self._symmetric_difference(self, arg_lists[0], isedit=True)
            val = self
        return val

    def add(self, elem: Filing) -> None:
        """Add and update cross-references."""
        if not isinstance(elem, Filing):
            msg = 'FilingSet can only contain Filing objects'
            raise TypeError(msg)
        if elem in self:
            return
        new_elem = self._deepcopy_filing_with_vmessages(elem)
        if elem.entity_api_id:
            id_ent = elem.entity_api_id
            ent_existing: Union[Entity, None] = next(
                (e for e in self.entities # type: ignore[misc]
                 if e.api_id == id_ent),
                None
                )
            if ent_existing:
                ent_existing.filings.add(new_elem)
                new_elem.entity = ent_existing
        self._filings.add(new_elem)

    def discard(self, elem: Filing) -> None:
        """Discard and update cross-references."""
        try:
            self.remove(elem)
        except KeyError:
            pass

    def remove(self, elem: Filing) -> None:
        """Remove and update cross-references."""
        if not isinstance(elem, Filing):
            msg = repr(elem)
            raise KeyError(msg)
        id_filing = elem.api_id
        match_elem = next((f for f in self if f.api_id == id_filing), None)
        if not match_elem:
            msg = repr(elem)
            raise KeyError(msg)
        if match_elem and match_elem.entity:
            match_elem.entity.filings.remove(match_elem)
        self._filings.remove(match_elem)

    def pop(self) -> Filing:
        """Remove a filing, return it, and update cross-references."""
        elem = self._filings.pop()
        if elem.entity:
            elem.entity.filings.remove(elem)
        return elem

    def copy(self) -> FilingSet:
        """Return shallow copy of FilingSet."""
        return FilingSet(self)

    def isdisjoint(self, other: Iterable[Filing]) -> bool:
        """
        Return True if two filing sets have a null intersection.

        Parameters
        ----------
        other : iterable of Filing
            An iterable of ``Filing`` objects.

        Returns
        -------
        bool
            True if there are no common filings in the two sets.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters([other])
        return self._filings.isdisjoint(arg_lists[0])

    def issubset(self, other: Iterable[Filing]) -> bool:
        """
        Report whether another filing set contains this set.

        Parameters
        ----------
        other : iterable of Filing
            An iterable of ``Filing`` objects.

        Returns
        -------
        bool
            True if ``other`` contains all filings in this set.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters([other])
        return self._filings.issubset(arg_lists[0])

    def issuperset(self, other: Iterable[Filing]) -> bool:
        """
        Report whether this set contains another filing set.

        Parameters
        ----------
        other : iterable of Filing
            An iterable of ``Filing`` objects.

        Returns
        -------
        bool
            True if this set contains all filings in ``other``.

        Raises
        ------
        ValueError
            When any item in an iterable is not ``Filing``.
        """
        arg_lists = self._check_arg_iters([other])
        return self._filings.issuperset(arg_lists[0])

    def _check_arg_iters(self, args: Sequence[Any]) -> list[list[Any]]:
        arg_lists: list[list[Any]] = []
        for arg in args:
            if isinstance(arg, FilingSet):
                arg_lists.append(list(arg))
                continue

            # Raise TypeError if not iterable
            argiter = iter(arg)

            arg_list = list(argiter)

            # Raise ValueError if any item type other than Filing
            if any(not isinstance(item, Filing) for item in arg_list):
                msg = 'Arguments must be iterables of Filing objects.'
                raise ValueError(msg)
            arg_lists.append(arg_list)
        return arg_lists

    def _deepcopy_entity(self, source: Entity) -> Entity:
        """Deep copy Entity and shallow copy its `filings`."""
        orig_filings = source.filings
        source.filings = set()
        new = copy.deepcopy(source)
        source.filings = orig_filings
        new.filings = orig_filings.copy()
        return new

    def _deepcopy_filing_with_vmessages(self, source: Filing) -> Filing:
        """
        Deep copy Filing and its `validation_messages`.

        Retain `entity` reference without copying.
        """
        orig_entity = source.entity
        source.entity = None
        new = copy.deepcopy(source)
        source.entity = new.entity = orig_entity
        return new

    def _deepcopy_filingset_contents(self, fs: FilingSet):
        new_filings = [self._deepcopy_filing_with_vmessages(f) for f in fs]
        fs.clear()
        fs._filings.update(new_filings)

        ents = list(fs.entities) # Freeze lazy collection
        for ent in ents:
            new_ent = self._deepcopy_entity(ent) # type: ignore[arg-type]
            new_ent_filings: set[Filing] = set()
            for filing in new_ent.filings:
                match_id = filing.api_id
                new_filing = next(f for f in fs if f.api_id == match_id)
                new_ent_filings.add(new_filing)
                new_filing.entity = new_ent
            new_ent.filings = new_ent_filings


# Register FilingSet as virtual subclass of MutableSet enabling
# isinstance and issubclass checks
MutableSet.register(FilingSet)
