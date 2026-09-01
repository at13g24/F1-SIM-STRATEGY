
# Import your blueprints from the other files!
from track import TRACK_DATABASE
from tyre import Tyre
from car import Car


def run_stint():
    # 1. Setup the Environment
    track = TRACK_DATABASE["Barcelona"]

    # 2. Setup the Car (Aggressively fueled to 100kg)
    mclaren = Car(chassis_name="MCL38", starting_fuel_kg=100.0)

    # 3. Mount the Tyres
    medium_compound = track.available_compounds[1]
    front_left = Tyre(compound_name=medium_compound, is_new=True)

    print(f"--- Starting 50-Lap Stint at {track.name} ---")
    print(f"Car: {mclaren.chassis_name} | Tyre: {front_left.compound}"
          f" (Medium) | Starting Fuel: 100kg")
    print(f"{'Lap':<4} | {'Net Pace Impact':<16} |"
          f" {'Engine Temp':<12} | {'Lift & Coast':<13} | {'Status'}")
    print("-" * 80)

    # 4. The Main Physics Loop
    for lap in range(1, 51):

        # Default to clean air
        gap = 5.0
        in_traffic = False

        # EVENT: Stuck in dirty air from Lap 15 to 25
        if 15 <= lap <= 25:
            gap = 1.0
            in_traffic = True

        # --- THE VIRTUAL RACE ENGINEER ---
        # Driver only lifts and coasts if the engine is getting dangerously hot
        current_lnc = 0.0
        if mclaren.engine_temp > 113.0:
            current_lnc = 15.0  # Heavy management to avoid 115C derating!
        elif mclaren.engine_temp > 108.0:
            current_lnc = 5.0   # Mild management as temps rise

        # Process Car Physics
        car_impact = mclaren.process_lap(
            track_object=track,
            gap_to_car_ahead=gap,
            lift_and_coast_pct=current_lnc
        )

        # Process Tyre Physics
        fl_stress = track.corner_stress["FL"]
        tyre_impact = front_left.calculate_performance_delta(
            track_object=track,
            current_track_temp=40.0,
            corner_stress_multiplier=fl_stress,
            in_dirty_air=in_traffic,
            chassis_modifier=mclaren.chassis_tyre_modifier
        )
        front_left.add_lap()

        # Calculate the net time gained/lost
        total_lap_impact = car_impact + tyre_impact

        # 5. Print the Telemetry
        # (Printing every lap so you can see the thermal curve unfold)
        if 12 <= lap <= 28 or lap % 10 == 0:
            traffic_flag = "⚠️ TRAFFIC" if in_traffic else "✅ CLEAN"
            # Highlight Heavy L&C
            lnc_str = f"{current_lnc}%" if current_lnc > 0 else "0.0%"

            print(f"{lap:02d}   | {total_lap_impact:+.3f}s"
                  f"          | {mclaren.engine_temp:.1f}C       |"
                  f" {lnc_str:<11}   | {traffic_flag}")


if __name__ == "__main__":
    run_stint()
