import math

# Function to calculate NTU
def calculate_NTU(C_min, C_max, U, A):
    return (U * A) / C_min

# Effectiveness for different heat exchanger types
def effectiveness_NTU(method, NTU, C_min_C_max_ratio):
    if method == "counterflow":
        if C_min_C_max_ratio != 1:
            return (1 - math.exp(-NTU * (1 - C_min_C_max_ratio))) / (1 - C_min_C_max_ratio * math.exp(-NTU * (1 - C_min_C_max_ratio)))
        else:
            return NTU / (1 + NTU)
    elif method == "parallelflow":
        return (1 - math.exp(-NTU * (1 + C_min_C_max_ratio))) / (1 + C_min_C_max_ratio)
    else:
        raise ValueError("Invalid method. Choose either 'counterflow' or 'parallelflow'.")

# Main function to calculate heat transfer rate
def heat_transfer_rate(method, C_min, C_max, U, A, T_hot_in, T_cold_in):
    NTU = calculate_NTU(C_min, C_max, U, A)
    C_min_C_max_ratio = C_min / C_max
    epsilon = effectiveness_NTU(method, NTU, C_min_C_max_ratio)
    
    Q_max = C_min * (T_hot_in - T_cold_in)
    Q = epsilon * Q_max
    
    return Q

# Example inputs
C_min = int(input("Minimum heat capacity rate (W/k): "))  # Minimum heat capacity rate (W/K)
C_max = int(input("Maximum heat capacity rate (W/K): "))  # Maximum heat capacity rate (W/K)
U = int(input("Overall heat transfer coefficient (W/m^2K): "))  # Overall heat transfer coefficient (W/m^2K)
A = int(input("Heat exchanger area (m^2): "))  # Heat exchanger area (m^2)
T_hot_in = int(input("Hot fluid inlet temperature (°C): ")) # Hot fluid inlet temperature (°C)
T_cold_in = int(input("Cold fluid inlet temperature (°C): ")) # Cold fluid inlet temperature (°C)

method = "counterflow"  # Choose either 'counterflow' or 'parallelflow'

# Calculate heat transfer rate
Q = heat_transfer_rate(method, C_min, C_max, U, A, T_hot_in, T_cold_in)
print(f"Heat Transfer Rate (Q): {Q} W")
