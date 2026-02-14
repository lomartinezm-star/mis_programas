# Programa con bug (igual al de la presentación)

password = input("Clave: ")

# Prints de debug
print(f"DEBUG tipo: {type(password)}")
print(f"DEBUG valor: [{password}]")
print(f"DEBUG len: {len(password)}")

if password == 1234:  # BUG: string vs int
    print("Acceso concedido")
else:
    print("Acceso denegado")