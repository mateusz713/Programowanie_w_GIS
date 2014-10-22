'''
Created on 22-10-2014

@author: Latino
'''
import string

zdanieWynikowe=""

def Palindrom(zdanie=""):
    global zdanieWynikowe
    zdanie.replace(" ", "")
    zdanieWynikowe = zdanie
    return zdanieWynikowe


Palindrom("   aaa   bbb ccc ddd")
print zdanieWynikowe


aaa="AAA bbb ccc"
print aaa
aaa.replace(" ", "")
print aaa