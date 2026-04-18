def calcular_billetes(monto):  

    if monto % 20 != 0: 
        print("Error: el monto debe ser múltiplo de 20") 
        return None  

    billetes_200 = monto // 200  
    monto = monto % 200  

    billetes_100 = monto // 100  
    monto = monto % 100  

    billetes_50 = monto // 50  
    monto = monto % 50 

    billetes_20 = monto // 20  

    print(billetes_200, "x Q200,",
          billetes_100, "x Q100,",
          billetes_50, "x Q50,",
          billetes_20, "x Q20")  

# Programa principal
if __name__ == "__main__":
    try:
        monto = int(input("Ingrese el monto a retirar (múltiplo de 20): "))  
        calcular_billetes(monto)  # Llama a la función
    except ValueError:
        print("Error: Ingrese un número válido.")  # Maneja errores si no es número