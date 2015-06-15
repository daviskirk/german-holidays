#!/usr/bin/env python

"""
State codes
"""

STATE_CODE_MAP = {
    'BW':'Baden-Württemberg',
    'BY':'Bayern',
    'BE':'Berlin',
    'BB':'Brandenburg',
    'HB':'Bremen',
    'HH':'Hamburg',
    'HE':'Hessen',
    'MV':'Mecklenburg-Vorpommern',
    'NI':'Niedersachsen',
    'NW':'Nordrhein-Westfalen',
    'RP':'Rheinland-Pfalz',
    'SL':'Saarland',
    'SN':'Sachsen',
    'ST':'Sachsen-Anhalt',
    'SH':'Schleswig-Holstein',
    'TH':'Thüringen',
}

class StateCodeError(KeyError):
    def __init__(self, message='', state_code=None):
        if state_code:
            code_str = '\n'.join('{} => {}'.format(k,v)
                                 for k,v in STATE_CODE_MAP.items())
            state_mode_msg = (
                'State code {} is not valid. Must be one of:\n{}'
            ).format(state_code, code_str)
            message += state_mode_msg
        super(StateCodeError, self).__init__(message)
