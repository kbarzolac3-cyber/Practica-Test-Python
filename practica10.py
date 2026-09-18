class Compras:

    def __init__(self):
        self.compras = []

    def agregar(self, producto, cantidad):
        self.compras.append((producto, cantidad))

    def mayores(self):
        resultado = []

        for compra in self.compras:
            if compra[1] >= 3:
                resultado.append(compra)

        return resultado

    def eliminar(self, producto):
        for compra in self.compras:
            if compra[0] == producto:
                self.compras.remove(compra)
                return


c = Compras()

c.agregar("Bread", 5)
c.agregar("Milk", 2)
c.agregar("Rice", 4)

print(c.compras)
print(c.mayores())

c.eliminar("Bread")

print(c.compras)