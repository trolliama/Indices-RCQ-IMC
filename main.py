import tkinter as tk
from tkinter import filedialog as filed
from os import getcwd
import csv
from Homens import Homem
from Mulheres import Mulher
from RCQ import RCQ
from IMC import IMC


def callFuncs(lista, funcs, *args):
    for func in clss.RCQ.pickFuncs(lista, funcs, *args):
        func()


if __name__ == '__main__':

    root = tk.Tk()
    filetypes = [('arquivo CSV', '.csv'), ('arquivo TXT', '.txt')]

    arquivo = filed.askopenfilename(parent=root,
                                    initialdir=getcwd(),
                                    title='Selecione o arquivo:',
                                    filetypes=filetypes)

    lista_homens = []
    lista_mulheres = []

    with open(arquivo) as arq:
        readCSV = csv.reader(arq, delimiter=',')
        for dados_pessoa in readCSV:
            if dados_pessoa:
                if 'M' in dados_pessoa:
                    obj = Homem(dados_pessoa)
                    lista_homens.append(obj)
                else:
                    obj = Mulher(dados_pessoa)
                    lista_mulheres.append(obj)

    graf_IMC = IMC(lista_homens, lista_mulheres)
    graf_RCQ = RCQ(lista_homens, lista_mulheres)
