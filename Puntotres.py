import numpy as np
import matplotlib.pyplot as plt
import control

# Definición de la función de transferencia del primer sistema
num1 = [1]
den1 = [1, 1, 0]
G1 = control.TransferFunction(num1, den1)

# Convertir la función de transferencia en una representación de espacio de estados
sys_ss1 = control.tf2ss(G1)

# Definición de los polos deseados para el primer sistema
zeta1 = 0.5916
omega_n1 = 1.387
des_poles1 = np.array([-zeta1*omega_n1 + omega_n1*1j, -zeta1*omega_n1 - omega_n1*1j])

# Cálculo del controlador para el primer sistema
K1 = control.acker(sys_ss1.A, sys_ss1.B, des_poles1)

# Cálculo de la función de transferencia en lazo cerrado para el primer sistema
sys_cl1 = control.StateSpace(sys_ss1.A - sys_ss1.B*K1, sys_ss1.B, sys_ss1.C, sys_ss1.D)

# Definición del tiempo de simulación
t_sim1 = np.linspace(0, 10, 1000)

# Respuesta al escalón unitario del primer sistema
t1, y_step1 = control.step_response(sys_cl1, T=t_sim1)

# Escalamiento de la respuesta para ajustar la referencia a 1
y_scaled1 = y_step1 * (1 / y_step1[-1])

# Cálculo de la energía del primer sistema
energy1 = np.trapz(y_scaled1**2, t1)

# Definición de la función de transferencia del segundo sistema
num2 = [1]
den2 = [1, 1, 0]
G2 = control.TransferFunction(num2, den2)

# Convertir la función de transferencia en una representación de espacio de estados
sys_ss2 = control.tf2ss(G2)

# Definición de los polos deseados para el segundo sistema
zeta2 = 0.5916
omega_n2 = 3.387
des_poles2 = np.array([-zeta2*omega_n2 + omega_n2*1j, -zeta2*omega_n2 - omega_n2*1j])

# Cálculo del controlador para el segundo sistema
K2 = control.acker(sys_ss2.A, sys_ss2.B, des_poles2)

# Cálculo de la función de transferencia en lazo cerrado para el segundo sistema
sys_cl2 = control.StateSpace(sys_ss2.A - sys_ss2.B*K2, sys_ss2.B, sys_ss2.C, sys_ss2.D)

# Definición del tiempo de simulación
t_sim2 = np.linspace(0, 10, 1000)

# Respuesta al escalón unitario del segundo sistema
t2, y_step2 = control.step_response(sys_cl2, T=t_sim2)

# Escalamiento de la respuesta para ajustar la referencia a 1
y_scaled2 = y_step2 * (1 / y_step2[-1])

# Cálculo de la energía del segundo sistema
energy2 = np.trapz(y_scaled2**2, t2)

# Graficar la energía de ambos sistemas
plt.plot(t1, y_scaled1**2, label='Realimentación a la salida')
plt.plot(t2, y_scaled2**2, label='Asignacion de Polo')
plt.xlabel('Tiempo')
plt.ylabel('Posicion Del Oscilador')
plt.title('Comparacion de los controladores Para del oscilador de Van der Pol ')
plt.legend()
plt.show()

print("Energía Control Realimentación a la salida:", energy1)
print("Energía Control Asignacion de Polo:", energy2)|
