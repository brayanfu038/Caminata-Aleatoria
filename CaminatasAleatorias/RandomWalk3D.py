import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from FileReader import FileManager
import os


# Inicializar contadores de coordenadas
verticalCounter = 0
horizontalCounter = 0
depthCounter = 0

# Obtén la ruta del directorio actual (carpeta2)
directorio_actual = os.path.dirname(__file__)

# Construye la ruta relativa para acceder a carpeta1 y archivo1.txt
ruta_relativa = os.path.join("..", "Numbers Generated", "UniformDistributionValues.txt")

# Combina la ruta del directorio actual con la ruta relativa
ruta_absoluta = os.path.abspath(os.path.join(directorio_actual, ruta_relativa))

fm = FileManager(str(ruta_absoluta))
fm.storage_numbers()
steps = fm.numbers

def random_walk():
    global verticalCounter, horizontalCounter, depthCounter  # Declarar las variables como globales

    # Listas para almacenar las coordenadas
    x_coords = [horizontalCounter]
    y_coords = [verticalCounter]
    z_coords = [depthCounter]

    n = 1/6
    # Realizar el salto de la rana
    for step in steps:
   
        if 0 < step <= n:
            verticalCounter += 1
        elif n < step <= 2 * n:
            verticalCounter -= 1
        elif 2 * n < step <= 3 * n:
            horizontalCounter += 1
        elif 3 * n < step <= 4 * n:
            horizontalCounter -= 1
        elif 4 * n < step <= 5 * n:
            depthCounter += 1
        else:
            depthCounter -= 1

        # Registrar las coordenadas
        x_coords.append(horizontalCounter)
        y_coords.append(verticalCounter)
        z_coords.append(depthCounter)

    # Crear una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficar el recorrido de la rana
    ax.plot(x_coords, y_coords, z_coords, marker='o')

    # Etiquetas de ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Mostrar el gráfico
    plt.show()

# Llama a la función random_walk para ejecutarla
random_walk()
