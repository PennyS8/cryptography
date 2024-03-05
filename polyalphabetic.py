import RSA_system as rsa
import helper
import math

# Defines the letter to number assignment starting with a = constant_mode
CONSTANT_MODE = 1

def word_split(sequence, length):
    separated_rows = []
    
    for i in range(length):
        separated_rows.append(sequence[i::length])
    
    return separated_rows

def calc_keyword_length(n, IC):
    return math.ceil((0.027*n) / ((IC * (n-1)) - (0.038*n) + 0.065))

def estimate_keyword_length(ciphertext):
    return

def find_vigenere_keyword(cipher_square, mappings, r):
    keyword = ''
    for i in range(r):
        column = [row[i] for row in cipher_square]
        most_common_letter = max(column, key=column.count)
        plaintext_char = mappings[most_common_letter]
        keyword += plaintext_char
    
    return keyword

def solve_polyalphabetic(ciphertext):
    # Removes all non-alpha characters and preserves punctutation in a list
    clean_text = helper.clean_text(ciphertext)[0]

    IC = rsa.calculate_IC(clean_text)
    n = len(clean_text)
    r_calculated = calc_keyword_length(n, IC)

    # cipher_square referes to the ciphertext being displayed in
    # a matrix size [r rows][n/r columns]
    cipher_square = word_split(clean_text, r_calculated)
    
    r_estimate = estimate_keyword_length(clean_text)

    print(f'Ciphertext: \n\t{ciphertext}\n')
    print(f'IC = {IC}')
    print(f'n = {n}')
    print(f'r = {r}\n')
    
    for row in cipher_square:
        line = ''
        for col in row:
            line += col + ' '
        print(line)

    decrypted = False
    while not decrypted:
        
        # Ask user for their guesses of ciphertext to plaintext mappings
        mappings = {}
        while len(mappings) < 2:
            cipher_char = input('\nEnter the ciphertext letter: ')

            if not cipher_char.isalpha():
                print('Invalid input. Please enter a valid ciphertext letter.')
                continue
            if not len(cipher_char) == 1:
                print('Invalid input. Please enter a single character.')
                continue

            plain_char = input(f'Enter your guess for the plaintext letter corresponding to {cipher_char}: ').strip().upper()
            mappings[(ord(cipher_char)-96-1) % 26] = (ord(plain_char)-96-1) % 26

        try:
            # Calculate the vigenere keyword
            # NOTE: this solves for the decryption key NOT the encryption key
            keyword = find_vigenere_keyword(cipher_square, mappings, r)
        except ValueError:
            print('\nError: ...')
            print('Try different mappings.')
            continue

if __name__ == '__main__':
    ciphertext = 'TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z'
    solve_polyalphabetic(ciphertext)
