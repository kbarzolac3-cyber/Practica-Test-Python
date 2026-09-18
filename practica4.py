class Inversor:

    def __init__(self):
        self.resultados = []

    def invertir(self, lista):
        resultado = []

        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])

        return resultado

    def invertir_muchas(self, *listas):
        resultado = {}

        for lista in listas:
            resultado[tuple(lista)] = self.invertir(lista)

        return resultado


i = Inversor()

print(i.invertir(["Mixi", "Matias", "Pedro"]))
print(i.invertir_muchas(["Mixi", "Matias"], ["Juan", "Kelly"]))