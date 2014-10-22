'''
Created on 22-10-2014

@author: Latino
'''
wynik=[]
def Usun_duplikat(duplikat=[]):
    global wynik
    wynik=list(set(duplikat))
    return wynik

Usun_duplikat(['kot','pies','kot','baba'])
print wynik