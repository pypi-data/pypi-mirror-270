"""Define tests for add_api_params parameter of query functions."""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

import xbrl_filings_api as xf


def test_get_filings_override_limit(asml22en_response):
    """`limit` can be overridden with `add_api_params`."""
    asml22_fxo = '724500Y6DUVHQD6OXN27-2022-12-31-ESEF-NL-0'
    fs = xf.get_filings(
        filters={
            'filing_index': asml22_fxo
            },
        sort=None,
        limit=10,
        flags=xf.GET_ONLY_FILINGS,
        add_api_params={'page[size]': '1'}
        )
    assert len(fs) == 1, 'Parameter limit override as 1'
