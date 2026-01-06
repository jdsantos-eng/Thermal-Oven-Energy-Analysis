# Dynamic Energetic Analysis of a Furnace-Type Thermal System
Data-driven analysis of energy consumption and operational efficiency of a thermal oven using Python simulations.

# Project Description
This project develops and analyzes a dynamic thermal model of a furnace-type heating system using ordinary differential equations and numerical simulation in Python. The objective is to evaluate start-up behavior, steady-state strategies, and energy consumption under different power control scenarios.

# Elements
-Lumped thermal modeling with two thermal masses (heating element and furnace chamber)
-Dynamic simulation using ODEs (scipy.solve_ivp)
-Startup analysis and heating time estimation
-Control-oriented power ramp modeling
-Steady-state power optimization to minimize energy consumption
-Parametric analysis across power levels and thermal losses
-Data analysis and visualization (pandas, matplotlib)

# Mathematical Model
TODO: Add detailed derivation and assumptions

# Key Results 
TODO: Add simulation outputs and discussion

#How to Run
git clone https://github.com/<jdsantos-eng>/<Thermal-Oven-Energy-Analysis>.git
cd <Thermal-Oven-Energy-Analysis>

-Windows
python -m venv .venv
.venv\Scripts\activate
-macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

python src/main.py   # Runs the entire workflow

In data/data.csv you can change the inputs for testing
Note: currently, the project can only run a single material at a time

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
