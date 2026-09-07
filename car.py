
class Car:
    def __init__(self, chassis_name, starting_fuel_kg=110.0,
                 base_fuel_burn_rate=2.0, fuel_effect_coeff=0.035,
                 chassis_tyre_modifier=1.0):
        self.chassis_name = chassis_name

        # 1. Fuel
        self.starting_fuel_kg = starting_fuel_kg
        self.current_fuel_kg = starting_fuel_kg
        self.base_fuel_burn_rate = base_fuel_burn_rate
        self.fuel_effect_coeff = fuel_effect_coeff

        # 2. Power Unit temp
        self.engine_temp = 100.0  # Clean air temp
        self.engine_redline = 125.0

        # 3. Chassis Modifier
        self.chassis_tyre_modifier = chassis_tyre_modifier

    def process_lap(self, track_object, gap_to_car_ahead=5.0,
                    lift_and_coast_pct=0.0):
        """
        Processes one lap of physics, focusing on fuel weight, lift & coast,
        and exponential thermal plateaus.
        """

        # A. Lift and Coast
        actual_fuel_burn = self.base_fuel_burn_rate * (1.0 -
                                                       (lift_and_coast_pct
                                                        / 100.0))
        self.current_fuel_kg -= actual_fuel_burn

        # L&C costs lap time (10% lift costs ~0.3s, - needs changing to be based on track)
        lnc_time_penalty = (lift_and_coast_pct / 10.0) * 0.3

        # B. Fuel loss, laptime gain
        kg_lost = self.starting_fuel_kg - self.current_fuel_kg
        weight_time_advantage = -(kg_lost * self.fuel_effect_coeff)

        # C. The baseline temp car "wants" to be at in clean air
        target_engine_temp = 100.0

        # Dirty air raises the target temp
        if gap_to_car_ahead < 2.0:
            wake_severity = 2.0 - gap_to_car_ahead
            # e.g., 0.5s gap = 1.5 severity. Target raises by ~22C to 122C
            target_engine_temp += (wake_severity
                                   * 15.0) * track_object.dirty_air_coefficient

        # Lift and Coast lowers the target temp
        target_engine_temp -= (lift_and_coast_pct * 1.5)

        # Newton's law of cooling. The engine moves 25% of the distance toward its target temp each lap
        temp_difference = target_engine_temp - self.engine_temp
        self.engine_temp += (temp_difference * 0.25)

        # Hard floor so engine doesn't freeze
        self.engine_temp = max(90.0, self.engine_temp)

        # D. Instead of a blunt cliff, the hybrid system progressively trims power
        # above 115C to protect the ICE, costing small fractions of a second.
        derating_penalty = 0.0
        if self.engine_temp > 115.0:
            over_temp = self.engine_temp - 115.0
            # Costs 0.05s per degree over 115C.
            # e.g., at 120C, penalty is 0.25s per lap.
            derating_penalty = over_temp * 0.05

# E. Net lap time calculation
        net_car_time_impact = (
            weight_time_advantage
            + lnc_time_penalty
            + derating_penalty
        )

        return net_car_time_impact
