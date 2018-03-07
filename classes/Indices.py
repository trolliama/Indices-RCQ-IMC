from Grafico import Grafico

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