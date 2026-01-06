# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 13:54:17 2026

@author: jdsan
"""

import matplotlib.pyplot as plt

def plot_results(df):
    fig, ax1 = plt.subplots()

    ax1.plot(df["Time [s]"], df["Oven Temperature [°C]"], label="Oven Temperature [°C]")
    ax1.plot(df["Time [s]"], df["Heating Rod Temperature [°C]"], label="Heating Rod Temperature [°C]", linestyle="--")
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Temperature [°C]")
    ax1.legend()
    ax1.grid(True)

    fig, ax2 = plt.subplots()
    ax2.plot(df["Time [s]"], df["Power [W]"])
    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("Power [W]")
    ax2.grid(True)

    plt.show()
