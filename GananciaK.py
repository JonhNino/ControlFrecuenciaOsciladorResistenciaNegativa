import numpy as np
from scipy import signal
A = np.array([[1, 2], [-1, 3]])  # Matriz de coeficientes de estado
B = np.array([[1], [0]])  # Matriz de coeficientes de entrada
# Definir la matriz de ganancia del observador de Luenberger L
L = np.array([[9], [14]])  # Reemplazar con los valores obtenidos

# Definir los autovalores deseados para el sistema controlado
desired_eigenvalues = np.array([-1, -2])

# Calcular la matriz de ganancia del controlador K utilizando la asignación de polos
K = signal.place_poles(A, B, desired_eigenvalues).gain_matrix

# Imprimir la matriz de ganancia del controlador K
print("Matriz de ganancia del controlador K:")
print(K)
