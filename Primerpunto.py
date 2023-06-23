import numpy as np
import control
import matplotlib.pyplot as plt

# Definición de la función de transferencia del sistema
num = [1]
den = [1, 1, 0]
G = control.TransferFunction(num, den)

# Convertir la función de transferencia en una representación de espacio de estados
sys_ss = control.tf2ss(G)

# Definición de los polos deseados
zeta = 0.5916
omega_n = 3.387
des_poles = np.array([-zeta*omega_n + omega_n*1j, -zeta*omega_n - omega_n*1j])

# Cálculo del controlador algebraico por asignación de polos
K = control.acker(sys_ss.A, sys_ss.B, des_poles)

# Cálculo de la función de transferencia en lazo cerrado
sys_cl = control.StateSpace(sys_ss.A - sys_ss.B*K, sys_ss.B, sys_ss.C, sys_ss.D)

# Definición del tiempo de simulación
t = np.linspace(0, 10, 1000)

# Respuesta al escalón unitario
t, y = control.step_response(sys_cl, T=t)

# Escalamiento de la respuesta para ajustar la referencia a 1
y_scaled = y * (1 / y[-1])  # Escalar la respuesta para que el último valor sea 1

# Gráfico de la respuesta al escalón unitario
plt.plot(t, y_scaled)
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.title('Control por Asignacion de Polos a un Sistema de Van Der Pool')
plt.grid(True)
plt.show()
