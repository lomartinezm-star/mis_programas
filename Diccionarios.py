# 1. Crear diccionario con información personal
persona = {
    "nombre": "Lester",
    "edad": 30,
    "ciudad": "Chimaltenango",
    "lenguaje_favorito": "JavaScript"
}

# 2. Agregar nueva clave 'universidad'
persona["universidad"] = "San Pablo"

# 3. Modificar la edad
persona["edad"] = 31

# 4. Iterar e imprimir cada par
for clave, valor in persona.items():
    print(clave, ":", valor)

# 5. Verificar si 'email' existe
if "email" in persona:
    print("Sí existe email")
else:
    print("No existe email")

# 6. Usar get() para 'telefono'
telefono = persona.get("telefono", "No disponible")
print("Teléfono:", telefono)