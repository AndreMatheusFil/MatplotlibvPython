import matplotlib.pyplot as plt
from numpy import *

legenda = ['Aluno1','Aluno2','Aluno3','Aluno4','Aluno5']
notas=[20,34,30,32,27]
notas2=[25,32,23,28,35]

x = arange(len(legenda))
largura = 0.3

grafico1 = plt.bar(x-0.15,notas,width=largura,label='Notas P1',color='purple')
grafico2 = plt.bar(x+0.15,notas2,width=largura,label='Notas P2',color='green')
plt.ylabel('Pontos')
plt.title('Pontuação por aluno')
plt.xticks(x,legenda)
plt.legend()
def legenda_automatica(grafico):
    """"Adiciona a legenda acima da coluna do grafico de acordo com a altura dele"""
    for i in grafico:
        altura = i.get_height()
        plt.annotate(f'{altura}',xy=(i.get_x()+i.get_width()/2,altura),xytext=(0,2),textcoords='offset points',ha='center')

legenda_automatica(grafico1)
legenda_automatica(grafico2)

plt.show()