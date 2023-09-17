import matplotlib.pyplot as plt
import random
from FileReader import FileManager
import os


# Obtén la ruta del directorio actual (carpeta2)
directorio_actual = os.path.dirname(__file__)

# Construye la ruta relativa para acceder a carpeta1 y archivo1.txt
ruta_relativa = os.path.join("..", "Numbers Generated", "UniformDistributionValues.txt")

# Combina la ruta del directorio actual con la ruta relativa
ruta_absoluta = os.path.abspath(os.path.join(directorio_actual, ruta_relativa))


fm = FileManager(str(ruta_absoluta))
fm.storage_numbers()
steps=fm.numbers

# Inicializar contadores de coordenadas
horizontalCounter = 0
verticalCounter = 0






# Listas para almacenar las coordenadas
x_coords = [horizontalCounter]
y_coords = [verticalCounter]

n=1/4
# Realizar el recorrido de la rana en 2D
for step in (steps):

    if 0<step <=n:
        verticalCounter += 1
    elif n<step <=2*n:
        verticalCounter -= 1
    elif 2*n<step <= 3*n:
        horizontalCounter += 1
    elif 3*n<step <= 4:
        horizontalCounter -= 1

    # Registrar las coordenadas
    x_coords.append(horizontalCounter)
    y_coords.append(verticalCounter)

# Crear el gráfico 2D
plt.plot(x_coords[:-1], y_coords[:-1], marker='o', color='blue', label='Puntos')
plt.plot(x_coords[-1], y_coords[-1], marker='o', color='red', label='Último Punto')
# Etiquetas de ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()
