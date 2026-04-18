def calcular_propina(subtotal, porcentaje):  #propina
    return subtotal * porcentaje / 100  


def calcular_total(subtotal, propina):  # Calcula total
    return subtotal + propina


def dividir_cuenta(total, personas):  # Divide personas
    if personas <= 0: 
        return "Error"
    return total / personas


def aplicar_descuento(subtotal, descuento):  #descuento
    return subtotal - (subtotal * descuento / 100)


def mostrar_menu():  
    print("\n1. Propina")
    print("2. Dividir cuenta")
    print("3. Descuento + propina")
    print("4. Salir")


def main():  # Función principal

    while True:  # Bucle

        mostrar_menu()  
        opcion = input("Opción: ")  #lee

        if opcion == "1":  # Opción 1
            subtotal = float(input("Subtotal: "))  
            porcentaje = float(input("Porcentaje: "))
            propina = calcular_propina(subtotal, porcentaje)
            total = calcular_total(subtotal, propina)
            print("Total:", total)

        elif opcion == "2":  # Opción 2
            total = float(input("Total: "))
            personas = int(input("Personas: "))
            print("Cada uno paga:", dividir_cuenta(total, personas))

        elif opcion == "3":  # Opción 3
            subtotal = float(input("Subtotal: "))
            descuento = float(input("Descuento: "))
            nuevo = aplicar_descuento(subtotal, descuento)
            propina = calcular_propina(nuevo, 10)
            total = calcular_total(nuevo, propina)
            print("Total:", total) 

        elif opcion == "4":  # Salir
            break  # Termina
        else:
            print("Opción inválida") 


main()  # Ejecuta
