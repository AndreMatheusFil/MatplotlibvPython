import matplotlib.pyplot as plt
from numpy import *

n= 10000000
n_colunas = 50
x = random.randn(n)

plt.hist(x, bins=n_colunas,density=False,histtype='bar',color='purple',label='Histograma X')
plt.legend()
plt.ylabel('Número de Ocorrencia')
plt.title('Histograma')
plt.show()



plt.hist(x, bins=n_colunas,density=False,histtype='bar',color='purple',label='Histograma X')

n2 = 5000000
y = 10 + random.randn(n2)
plt.hist(y,bins=n_colunas,density=False,histtype='bar',color='yellow',label='Histograma Y')

plt.legend()
plt.ylabel('Número de Ocorrencia')
plt.title('Histograma')
plt.show()

