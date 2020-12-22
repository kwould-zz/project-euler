"""
largest prime,

a prime means that no number below it is a factor
we can iterate through primes 
"""

def main(num):
    factors = []
    d = 2
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num /= d
        d = d + 1
    print(max(factors))


main(600851475143)