import matplotlib.pyplot as plt

nome = 'Calabresa','Marquerita','Caipira','Peruana'

valores = [2,2,2,2]
destaque = (0,0,0,0)
plt.pie(valores,explode=destaque,labels=nome, autopct='%1.2f%%',shadow=True,startangle=90)
plt.legend(nome,title='Sabores',loc='lower right')
plt.axis('equal') #Permite que a caixa da legenda se movimenta pelo tamanho
plt.title('Pizzas')
plt.show()


nome = 'Eduardo','Ana','Giovane','Daniel','Bruna','Luca','André'
valores = [100,120,90,95,80,80,200]
destaque = (0,0,0,0,0.1,0.1,0)

plt.pie(valores,explode=destaque,labels=nome, autopct='%1.2f%%',shadow=False,startangle=30)
plt.legend(nome,title='Apostadores',loc='upper right')
plt.axis('equal') #Permite que a caixa da legenda se movimenta pelo tamanho
plt.title('Bolão')
plt.show()
