class Rangos:

    def __init__(self):
        self.rangos = []

    def crear(self, inicio, fin):
        numeros = []

        for numero in range(inicio, fin + 1):
            numeros.append(numero)

        return tuple(numeros)

    def unir(self, *rangos):
        resultado = set()

        for rango in rangos:
            for numero in range(rango[0], rango[1] + 1):
                resultado.add(numero)

        return list(resultado)


r = Rangos()

print(r.crear(1, 4))
print(r.unir((1, 3), (3, 5)))