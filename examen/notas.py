def promedio(notas): 
    suma = 0  #acumulador
    for nota in notas:  
        suma += nota  # cada
    return suma / len(notas)  #cantidad


def mayor(notas): 
    mayor_nota = notas[0]  
    for nota in notas:
        if nota > mayor_nota:  
            mayor_nota = nota 
    return mayor_nota 


def menor(notas): 
    menor_nota = notas[0]
    for nota in notas:
        if nota < menor_nota:
            menor_nota = nota
    return menor_nota


def contar_aprobados(notas, minimo=61):
    aprobados = 0  # Contador
    for nota in notas:
        if nota >= minimo: 
            aprobados += 1 
    return aprobados


def reporte(notas):  
    print("Promedio:", promedio(notas)) 
    print("Nota mayor:", mayor(notas))  
    print("Nota menor:", menor(notas))
    print("Aprobados:", contar_aprobados(notas))  

# Programa principal
if __name__ == "__main__":
    try:
        entrada = input("Ingrese las notas separadas por comas (ej: 85,90,78): ") 
        notas_str = entrada.split(",")  # Separa por comas
        notas = [float(nota.strip()) for nota in notas_str]  # Convierte
        
        if notas: 
            reporte(notas) 
        else:
            print("No se ingresaron notas válidas.")
    except ValueError:
        print("Error: Ingrese números válidos separados por comas.")