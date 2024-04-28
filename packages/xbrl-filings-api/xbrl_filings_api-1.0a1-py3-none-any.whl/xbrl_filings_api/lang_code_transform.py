"""
Define alpha-3 to alpha-2 language code transformations.

Defines :class:`dict` ``LANG_CODE_TRANSFORM`` for tranformation of
offial European Union languages from ISO 639-2 (alpha-3 codes) to ISO
639-1 (alpha-2 codes).

The transformations are needed for year 2020 ESEF reports when
requirements to report the language in the file name were obscure. They
affect the resolution of derived attribute `Filing.language`.

"""

# SPDX-FileCopyrightText: 2023 Lauri Salmela <lauri.m.salmela@gmail.com>
#
# SPDX-License-Identifier: MIT

__all__ = ['LANG_CODE_TRANSFORM']


LANG_CODE_TRANSFORM = {
    'bul': 'bg', # Bulgarian
    'ces': 'cs', # Czech
    'dan': 'da', # Danish
    'deu': 'de', # German
    'ell': 'el', # Greek
    'eng': 'en', # English
    'est': 'et', # Estonian
    'fin': 'fi', # Finnish
    'fra': 'fr', # French
    'gle': 'ga', # Irish
    'hrv': 'hr', # Croatian
    'hun': 'hu', # Hungarian
    'ita': 'it', # Italian
    'lav': 'lv', # Latvian
    'lit': 'lt', # Lithuanian
    'mlt': 'mt', # Maltese
    'nld': 'nl', # Dutch
    'pol': 'pl', # Polish
    'por': 'pt', # Portuguese
    'ron': 'ro', # Romanian
    'slk': 'sk', # Slovak
    'slv': 'sl', # Slovenian
    'spa': 'es', # Spanish
    'swe': 'sv', # Swedish
}
