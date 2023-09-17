import random
import matplotlib.pyplot as plt
import math

horizontalCounter = 0
verticalCounter = 0

x_coords = [horizontalCounter]
y_coords = [verticalCounter]

distancia = 450
print("Distancia max",distancia)
i =0 
count = 0
while (verticalCounter != 300 or horizontalCounter != 250):
    step = random.randint(1, 4)
    count+=1
    if step == 1:
        # Movimiento hacia arriba
        verticalCounter += 1
    elif step == 2:
        # Movimiento hacia abajo
        verticalCounter -= 1
    elif step == 3:
        # Movimiento hacia la derecha
        horizontalCounter += 1
    elif step == 4:
        # Movimiento hacia la izquierda
        horizontalCounter -= 1

# Imprimir los puntos generados
    x_coords.append(horizontalCounter)
    y_coords.append(verticalCounter)
    currentDistance = math.sqrt((250 - x_coords[-1])**2 + (300 - y_coords[-1])**2)
    print("count: ",count)

    if currentDistance > distancia:
     count=0 
    horizontalCounter = 0
    verticalCounter = 0
    x_coords = [horizontalCounter]
    y_coords = [verticalCounter]


# Crear una figura y ejes
fig, ax = plt.subplots()  
# Graficar los puntos al final del bucle
ax.plot(x_coords[:-1], y_coords[:-1], marker='o', color='blue', label='Puntos')
ax.plot(x_coords[-1], y_coords[-1], marker='o', color='red', label='Último Punto')

# Etiquetas de ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

# Mostrar el gráfico
plt.show()

   