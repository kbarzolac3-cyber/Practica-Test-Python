class Codigo:

    def __init__(self):
        self.historial = {}

    def cambiar_letra(self, letra, desplazamiento):
        posicion = ord(letra.lower()) - ord("a")
        nueva = (posicion + desplazamiento) % 26

        return chr(ord("a") + nueva)

    def cambiar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.cambiar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


c = Codigo()

print(c.cambiar_palabra("casa", 2))
print(c.historial)