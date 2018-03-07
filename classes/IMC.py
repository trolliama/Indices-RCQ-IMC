from Indices import Indices

class IMC(Indices):
    def __init__(self, homens, mulheres):
        self.homens = homens
        self.mulheres = mulheres

        tiposIMC = ("Abaixo do peso", "Excesso de peso", "Obesidade leve",
                    "Obesidade mórbida", "Obesidade severa", "Peso normal")

        Indices.__init__(self, tiposIMC, 'IMC')