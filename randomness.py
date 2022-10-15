""" 
randomness is used for making a random number
in python, there're using Mersenne Twister algo to create randomness.
"""
from random import randrange, randint, random
# untuk membuat random number dari suatu range kita bisa menggunakan randrange
print(randrange(1, 20, 3))
print(randint(3, 40))
print(random())
print(round(random()))
