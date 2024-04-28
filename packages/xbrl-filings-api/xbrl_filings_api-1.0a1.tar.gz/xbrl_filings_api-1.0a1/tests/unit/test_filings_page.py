"""Define tests for `FilingsPage`."""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

import re

import pytest
import responses

import xbrl_filings_api as xf


@pytest.fixture
def oldest3_fi_ent_vmessages_filingspage(oldest3_fi_ent_vmessages_response):
    """
    FilingPage for ``oldest3_fi_ent_vmessages`` with entities and
    validation messages.
    """
    piter = xf.filing_page_iter(
        filters={'country': 'FI'},
        sort='date_added',
        limit=3,
        flags=(xf.GET_ENTITY | xf.GET_VALIDATION_MESSAGES),
        add_api_params=None
        )
    return next(piter)


def test_attributes(oldest3_fi_ent_vmessages_filingspage):
    """Test attributes of `FilingsPage`."""
    fpage: xf.FilingsPage = oldest3_fi_ent_vmessages_filingspage
    assert fpage.query_filing_count > 10
    assert len(fpage.filing_list) == 3
    for filing in fpage.filing_list:
        assert isinstance(filing, xf.Filing)
    assert len(fpage.entity_list) == 3
    for ent in fpage.entity_list:
        assert isinstance(ent, xf.Entity)
    assert len(fpage.validation_message_list) > 3
    for vmsg in fpage.validation_message_list:
        assert isinstance(vmsg, xf.ValidationMessage)


def test_repr(oldest3_fi_ent_vmessages_filingspage):
    """Test `__repr__` of `FilingsPage`."""
    e_repr1 = (
        "FilingsPage(request_url='")
    e_repr2 = (
        "', query_time=datetime("
        )
    e_repr3 = (
        '), len(filing_list)=3, len(entity_list)=3, '
        'len(validation_message_list)=45)'
        )
    fpage: xf.FilingsPage = oldest3_fi_ent_vmessages_filingspage
    fpage_repr = repr(fpage)
    assert fpage_repr.startswith(e_repr1)
    assert e_repr2 in fpage_repr
    assert fpage_repr.endswith(e_repr3)


def test_included_resource_api_id_as_int():
    """
    Test included resource api_id from API as int resolved to final
    objects.
    """
    rsps_with_int_included_id = {
        'data': [{
            'type': 'filing',
            'attributes': {
                'fxo_id': '724500Y6DUVHQD6OXN27-2022-12-31-ESEF-NL-0',
                'package_url': (
                    '/724500Y6DUVHQD6OXN27/2022-12-31/ESEF/NL/0'
                    '/asml-2022-12-31-en.zip'
                    )
                },
            'relationships': {
                'entity': {
                    'links': {'related': '/api/entities/724500Y6DUVHQD6OXN27'},
                    'data': {'type': 'entity', 'id': 123456789}
                    },
                'validation_messages': {
                    'links': {
                        'related': '/api/filings/123/validation_messages'},
                    'data': [
                        {'type': 'validation_message', 'id': 987654}
                        ]
                    },
                },
            'id': '123',
            'links': {'self': '/api/filings/123'}
            }],
        'included': [
            {
                'type': 'entity',
                'id': 123456789,
                'attributes': {},
                'relationships': {},
                'links': {'self': '/api/entities/123456789'}
            },
            {
                'type': 'validation_message',
                'attributes': {
                    'code': 'xbrl.5.2.5.2:calcInconsistency',
                    'message': 'Calculation inconsistent',
                    'severity': 'INCONSISTENCY'
                    },
                'id': 987654
            },
            ],
        'links': {
            'self': 'https://filings.xbrl.org/api/filings'
            },
        'meta': {'count': 0},
        'jsonapi': {'version': '1.0'}
        }
    fs: xf.FilingSet
    with responses.RequestsMock() as rsps:
        rsps.get(
            url=re.compile(r'.+'),
            json=rsps_with_int_included_id,
        )
        fs = xf.get_filings(flags=xf.GET_ENTITY | xf.GET_VALIDATION_MESSAGES)
    assert len(fs) == 1
    filing = next(iter(fs))
    assert len(filing.validation_messages) == 1
    vmsg = next(iter(filing.validation_messages))
    assert isinstance(vmsg, xf.ValidationMessage)
    assert vmsg.api_id == '987654'
    ent = filing.entity
    assert isinstance(ent, xf.Entity)
    assert ent.api_id == '123456789'


