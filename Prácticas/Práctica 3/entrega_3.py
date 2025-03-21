# -*- coding: utf-8 -*-
"""Entrega 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BoPI9KJ7FQmi3_O1XBT6_iBNC-AefiSf

**Particle in a 1D Box**

Numerical solution particle in a box (infinite potential barriers in the box edges).
The code assumed the particle is an electron and we use Atomic Units.

We start importing libraries:
"""

import numpy as np
import matplotlib.pyplot as plt

"""We define a function with the potential for the Schrödinger Equation. In this case is zero everywhere but it can be modified easily by any function as you like:"""

# Potential as a function of position (V-shaped potential)
def getV(x):
    alpha = 2.0  # Controla la inclinación del "V"
    if abs(x) < 5.0:  # Cambié el límite de 1 a 3 para un pozo más amplio
        potvalue = alpha * abs(x)  # Potencial lineal en forma de "V"
    else:
        potvalue = 10.0  # Potencial infinito fuera de la caja
    return potvalue

"""And now we define a function that calculates the matrix (denoted by F in the theoretical derivation) that encodes the Schrödinger Equation in finite diference form for n points from 0 to n-1"""

#Discretized Schrodinger equation in n points (FROM 0 to n-1)
def Eq(n,h,x):
    F = np.zeros([n,n])
    for i in range(0,n):
        F[i,i] = -2*((h**2)*getV(x[i]) + 1)
        if i > 0:
           F[i,i-1] = 1
           if i < n-1:
              F[i,i+1] = 1
    return F

"""Up to now, the code does nothing explicitly. We have just defined how to calculate the potential and how to calculate the matrix F

Let us now start the numerical solution, entering the parameters that we need: the discretization h and the size of the box.
"""

# Interval for calculating the wave function [-L/2,L/2]
L = 10 #Ahora va de -5 a 5
xlower = -L/2.0
xupper = L/2.0

#Discretization options
h = 0.01  #discretization in space, peor que la infinita de 0.01 a 0.02, se ha pillado estos valors para comparar

#Create coordinates at which the solution will be calculated
x = np.arange(xlower,xupper+h,h)
#grid size (how many discrete points to use in the range [-L/2,L/2])
npoints=len(x)

print("Using",npoints, "grid points.")

"""Now we can calculate F explicitly and diagonalize. The result of the diagonalization is **not ordered** so we have to order the results (energies and wavefunctions) by energy values."""

#Calculation of discrete form of Schrodinger Equation and diagonalization
F=Eq(npoints,h,x)
eigenValues, eigenVectors = np.linalg.eig(F)

#Order results by eigenvalue
# w ordered eigenvalues and vs ordered eigenvectors
idx = eigenValues.argsort()[::-1]
w = eigenValues[idx]
vs = eigenVectors[:,idx]

#Energy Level
E = - w/(2.0*h**2)

"""Print **Energy Results** and compare with Exact analytical result:"""

#Energy Levels, no importa, no se compara ahora, tendria que usar aproximación mas pequeña para que converja mejor, estado 3 se escapa, no está ligado, partícula libre que no está confinada.
E = - w/(2.0*h**2)
for k in range(0,5):
  E_exact=(float(k+1)*(np.pi))**2.0/(2.0*L*L)
  print("n=",k,", E(numeric)=%.4f" %E[k])

"""Now let us show the Wavefunctions obtained in the diagonalization process"""

#Init Wavefunction (empty list with npoints elements), mostramos los dos que están ligados
psi = [None]*npoints

#Calculation of normalised Wave Functions
for k in range(0,len(w)):
	psi[k] = vs[:,k]
	integral = h*np.dot(psi[k],psi[k])
	psi[k] = psi[k]/integral**0.5

#Plot Wave functions
print("Plotting")

#v = int(input("\n Quantum Number (enter 0 for ground state):\n>"))
for v in range(0,5):
	plt.plot(x,psi[v],label=r'$\psi_v(x)$, k = ' + str(v))
	plt.title(r'$n=$'+ str(v) + r', $E_n$=' + '{:.4f}'.format(E[v]))
	plt.legend()
	plt.xlabel(r'$x$ (a.u.)')
	plt.ylabel(r'$\psi(x)$')
	plt.show()

print("Bye")
#En el fundamental lo mas probable es en medio de la caja, en el otro es mas probable ligeramente desplazado, la caja va de -1 a 1, hay un tunneling ahora

# Discretization options
h_values = [0.1,0.05,0.02, 0.01, 0.005]  # Valores de h a probar

# Comparación de energías para diferentes valores de h
for h in h_values:
    # Create coordinates at which the solution will be calculated
    x = np.arange(xlower, xupper + h, h)
    npoints = len(x)
    print(f"\nUsing {npoints} grid points with h = {h}")

    # Calculation of discrete form of Schrodinger Equation and diagonalization
    F = Eq(npoints, h, x)
    eigenValues, eigenVectors = np.linalg.eig(F)

    # Order results by eigenvalue
    idx = eigenValues.argsort()[::-1]
    w = eigenValues[idx]
    vs = eigenVectors[:, idx]

    # Energy Levels
    E = -w / (2.0 * h**2)

    # Print energies for the first 5 states
    print("Energy levels for the first 5 states:")
    for k in range(0, 5):
        print(f"n = {k}, E(numeric) = {E[k]:.4f}")

