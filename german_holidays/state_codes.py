#!/usr/bin/env python

"""
State codes
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

INVERSE_STATE_CODE_MAP = {
    v: k for k, v in STATE_CODE_MAP.items()
}

INVERSE_STATE_CODE_MAP.update(
    {
        'Baden-Württemberg': 'BW',
        'Bavaria': 'BY',
        'Berlin': 'BE',
        'Brandenburg': 'BB',
        'Bremen': 'HB',
        'Hamburg': 'HH',
        'Hesse': 'HE',
        'Lower Saxony': 'NI',
        'Mecklenburg-Western Pomerania': 'MV',
        'North Rhine-Westphalia': 'NW',
        'Northrhine-Westphalia': 'NW',
        'Rhineland-Palatinate': 'RP',
        'Saarland': 'SL',
        'Saxony': 'SN',
        'Saxony-Anhalt': 'ST',
        'Schleswig-Holstein': 'SH',
        'Thuringia': 'TH',
    }
)

for k, v in tuple(INVERSE_STATE_CODE_MAP.items()):
    keys = [
        k.lower(),
        k.upper(),
        k.replace('-', ' '),
        k.lower().replace('-', ' '),
        k.upper().replace('-', ' '),
    ]
    for k in keys:
        INVERSE_STATE_CODE_MAP[k] = v


class StateCodeError(KeyError):
    def __init__(self, message='', state_code=None):
        if state_code:
            code_str = '\n'.join('{} => {}'.format(k, v)
                                 for k, v in STATE_CODE_MAP.items())
            state_mode_msg = (
                'State code {} is not valid. Must be one of:\n{}'
            ).format(state_code, code_str)
            message += state_mode_msg
        super(StateCodeError, self).__init__(message)
