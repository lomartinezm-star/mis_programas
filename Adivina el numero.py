import random
numero_secreto = random.randint(1, 100)
intentos_maximos = 7
intentos = 0
while True:
    intento = int(input("Adivina el numero (1-100): "))
    intentos += 1
    if intento < numero_secreto:
        print("Mas alto.")
    elif intento > numero_secreto:
        print("Mas bajo.")
    else:
        print(f"Correcto en " f" {intentos} intentos.")
        if intentos <= intentos_maximos:
            break
        else:
            print(f"Perdiste. El numero era {numero_secreto}.") 
            break