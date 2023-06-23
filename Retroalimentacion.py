import control
import matplotlib.pyplot as plt

# Definir la función de transferencia de la planta
plant_tf = control.TransferFunction([1], [1, 1, 0])

# Definir la función de transferencia del controlador proporcional
K = 1  # Ajustar el valor de K según sea necesario
controller_tf = control.TransferFunction([K], [1])

# Crear el sistema de retroalimentación
feedback_system = control.feedback(plant_tf * controller_tf)

# Obtener la respuesta al escalón del sistema
t, y = control.step_response(feedback_system)

# Graficar la respuesta al escalón
plt.plot(t, y)
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.title('Respuesta al escalón del sistema de retroalimentación')
plt.grid(True)
plt.show()
