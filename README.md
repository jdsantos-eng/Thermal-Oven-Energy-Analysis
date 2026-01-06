# Dynamic Energetic Analysis of a Furnace-Type Thermal System
Data-driven analysis of energy consumption and operational efficiency of a thermal oven using Python simulations.

# Project Description
This project develops and analyzes a dynamic thermal model of a furnace-type heating system using ordinary differential equations and numerical simulation in Python. The objective is to evaluate start-up behavior, steady-state strategies, and energy consumption under different power control scenarios.

# Elements
- Lumped thermal modeling with two thermal masses (heating element and furnace chamber)
- Dynamic simulation using ODEs (scipy.solve_ivp)
- Startup analysis and heating time estimation
- Control-oriented power ramp modeling
- Steady-state power optimization to minimize energy consumption
- Parametric analysis across power levels and thermal losses
- Data analysis and visualization (pandas, matplotlib)

# Mathematical Model
TODO: Add detailed derivation and assumptions

# Key Results 
TODO: Add simulation outputs and discussion

# How to Run
## 1. Clone the repository
```bash
git clone https://github.com/jdsantos-eng/Thermal-Oven-Energy-Analysis.git
cd Thermal-Oven-Energy-Analysis
```

## 2. Create and activate a virtual environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Run the full simulation workflow
```bash
python src/main.py
```

This command runs:
- The ODE-based thermal model  
- The numerical integration  
- The power-ramp logic  
- The energy/performance analysis  
- The plotting utilities  

## 5. Modify inputs (optional)
You can adjust test parameters in:

```
data/data.csv
```

**Note:** At the moment, the project supports running simulations for **one material at a time**.

## Project Structure
```
project/
│
├── src/                # Source code (models, simulation, utilities)
│   ├── odes.py         # ODE system definition (thermal dynamics)
│   ├── simulation.py   # Numerical integration logic
│   ├── power_ramp.py   # Power ramp model (smooth transitions)
│   ├── analysis.py     # Energy and performance calculations
│   ├── plots.py        # Visualization utilities
│   └── main.py         # Entry point to run predefined scenarios
│
├── data/               # Input
│   └── data.csv        # Physical assumptions and material properties
│
├── notebooks/          # Exploratory analysis and explanation (TODO)
│   └── Model_Exploration.ipynb
│
├── README.md           # Project documentation
└── requirements.txt    # Project libreries
```
