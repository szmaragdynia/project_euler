'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


#this worked, but it was too painfully inefficient to use that function here, even though I wanted to be lazy. But I just could.not.do.that.
#from importlib import import_module
#mymethod = getattr(import_module("3"), "generate_primes")
#print(mymethod(10))

#todo: code below is very bad. Look&learn: https://en.wikipedia.org/wiki/Primality_test
'''
import numpy as np

def findPrimesBelow(treshold, output_primes = []):
    if treshold <= 2:
        return "There are no primes smaller than 2. Error."

    output_primes_size = len(output_primes)
    if output_primes_size == 0:
        output_primes.append(2)                 #add first prime number manually
    
    suspected_prime = 2                         #to start with 2(!)
    while output_primes[-1] < treshold:         #while last added prime is still lower than the threshold below which to look for 
        for prime in output_primes:
            if suspected_prime % prime == 0:    #if new number is divisible by some prime
                break                           #leave for loop, and increment again
        else:                                   #if no known primes divided "suspected_prime" ; executes after the loop completes normally
            output_primes.append(suspected_prime) 
        suspected_prime+=1
    else: 
        output_primes.pop()                     #last element was above threshold
    return output_primes

primes = findPrimesBelow(2000000)
#print(primes) 

sum = np.sum(primes)
print(sum)
'''