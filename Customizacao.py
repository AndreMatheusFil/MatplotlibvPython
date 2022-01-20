import matplotlib.pyplot as plt
from numpy import *

t = arange(0.01, 10, 0.01)
dados1 = exp(t)
dados2 = sin(2 * pi * t)

plt.plot(t, dados1, color='red', label='exp(t)')
plt.yscale('log')
plt.xlabel('tempo(s)')
plt.ylabel('exp(t)', color='red')
plt.tick_params(axis='y', labelcolor='red')  # muda a cor dos dados do eixo escolhido
plt.legend()

plt.twinx()  # permite a duplicação do eixo X
plt.plot(t, dados2, color='blue', label='sen(2$\pi$t)')
plt.ylabel('sin(t)', color='blue')
plt.tick_params(axis='y', labelcolor='blue')
plt.title('Gráficos em função do tempo')
plt.legend()
plt.show()

t = arange(0.01, 5, 0.01)
s = cos(2 * pi * t)

plt.plot(t, s, label='cos(2$\pi$t)', color='orange')
plt.annotate('Valor maximo', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='Black', shrink=0.1))
plt.legend()
plt.title('Função cosseno')
plt.ylim(-2, 2)
plt.show()
