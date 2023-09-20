# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
ore_grade = 0.8  # Copper ore grade (%)
furnace_temperature = 1200  # Furnace temperature (°C)
energy_cost_per_unit = 0.05  # Energy cost per unit (e.g., kWh)
smelting_time = 4  # Smelting time (hours)

# Calculate copper yield and energy consumption
copper_yield = ore_grade * 0.9  # Assume 90% recovery
energy_consumption = energy_cost_per_unit * furnace_temperature * smelting_time

# Print results
print(f"Copper Yield: {copper_yield:.2f} kg")
print(f"Energy Consumption: {energy_consumption:.2f} kWh")

# Visualization (optional)
labels = ['Copper Yield', 'Energy Consumption']
values = [copper_yield, energy_consumption]
plt.bar(labels, values)
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.title('Copper Smelting Process Simulation')
plt.show()
