def cifrar_caracter(caracter, desplazamiento): 

    if caracter.isalpha():  #letra

        base = ord('a')  

        posicion = ord(caracter.lower()) - base  #número

        nueva = (posicion + desplazamiento) % 26  

        return chr(base + nueva)  #letra

    return caracter  


def cifrar_mensaje(mensaje, desplazamiento):  # Cifra

    resultado = ""  

    for caracter in mensaje:  
        resultado += cifrar_caracter(caracter, desplazamiento)  

    return resultado  # Devuelve


def descifrar_mensaje(mensaje, desplazamiento):  # Descifra
    return cifrar_mensaje(mensaje, -desplazamiento)  

# Programa principal
if __name__ == "__main__":
    try:
        mensaje = input("Ingrese el mensaje: ")
        desplazamiento = int(input("Ingrese el desplazamiento (número entero): ")) 
        opcion = input("¿Cifrar (C) o descifrar (D)?: ").upper() 
        
        if opcion == "C":
            resultado = cifrar_mensaje(mensaje, desplazamiento) 
            print("Mensaje cifrado:", resultado)
        elif opcion == "D":
            resultado = descifrar_mensaje(mensaje, desplazamiento)
            print("Mensaje descifrado:", resultado)
        else:
            print("Opción inválida. Use C o D.")
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")