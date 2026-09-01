
"""
Initializes a Track configuration profile.

:param name: e.g., 'Barcelona', 'Monaco', 'Spa'
:param baseline_lap_time: Theoretical clean-air lap time with low fuel
:param base_abrasion: Track surface roughness modifier (1.0 is baseline)
:param pit_entry_loss: Time lost on the IN-LAP driving into the pits
:param pit_exit_loss: Time lost on the OUT-LAP driving out of the pits
:param corner_stress: Dict defining relative stress multipliers for
                    {'FL', 'FR', 'RL', 'RR'}
"""


class Track:
    def __init__(self, name, baseline_lap_time, base_abrasion, pit_entry_loss,
                 pit_exit_loss, corner_stress, available_compounds,
                 dirty_air_coefficient):
        self.name = name
        self.baseline_lap_time = baseline_lap_time
        self.base_abrasion = base_abrasion
        self.pit_entry_loss = pit_entry_loss
        self.pit_exit_loss = pit_exit_loss
        self.corner_stress = corner_stress
        self.available_compounds = available_compounds
        self.dirty_air_coefficient = dirty_air_coefficient


# --- Complete F1 Calendar Track Configuration Database ---
TRACK_DATABASE = {
    "Bahrain": Track(
        name="Bahrain",
        baseline_lap_time=93.5,
        base_abrasion=1.30,
        pit_entry_loss=7.0,
        pit_exit_loss=12.5,
        corner_stress={"FL": 0.90, "FR": 0.95, "RL": 1.25, "RR": 1.30},
        available_compounds=["C1", "C2", "C3"],
        dirty_air_coefficient=1.00
    ),
    "Jeddah": Track(
        name="Jeddah",
        baseline_lap_time=91.5,
        base_abrasion=0.95,
        pit_entry_loss=6.0,
        pit_exit_loss=11.0,
        corner_stress={"FL": 1.15, "FR": 1.25, "RL": 1.00, "RR": 1.05},
        available_compounds=["C2", "C3", "C4"],
        dirty_air_coefficient=1.05
    ),
    "Melbourne": Track(
        name="Melbourne",
        baseline_lap_time=77.5,
        base_abrasion=1.05,
        pit_entry_loss=7.5,
        pit_exit_loss=11.5,
        corner_stress={"FL": 1.10, "FR": 1.15, "RL": 1.05, "RR": 1.10},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=1.10
    ),
    "Suzuka": Track(
        name="Suzuka",
        baseline_lap_time=91.0,
        base_abrasion=1.35,
        pit_entry_loss=5.5,
        pit_exit_loss=12.0,
        corner_stress={"FL": 1.35, "FR": 1.30, "RL": 1.20, "RR": 1.25},
        available_compounds=["C1", "C2", "C3"],
        dirty_air_coefficient=1.25
    ),
    "Shanghai": Track(
        name="Shanghai",
        baseline_lap_time=97.0,
        base_abrasion=1.10,
        pit_entry_loss=6.0,
        pit_exit_loss=13.0,
        corner_stress={"FL": 1.40, "FR": 0.90, "RL": 1.15, "RR": 0.95},
        available_compounds=["C2", "C3", "C4"],
        dirty_air_coefficient=1.00
    ),
    "Miami": Track(
        name="Miami",
        baseline_lap_time=89.5,
        base_abrasion=1.00,
        pit_entry_loss=6.5,
        pit_exit_loss=12.5,
        corner_stress={"FL": 1.05, "FR": 1.15, "RL": 1.10, "RR": 1.20},
        available_compounds=["C2", "C3", "C4"],
        dirty_air_coefficient=1.05
    ),
    "Imola": Track(
        name="Imola",
        baseline_lap_time=77.0,
        base_abrasion=1.15,
        pit_entry_loss=8.0,
        pit_exit_loss=14.0,
        corner_stress={"FL": 1.10, "FR": 1.25, "RL": 1.05, "RR": 1.15},
        available_compounds=["C4", "C5", "C6"],
        dirty_air_coefficient=1.15
    ),
    "Monaco": Track(
        name="Monaco",
        baseline_lap_time=74.5,
        base_abrasion=0.85,
        pit_entry_loss=11.0,
        pit_exit_loss=12.0,
        corner_stress={"FL": 1.00, "FR": 1.00, "RL": 1.00, "RR": 1.00},
        available_compounds=["C4", "C5", "C6"],
        dirty_air_coefficient=1.20
    ),
    "Montreal": Track(
        name="Montreal",
        baseline_lap_time=74.0,
        base_abrasion=0.95,
        pit_entry_loss=5.0,
        pit_exit_loss=10.5,
        corner_stress={"FL": 0.95, "FR": 1.00, "RL": 1.25, "RR": 1.30},
        available_compounds=["C2", "C3", "C4"],
        dirty_air_coefficient=0.85
    ),
    "Barcelona": Track(
        name="Barcelona",
        baseline_lap_time=78.0,
        base_abrasion=1.20,
        pit_entry_loss=6.5,
        pit_exit_loss=10.5,
        corner_stress={"FL": 1.35, "FR": 0.85, "RL": 1.10, "RR": 0.90},
        available_compounds=["C1", "C2", "C3"],
        dirty_air_coefficient=1.15
    ),
    "Spielberg": Track(
        name="Spielberg",
        baseline_lap_time=68.0,
        base_abrasion=1.05,
        pit_entry_loss=5.5,
        pit_exit_loss=11.0,
        corner_stress={"FL": 1.00, "FR": 1.20, "RL": 1.05, "RR": 1.25},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=0.90
    ),
    "Silverstone": Track(
        name="Silverstone",
        baseline_lap_time=89.0,
        base_abrasion=1.30,
        pit_entry_loss=4.5,
        pit_exit_loss=11.5,
        corner_stress={"FL": 1.40, "FR": 1.15, "RL": 1.25, "RR": 1.10},
        available_compounds=["C1", "C2", "C3"],
        dirty_air_coefficient=1.10
    ),
    "Budapest": Track(
        name="Budapest",
        baseline_lap_time=80.5,
        base_abrasion=1.10,
        pit_entry_loss=6.0,
        pit_exit_loss=12.0,
        corner_stress={"FL": 1.20, "FR": 1.15, "RL": 1.15, "RR": 1.10},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=1.20
    ),
    "Spa": Track(
        name="Spa",
        baseline_lap_time=105.0,
        base_abrasion=1.20,
        pit_entry_loss=6.5,
        pit_exit_loss=13.0,
        corner_stress={"FL": 1.25, "FR": 1.20, "RL": 1.15, "RR": 1.15},
        available_compounds=["C1", "C3", "C4"],
        dirty_air_coefficient=0.95
    ),
    "Zandvoort": Track(
        name="Zandvoort",
        baseline_lap_time=74.0,
        base_abrasion=1.25,
        pit_entry_loss=7.0,
        pit_exit_loss=11.0,
        corner_stress={"FL": 1.30, "FR": 1.10, "RL": 1.20, "RR": 1.05},
        available_compounds=["C2", "C3", "C4"],
        dirty_air_coefficient=1.20
    ),
    "Monza": Track(
        name="Monza",
        baseline_lap_time=81.0,
        base_abrasion=1.10,
        pit_entry_loss=7.5,
        pit_exit_loss=14.0,
        corner_stress={"FL": 1.10, "FR": 1.15, "RL": 1.15, "RR": 1.20},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=0.75
    ),
    "Baku": Track(
        name="Baku",
        baseline_lap_time=103.5,
        base_abrasion=0.90,
        pit_entry_loss=9.5,
        pit_exit_loss=12.0,
        corner_stress={"FL": 1.00, "FR": 1.20, "RL": 1.05, "RR": 1.25},
        available_compounds=["C4", "C5", "C6"],
        dirty_air_coefficient=0.80
    ),
    "Singapore": Track(
        name="Singapore",
        baseline_lap_time=95.0,
        base_abrasion=1.00,
        pit_entry_loss=7.0,
        pit_exit_loss=15.0,
        corner_stress={"FL": 1.15, "FR": 1.15, "RL": 1.30, "RR": 1.30},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=1.15
    ),
    "Austin": Track(
        name="Austin",
        baseline_lap_time=97.5,
        base_abrasion=1.20,
        pit_entry_loss=6.0,
        pit_exit_loss=12.5,
        corner_stress={"FL": 1.10, "FR": 1.30, "RL": 1.05, "RR": 1.25},
        available_compounds=["C1", "C3", "C4"],
        dirty_air_coefficient=1.05
    ),
    "Mexico": Track(
        name="Mexico",
        baseline_lap_time=80.0,
        base_abrasion=1.00,
        pit_entry_loss=6.5,
        pit_exit_loss=13.5,
        corner_stress={"FL": 1.15, "FR": 1.10, "RL": 1.20, "RR": 1.15},
        available_compounds=["C2", "C4", "C5"],
        dirty_air_coefficient=0.70
    ),
    "Interlagos": Track(
        name="Interlagos",
        baseline_lap_time=72.5,
        base_abrasion=1.15,
        pit_entry_loss=5.0,
        pit_exit_loss=13.5,
        corner_stress={"FL": 1.05, "FR": 1.30, "RL": 1.10, "RR": 1.25},
        available_compounds=["C2", "C3", "C4"],
        dirty_air_coefficient=0.95
    ),
    "Las_Vegas": Track(
        name="Las Vegas",
        baseline_lap_time=94.5,
        base_abrasion=0.85,
        pit_entry_loss=6.0,
        pit_exit_loss=12.0,
        corner_stress={"FL": 1.10, "FR": 1.15, "RL": 1.15, "RR": 1.20},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=0.75
    ),
    "Qatar": Track(
        name="Qatar",
        baseline_lap_time=84.5,
        base_abrasion=1.35,
        pit_entry_loss=6.5,
        pit_exit_loss=13.0,
        corner_stress={"FL": 1.35, "FR": 1.25, "RL": 1.20, "RR": 1.15},
        available_compounds=["C1", "C2", "C3"],
        dirty_air_coefficient=1.25
    ),
    "Abu_Dhabi": Track(
        name="Abu Dhabi",
        baseline_lap_time=88.5,
        base_abrasion=1.05,
        pit_entry_loss=8.5,
        pit_exit_loss=13.5,
        corner_stress={"FL": 1.10, "FR": 1.10, "RL": 1.20, "RR": 1.25},
        available_compounds=["C3", "C4", "C5"],
        dirty_air_coefficient=1.00
    ),
}
