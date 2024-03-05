import helper
import RSA_system as rsa

CONSTANT_MODE = 1

def word_split(sequence, length):
    # Print out each line
    for i in range(length):
        print(sequence[i::length])

def solve_vigenere(ciphertext):
    # Remove spaces
    clean_text = helper.clean_text(ciphertext)[0]
    
    IC = rsa.calculate_IC(clean_text)
    n = len(clean_text)
    r = rsa.estimate_keyword_length(n, IC)

    print(f'Ciphertext: \n\t{ciphertext}\n')
    print(f'IC = {IC}')
    print(f'n = {n}')
    print(f'r = {r}')
    print(f'\n{word_split(clean_text, r)}\n')

if __name__ == '__main__':
    ciphertext = 'TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z'
    solve_vigenere(ciphertext)
