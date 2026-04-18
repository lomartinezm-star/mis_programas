def tabla(numero): 
    for i in range(1, 11):  
        print(numero, "x", i, "=", numero * i) 


def es_primo(numero): 
    if numero < 2:  #no son
        return False

    for i in range(2, numero):  
        if numero % i == 0:  # Si divide exacto
            return False  # No es

    return True


def tablas_primos(limite): 
    for numero in range(2, limite + 1):  # 2 al límite
        if es_primo(numero):  # Si es
            print("\nTabla del", numero)
            tabla(numero)  # Imprime
            
# Programa principal
if __name__ == "__main__":
    try:
        limite = int(input("Ingrese el límite para buscar primos: "))  # Pide límite
        if limite < 2:
            print("El límite debe ser al menos 2.")
        else:
            tablas_primos(limite)  # Llama a la F
    except ValueError:
        print("Error: Ingrese un número entero válido.") 