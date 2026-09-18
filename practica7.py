class Mascotas:

    def __init__(self):
        self.mascotas = {}

    def agregar(self, nombre, edad):
        self.mascotas[nombre] = edad

    def mayores(self, edad):
        resultado = []

        for nombre, edad_mascota in self.mascotas.items():
            if edad_mascota >= edad:
                resultado.append(nombre)

        return resultado

    def promedio(self):
        return sum(self.mascotas.values()) / len(self.mascotas)


m = Mascotas()

m.agregar("Kaory", 5)
m.agregar("Max", 2)
m.agregar("Laica", 7)

print(m.mascotas)
print(m.mayores(5))
print(m.promedio())