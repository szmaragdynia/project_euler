'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# is there non-brute-force approach? (at least not so much)

from importlib import import_module

mymethod = getattr(import_module("3"), "generate_primes")

#import_module('3','generate_primes')

#from three import generate_primes

#generate_primes(3)

