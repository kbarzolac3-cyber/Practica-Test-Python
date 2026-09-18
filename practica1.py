class Notas:

    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas)


notas = Notas()

notas.agregar_nota(80)
notas.agregar_nota(90)
notas.agregar_nota(70)

print(notas.notas)
print(notas.promedio())