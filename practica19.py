class Almacen:

    def __init__(self):
        self.productos = {}

    def agregar(self, producto, cantidad):
        self.productos[producto] = cantidad

    def retirar(self, producto, cantidad):

        if producto in self.productos:

            if self.productos[producto] >= cantidad:
                self.productos[producto] -= cantidad
                return True

        return False

    def pocos(self, minimo):

        resultado = []

        for producto, cantidad in self.productos.items():

            if cantidad < minimo:
                resultado.append(producto)

        return resultado


a = Almacen()

a.agregar("Bread", 20)
a.agregar("Sugar", 5)

print(a.productos)

print(a.retirar("Bread", 10))

print(a.productos)

print(a.pocos(15))