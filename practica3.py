class Libros:

    def __init__(self):
        self.libros = {}

    def agregar(self, nombre, precio):
        self.libros[nombre] = precio

    def total(self):
        total = 0

        for precio in self.libros.values():
            total += precio

        return total

    def buscar(self, minimo, maximo):
        resultado = []

        for nombre, precio in self.libros.items():
            if minimo <= precio <= maximo:
                resultado.append(nombre)

        return resultado


l = Libros()

l.agregar("La culpa es de la vaca", 10)
l.agregar("Abitos Atomicos", 15)
l.agregar("Mujercitas", 8)

print(l.libros)
print(l.total())
print(l.buscar(8, 10))