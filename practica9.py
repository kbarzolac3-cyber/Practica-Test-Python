class Letras:

    def __init__(self):
        self.texto_largo = ""

    def es_vocal(self, letra):
        return letra.lower() in "aeiou"

    def contar(self, texto):
        vocales = 0
        consonantes = 0
        numeros = 0

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        for letra in texto:

            if letra.isdigit():
                numeros += 1

            elif letra.isalpha():

                if self.es_vocal(letra):
                    vocales += 1
                else:
                    consonantes += 1

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "numeros": numeros
        }


l = Letras()

print(l.contar("Casa123"))
print(l.texto_largo)