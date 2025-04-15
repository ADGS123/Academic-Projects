
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
R=8.314 #constante de los gases
Tc= 304.1 #temperatura crítica
Pc=7.38e6 #presión crítica

#constantes de Van der Waals
a=(27/64)*Tc**2*R**2/Pc 
b=(R*Tc)/(8*Pc)

def Pvw(T,Vm): #ecuación de Van der Waals
    Pvw=R*T/(Vm-b)-a/(Vm**2)
    return Pvw

fig=plt.figure(1) #gráfica de las isotermas
for T in np.array([243,258,274,304]): #para cada temperatura
    Vm=np.logspace(np.log10(b*1.01),2+np.log10(R*Tc/Pc),100) #volumen en escala logaritmica para visualizar
    plt.semilogx(Vm,Pvw(T,Vm),label=str(T)+"K") #graficación
    plt.title("Isotermas de Van der Waals-C02")
    plt.ylabel(r"${P(\mathrm{Pa})}$")
    plt.xlabel(r"$\bar{V}(\mathrm{m^{3}mol^{-1}})$")
    plt.ylim(-1*Pc,Pc*3)
    plt.xlim(b,(100*R*Tc/Pc))

#4.82e+06,4.26e+06,3.30e+06#
    
#líneas horizontales marcando las "zonas prohibidas" y los puntos mestaestables de las isotermas
#Una línea para cada isoterma    
xdata = list(range(10))
ydata = [_*2 for _ in xdata]
plt.plot(xdata, ydata, 'b')
plt.axhline(y=4.82e+06, xmin=0.08, xmax=0.48, color="black")
plt.grid()

xdata = list(range(10))
ydata = [_*2 for _ in xdata]
plt.plot(xdata, ydata, 'b')
plt.axhline(y=3.91e+06, xmin=0.06, xmax=0.5, color="yellow")
plt.grid()


xdata = list(range(10))
ydata = [_*2 for _ in xdata]
plt.plot(xdata, ydata, 'b')
plt.axhline(y=3.01e+06, xmin=0.04, xmax=0.6, color="purple")
plt.grid()

#muestra los gráficos
plt.legend()

plt.show()
