
from matplotlib import pyplot as plt

#programa para tabular una función x^2#

print("Tabuladora de 5 valores de la función x^2")
X=[int(input("dame un numero")) for i in range(5)]
Y=[X[j]*X[j] for j in range(5)]

for k in Y:
    print(k)

Fig, ax=plt.subplots()
ax.scatter(X,Y)
ax.set_xlabel("Dominio")
ax.set_ylabel("Contradominio")
ax.set_title("F(x)=x^2")

plt.show()

    



    


