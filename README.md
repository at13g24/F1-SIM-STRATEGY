# F1-SIM-STRATEGY
F1 race strategy simulation, simulating tyre wear and pit windows through different track, car, and tyre classes

## Core Architecture
* **Car Dynamics (`car.py`):** Handles fuel weight reduction (gaining pace as fuel burns off at a base rate of 2.0 kg per lap) and engine thermodynamics[cite: 1]. It uses Newton's Law of Cooling to simulate thermal plateaus, triggering progressive hybrid derating if the engine crosses 115°C[cite: 1].
* **Track Environment (`track.py`):** A configuration database for the F1 calendar[cite: 4]. It stores baseline lap times, abrasion metrics, corner stress loads, and a unique `dirty_air_coefficient` for each circuit[cite: 4].
* **Tyre Physics (`tyre.py`):** Scales tire degradation dynamically based on track length[cite: 5]. Internal tire temps spike based on corner loads and dirty air, causing the rubber to hit a non-linear performance cliff[cite: 5].
* **Data Integration (`outlap_data.py`):** Hooks into the `fastf1` API to pull real race data, isolating and plotting green-flag out-laps under 105 seconds from the 2025 Barcelona GP[cite: 2].

## The "Virtual Race Engineer"
The main loop (`simulation.py`) runs a 50-lap stint with dynamic traffic logic[cite: 3].
* When trapped within 2.0s of another car, the engine's target equilibrium temp spikes[cite: 1].
* If temps cross 108.0°C, the logic applies 5.0% Lift & Coast to manage it[cite: 3].
* At critical levels (> 113.0°C), it forces 15.0% Lift & Coast to actively drop temps and prevent the power unit from derating[cite: 3].

## Telemetry Output
The script outputs turn-by-turn telemetry, showing exactly when the tire/fuel crossover effect collapses under thermal stress[cite: 3].
