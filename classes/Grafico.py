import matplotlib.pyplot as plt

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