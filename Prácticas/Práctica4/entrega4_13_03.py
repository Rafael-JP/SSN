# -*- coding: utf-8 -*-
"""Entrega4_13_03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JJy6KF1X_sMs-Eynr24ucAP5CbLz05ax
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Para graficar en 3D

# Entrada del usuario
total_random_points = int(input("\nEnter number of points for Monte Carlo estimate of Sphere Volume?\n>"))

# Inicialización de contadores
inside_sphere = 0
inside_cube = 0

# Listas para guardar puntos dentro y fuera de la esfera
points_inside = []
points_outside = []

# Generación de puntos aleatorios
while inside_cube < total_random_points:
    # Generar un punto aleatorio en 3D
    x = np.random.uniform(-1.0, 1.0)
    y = np.random.uniform(-1.0, 1.0)
    z = np.random.uniform(-1.0, 1.0)

    # Contar puntos dentro del cubo
    inside_cube += 1

    # Verificar si el punto está dentro de la esfera
    if x**2 + y**2 + z**2 <= 1.0:
        inside_sphere += 1
        points_inside.append((x, y, z))
    else:
        points_outside.append((x, y, z))

# Cálculo de la fracción de puntos dentro de la esfera
sphere_ratio = inside_sphere / inside_cube

# Estimación de π y el volumen de la esfera
pi_approx = 6.0 * sphere_ratio
sphere_volume_approx = (4.0 / 3.0) * pi_approx  # Volumen de la esfera

# Resultados
print('\n--------------')
print('\nResultados')
print('\nNúmero de puntos dentro del cubo:', inside_cube)
print('Número de puntos dentro de la esfera:', inside_sphere)
print('Fracción de puntos dentro de la esfera:', sphere_ratio * 100, '%')
print('\nEstimación de π:', pi_approx)
print('Valor exacto de π:', np.pi)
print('\nVolumen estimado de la esfera:', sphere_volume_approx)
print('Volumen exacto de la esfera:', (4.0 / 3.0) * np.pi)

# Visualización en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Convertir listas de puntos a arrays de numpy
points_inside = np.array(points_inside)
points_outside = np.array(points_outside)

# Graficar puntos dentro de la esfera en rojo
if len(points_inside) > 0:
    ax.scatter(points_inside[:, 0], points_inside[:, 1], points_inside[:, 2], c='r', marker='o', s=1)

# Graficar puntos fuera de la esfera en azul
if len(points_outside) > 0:
    ax.scatter(points_outside[:, 0], points_outside[:, 1], points_outside[:, 2], c='b', marker='o', s=1)

# Configuración de la gráfica
ax.set_title('Monte Carlo: Estimación del volumen de una esfera')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Mostrar la gráfica
plt.show()

