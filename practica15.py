class Numeros:

    def __init__(self):
        self.divisores = {}

    def encontrar(self, numero):
        resultado = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                resultado.append(i)

        return tuple(resultado)

    def es_perfecto(self, numero):
        divisores = self.encontrar(numero)

        suma = 0

        for divisor in divisores:
            if divisor != numero:
                suma += divisor

        return suma == numero


n = Numeros()

print(n.encontrar(6))
print(n.es_perfecto(6))