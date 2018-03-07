from Pessoa import Pessoa

class Mulher(Pessoa):
    """construtor do objeto mulher,questão de organização"""
    def __init__(self, args):
        self.sexo = args[0]
        self.idade, self.peso, self.alt, self.pem_c, self.pem_q = list(map(float, args[1:]))

        Pessoa.__init__(self, 'Tabelas_RCQ/RCQ-FEMININO.csv')