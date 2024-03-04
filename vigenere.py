from helper import convert_to_char, decrypt_with_shifts, calculate_shift, convert_to_index

def word_split(seq, split):
    """
    Split the input sequence into lines of a specified length, removing spaces.

    Args:
        seq (str): The input sequence to be split.
        split (int): The length of each line.

    Returns:
        None
    """
    # Remove spaces
    seq = seq.replace(" ", "")

    # Print out each line
    for i in range(split):
        print(seq[i::split])

def guessing_e(e):
    """
    Guess the key and decrypt the text using Caesar cipher.

    Args:
        e (list): A list of guesses for the Caesar cipher key.

    Returns:
        None
    """
    L = len(e)
    t = [0] * L  # Initialize an array of zeros with the same length as e
    loop = True

    while loop:
        for i in range(L):
            print(convert_to_char(e[i][t[i]], 0), end="")
        print()
        for i in range(L):
            print(convert_to_char(e[i][t[i]], 1), end="")
        print()

        # Check if all positions have been iterated through
        if all(t[i] >= len(e[i]) - 1 for i in range(L)):
            loop = False
        else:
            # Increment the current position or reset if at the end
            for i in range(L):
                if t[i] < len(e[i]) - 1:
                    t[i] += 1
                    break
                else:
                    t[i] = 0

if __name__ == '__main__':
    # Input sequence and key length
    seq = "TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z"
    key_length = 7

    # Split the sequence into lines
    print("Sequence split into lines:")
    word_split(seq, key_length)

    # Guess the key and decrypt the text
    print("\nDecryption with guessed key:")
    e = [[19], [7], [4], [14], [17], [4], [12]]  # Guesses for the Caesar cipher key
    guessing_e(e)

    # Guessing for decryption with a fixed key
    print("\nDecryption with fixed key:")
    e = [['x'], ['b'], ['b'], ['b'], ['b'], ['b'], ['b']]  # Fixed key for decryption
    guessing_e(e)

    # Calculate the shift for two characters
    print("\nShift between 'e' and 'a':", calculate_shift('e', 'a'))
