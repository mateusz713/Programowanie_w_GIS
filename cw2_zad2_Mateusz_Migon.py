'''
Created on 22-10-2014

@author: Latino
'''
import string
import types

zdanieWynikowe=""

def Palindrom(zdanie=""):
    print "Wyrazenie: " +zdanie
    global zdanieWynikowe
    zdanieWynikowe = zdanie
    zdanieWynikowe=zdanieWynikowe.replace(" ", "")
#    i=len(zdanieWynikowe)/2
#    while i:
#        i-=1
#        if zdanieWynikowe[i] != zdanieWynikowe[-i-1]:
#            print False
#        else:
#            print True
    if zdanieWynikowe[::-1] == zdanieWynikowe:
        print True
        print "Jest palindromem"
    else:
        print False 
        print "Nie jest palindromem"
        
    return zdanieWynikowe


Palindrom("aaa bbbb aaa")

