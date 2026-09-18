class Estudiantes:

    def __init__(self):
        self.notas = {}

    def registrar(self, nombre, nota):
        self.notas[nombre] = nota

    def aprobados(self):
        resultado = []

        for nombre, nota in self.notas.items():
            if nota >= 70:
                resultado.append(nombre)

        return resultado

    def mejor(self):
        mejor = None
        nota_mayor = 0

        for nombre, nota in self.notas.items():
            if nota > nota_mayor:
                nota_mayor = nota
                mejor = nombre

        return (mejor, nota_mayor)


e = Estudiantes()

e.registrar("Karla", 90)
e.registrar("Leo", 60)
e.registrar("Mixi", 80)

print(e.notas)
print(e.aprobados())
print(e.mejor())