
import numpy as np
import matplotlib.pyplot as plt

X=np.array([1,2,3,4,5])
Y=np.array([1,4,9,16,25])
dX=0.5
dY=0.2

Fig, ax=plt.subplots()
ax.scatter(X,Y)
ax.errorbar(X,Y,yerr=dY,xerr=dX,capsize=5,elinewidth=1,
            linewidth=0,marker='o',markerfacecolor='r',label='puntos esperimentales')
ax.set_xlabel('Tiempo(s)')
ax.set_ylabel('Posicion(m)')
ax.set_xlim(0,10)
ax.set_ylim(0,30)
ax.set_title("Crecimiento cuadrático")
ax.legend(loc='upper left')
plt.show()

