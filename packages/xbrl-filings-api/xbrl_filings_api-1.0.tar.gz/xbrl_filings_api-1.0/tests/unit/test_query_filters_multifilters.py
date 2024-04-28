"""Define tests for multifilters of query functions."""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

# Allow unnecessary double quotes as file includes SQL statements.
# ruff: noqa: Q000

import sqlite3
from datetime import datetime, timezone

import pytest

import xbrl_filings_api as xf

UTC = timezone.utc

pytestmark = pytest.mark.multifilter


def test_get_filings_api_id(multifilter_api_id_response):
    """Requested `api_id` filings are returned."""
    shell_api_ids = '1134', '1135', '4496', '4529'
    fs = xf.get_filings(
        filters={
            'api_id': shell_api_ids
            },
        sort=None,
        limit=4,
        flags=xf.GET_ONLY_FILINGS
        )
    received_api_ids = {filing.api_id for filing in fs}
    assert received_api_ids == set(shell_api_ids)


@pytest.mark.sqlite
def test_to_sqlite_api_id(
        multifilter_api_id_response, db_record_count, tmp_path, monkeypatch):
    """Filtering by `api_id` inserted to db."""
    monkeypatch.setattr(xf.options, 'views', None)
    shell_api_ids = '1134', '1135', '4496', '4529'
    db_path = tmp_path / 'test_to_sqlite_api_id.db'
    xf.to_sqlite(
        path=db_path,
        update=False,
        filters={
            'api_id': shell_api_ids
            },
        sort=None,
        limit=4,
        flags=xf.GET_ONLY_FILINGS
        )
    assert db_path.is_file()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        "SELECT api_id FROM Filing "
        "WHERE api_id IN (?, ?, ?, ?)",
        shell_api_ids
        )
    saved_ids = {row[0] for row in cur.fetchall()}
    assert saved_ids == set(shell_api_ids)
    assert db_record_count(cur) == 4
    con.close()


def test_get_filings_country_only_first(multifilter_country_response):
    """Requested `country` filings are returned."""
    country_codes = ['FI', 'SE', 'NO']
    fs = xf.get_filings(
        filters={
            'country': country_codes
            },
        sort=None,
        limit=3,
        flags=xf.GET_ONLY_FILINGS
        )
    assert len(fs) == 3, 'Requested number of filings returned'
    received_countries = {filing.country for filing in fs}
    assert 'FI' in received_countries, 'Only FI available, match count'
    assert 'SE' not in received_countries, 'Too many FI filings'
    assert 'NO' not in received_countries, 'Too many FI filings'


@pytest.mark.sqlite
def test_to_sqlite_country_only_first(
        multifilter_country_response, db_record_count, tmp_path, monkeypatch):
    """Filtering by `country` filings inserted to db."""
    monkeypatch.setattr(xf.options, 'views', None)
    country_codes = ['FI', 'SE', 'NO']
    db_path = tmp_path / 'test_to_sqlite_country_only_first.db'
    xf.to_sqlite(
        path=db_path,
        update=False,
        filters={
            'country': country_codes
            },
        sort=None,
        limit=3,
        flags=xf.GET_ONLY_FILINGS
        )
    assert db_path.is_file()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        "SELECT country FROM Filing "
        "WHERE country IN (?, ?, ?)",
        country_codes
        )
    saved_countries = {row[0] for row in cur.fetchall()}
    assert saved_countries == {'FI'}
    assert db_record_count(cur) == 3
    con.close()


def test_get_filings_filing_index(
        multifilter_filing_index_response):
    """Requested `filing_index` filings are returned."""
    filing_index_codes = (
        '21380068P1DRHMJ8KU70-2021-12-31-ESEF-GB-0',
        '21380068P1DRHMJ8KU70-2021-12-31-ESEF-NL-0'
        )
    fs = xf.get_filings(
        filters={
            'filing_index': filing_index_codes
            },
        sort=None,
        limit=2,
        flags=xf.GET_ONLY_FILINGS
        )
    received_countries = {filing.filing_index for filing in fs}
    assert received_countries == set(filing_index_codes)


@pytest.mark.sqlite
def test_to_sqlite_filing_index(
        multifilter_filing_index_response, db_record_count, tmp_path,
        monkeypatch):
    """Filtering by `filing_index` filings inserted to db."""
    monkeypatch.setattr(xf.options, 'views', None)
    filing_index_codes = (
        '21380068P1DRHMJ8KU70-2021-12-31-ESEF-GB-0',
        '21380068P1DRHMJ8KU70-2021-12-31-ESEF-NL-0'
        )
    db_path = tmp_path / 'test_to_sqlite_filing_index.db'
    xf.to_sqlite(
        path=db_path,
        update=False,
        filters={
            'filing_index': filing_index_codes
            },
        sort=None,
        limit=2,
        flags=xf.GET_ONLY_FILINGS
        )
    assert db_path.is_file()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        "SELECT filing_index FROM Filing "
        "WHERE filing_index IN (?, ?)",
        filing_index_codes
        )
    saved_fxo = {row[0] for row in cur.fetchall()}
    assert saved_fxo == set(filing_index_codes)
    assert db_record_count(cur) == 2
    con.close()


def test_get_filings_reporting_date(multifilter_reporting_date_response):
    """Test raising APIError for `reporting_date` filtering."""
    dates = '2020-12-31', '2021-12-31', '2022-12-31'
    with pytest.raises(xf.APIError, match=r'FilingSchema has no attribute'):
        with pytest.warns(xf.FilterNotSupportedWarning):
            _ = xf.get_filings(
                filters={
                    'reporting_date': dates
                    },
                sort=None,
                limit=3,
                flags=xf.GET_ONLY_FILINGS
                )


