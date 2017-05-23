# -*- coding: utf-8 -*-

"""
Two-letter codes for each federal state of the Federal Republic of Germany

STATE_CODE_MAP is a dict mapping from the two-letter state code to the
full name of the state in German.

INVERSE_STATE_CODE_MAP is a dict mapping from the name (in either English
or German) to the two-letter state code.
"""

STATE_CODE_MAP = {
    'BW': 'Baden-Württemberg',
    'BY': 'Bayern',
    'BE': 'Berlin',
    'BB': 'Brandenburg',
    'HB': 'Bremen',
    'HH': 'Hamburg',
    'HE': 'Hessen',
    'MV': 'Mecklenburg-Vorpommern',
    'NI': 'Niedersachsen',
    'NW': 'Nordrhein-Westfalen',
    'RP': 'Rheinland-Pfalz',
    'SL': 'Saarland',
    'SN': 'Sachsen',
    'ST': 'Sachsen-Anhalt',
    'SH': 'Schleswig-Holstein',
    'TH': 'Thüringen',
}

_state_code_str = '\n'.join('{} => {}'.format(k, v)
                            for k, v in STATE_CODE_MAP.items())

INVERSE_STATE_CODE_MAP = {
    v: k for k, v in STATE_CODE_MAP.items()
}

# Add english names to the inverse state code map
INVERSE_STATE_CODE_MAP.update(
    {
        'Bavaria': 'BY',
        'Hesse': 'HE',
        'Lower Saxony': 'NI',
        'Mecklenburg-Western Pomerania': 'MV',
        'North Rhine-Westphalia': 'NW',
        'Northrhine-Westphalia': 'NW',
        'Rhineland-Palatinate': 'RP',
        'Saxony': 'SN',
        'Saxony-Anhalt': 'ST',
        'Thuringia': 'TH',
    }
)

# Add normalised / canonicalised names
for k, v in tuple(INVERSE_STATE_CODE_MAP.items()):
    INVERSE_STATE_CODE_MAP[k.replace('ü', 'u')] = v
    INVERSE_STATE_CODE_MAP[k.replace('ü', 'ue')] = v
for k, v in tuple(INVERSE_STATE_CODE_MAP.items()):
    INVERSE_STATE_CODE_MAP[k.replace('-', ' ')] = v
for k, v in tuple(INVERSE_STATE_CODE_MAP.items()):
    INVERSE_STATE_CODE_MAP[k.lower()] = v
    INVERSE_STATE_CODE_MAP[k.upper()] = v

# Allow lower-case state codes in STATE_CODE_MAP
for k, v in tuple(STATE_CODE_MAP.items()):
    STATE_CODE_MAP[k.lower()] = v
# Allow state codes as bytes
for k, v in tuple(STATE_CODE_MAP.items()):
    STATE_CODE_MAP[bytes(k, encoding='ASCII')] = v


class StateCodeError(KeyError):
    def __init__(self, message='', state_code=None):
        if state_code:
            state_mode_msg = (
                'State code {} is not valid. Must be one of:\n{}'
            ).format(state_code, _state_code_str)
            message += state_mode_msg
        super(StateCodeError, self).__init__(message)
