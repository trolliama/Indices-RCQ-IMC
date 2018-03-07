from Indices import Indices

class RCQ(Indices):
    def __init__(self, homens, mulheres):
        self.homens = homens
        self.mulheres = mulheres

        tiposRCQ = ("Normal", "Risco Alto", "Risco Muito Alto", "Risco Médio")

        Indices.__init__(self, tiposRCQ, 'RCQ')