@pytest.mark.sqlite
def test_to_sqlite_reporting_date(
        multifilter_reporting_date_response, tmp_path, monkeypatch):
    """
    Test raising APIError for `reporting_date` filtering, to_sqlite.
    """
    monkeypatch.setattr(xf.options, 'views', None)
    dates = '2020-12-31', '2021-12-31', '2022-12-31'
    db_path = tmp_path / 'test_to_sqlite_reporting_date.db'
    with pytest.raises(xf.APIError, match=r'FilingSchema has no attribute'):
        with pytest.warns(xf.FilterNotSupportedWarning):
            xf.to_sqlite(
                path=db_path,
                update=False,
                filters={
                    'reporting_date': dates
                    },
                sort=None,
                limit=3,
                flags=xf.GET_ONLY_FILINGS
                )
    assert not db_path.is_file()


@pytest.mark.datetime
def test_get_filings_processed_time_str(
        multifilter_processed_time_response):
    """Test string filtered `processed_time` returns 2 filings."""
    cloetta_sv_strs = (
        '2023-01-18 11:02:06.724768',
        '2023-05-16 21:07:17.825836'
        )
    cloetta_sv_objs = (
        datetime(2023, 1, 18, 11, 2, 6, 724768, tzinfo=UTC),
        datetime(2023, 5, 16, 21, 7, 17, 825836, tzinfo=UTC)
        )
    fs = xf.get_filings(
        filters={
            'processed_time': cloetta_sv_strs
            },
        sort=None,
        limit=2,
        flags=xf.GET_ONLY_FILINGS
        )
    received_dts = {filing.processed_time for filing in fs}
    assert cloetta_sv_objs[0] in received_dts
    assert cloetta_sv_objs[1] in received_dts
    assert len(received_dts) == 2
    received_strs = {filing.processed_time_str for filing in fs}
    assert cloetta_sv_strs[0] in received_strs
    assert cloetta_sv_strs[1] in received_strs


@pytest.mark.sqlite
@pytest.mark.datetime
def test_to_sqlite_processed_time_str(
        multifilter_processed_time_response, db_record_count, tmp_path,
        monkeypatch):
    """Test string filtered `processed_time` filings inserted to db."""
    monkeypatch.setattr(xf.options, 'views', None)
    cloetta_sv_strs = (
        '2023-01-18 11:02:06.724768',
        '2023-05-16 21:07:17.825836'
        )
    db_path = tmp_path / 'test_to_sqlite_processed_time_str.db'
    xf.to_sqlite(
        path=db_path,
        update=False,
        filters={
            'processed_time': cloetta_sv_strs
            },
        sort=None,
        limit=2,
        flags=xf.GET_ONLY_FILINGS
        )
    assert db_path.is_file()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        "SELECT processed_time FROM Filing "
        "WHERE processed_time IN (?, ?)",
        cloetta_sv_strs
        )
    saved_proc_times = {row[0] for row in cur.fetchall()}
    assert saved_proc_times == set(cloetta_sv_strs)
    assert db_record_count(cur) == 2
    con.close()


@pytest.mark.datetime
def test_get_filings_processed_time_datetime_utc(
        multifilter_processed_time_response):
    """
    Test datetime (UTC) filtered `processed_time` returns 2 filings.
    """
    cloetta_sv_objs = (
        datetime(2023, 1, 18, 11, 2, 6, 724768, tzinfo=UTC),
        datetime(2023, 5, 16, 21, 7, 17, 825836, tzinfo=UTC)
        )
    cloetta_sv_strs = (
        '2023-01-18 11:02:06.724768',
        '2023-05-16 21:07:17.825836'
        )
    fs = xf.get_filings(
        filters={
            'processed_time': cloetta_sv_objs
            },
        sort=None,
        limit=2,
        flags=xf.GET_ONLY_FILINGS
        )
    received_dts = {filing.processed_time for filing in fs}
    assert len(received_dts) == 2
    for utc_dt in cloetta_sv_objs:
        assert utc_dt in received_dts
    received_strs = {filing.processed_time_str for filing in fs}
    assert len(received_strs) == 2
    for str_dt in cloetta_sv_strs:
        assert str_dt in received_strs


@pytest.mark.datetime
def test_get_filings_processed_time_datetime_naive(
        multifilter_processed_time_response):
    """
    Test datetime (naive) filtered `processed_time` returns 2 filings.
    """
    cloetta_sv_objs = (
        datetime(2023, 1, 18, 11, 2, 6, 724768, tzinfo=None),
        datetime(2023, 5, 16, 21, 7, 17, 825836, tzinfo=None)
        )
    cloetta_sv_strs = (
        '2023-01-18 11:02:06.724768',
        '2023-05-16 21:07:17.825836'
        )
    fs = xf.get_filings(
        filters={
            'processed_time': cloetta_sv_objs
            },
        sort=None,
        limit=2,
        flags=xf.GET_ONLY_FILINGS
        )
    received_dts = {filing.processed_time for filing in fs}
    assert len(received_dts) == 2
    for naive_dt in cloetta_sv_objs:
        assert naive_dt.replace(tzinfo=UTC) in received_dts
    received_strs = {filing.processed_time_str for filing in fs}
    for str_dt in cloetta_sv_strs:
        assert str_dt in received_strs


def test_raises_get_filings_none_filter():
    """Test raising for filter value None in multifilter."""
    api_ids = '1134', '1135', None, '4529'
    with pytest.raises(
            ValueError,
            match=(r'Value None is not allowed for filters, field "api_id", '
                   r'multifilter index 2')):
        _ = xf.get_filings(
            filters={
                'api_id': api_ids
                },
            sort=None,
            limit=4,
            flags=xf.GET_ONLY_FILINGS
            )
