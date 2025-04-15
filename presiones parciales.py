import numpy as np
import math
e=math.e #exponencial
p=['N_2','O_2','Ar','CO_2','Ne','He'] #composiciones químicas del aire
fr=[0.7809,0.2093,0.0093,0.0003,0.000018,0.000005] #fracciones de los elementos de P en el aire
M=[0.0141,0.016,0.03995,0.04401,0.02018,0.004] #masas de los elementos en aire
g=9.81 #gravedad
R=8.3144 #constante de los gases
T=288.15 #temperatura ambiente 
z=693.42#altura en metros
po=101325 #presión atmosférica


A=[fr[i]*po*e**((-g*M[i]*z)/(R*T)) for i in range(6)]
s=sum(A)
print('presion parcial =',s)
