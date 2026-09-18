class Cursos:

    def __init__(self):
        self.cursos = {}

    def crear(self, curso):
        self.cursos[curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor(self):
        mayor = ""
        cantidad = 0

        for curso, estudiantes in self.cursos.items():
            if len(estudiantes) > cantidad:
                cantidad = len(estudiantes)
                mayor = curso

        return mayor


c = Cursos()

c.crear("Python")
c.crear("Java")

c.agregar_estudiante("Python", "Ana")
c.agregar_estudiante("Python", "Luis")
c.agregar_estudiante("Java", "Pedro")

print(c.cursos)
print(c.curso_mayor())