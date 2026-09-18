class Frutas:

    def __init__(self):
        self.frutas = []
        self.unicas = set()

    def agregar(self, fruta):
        self.frutas.append(fruta)
        self.unicas.add(fruta)

    def agregar_muchas(self, *frutas):
        for fruta in frutas:
            self.agregar(fruta)

    def cantidad(self):
        return len(self.unicas)


f = Frutas()

f.agregar_muchas("manzana", "pera", "manzana", "uva")

print(f.frutas)
print(f.unicas)
print(f.cantidad())