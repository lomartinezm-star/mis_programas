# Lester Martinez 2500451
#------------------------------------------------------------------------------
# 1 y 2 Tupla y desempaquetado
coordenadas = (14.6349, -90.5069)
lat, lon = coordenadas

print(lat, lon)
#------------------------------------------------------------------------------
# 3. Función de estadísticas
def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

print(estadisticas([10, 5, 20, 15, 8]))
#------------------------------------------------------------------------------
# 4. Diccionario con tuplas como claves
distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45
}

print(distancias)
#------------------------------------------------------------------------------
# 5. Intentar modificar la tupla
coordenadas[0] = 15  # ERROR: las tuplas son inmutables, no se pueden modificar
