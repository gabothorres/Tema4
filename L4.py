# Solución del Laboratorio 4

# Parte a

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias C y Z
vaC = stats.norm(5, np.sqrt(0.2))
vaZ = stats.uniform(0, np.pi/2)

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (C y Z independientes)
# Se toma un valor constante de omega, el cual es 2
omega = 2
for i in range(N):
	C = vaC.rvs()
	Z = vaZ.rvs()
	x_t = C * np.cos(omega*t + Z)
	X_t[i,:] = x_t
	plt.plot(t, x_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(X_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = (10/np.pi) * (np.cos(omega*t)-np.sin(omega*t))
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# Parte b)

# Creación de las muestras del proceso x(t) (C), tomando omega y la fase como constantes
# Se toma un valor constante de la fase, el cual es 0
theta = 0

# Inicialización del proceso aleatorio X(t) con N realizaciones
X_t_2 = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

for i in range(N):
	C_2 = vaC.rvs()
	x_t_2 = C_2 * np.cos(omega*t + theta)
	X_t_2[i,:] = x_t_2

# Promedio de las N realizaciones en cada instante (cada punto en t)
P_2 = [np.mean(X_t_2[:,i]) for i in range(len(t))]

# T valores de desplazamiento tau
desplazamiento_2 = np.arange(T)
taus_2 = desplazamiento_2/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr_2 = np.empty((N, len(desplazamiento_2)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento_2):
		corr_2[n, i] = np.correlate(X_t_2[n,:], np.roll(X_t_2[n,:], tau))/T
	plt.plot(taus_2, corr_2[n,:])

# Valor teórico de correlación
Rxx_2 = 25.2 * np.cos(omega*t+theta)*np.cos(omega*(t+taus_2)+theta)

# Gráficas de correlación para cada realización y la
plt.plot(taus_2, Rxx_2, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()
