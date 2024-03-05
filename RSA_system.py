import math
import helper

def prime_factorization(n):
    '''
    returns the list of primes who's total product is n
    '''
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
    '''
    Calculates Euler's totient function (phi function)
    for a given positive integer

    Parameters:
        n: Positive integer
    Returns:
        int: Value of the Euler's totient function of n
    Example:
        euler_totient_function(10)
        factors of 10: 1, 2, 5
        10 * (1 - (1/2)) * (1 - (1/5)) = 4
    '''
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

def expected_num_identical_pairs(message_length, keyword_length):
    if message_length <= 0:
        raise ValueError('Invalid "message_length" in RSA_system.py:\n' +
                         '\texpected_num_identical_pairs(), "message_length" must be > 0.')
    if keyword_length <= 0:
        raise ValueError('Invalid "keyword_length" in RSA_system.py:\n' +
                         '\texpected_num_identical_pairs(), "keyword_length" must be > 0.')

    n, r = message_length, keyword_length
    k = (0.065 * n * (n-r) / (2*r)) + (0.038 * n^2 * (r-1)) / (2*r)

    return k

def friedman_test(IC):
    '''
    Perform the Friedman Test to estimate the probable key type (monoalphabetic or polyalphabetic)
    and the key length for a ciphertext given its Index of Coincidence (IC).

    Parameters:
    IC (float): The Index of Coincidence (IC) of the ciphertext.

    Returns:
    tuple: A tuple containing two elements:
           - A string indicating the probable key type: 'poly' for polyalphabetic or 'mono' for monoalphabetic.
           - A float indicating the estimated key length based on the Friedman Test.
    '''
    rtn = ''
    K = (0.065-0.038) / (0.038-IC)

    if abs(K - 0.065) >= abs(K - 0.038):
        rtn = 'mono'
    else:
        rtn = 'poly'

    return rtn, K

def calculate_IC(ciphertext):
    total_characters = len(ciphertext)
    frequency = {}
    IC_sum = 0 # index of coincidence
    
    # Count the occurrences of each letter
    for char in ciphertext:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    # Calculate the Index of Coincidence
    for count in frequency.values():
        IC_sum += count * (count - 1)

    IC = IC_sum / (total_characters * (total_characters - 1))

    return IC

def estimate_keyword_length(n, IC):
    return math.ceil((0.027*n) / ((IC * (n-1)) - (0.038*n) + 0.065))

def main(ciphertext):

    print(f'Input Ciphertext:\n\t{ciphertext}')
    
    clean_text = helper.clean_text(ciphertext)
    n = len(clean_text)
    IC = calculate_IC(clean_text)
    K = friedman_test(IC) # returns ((string) ['mono'/'poly'], (long) K)

    print(f'Message without spacing: \n\t {clean_text}')
    print(f'Message length: {n}')
    print(f'Index of Coincidence: {IC}')

    print(f'Prime factorization of {n}:', prime_factorization(n))

    print(f'Euler\'s totient function value for {n}:', int(euler_totient_function(n)))

    print(f'Friedman test: K = {K[1]}, likely an {K[0]}alphabetic cipher.')

if __name__ == '__main__':
    ciphertext = 'TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z'
    main(ciphertext)