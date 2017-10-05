import matplotlib.pyplot as plt
import csv


class Grafico:

    def saveGraf(self, lista, title, tipos):

        local_tipos = []
        lista_combinada = list(zip(tipos, lista))
        cols = ['yellow', 'orange', 'b', 'g', 'r', 'silver']
        for tipo, pct in lista_combinada:
            if pct:
                local_tipos.append(tipo)
            else:
                lista.remove(0)
        plt.pie(lista, startangle=90, shadow=True, autopct='%1.1f%%',
                colors=cols[:len(tipos)])
        plt.axis('equal')

        plt.title(title)
        plt.legend(labels=local_tipos)
        plt.savefig('Gráficos/' + title + '.png')

        plt.close()


class Indices(Grafico):
    def __init__(self, tipos, ind):
        self.ind = ind
        self.tipos = tipos

        self.dicQnt_tipo = {k: [0, 0] for k in tipos}

        if self.homens:
            self.calcQntTipoHomem()

        if self.mulheres:
            self.calcQntTipoMulher()

    def calcQntTipoHomem(self):
        for homem in self.homens:
            self.dicQnt_tipo[getattr(homem, 'tipo'+self.ind)][0] += 1
        self.listaPctHomem()

    def calcQntTipoMulher(self):
        for mulher in self.mulheres:
            self.dicQnt_tipo[getattr(mulher, 'tipo'+self.ind)][1] += 1
        self.listaPctMulher()

    def listaPctMulher(self):
        pct_mulher = []

        for k, v in sorted(self.dicQnt_tipo.items()):
            m = v[1]
            pct_mulher.append((m * 100) / len(self.mulheres))

        Grafico.saveGraf(self, pct_mulher, self.ind+' - FEMININO', self.tipos)

    def listaPctHomem(self):
        pct_homem = []

        for k, v in sorted(self.dicQnt_tipo.items()):
            h = v[0]
            pct_homem.append((h * 100) / len(self.homens))

        Grafico.saveGraf(self, pct_homem, self.ind+' - MASCULINO', self.tipos)


class RCQ(Indices):
    def __init__(self, homens, mulheres):
        self.homens = homens
        self.mulheres = mulheres

        tiposRCQ = ("Normal", "Risco Alto", "Risco Muito Alto", "Risco Médio")

        Indices.__init__(self, tiposRCQ, 'RCQ')


class IMC(Indices):
    def __init__(self, homens, mulheres):
        self.homens = homens
        self.mulheres = mulheres

        tiposIMC = ("Abaixo do peso", "Excesso de peso", "Obesidade leve",
                    "Obesidade mórbida", "Obesidade severa", "Peso normal")

        Indices.__init__(self, tiposIMC, 'IMC')


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


class Mulher(Pessoa):
    """construtor do objeto mulher,questão de organização"""
    def __init__(self, args):
        self.sexo = args[0]
        self.idade, self.peso, self.alt, self.pem_c, self.pem_q = list(map(float, args[1:]))

        Pessoa.__init__(self, 'Tabelas_RCQ/RCQ-FEMININO.csv')


class Homem(Pessoa):
    """construtor do objeto homem,questão de organização"""
    def __init__(self, args):
        self.sexo = args[0]
        self.idade, self.peso, self.alt, self.pem_c, self.pem_q = list(map(float, args[1:]))

        Pessoa.__init__(self, 'Tabelas_RCQ/RCQ-MASCULINO.csv')
