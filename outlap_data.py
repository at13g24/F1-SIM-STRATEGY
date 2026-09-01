
import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

# 1. Setup and Cache
fastf1.Cache.enable_cache('f1_cache')
fastf1.plotting.setup_mpl()  # Turns on F1-style dark mode graphs

# 2. Load the 2025 Barcelona Race
print("Loading 2025 Barcelona Race Data...")
session = fastf1.get_session(2025, 'Spain', 'R')
session.load(telemetry=False, weather=False)

# 3. Isolate the Out-Laps
laps = session.laps
# An out-lap is defined as any lap that has a recorded "Pit Out Time"
out_laps = laps[laps['PitOutTime'].notna()]

# Convert the lap times from Python 'timedelta' objects into raw seconds
out_lap_times = out_laps['LapTime'].dt.total_seconds().dropna()

# 4. Clean the Data (Remove Safety Cars)
green_flag_out_laps = out_lap_times[out_lap_times < 105]

print(
      f"\nSuccessfully isolated {len(green_flag_out_laps)} "
      f"green-flag out-laps."
      )

# 5. Plot the Histogram
plt.figure(figsize=(10, 6))
plt.hist(green_flag_out_laps, bins=15, color='cyan', edgecolor='white',
         alpha=0.8)

plt.title("2025 Barcelona GP: Distribution of Green-Flag Out-Laps")
plt.xlabel("Out-Lap Time (Seconds)")
plt.ylabel("Frequency (Number of Occurrences)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
