'''
Created on 22-10-2014

@author: Latino
'''
import math

lista=[]
lista2=[]

def funkcja_kwadratowa(a,b,c,x):
    y=a*x**2+b*x+c
    return lista2.append(y)

def delta(a,b,c):
    return b**2-4*a*c

def miejsca_zerowe(a,b,c):
    d = delta(a,b,c)
    if d>0:
        x1=(-float(b)-math.sqrt(d))/(2.0*float(a))
        x2=(-float(b)+math.sqrt(d))/(2.0*float(a))
        lista.append(x1)
        lista.append(x2) 
        return lista
    elif d<0:
        lista.append(None)
        return lista
    else:
        x=-b/(2*a)
        lista.append(x)
        return lista


miejsca_zerowe(1,0,1)
miejsca_zerowe(1,4,-8)
miejsca_zerowe(1,1,1)


print "Miejsca zerowe "+str(lista)
for x in xrange(-10,10):
    funkcja_kwadratowa(1, 1, 1, x)
print "Wartosci funkcji "+str(lista2)
    
    
    
    
