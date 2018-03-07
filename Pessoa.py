import csv

class Pessoa():
    def __init__(self, arquivo):
        self.arq = arquivo

        self.calcularIMC()
        self.calcularRCQ()

        self.atribTipoIMC()
        self.atribConjuntoTipoRCQ()

    def calcularIMC(self):
        self.IMC = round(self.peso / self.alt ** 2, 1)

    def calcularRCQ(self):
        self.RCQ = round(self.pem_c / self.pem_q, 2)

    def atribTipoIMC(self):
        list_tipoIMC = (('Abaixo do peso', 18.5), ('Peso normal', 25), ('Excesso de peso', 30),
                        ('Obesidade leve', 35), ('Obesidade severa', 40.1))

        self.tipoIMC = 'Obesidade mórbida'

        for tipo, num in list_tipoIMC:
            if self.IMC < num:
                self.tipoIMC = tipo
                break

    def atribConjuntoTipoRCQ(self):
        faixa_etaria = ["%.2f <29", "%.2f<39", "%.2f<49", "%.2f<59"]

        with open(self.arq) as csvfile:
            tipos = csv.DictReader(csvfile)

            for ind, x in enumerate(tipos):
                tiposRCQ = x
                if eval(faixa_etaria[ind] % self.idade):
                    break
        self.atribTipoRCQ(tiposRCQ)

    def atribTipoRCQ(self, tiposRCQ):

        self.tipoRCQ = "Risco Muito Alto"
        for tipo, num in sorted(tiposRCQ.items()):
            if self.RCQ < float(num):
                self.tipoRCQ = tipo
                break
