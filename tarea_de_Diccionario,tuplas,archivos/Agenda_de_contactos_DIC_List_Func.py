# Lista global de contactos
contactos = []

# 1. Agregar contacto
def agregar_contacto():
    nombre = input("Nombre: ").strip()
    
    if nombre == "":
        print("Error: el nombre no puede estar vacío")
        return
    
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    contactos.append(contacto)
    print("Contacto agregado correctamente")


# 2. Buscar contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ").strip()
    
    encontrado = False
    
    for c in contactos:
        if c.get("nombre").lower() == nombre.lower():
            print("\nContacto encontrado:")
            print(f"Nombre: {c.get('nombre')}")
            print(f"Teléfono: {c.get('telefono')}")
            print(f"Email: {c.get('email')}")
            encontrado = True
            break
    
    if not encontrado:
        print("Contacto no encontrado")


# 3. Mostrar todos los contactos
def mostrar_contactos():
    if len(contactos) == 0:
        print("No hay contactos guardados")
        return
    
    print("\nLista de contactos:")
    for i, c in enumerate(contactos, start=1):
        print(f"\nContacto {i}:")
        print(f"Nombre: {c.get('nombre')}")
        print(f"Teléfono: {c.get('telefono')}")
        print(f"Email: {c.get('email')}")


# 4. Eliminar contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    
    for c in contactos:
        if c.get("nombre").lower() == nombre.lower():
            contactos.remove(c)
            print("Contacto eliminado correctamente")
            return
    
    print("Contacto no encontrado")


# Menú principal
def menu():
    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")


# Ejecutar programa
menu()