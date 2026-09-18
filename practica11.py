class Contador:

    def __init__(self):
        self.datos = {}

    def agregar(self, dato):
        if dato in self.datos:
            self.datos[dato] += 1
        else:
            self.datos[dato] = 1

    def mas_repetido(self):
        mayor = 0
        resultado = None

        for dato, cantidad in self.datos.items():
            if cantidad > mayor:
                mayor = cantidad
                resultado = dato

        return resultado

    def frecuencia(self, dato):
        if dato in self.datos:
            return self.datos[dato]

        return 0


c = Contador()

c.agregar("Pink")
c.agregar("Blue")
c.agregar("Pink")
c.agregar("Pink")

print(c.datos)
print(c.mas_repetido())
print(c.frecuencia("Pink"))