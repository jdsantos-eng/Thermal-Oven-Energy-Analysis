# -*- coding: utf-8 -*-
"""
@author: jdsan
"""

import numpy as np
from scipy.integrate import solve_ivp
from odes import thermal_odes

def run_simulation(params,r_max,t_span,y0,dt=1.0):
    t_eval = np.arange(t_span[0],t_span[1]+dt,dt)
    sol = solve_ivp(
        fun=lambda t, y:thermal_odes(t,y,params,r_max),
        t_span = t_span,
        y0=y0,
        t_eval=t_eval,
        method="RK45")
    
    return sol