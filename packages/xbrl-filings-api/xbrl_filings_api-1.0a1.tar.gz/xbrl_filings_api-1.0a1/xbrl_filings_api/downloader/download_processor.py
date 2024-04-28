"""Define sequential and parallel download functions."""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

import asyncio
import hashlib
import urllib.parse
from collections.abc import AsyncIterator
from pathlib import Path, PurePath
from typing import Optional, Union

import requests

from xbrl_filings_api.downloader import stats
from xbrl_filings_api.downloader.download_result import DownloadResult
from xbrl_filings_api.downloader.download_specs import DownloadSpecs
from xbrl_filings_api.downloader.exceptions import CorruptDownloadError

__all__ = [
    'download',
    'download_async',
    'download_parallel',
    'download_parallel_aiter',
    'validate_stem_pattern',
    ]


def download(
        url: str,
        to_dir: Union[str, PurePath],
        *,
        stem_pattern: Optional[str] = None,
        filename: Optional[str] = None,
        sha256: Optional[str] = None,
        timeout: float = 30.0
        ) -> str:
    """
    Download a file synchronously.

    See documentation of `download_async`.
    """
    return asyncio.run(download_async(
        url, to_dir,
        stem_pattern=stem_pattern, filename=filename, sha256=sha256,
        timeout=timeout
        ))


async def download_async(
        url: str,
        to_dir: Union[str, PurePath],
        *,
        stem_pattern: Optional[str] = None,
        filename: Optional[str] = None,
        sha256: Optional[str] = None,
        timeout: float = 30.0
        ) -> str:
    """
    Download a file asynchronously.

    The directories in parameter ``to_dir`` will be created if they do
    not exist. If no ``filename`` is given, name is derived from
    parameter ``url``. If file already exists, it will be overwritten.

    If the ``sha256`` does not match with the checksum of the downloaded
    file,
    :exc:`xbrl_filings_api.downloader.exceptions.CorruptDownloadError`
    will be raised and the name of the downloaded file will be appended
    with ``".corrupt"``.

    If download is interrupted, the file will be left with a suffix
    ``".unfinished"``.

    If no name could be derived from ``url``, the file will be named
    ``file0001``, ``file0002``, etc. In this case a new file is always
    created.

    Parameters
    ----------
    url : str
        URL to download.
    to_dir : path-like
        Directory to save the file.
    stem_pattern : str, optional
        Pattern to add to the filename stems. Placeholder ``"/name/"``
        is always required.
    filename : str, optional
        Name to be used for the saved file.
    sha256 : str, optional
        Expected SHA-256 checksum as a hex string. Case-insensitive. No
        checksum is calculated if this parameter is not given.
    timeout : float, default 30.0
        Maximum timeout for getting an initial response from the server
        in seconds.

    Returns
    -------
    str
        Local path where the downloaded file was saved.

    Raises
    ------
    xbrl_filings_api.downloader.exceptions.CorruptDownloadError
        Attribute `Filing.package_sha256` does not match the calculated
        hash of package file.
    requests.HTTPError
        HTTP status error occurs.
    requests.ConnectionError
        Connection fails.
    """
    validate_stem_pattern(stem_pattern)
    if not isinstance(to_dir, Path):
        to_dir = Path(to_dir)
    to_dir.mkdir(parents=True, exist_ok=True)

    if not filename:
        uqurl = urllib.parse.unquote(url)
        filename = urllib.parse.urlparse(uqurl).path.split('/')[-1]
        if filename.strip() == '':
            num = 1
            while (to_dir / f'file{num:04}').is_file():
                num += 1
            filename = f'file{num:04}'

    res = requests.get(url, stream=True, timeout=timeout)
    res.raise_for_status()

    hash_ = None
    if sha256:
        hash_ = hashlib.sha256()

    if stem_pattern:
        fnpath = Path(filename)
        filename = stem_pattern.replace('/name/', fnpath.stem) + fnpath.suffix

    save_path = Path.cwd() / to_dir / filename
    temp_path = save_path.with_suffix(f'{save_path.suffix}.unfinished')
    with open(temp_path, 'wb') as fd:
        for chunk in res.iter_content(chunk_size=None):
            fd.write(chunk)
            if sha256 and hash_:
                hash_.update(chunk)
            stats.byte_counter += len(chunk)
            await asyncio.sleep(0.0)
    stats.item_counter += 1

    if sha256 and hash_:
        if hash_.digest() != bytes.fromhex(sha256):
            corrupt_path = save_path.with_suffix(f'{save_path.suffix}.corrupt')
            corrupt_path.unlink(missing_ok=True)
            path = str(temp_path.rename(corrupt_path))

            calculated = hash_.hexdigest().lower()
            expected = sha256.lower()
            raise CorruptDownloadError(path, url, calculated, expected)

    save_path.unlink(missing_ok=True)
    temp_path.rename(save_path)
    return str(save_path)


