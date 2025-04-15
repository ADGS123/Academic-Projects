

a=float(input('dame el valor de a')) #medicion 1
da=float(input('dame el valor de da')) #incertidumbre de la medicion 1
b=float(input('dame el valor de b')) #medicion 2
db=float(input('dame el valor de db'))#incertidumbre de la medición 2
c=a*b #producto de mediciones
dc=a*db+b*da #incertidumbre del producto
print('%f+-%f'%(c,dc))
