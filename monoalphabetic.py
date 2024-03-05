import helper

def solve_affine(mappings):
    x1, y1 = list(mappings.keys())[0], mappings[list(mappings.keys())[0]]
    x2, y2 = list(mappings.keys())[1], mappings[list(mappings.keys())[1]]

    # Calculate a
    x_diff = x2 - x1
    if x_diff < 0:
        x_diff += 26  # Ensure x_diff is positive within Z26
    inv_x_diff = helper.modular_inverse(x_diff, 26)
    a = (y2 - y1) * inv_x_diff % 26

    # Calculate b
    b = (y1 - (a*x1)) % 26

    return a, b

def solve_monoalphabetic(ciphertext):
    
    # Print monographs and digraphs
    helper.print_monographs(ciphertext)
    helper.print_digraphs(ciphertext)
    helper.print_trigraphs(ciphertext)
    
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
            # Calculate the affine key (a, b)
            a, b = solve_affine(mappings)
        except ValueError:
            print('\nError: The selected mappings result in a non-invertible base for the affine cipher calculation.')
            print('Try different mappings.')
            continue

        # Decrypt the ciphertext using the affine key
        cipher_nums = helper.string_to_num_list(helper.clean_text(ciphertext)[0], 1)
        plain_nums = []
        for num in cipher_nums:
            plain_nums.append(((a*num) + b) % 26)
        plaintext = helper.num_list_to_string(plain_nums, 1)

        # Print the affine key and decrypted plaintext
        print(f'\nAffine Key: ({a}*x) + {b}')
        print(f'Decrypted plaintext:\n\t{plaintext}')

        result = input('Is the above a valid english sentence? (yes/no): ')
        if result == 'yes':
            decrypted = True
        elif result == 'quit':
            break

    return

if __name__ == '__main__':
    ciphertext = 'EXD UUT JZE JEL LXU GCJ CPQ CRJ QWQ DGE DQC RJQ DQG JCR WEG GMO QJZ QKU RJD EDY JZQ RHY JZQ SQL LUD NQD CRW XDC RKC XLQ JZQ DQC GEL USQ GJR URC RJQ DQG JCR WXU GCJ CPQ CRJ QWQ DHM JZQ YJZ EJG XDQ JJY CRJ QDQ GJC RWE KUR JDE NCK JCU R'
    solve_monoalphabetic(ciphertext)
