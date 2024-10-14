# Heat-Exchanger-Performance-Analysis-Using-the-NTU-Method-



This Python script implements the NTU (Number of Transfer Units) Method for analyzing the performance of a heat exchanger. The NTU method is widely used when the outlet temperatures of fluids are unknown, allowing for the calculation of the heat transfer rate between two fluids in a heat exchanger.

Key Features

Calculate NTU (Number of Transfer Units): The script calculates the NTU based on the heat exchanger's parameters such as heat capacity rates, overall heat transfer coefficient, and surface area.

Effectiveness Calculation: The code provides the effectiveness (ε) of the heat exchanger for two common configurations:

Counterflow heat exchanger

Parallelflow heat exchanger


Inputs

Heat capacity rates of hot and cold fluids (C_min, C_max)

Overall heat transfer coefficient (U)

Heat exchanger surface area (A)

Inlet temperatures of hot and cold fluids (T_hot_in, T_cold_in)

Choice of heat exchanger type (Counterflow or Parallelflow)


Output

Heat transfer rate (Q) in watts (W)

