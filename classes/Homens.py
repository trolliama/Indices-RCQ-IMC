from Pessoa import Pessoa

class Homem(Pessoa):
    """construtor do objeto homem,questão de organização"""
    def __init__(self, args):
        self.sexo = args[0]
        self.idade, self.peso, self.alt, self.pem_c, self.pem_q = list(map(float, args[1:]))

        Pessoa.__init__(self, 'Tabelas_RCQ/RCQ-MASCULINO.csv')