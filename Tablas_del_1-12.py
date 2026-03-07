

print("Tablas del 1 AL 12")

for num in range(1, 13):
    print(f"\n--- tabla del {num} ---")

    for i in range(1, 13):   # multiplicaciones del 1 al 12
        resultado = num * i
        print(f"{num} x {i:2d} = {resultado}")