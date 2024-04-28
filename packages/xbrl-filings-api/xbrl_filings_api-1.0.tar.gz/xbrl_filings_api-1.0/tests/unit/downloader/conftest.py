"""Configure `pytest.downloader` subpackage."""

import hashlib
import urllib.parse
from pathlib import PurePosixPath
from typing import Union

import pytest
import responses

from xbrl_filings_api.downloader import DownloadSpecs


@pytest.fixture(scope='module')
def mock_response_data():
    """Arbitrary data for mock download, 1000 chars."""
    return '0123456789' * 100


@pytest.fixture(scope='module')
def mock_response_sha256(mock_response_data):
    """SHA-256 hash for fixture mock_response_data."""
    fhash = hashlib.sha256(
        string=mock_response_data.encode(encoding='utf-8'),
        usedforsecurity=False
        )
    return fhash.hexdigest()


@pytest.fixture(scope='module')
def mock_response_data_charcount(mock_response_data):
    """Character count for fixture mock_response_data."""
    return len(mock_response_data)


@pytest.fixture(scope='module')
def mock_url_response(mock_response_data):
    """Add a `responses` mock URL with fixt mock_response_data body."""
    def _mock_url_response(
            url: str, rsps: Union[responses.RequestsMock, None] = None):
        nonlocal mock_response_data
        if rsps is None:
            rsps = responses
        rsps.add(
            method=responses.GET,
            url=url,
            body=mock_response_data,
            headers={}
            )
    return _mock_url_response


@pytest.fixture
def plain_specs():
    """Return a plain `DownloadSpecs` object."""
    def _plain_specs(url, path, *, info=None):
        return DownloadSpecs(
            url=url,
            to_dir=path,
            stem_pattern=None,
            filename=None,
            sha256=None,
            info=info
            )
    return _plain_specs


@pytest.fixture
def hashfail_specs():
    """Return a failing `sha256` hash check `DownloadSpecs` object."""
    def _hashfail_specs(url, path, *, info=None):
        e_file_sha256 = '0' * 64
        return DownloadSpecs(
            url=url,
            to_dir=path,
            stem_pattern=None,
            filename=None,
            sha256=e_file_sha256,
            info=info
            )
    return _hashfail_specs


@pytest.fixture
def stem_renamed_specs():
    """Return a '_renamed' suffixed file stem `DownloadSpecs` object."""
    def _stem_renamed_specs(url, path, *, info=None):
        return DownloadSpecs(
            url=url,
            to_dir=path,
            stem_pattern='/name/_renamed',
            filename=None,
            sha256=None,
            info=info
            )
    return _stem_renamed_specs


@pytest.fixture
def filename_renamed_specs():
    """Return a ``renamed.abc`` filename `DownloadSpecs` object."""
    def _filename_renamed_specs(url, path, *, info=None):
        return DownloadSpecs(
            url=url,
            to_dir=path,
            stem_pattern=None,
            filename='renamed.abc',
            sha256=None,
            info=info
            )
    return _filename_renamed_specs


@pytest.fixture(scope='module')
def url_filename():
    """Get the filename from URL."""
    def _url_filename(url):
        url_path = urllib.parse.urlparse(url).path
        return PurePosixPath(url_path).name
    return _url_filename