def download_parallel(
        items: list[DownloadSpecs],
        *,
        max_concurrent: Union[int, None] = None,
        timeout: float = 30.0
        ) -> list[DownloadResult]:
    """
    Download multiple files in parallel.

    The order in parameter ``items`` is not guaranteed on the returned
    list.

    See documentation of `download_parallel_aiter`.

    Parameters
    ----------
    items : list of DownloadSpecs
    max_concurrent : int or None, default None
    timeout : float, default 30.0

    Returns
    -------
    list of DownloadResult
        Contains information on the finished download.
    """
    async def _download_parallel_async(
            items: list[DownloadSpecs],
            max_concurrent: Union[int, None],
            timeout: float
            ) -> list[DownloadResult]:
        results = []
        dliter = download_parallel_aiter(
            items,
            max_concurrent=max_concurrent,
            timeout=timeout
            )
        async for item in dliter:
            results.append(item)
        return results
    return asyncio.run(
        _download_parallel_async(items, max_concurrent, timeout))


async def download_parallel_aiter(
        items: list[DownloadSpecs],
        *,
        max_concurrent: Union[int, None] = None,
        timeout: float = 30.0
        ) -> AsyncIterator[DownloadResult]:
    """
    Download multiple files in parallel, return asynchronous iterator.

    The ordering in parameter ``items`` defines the order in which the
    requests will be started. As the downloads take arbitrary periods of
    time to finish, it does not guarantee the same order in the yielded
    results. For this purpose, an additional any-typed attribute
    ``info`` of both `DownloadSpecs` and `DownloadResult` is provided to
    keep track of individual downloads.

    Yielded `DownloadResult` objects will not have the
    :attr:`~DownloadResult.path` attribute value when the ``sha256``
    check fails even though the file is in fact saved with filename
    suffix ``".corrupt"``.

    Calls function `download_async` via parameter ``items``.

    Parameters
    ----------
    items : list of DownloadSpecs
        Instances of `DownloadSpecs` accept the same parameters as
        function `download_async` with an additional no-op attribute
        :attr:`~DownloadSpecs.info`.
    max_concurrent : int or None, default None
        Maximum number of simultaneous downloads allowed at any moment.
        If :pt:`None`, all downloads will be started immediately. If
        ``1``, downloading will be sequential.
    timeout : float, default 30.0
        Maximum timeout for getting the initial response for a single
        download from the server in seconds.

    Yields
    ------
    DownloadResult
        Contains information on the finished download.
    """
    itemlen = len(items)
    if max_concurrent is None:
        max_concurrent = itemlen
    else:
        max_concurrent = min(max_concurrent, itemlen)

    dlque: asyncio.Queue[Union[DownloadSpecs, None]] = asyncio.Queue()
    for item in items:
        dlque.put_nowait(item)
    # Termination markers for each worker
    for _ in range(max_concurrent):
        dlque.put_nowait(None)

    resultque: asyncio.Queue[DownloadResult] = asyncio.Queue()

    tasks: set[asyncio.Task] = set()
    for worker_num in range(1, max_concurrent + 1):
        task = asyncio.create_task(
            _download_parallel_worker(dlque, resultque, timeout),
            name=f'worker-{worker_num}'
            )
        tasks.add(task)

    for _ in range(itemlen):
        result = await resultque.get()
        yield result


async def _download_parallel_worker(
        dlque: asyncio.Queue[Union[DownloadSpecs, None]],
        resultque: asyncio.Queue[DownloadResult],
        timeout: float
        ) -> None:
    """Coroutine worker for `download_parallel_aiter`."""
    while True:
        item: Union[DownloadSpecs, None] = await dlque.get()
        if item is None:
            break
        result = None
        try:
            path = await download_async(
                item.url,
                item.to_dir,
                stem_pattern=item.stem_pattern,
                filename=item.filename,
                sha256=item.sha256,
                timeout=timeout
                )
        except Exception as err:
            result = DownloadResult(
                url=item.url, err=err, info=item.info)
        else:
            result = DownloadResult(
                url=item.url, path=path, info=item.info)
        resultque.put_nowait(result)
        dlque.task_done()


def validate_stem_pattern(stem_pattern: Union[str, None]):
    """
    Validate parameter ``stem_pattern`` of module functions.

    Parameters
    ----------
    stem_pattern : str or None
        Stem pattern parameter.

    Raises
    ------
    ValueError
        When stem pattern is invalid.
    """
    if stem_pattern and '/name/' not in stem_pattern:
        msg = (
            'Placeholder "/name/" missing in \'stem_pattern\' value '
            + repr(stem_pattern)
            )
        raise ValueError(msg)
