class Analizador:

    def __init__(self):
        self.numeros = []

    def es_positivo(self, numero):
        return numero >= 0

    def separar(self, *numeros):
        resultado = {
            "positivos": [],
            "negativos": []
        }

        for numero in numeros:
            self.numeros.append(numero)

            if self.es_positivo(numero):
                resultado["positivos"].append(numero)
            else:
                resultado["negativos"].append(numero)

        return resultado


a = Analizador()

print(a.separar(5, -2, 8, -1, 3))