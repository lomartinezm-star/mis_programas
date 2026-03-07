nombre = input("Ingrese su nombre: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"{nombre}, tu promedio es {promedio}")

if promedio >= 61:
    print("Aprobado")
else:
    print("Reprobado")