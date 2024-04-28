"""Define `ValidationMessage` class."""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import logging
import re
import urllib.parse
from pathlib import PurePosixPath
from typing import TYPE_CHECKING, Optional, Union

from xbrl_filings_api.api_request import APIRequest
from xbrl_filings_api.api_resource import APIResource
from xbrl_filings_api.constants import Prototype
from xbrl_filings_api.scope_flag import ScopeFlag

if TYPE_CHECKING:
    from xbrl_filings_api.filing import Filing

__all__ = ['ValidationMessage']

logger = logging.getLogger(__name__)


class ValidationMessage(APIResource):
    """
    Message for a filing in the database from a validator software.

    Validation messages are issues in XBRL standard conformance, and the
    formula rules defined in the XBRL taxonomy.

    Country-specific filing rules defined by financial regulatory
    authorities and other agencies are not in the scope of validation.
    The rules defined in ESEF Reporting Manual are not checked if they
    are not codified in the taxonomy formula rules.

    Calculation inconsistency is the term used for issues in accounting
    coherence.

    Derived attributes beginning ``calc_`` are only available when
    `code` is ``'xbrl.5.2.5.2:calcInconsistency'``. The ones beginning
    ``duplicate_`` are available for `code`
    ``'message:tech_duplicated_facts1'`` if the values are numeric. They
    are parsed out from the `text` of the message.

    Notes
    -----
    The source of validation has not been published by the API provider.
    However, it seems likely that they originate from Arelle software as
    they seem similar and JSON and iXBRL viewer files are also generated
    with it.
    """

    TYPE = 'validation_message'
    SEVERITY = 'attributes.severity'
    TEXT = 'attributes.message'
    CODE = 'attributes.code'

    _FILING_FLAG = ScopeFlag.GET_VALIDATION_MESSAGES

    _LINE_ITEM_RE = re.compile(r'\bfrom (\S+)')
    _SHORT_ROLE_RE = re.compile(r'\blink role (\S+)')
    _REPORTED_SUM_RE = re.compile(r'\breported sum (\S+)')
    _COMPUTED_SUM_RE = re.compile(r'\bcomputed sum (\S+)')
    _CONTEXT_ID_RE = re.compile(r'\bcontext (\S+)')
    _UNREPORTED_ITEMS_RE = re.compile(r'\bunreportedContributingItems (.+)')
    _COMMA_RE = re.compile(r'\s*,\s*')
    _DUPLICATE_1_RE = re.compile(r'\bvalue:\s*(\S+)')
    _DUPLICATE_2_RE = re.compile(r'!=\s+(\S+)')

    def __init__(
            self,
            json_frag: Union[dict, Prototype],
            api_request: Optional[APIRequest] = None
            ) -> None:
        # Signatures::
        #     ValidationMessage(
        #         json_frag: dict,
        #         api_request: APIRequest
        #         )
        #     ValidationMessage(json_frag: Prototype)
        super().__init__(json_frag, api_request)

        self.code: Union[str, None] = self._json.get(self.CODE)
        """
        The code describing the source of the broken rule.

        For example, code ``'xbrl.5.2.5.2:calcInconsistency'`` refers to
        XBRL 2.1 base specification heading 5.2.5.2 with title "The
        <calculationArc> element".
        """

        self.severity: Union[str, None] = self._json.get(self.SEVERITY)
        """
        Severity of the validation message.

        Can be ``ERROR``, ``WARNING`` or ``INCONSISTENCY``.
        Might include ``ERROR-SEMANTIC`` and ``WARNING-SEMANTIC`` but
        most likely not.

        Arelle has also more message levels, but these are very
        certainly not included anywhere (``(DYNAMIC)``, ``CRITICAL``,
        ``DEBUG``, ``EXCEPTION``, ``INFO``, ``INFO-RESULT``).
        """

        self.text: Union[str, None] = self._json.get(self.TEXT)
        """Validation message text."""
        if isinstance(self.text, str):
            self.text = self.text.strip()

        self.calc_computed_sum: Union[float, None] = None
        """
        Derived computed sum of the calculation inconsistency.

        Based on attribute `text` for validation messages whose `code`
        is ``'xbrl.5.2.5.2:calcInconsistency'``.
        """

        self.calc_reported_sum: Union[float, None] = None
        """
        Derived reported sum of the calculation inconsistency.

        Based on attribute `text` for validation messages whose `code`
        is ``'xbrl.5.2.5.2:calcInconsistency'``.
        """

        self.calc_context_id: Union[str, None] = None
        """
        Derived XBRL context ID of the calculation inconsistency.

        Based on attribute `text` for validation messages whose `code`
        is ``'xbrl.5.2.5.2:calcInconsistency'``.
        """

        self.calc_line_item: Union[str, None] = None
        """
        Derived line item name of the calculation inconsistency.

        This field contains the qualified name of the line item (XBRL
        concept) with the taxonomy prefix and the local name parts. It
        could be for example ``ifrs-full:Assets``.

        Based on attribute `text` for validation messages whose `code`
        is ``'xbrl.5.2.5.2:calcInconsistency'``.
        """

        self.calc_short_role: Union[str, None] = None
        """
        Derived last part of the link role of the calculation
        inconsistency.

        For example a link role URI
        "http://www.example.com/esef/taxonomy/2022-12-31/FinancialPositionConsolidated"
        is truncated to "FinancialPositionConsolidated".

        Based on attribute `text` for validation messages whose `code`
        is ``'xbrl.5.2.5.2:calcInconsistency'``.
        """

        self.calc_unreported_items: Union[list[str], None] = None
        """
        Derived unreported contributing line items of the calculation
        inconsistency.

        This refers to the line item names of items which are defined as
        the addends for `calc_line_item` in any of the link roles in the
        XBRL taxonomies of this report and which were not reported in
        the same XBRL context with this fact.

        When the data is output to a database, this field is a string
        with parts joined by a newline character.

        Based on attribute `text` for validation messages whose `code`
        is ``'xbrl.5.2.5.2:calcInconsistency'``.
        """

        self.duplicate_greater: Union[float, None] = None
        """
        Derived greater item of the duplicate pair.

        Based on attribute `text` for validation messages whose `code`
        is ``'message:tech_duplicated_facts1'``.

        Does not include code ``'formula:assertionUnsatisfied'`` with
        ``tech_duplicated_facts1`` in the beginning of the message (more
        than 2 duplicated facts).
        """

        self.duplicate_lesser: Union[float, None] = None
        """
        Derived lesser item of the duplicate pair.

        Based on attribute `text` for validation messages whose `code`
        is ``'message:tech_duplicated_facts1'``.

        Does not include code ``'formula:assertionUnsatisfied'`` with
        ``tech_duplicated_facts1`` in the beginning of the message (more
        than 2 duplicated facts).
        """

        self.filing_api_id: Union[str, None] = None
        """`api_id` of `filing` object."""

        self.filing: Union[Filing, None] = None
        """Filing of this validation message."""

        self._json.close()

        if self.code == 'xbrl.5.2.5.2:calcInconsistency':
            self._derive_calc_prefixed_attrs()
        elif self.code == 'message:tech_duplicated_facts1':
            self._derive_duplicate_prefixed_attrs()

    def __repr__(self) -> str:
        """Return repr with `api_id`, `code` and `severity`."""
        return (
            f'{type(self).__name__}('
            f'api_id={self.api_id!r}, code={self.code!r}, '
            f'severity={self.severity!r})'
            )

    def __str__(self) -> str:
        r"""
        Return "[`severity`\ [:3] `code`] `text`".

        Attribute ``severity`` shows only the first three characters.
        Square brackets are used to encompass ``severity`` and ``code``.
        """
        text = '' if self.text is None else f' {self.text}'
        plist = []
        if self.severity:
            plist.append(self.severity[:3])
        if self.code:
            plist.append(self.code)
        prefix = ' '.join(plist)
        return f'[{prefix}]{text}'

    def _derive_calc(self, re_obj: re.Pattern) -> Union[str, None]:
        mt = re_obj.search(self.text)
        if mt:
            return mt[1]
        return None

    def _derive_calc_float(
            self, re_obj: re.Pattern, attr_name: str) -> Union[float, None]:
        calc_str = self._derive_calc(re_obj)
        calc_float = None
        if calc_str is not None:
            try:
                calc_float = float(calc_str.replace(',', ''))
            except ValueError:
                msg = (
                    f'String {calc_str!r} of attribute {attr_name!r} could '
                    'not be parsed into float.'
                    )
                logger.warning(msg, stacklevel=2)
        return calc_float

    def _derive_calc_prefixed_attrs(self):
        self.calc_computed_sum = self._derive_calc_float(
            self._COMPUTED_SUM_RE, 'calc_computed_sum')
        self.calc_reported_sum = self._derive_calc_float(
            self._REPORTED_SUM_RE, 'calc_reported_sum')
        self.calc_context_id = self._derive_calc(self._CONTEXT_ID_RE)
        self.calc_line_item = self._derive_calc(self._LINE_ITEM_RE)
        unreported_items = self._derive_calc(self._UNREPORTED_ITEMS_RE)
        self.calc_short_role = self._derive_calc_short_role()

        if unreported_items and unreported_items.lower() != 'none':
            self.calc_unreported_items = (
                self._COMMA_RE.split(unreported_items))

    def _derive_calc_short_role(self) -> Union[str, None]:
        matched_uri = self._derive_calc(self._SHORT_ROLE_RE)
        if not matched_uri:
            return None

        uri_path = ''
        try:
            parse_res = urllib.parse.urlparse(matched_uri)
        except ValueError:
            pass
        else:
            uri_path = parse_res.path
        if not uri_path.strip():
            return None
        uri_path = urllib.parse.unquote(uri_path)

        short_role = None
        try:
            plib_path = PurePosixPath(uri_path)
        except ValueError:
            pass
        else:
            short_role = plib_path.name
        return short_role

    def _derive_duplicate_prefixed_attrs(self):
        duplicate_1 = self._derive_calc_float(
            self._DUPLICATE_1_RE, 'duplicate_*')
        duplicate_2 = self._derive_calc_float(
            self._DUPLICATE_2_RE, 'duplicate_*')
        if (isinstance(duplicate_1, float)
                and isinstance(duplicate_2, float)):
            self.duplicate_greater = max(duplicate_1, duplicate_2)
            self.duplicate_lesser = min(duplicate_1, duplicate_2)
