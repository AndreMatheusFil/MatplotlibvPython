import matplotlib.pyplot as plt
from numpy import *

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 35, 30, 34, 27]
notas_2 = [25, 32, 32, 20, 26]

y = arange(len(legenda))
altura = 0.3

grafico1 = plt.barh(y - altura / 2, notas_1, height=altura, label='Notas P1', color='yellow')
grafico2 = plt.barh(y + altura / 2, notas_2, height=altura, label='Notas P2', color='cyan')
plt.xlabel('Pontos')
plt.title('Pontuação por aluno')
plt.yticks(y, legenda)
plt.legend()


def legenda_automatica(grafico):
    for i in grafico:
        comprimento = i.get_width()
        plt.annotate(f'{comprimento}', xy=(comprimento, i.get_y() + i.get_height() / 2), xytext=(10, -4),
                     textcoords='offset points', ha='center')


legenda_automatica(grafico1)
legenda_automatica(grafico2)
plt.show()

legenda = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
notas_1 = [20, 35, 30, 34, 27]
notas_2 = [25, 32, 32, 20, 26]
notas_3 = [28, 30, 34, 27, 22]

dados_zip = zip(legenda, notas_1, notas_2, notas_3)
y = arange(len(legenda))

dados_dict = {dados[0]: max(dados[1], dados[2], dados[3]) for dados in dados_zip}
print(dados_dict)

grafico1 = plt.barh(y,dados_dict.values(),height=altura,label='Maior nota', align='center',color='red')
plt.xlabel('Notas')
plt.title('Nota mais alta')
plt.yticks(y,dados_dict.keys())
legenda_automatica(grafico1)
plt.legend()
plt.show()