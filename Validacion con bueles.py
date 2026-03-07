# validar entrada del usuario
edad = -1
while edad < 0 or edad > 120:
    edad = int(input("tu edad (0-120): "))
    if edad < 0 or edad > 120:
        print("edad no valida, intentalo de nuevo")
print(f"tu edad es: {edad}")

