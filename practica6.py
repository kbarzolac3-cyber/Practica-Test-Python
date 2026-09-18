class Calificaciones:

    def __init__(self):
        self.calificaciones = []

    def agregar(self, *notas):
        for nota in notas:
            self.calificaciones.append(nota)

    def mayor(self):
        return max(self.calificaciones)

    def menor(self):
        return min(self.calificaciones)

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


c = Calificaciones()

c.agregar(80, 90, 70, 85)

print(c.calificaciones)
print(c.mayor())
print(c.menor())
print(c.promedio())