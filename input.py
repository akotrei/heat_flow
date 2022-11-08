import numpy as np

# set T0i here if length is not equal to @N T0i = 0 for all @i will be used
t_start = [] # initial temperature at grid points (K)

R1 = 0.05  # internal radius (meter)
R2 = 0.45  # external radius (meter)
DELTA_T = 10.0  # simulation time (second)
RO = 2700.0  # medium density (kilogram / meter**3)
C_RO = 900.0  # specific heat capacity (Joule / (kilogram * K))
LAMBDA = 247.0  # thermal conductivity coefficient (Watt / (meter * K))
N = 100  # cell count
M = 10000 # time direction cell's count
A1 = 100.0  # internal heat transfer coefficient (Watt / (meter**2 * K))
A2 = 100.0  # external heat transfer coefficient (Watt / (meter**2 * K))
T1 = 100000.0  # internal radius temperature (K)
T2 = 10.0  # external radius temperature (K)

if len(t_start) == N:
    T0 = np.array(t_start)
else:
    T0 = np.full((N,), 0.0)
