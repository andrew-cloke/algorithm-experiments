# python program to print prime factors
 
import math

def primefactors(n):
   #even number divisible
   while n % 2 == 0:
      print (2),
      n = n / 2
    
   # n became odd
   # Go through the seq 3,5,7,9,11,13,15, etc looking for divisibility
   # Don't worry about the fact that 9,15, etc aren't prime,
   # n can't be divisible by them, as their prime factors will already have been found and "removed"
   for i in range(3,int(math.sqrt(n))+1,2):
     
        while (n % i == 0):
            print (i)
            n = n / i
    
   if n > 2:
      print (n)
 
n = int(input("Enter the number for calculating the prime factors :\n"))
primefactors(n)
