import math

def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:                                     
            return False
    return True

def print_primes(n):
    for num in range(2,n+1):
        if is_prime(num):
            print(num)
            
n = int(input())
print_primes(n)
        