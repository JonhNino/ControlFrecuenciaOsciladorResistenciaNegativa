import numpy as np
from scipy import signal

A = np.array([[1, 2], [-1, 3]])  # Matriz de coeficientes de estado
B = np.array([[1], [0]])  # Matriz de coeficientes de entrada

controllability_matrix = np.column_stack((B, A @ B))
rank_controllability_matrix = np.linalg.matrix_rank(controllability_matrix)

if rank_controllability_matrix == A.shape[0]:
    print("El sistema es completamente controlable.")
    C = np.array([[1, 0]])  # Matriz de coeficientes de salida

    desired_eigenvalues = np.array([-2, -3])  # Autovalores deseados del observador

    L = signal.place_poles(A.T, C.T, desired_eigenvalues).gain_matrix.T  # Ganancia del observador de Luenberger

    print("Matriz de ganancia L del observador de Luenberger:")
    print(L)
else:
    print("El sistema no es completamente controlable.")
