# Lester Martinez 2500451

print("Tablas del 1 AL 12")

for num in range(1, 13):
    print(f"\n--- tabla del {num} ---")

    for i in range(1, 13): 
        resultado = num * i
        print(f"{num} x {i:2d} = {resultado}")