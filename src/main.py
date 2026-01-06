# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 13:44:23 2026

@author: jdsan
"""
from simulation import run_simulation
from analysis import build_dataframe
from plots import plot_results
import pandas as pd


y0 = []
reader = pd.read_csv("../data/data.csv", skiprows=1)
params= dict(zip(reader["key"], reader["value"].astype(float)))

"""Guide, material settings"""
Cr = params["Heating rod thermal capacity"]  # Thermal capacity of the heating rod [J/K] = [J/°C]
Co = params["Oven thermal capacity"]         # Thermal capacity of the oven [J/K] = [J/°C]
Kro = params["Thermal conductance from rod to oven"]  # Thermal conductance coefficient [W/K
Koe = params["Thermal conductance from oven to ambient"]  # Thermal conductance coefficient [W/K]
Te = params["Ambient temperature"]           # Ambient temperature [°C]
Pt = params["Target power"]                  # Expected max power [W]
r_max = params["Maximum rate of change of power"]   #Maximum rate of change of power

"""Initial parameters"""
y0.append(params["Initial rod temperature"])     # Initial temperature of the heating rod
y0.append(params["Initial oven temperature"])    # Initial temperature of the oven
y0.append(params["Initial power input"])         # Initial power applied to the system

t_span = (0,2000) #Simulation time

sol = run_simulation(
    params=params,
    r_max=r_max,
    t_span=t_span,
    y0=y0)

df = build_dataframe(sol,scenario_id="Material_A")
print(df)

plot_results(df)
