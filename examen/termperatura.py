def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def convertir(valor, origen, destino):
    if origen == destino:
        return valor
    
    if origen == "F":
        valor = fahrenheit_a_celsius(valor)
    elif origen == "K":
        valor = valor - 273.15
    
    if destino == "F":
        return celsius_a_fahrenheit(valor)
    elif destino == "K":
        return celsius_a_kelvin(valor)
    else:
        return valor

# Programa principal
if __name__ == "__main__":
    try:
        valor = float(input("Ingrese el valor de temperatura: "))
        origen = input("Ingrese la unidad de origen (C, F, K): ").upper()
        destino = input("Ingrese la unidad de destino (C, F, K): ").upper()
        
        if origen not in ["C", "F", "K"] or destino not in ["C", "F", "K"]:
            print("Unidades inválidas. Use C, F o K.")
        else:
            resultado = convertir(valor, origen, destino)
            print(f"{valor} {origen} = {resultado:.2f} {destino}")
    except ValueError:
        print("Error: Ingrese un número válido para la temperatura.")