import matplotlib.pyplot as plt
import random
from matplotlib.ticker import MaxNLocator
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

# Inicializar contadores
count = 0

# Crear una serie para almacenar los datos
x_coords = [0]
y_coords = [0]
print("hola")
n=1/2
i=0
# Realizar el recorrido en 1D de la rana
for step in (steps):
    

    if step <= 1/2:
        count += 1
    else:
        count -= 1

    # Registrar las coordenadas en la serie
    i += 1
    x_coords.append(i)
    y_coords.append(count)

# Crear el gráfico 1D
plt.plot(x_coords, y_coords, marker='o')

# Etiquetas de ejes
plt.xlabel('Pasos')
plt.ylabel('Posición en el Eje X')

# Alinear los marcadores de los ejes X y asegurarse de que sean números enteros
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Mostrar el gráfico
plt.show()
