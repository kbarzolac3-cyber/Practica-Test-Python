class Clasificador:

    def __init__(self):
        self.grupos = {
            "niño": [],
            "joven": [],
            "adulto": []
        }

    def clasificar(self, edad):

        if edad < 13:
            return "niño"

        elif edad < 18:
            return "joven"

        else:
            return "adulto"

    def agrupar(self, *edades):

        for edad in edades:
            grupo = self.clasificar(edad)
            self.grupos[grupo].append(edad)

        return self.grupos


c = Clasificador()

print(c.agrupar(10, 15, 20, 30))