def test_rogue_validation_messages_logging(caplog):
    """Test logging when ValidationMessage has no attribute filing."""
    e_log = (
        "No filing defined for ValidationMessage("
        "api_id='987654', code='xbrl.5.2.5.2:calcInconsistency', "
        "severity='INCONSISTENCY')"
        )
    rsps_with_rogue_vmsg = {
        'data': [{
            'type': 'filing',
            'attributes': {
                'fxo_id': '724500Y6DUVHQD6OXN27-2022-12-31-ESEF-NL-0',
                'package_url': (
                    '/724500Y6DUVHQD6OXN27/2022-12-31/ESEF/NL/0'
                    '/asml-2022-12-31-en.zip'
                    )
                },
            'id': '123',
            'links': {'self': '/api/filings/123'}
            }],
        'included': [{
            'type': 'validation_message',
            'attributes': {
                'code': 'xbrl.5.2.5.2:calcInconsistency',
                'message': 'Calculation inconsistent',
                'severity': 'INCONSISTENCY'
                },
            'id': '987654'
            }],
        'links': {
            'self': 'https://filings.xbrl.org/api/filings'
            },
        'meta': {'count': 0},
        'jsonapi': {'version': '1.0'}
        }
    with responses.RequestsMock() as rsps:
        rsps.get(
            url=re.compile(r'.+'),
            json=rsps_with_rogue_vmsg,
        )
        _ = xf.get_filings(flags=xf.GET_VALIDATION_MESSAGES)
    assert e_log in caplog.text


def test_same_filing_on_another_page_logging(caplog):
    """
    Test logging when Filing with the same `api_id` is returned again.
    """
    e_log = "Same filing returned again, api_id='2'"
    rsps_1st_page = {
        'data': [
            {
                'type': 'filing',
                'attributes': {
                    'country': 'SE',
                    'period_end': '2021-12-31',
                    'fxo_id': '549300CSLHPO6Y1AZN37-2021-12-31-ESEF-SE-1'
                },
                'id': '2'
            },
            {
                'type': 'filing',
                'attributes': {
                    'country': 'SE',
                    'period_end': '2021-12-31',
                    'fxo_id': '549300CSLHPO6Y1AZN37-2021-12-31-ESEF-SE-0'
                },
                'id': '1'
            }
        ],
        'links': {
            'next': (
                'https://filings.xbrl.org/api/filings?page%5Bsize%5D=2&'
                'filter%5Bcountry%5D=SE&sort=date_added&page%5Bnumber%5D=2'
                )
        },
        'meta': {'count': 3},
        'jsonapi': {'version': '1.0'}
        }
    rsps_2nd_page = {
        'data': [
        {
            'type': 'filing',
            'attributes': {
                'country': 'SE',
                'period_end': '2021-12-31',
                'fxo_id': '549300CSLHPO6Y1AZN37-2021-12-31-ESEF-SE-1'
            },
            'id': '2'
        },
        {
            'type': 'filing',
            'attributes': {
                'country': 'SE',
                'period_end': '2021-12-31',
                'fxo_id': '5493001NNP6HM67OVU09-2021-12-31-ESEF-SE-0'
            },
            'id': '2240'
            }
        ],
        'links': {
            'next': None
        },
        'meta': {'count': 3},
        'jsonapi': {'version': '1.0'}
        }

    with responses.RequestsMock() as rsps:
        any_url_re = re.compile(r'.+')
        rsps.get(url=any_url_re, json=rsps_1st_page)
        rsps.get(url=any_url_re, json=rsps_2nd_page)
        _ = xf.get_filings(flags=xf.GET_VALIDATION_MESSAGES)
    assert e_log in caplog.text
