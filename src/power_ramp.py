# -*- coding: utf-8 -*-
"""
@author: jdsantos-eng
"""

"""POWER.PY"""

import numpy as np

def power_ramp(t:float,Pc: float,Pt: float,r_max:float)->float:
    #Pc: Current Power [W]
    #Pt: Target Power [W]
    #r_mx: Max change rate of power [W/s]
    if not abs(Pt-Pc) < 1e-6:
        value = np.clip(Pt-Pc,-r_max,r_max)
    return value