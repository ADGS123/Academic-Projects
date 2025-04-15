from matplotlib import pyplot as py
import numpy as np
from vpython import*
grafica=graph(xtitle="posicion (rad)",ytitle="velocidad (rad/s)")
posicion=gcurve(color=color.blue)
h=0.01 # incremento del método de euler
g=9.81 #gravedad
l=0.5 #longitud del pendulo
x=pi/5 #ángulo
b=1.2 # coeficiente de amortiguamiento
v=0.0 #velocidad angular instantánea
def f(x,v): #Fuerza en la componente horizontal
    return(-g/l*sin(x)-b*v)

for t in range(1000): #metodo de euler
    v=v+f(x,v)*h
    x=x+v*h
    posicion.plot(pos=(x,v))
sleep(0)
