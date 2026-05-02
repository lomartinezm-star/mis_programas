class Estudiante:

    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61
    
#ejemplo
e1 = Estudiante("Lester", "2026", "Ingeniería")

e1.agregar_nota(70)
e1.agregar_nota(80)

print(e1.promedio())
print(e1.aprobado())