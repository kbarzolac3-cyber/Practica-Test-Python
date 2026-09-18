class Buscador:

    def __init__(self):
        self.palabras = []

    def buscar(self, texto, inicio):

        resultado = []

        for palabra in texto.split():

            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def agrupar(self, texto):

        resultado = {}

        for palabra in texto.split():

            largo = len(palabra)

            if largo not in resultado:
                resultado[largo] = []

            resultado[largo].append(palabra)

        return resultado

    def unicas(self):

        return set(self.palabras)


b = Buscador()

texto = "casa carro perro casa"

print(b.buscar(texto, "ca"))

print(b.agrupar(texto))

b.palabras = texto.split()

print(b.unicas())