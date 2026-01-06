# -*- coding: utf-8 -*-
"""
@author: jdsan
"""

import pandas as pd
import numpy as np

def build_dataframe(sol,scenario_id):
    df = pd.DataFrame({
        "Time [s]": sol.t,
        "Heating Rod Temperature [°C]": sol.y[0],
        "Oven Temperature [°C]":sol.y[1],
        "Power [W]": sol.y[2]})
    
    return df