
cuadrados = [] # Creamos una lista vacía para almacenar los cuadrados
for x in range(1,6):
    cuadrados.append(x**2)
print(cuadrados)



cuadrados = [x ** 2 
             for x in range(1, 6)] # Usamos una comprensión de listas para crear la lista de cuadrados
print(cuadrados)