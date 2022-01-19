import matplotlib.pyplot as plt

def func_terc_grau(x,a=1,b=1,c=1,d=1):
    y = a*x**3+b*x**2+c*x+d
    return y

list_x = range(-5,5,1)
list_y = []
for i in list_x:
    list_y.append(func_terc_grau(i))

plt.plot(list_x,list_y,color="g",label= "função de f(x)") #grafico linha
plt.scatter(list_x,list_y) #grafico bolinha
plt.legend()
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.title("Função do terceiro grau")
plt.show()