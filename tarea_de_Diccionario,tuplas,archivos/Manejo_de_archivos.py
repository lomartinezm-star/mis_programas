import json

# 1. Escribir 5 tareas iniciales
def escribir_tareas():
    tareas = [
        "Hacer tarea de programación",
        "Estudiar para examen",
        "Ir al gimnasio",
        "Comprar comida",
        "Leer un libro"
    ]
    
    with open("tareas.txt", "w") as f:
        for tarea in tareas:
            f.write(tarea + "\n")

# 2. Leer y mostrar tareas numeradas
def mostrar_tareas():
    try:
        with open("tareas.txt", "r") as f:
            lineas = f.readlines()
            
            print("\nLista de tareas:")
            for i, tarea in enumerate(lineas, start=1):
                print(f"{i}. {tarea.strip()}")
                
            return lineas
    except FileNotFoundError:
        print("El archivo no existe")
        return []

# 3. Agregar nuevas tareas
def agregar_tarea():
    nueva = input("\nNueva tarea: ")
    
    with open("tareas.txt", "a") as f:
        f.write(nueva + "\n")
    
    print("Tarea agregada")

# BONUS: guardar en JSON
def guardar_json(tareas):
    lista = []
    
    for t in tareas:
        lista.append({
            "tarea": t.strip(),
            "completada": False
        })
    
    with open("tareas.json", "w") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


# ---- PROGRAMA PRINCIPAL ----

# Paso 1
escribir_tareas()

# Paso 2
tareas = mostrar_tareas()

# Paso 3
agregar_tarea()

# Paso 4
tareas = mostrar_tareas()
print("\nTotal de tareas:", len(tareas))

# Bonus
guardar_json(tareas)
print("Archivo JSON creado")