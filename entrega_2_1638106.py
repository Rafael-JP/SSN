# -*- coding: utf-8 -*-
"""Entrega_2_1638106.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EbeYzlvm4fSJw5NJlufWlduIuWaOf3m3
"""

# -------------------------------------------------------
# Comparación de Verlet y Feynman
# -------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 1.0  # Force constant
m = 1.0  # Mass
x0 = 1.0  # Initial position
v0 = 0.0  # Initial velocity

# Input time step and number of steps
dt = float(input("\n Time step dt (Ideal 0.1):\n>"))
ntot = int(input("\n Number of time steps (Ideal 100):\n>"))

# Function for Feynman method with different energy calculations.
def feynman_method(dt, ntot, k, m, x0, v0):
    t = np.zeros(ntot + 1)
    x = np.zeros(ntot + 1)
    v_hk = np.zeros(ntot + 2)  # Velocity at half step
    E_vhk = np.zeros(ntot + 1)  # Energy using v_hk
    E_vavg = np.zeros(ntot + 1)  # Energy using v_avg
    E_vquad = np.zeros(ntot + 1)  # Energy using quadratic interpolation

    # Condcioens iniciales
    t[0] = 0.0
    x[0] = x0
    v_hk[0] = v0 + (dt / 2.0) * (-x0)  # v_hk at t = dt/2, se tiene en cuenta el primer calculo de la velocidad como paso especial con tal de empezar fuera del mismo tiempo que x y a

    # Calcular energia inicial, misma energia inicial para todos
    E0 = 0.5 * m * v0**2 + 0.5 * k * x0**2
    E_vhk[0] = E0
    E_vavg[0] = E0
    E_vquad[0] = E0

    # Primer paso con tratamiento especial
    a = -x[0]  # Aceleración, k/m es 1
    v_hk[1] = v_hk[0] + a * dt  # Velocidad en primer paso = dt/2
    x[1] = x[0] + dt * v_hk[1]  # Nueva posición
    t[1] = t[0] + dt  # Actualización del tiempo

    # Calculo energia en el primer paso
    E_vhk[1] = 0.5 * m * v_hk[1]**2 + 0.5 * k * x[1]**2
    v_avg = (v_hk[0] + v_hk[1]) / 2.0
    E_vavg[1] = 0.5 * m * v_avg**2 + 0.5 * k * x[1]**2
    v_quad = v_hk[0] + (dt / 2.0) * a + (dt**2 / 8.0) * (a - (-x[1])) / dt
    E_vquad[1] = 0.5 * m * v_quad**2 + 0.5 * k * x[1]**2

    # Evolución del tiempo en loop
    for i in range(1, ntot):
        # Calculo de la aceleración en la nueva posición
        a = -x[i]
        # Velocity cambio de la velocidad intermedia
        v_hk[i + 1] = v_hk[i] + a * dt
        # Nueva posición
        x[i + 1] = x[i] + dt * v_hk[i + 1]
        # Actualización tiempo
        t[i + 1] = t[i] + dt
        # Calcuar energia para siguiente paso
        E_vhk[i + 1] = 0.5 * m * v_hk[i + 1]**2 + 0.5 * k * x[i + 1]**2
        v_avg = (v_hk[i] + v_hk[i + 1]) / 2.0 #Se hace la media
        E_vavg[i + 1] = 0.5 * m * v_avg**2 + 0.5 * k * x[i + 1]**2 #Calculo con la velocidad coordinada
        v_quad = v_hk[i] + (dt / 2.0) * a + (dt**2 / 8.0) * (a - (-x[i + 1])) / dt #Cálculo para aproximación 2, se aproxima de forma cuadratica
        E_vquad[i + 1] = 0.5 * m * v_quad**2 + 0.5 * k * x[i + 1]**2 #Calculo con la velocidad obtenida de forma cuadrática

    return t, E_vhk / E0, E_vavg / E0, E_vquad / E0  # Normalized energy

# Usar diferentes pasos o lo energias, se puede cambiar arriba
t, E_vhk, E_vavg, E_vquad = feynman_method(dt, ntot, k, m, x0, v0)

# Plot todo
plt.figure(figsize=(12, 6))

# Plot energia vs tiempo para todos los metodos
plt.plot(t, E_vhk, 'r-', label='Energy (v_hk)')
plt.plot(t, E_vavg, 'g-', label='Energy (v_avg)')
plt.plot(t, E_vquad, 'b-', label='Energy (v_quad)')
plt.axhline(1.0, color='black', linestyle='--', label='Ideal Energy Conservation')
plt.ylabel('Energy / E0')
plt.xlabel('Time')
plt.legend()
plt.title('Comparison of Energy Calculation Methods in Feynman')

# Plot error en cada energia
plt.figure(figsize=(12, 6))
plt.plot(t, np.abs(E_vhk - 1.0), 'r-', label='Error (v_hk)')
plt.plot(t, np.abs(E_vavg - 1.0), 'g-', label='Error (v_avg)')
plt.plot(t, np.abs(E_vquad - 1.0), 'b-', label='Error (v_quad)')
plt.ylabel('|Energy / E0 - 1|')
plt.xlabel('Time')
plt.legend()
plt.title('Error in Energy Calculation Methods in Feynman')

# Mostrar el plot
plt.show()

