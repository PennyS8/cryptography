import math

def prime_factorization(n):
    factors = []
    # Handle the case when the number is divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # After the above loop, n must be odd.
    # We can start from 3 and iterate through odd numbers.
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is still greater than 2, it must be a prime number itself.
    if n > 2:
        factors.append(n)
    
    return factors

def euler_totient_function(n):
    """
    Calculates Euler's totient function (phi function) for a given positive integer.

    Parameters:
    n (int): The positive integer for which Euler's totient function will be calculated.

    Returns:
    int: The value of Euler's totient function for the input integer.

    Example:
    >>> euler_totient_function(10)
    4
    >>> euler_totient_function(12)
    4
    >>> euler_totient_function(17)
    16
    """
    factors = prime_factorization(n)    
    phi_n = n
    
    for factor in set(factors): # using set to avoid repeated factors
        phi_n *= (factor - 1) / factor

    return phi_n

def list_relative_primes(n):
    relative_primes = []
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            relative_primes.append(i)
    return relative_primes

# Example usage:
n = int(input('Enter a number: '))
'''
list = list_relative_primes(n)
print("List of numbers relatively prime to", n,
      "and smaller than", n, "is:", list_relative_primes(n))
'''
print("Prime factorization of", n, "is:", prime_factorization(n))

print("Euler's totient function value for", n,
      "is:", euler_totient_function(n))
