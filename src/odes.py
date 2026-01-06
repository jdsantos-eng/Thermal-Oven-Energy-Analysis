# -*- coding: utf-8 -*-
"""
@author: jdsantos-eng
"""
from power_ramp import power_ramp
def thermal_odes(t,y,params,r_max):
    #y[0] -> Initial heating rod temperature
    #y[1] -> Initial Oven temperature
    #y[2] -> Initial Applied Power
    Tr,To,Pc = y
    Cr = params["Heating rod thermal capacity"]  # Thermal capacity of the heating rod [J/K] = [J/°C]
    Co = params["Oven thermal capacity"]         # Thermal capacity of the oven [J/K] = [J/°C]
    Kro = params["Thermal conductance from rod to oven"]  # Thermal conductance coefficient [W/K
    Koe = params["Thermal conductance from oven to ambient"]  # Thermal conductance coefficient [W/K]
    Te = params["Ambient temperature"]           # Ambient temperature [°C]
    Pt = params["Target power"]                  # Expected max power [W]
    r_max = params["Maximum rate of change of power"]   #Maximum rate of change of power
    
    #Power dynamics simulation
    dP_dt = power_ramp(t,Pc,Pt,r_max)
    
    #Thermal dynamics equations
    dTr_dt = (Pc-Kro*(Tr-To)/Cr)
    dTo_dt = (Kro*(Tr-To)-Koe*(To-Te))/Co
    return [dTr_dt,dTo_dt,dP_dt]