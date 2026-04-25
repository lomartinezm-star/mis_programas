import json

# 1. JSON con 3 cursos
json_cursos = '''
[
    {
        "nombre": "Programación I",
        "codigo": "PROG101",
        "creditos": 4,
        "horario": "Lunes 8-10",
        "prerequisitos": []
    },
    {
        "nombre": "Matemática Básica",
        "codigo": "MAT101",
        "creditos": 3,
        "horario": "Martes 10-12",
        "prerequisitos": []
    },
    {
        "nombre": "Estructuras de Datos",
        "codigo": "PROG201",
        "creditos": 5,
        "horario": "Miércoles 2-4",
        "prerequisitos": ["PROG101"]
    }
]
'''

# 2. Convertir JSON a lista de diccionarios
cursos = json.loads(json_cursos)

# 3. Mostrar cursos con más de 3 créditos
print("Cursos con más de 3 créditos:")
for curso in cursos:
    if curso.get("creditos", 0) > 3:
        print(curso.get("nombre"), "-", curso.get("creditos"), "créditos")

# 4. Buscar curso por código
codigo = input("\nIngrese código a buscar: ")

for curso in cursos:
    if curso.get("codigo") == codigo:
        print("\nCurso encontrado:")
        print(curso)
        break
else:
    print("Curso no encontrado")

# 5. Modificar horario
codigo_mod = input("\nIngrese código para modificar horario: ")

for curso in cursos:
    if curso.get("codigo") == codigo_mod:
        nuevo = input("Nuevo horario: ")
        curso["horario"] = nuevo
        print("Horario actualizado")
        break

# 6. Convertir de nuevo a JSON
nuevo_json = json.dumps(cursos, indent=4, ensure_ascii=False)

print("\nJSON actualizado:")
print(nuevo_json)