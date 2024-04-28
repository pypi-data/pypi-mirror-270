"""Print the name of the package and its version."""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

import sys

from xbrl_filings_api.__about__ import __version__

module_name = vars(sys.modules[__name__])['__package__']

print(f'\n{module_name} version {__version__}')
