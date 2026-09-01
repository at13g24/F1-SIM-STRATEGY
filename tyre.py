
import math

# 1. DYNAMIC CONFIGURATION DATABASE
# Calibrated to an 80.0s baseline track. Temps compressed to 85-100C.
COMPOUND_SPECS = {
    "C1": {"base_deg": 0.04, "optimal_temp": 100.0,
           "pace_rating": 1.2,  "cliff_lap": 42},
    "C2": {"base_deg": 0.06, "optimal_temp": 97.0,
           "pace_rating": 0.6,  "cliff_lap": 32},
    "C3": {"base_deg": 0.08, "optimal_temp": 94.0,
           "pace_rating": 0.0,  "cliff_lap": 24},
    "C4": {"base_deg": 0.12, "optimal_temp": 91.0,
           "pace_rating": -0.6, "cliff_lap": 16},
    "C5": {"base_deg": 0.18, "optimal_temp": 88.0,
           "pace_rating": -1.2, "cliff_lap": 10},
    "C6": {"base_deg": 0.24, "optimal_temp": 85.0,
           "pace_rating": -1.8, "cliff_lap": 7}
}


class Tyre:
    def __init__(self, compound_name, is_new=True, prior_laps=0):
        if compound_name not in COMPOUND_SPECS:
            raise ValueError(f"Unknown compound: {compound_name}")

        specs = COMPOUND_SPECS[compound_name]
        self.compound = compound_name
        self.optimal_temp = specs["optimal_temp"]
        self.base_cliff_lap = specs["cliff_lap"]
        self.base_deg_rate = specs["base_deg"]
        self.base_pace_rating = specs["pace_rating"]

        self.current_temp = 70.0  # Blanket temp
        self.age_laps = prior_laps
        self.is_new = is_new
        self.surface_damage_multiplier = 1.0 if is_new else 1.05

    def calculate_performance_delta(self, track_object, current_track_temp,
                                    corner_stress_multiplier,
                                    in_dirty_air=False, driver_modifier=1.0,
                                    chassis_modifier=1.0):

        # --- NEW: DISTANCE SCALING ---
        # Calculate how long this track is compared to our 80s baseline
        track_scale_factor = track_object.baseline_lap_time / 80.0

        # Scale the cliff lap (longer track = fewer laps until the cliff)
        actual_cliff_lap = self.base_cliff_lap / track_scale_factor

        # Scale the base degradation severity
        actual_deg_rate = self.base_deg_rate * track_scale_factor

        # 1. DYNAMIC BASELINE & PACE SCALING
        baseline_compound = track_object.available_compounds[1]
        baseline_rating = COMPOUND_SPECS[baseline_compound]["pace_rating"]

        # Scale the pace delta so longer tracks yield bigger time gaps
        relative_pace_delta = (self.base_pace_rating
                               - baseline_rating) * track_scale_factor
        if not self.is_new:
            relative_pace_delta += 0.2

        # 2. THERMODYNAMIC MODEL
        generated_heat = current_track_temp + (corner_stress_multiplier * 50.0)
        if in_dirty_air:
            generated_heat *= track_object.dirty_air_coefficient

        self.current_temp = (self.current_temp * 0.5) + (generated_heat * 0.5)

        temp_delta = abs(self.optimal_temp - self.current_temp)
        thermal_multiplier = 1.0 + (temp_delta * 0.015)

        # 3. WEAR CALCULATION
        total_modifier = math.prod([
            track_object.base_abrasion,
            corner_stress_multiplier,
            thermal_multiplier,
            driver_modifier,
            chassis_modifier,
            self.surface_damage_multiplier
        ])

        linear_wear = (actual_deg_rate * self.age_laps) * total_modifier

        cliff_penalty = 0.0
        if self.age_laps > actual_cliff_lap:
            over_limit = self.age_laps - actual_cliff_lap
            cliff_penalty = (over_limit ** 2) * 0.05

        return relative_pace_delta + linear_wear + cliff_penalty

    def add_lap(self):
        self.age_laps += 1
