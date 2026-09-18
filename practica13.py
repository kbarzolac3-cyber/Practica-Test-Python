class Mezclador:

    def __init__(self):
        self.resultados = []

    def mezclar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def mezclar_muchas(self, *listas):
        resultado = list(listas[0])

        for lista in listas[1:]:
            resultado = self.mezclar(resultado, lista)

        return resultado


m = Mezclador()

print(m.mezclar(["A", "B"], ["C", "D"]))