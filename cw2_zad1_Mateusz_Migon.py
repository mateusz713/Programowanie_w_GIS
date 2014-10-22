'''
Created on 22-10-2014

@author: Latino
'''

def FizzBuzz(n):
    a=1
    while a<n:
        if a%3==0 and a%5==0:
            print "Fizz Buzz"
            a+=1
        elif a%5==0:
            print "Buzz"
            a+=1
        elif a%3==0:
            print "Fizz"
            a+=1
        else:
            print str(a)
            a+=1
            
FizzBuzz(20)