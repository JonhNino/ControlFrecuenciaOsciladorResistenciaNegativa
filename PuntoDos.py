import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import control

# Definir la función que representa el sistema del oscilador de Van der Pol
def vanderpol(t, y):
    mu = 1.0  # Parámetro de no linealidad
    dydt = [y[1], mu * (1 - y[0] ** 2) * y[1] - y[0]]
    return dydt

# Definir la función que representa el controlador
def controlador(t, y):
    K = np.array([[1, 0]])  # Ganancia del controlador
    u = -np.dot(K, y)  # Ley de control por realimentación de estados
    return u

# Condiciones iniciales
y0 = [1, 0]  # [Posición inicial, Velocidad inicial]
t_span = [0, 10]  # Rango de tiempo de simulación

# Simulación del sistema con realimentación dinámica a la salida
sol = solve_ivp(vanderpol, t_span, y0, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], 100))
y = sol.y[0]  # Posición del oscilador

# Simulación del sistema con realimentación dinámica a la salida y controlador
sol_control = solve_ivp(lambda t, y: vanderpol(t, y) + controlador(t, y), t_span, y0, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], 100))
y_control = sol_control.y[0]  # Posición del oscilador con control

# Definición de la función de transferencia del sistema
num = [1]
den = [1, 1, 0]
G = control.TransferFunction(num, den)

# Convertir la función de transferencia en una representación de espacio de estados
sys_ss = control.tf2ss(G)

# Definición de los polos deseados
zeta = 0.5916
omega_n = 1.387
des_poles = np.array([-zeta*omega_n + omega_n*1j, -zeta*omega_n - omega_n*1j])

# Cálculo del controlador 
K = control.acker(sys_ss.A, sys_ss.B, des_poles)

# Cálculo de la función de transferencia en lazo cerrado
sys_cl = control.StateSpace(sys_ss.A - sys_ss.B*K, sys_ss.B, sys_ss.C, sys_ss.D)

# Definición del tiempo de simulación
t_sim = np.linspace(0, 10, 1000)

# Respuesta al escalón unitario
t, y_step = control.step_response(sys_cl, T=t_sim)

# Escalamiento de la respuesta para ajustar la referencia a 1
y_scaled = y_step * (1 / y_step[-1])  # Escalar la respuesta para que el último valor sea 1

# Gráfico de los resultados
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label='Sin control')
plt.plot(t_sim, y_scaled, label='Con control')
plt.xlabel('Tiempo')
plt.ylabel('Posición del oscilador')
plt.title('Simulación del oscilador de Van der Pol con realimentación a la salida')
plt.legend()
plt.grid(True)
plt.show()
