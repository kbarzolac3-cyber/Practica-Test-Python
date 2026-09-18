import math

class Distancia:

    def __init__(self):
        self.distancias = []

    def calcular(self, punto1, punto2):

        x1 = punto1[0]
        y1 = punto1[1]

        x2 = punto2[0]
        y2 = punto2[1]

        distancia = math.sqrt(
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        )

        self.distancias.append(distancia)

        return distancia


d = Distancia()

print(d.calcular((0, 0), (3, 4)))