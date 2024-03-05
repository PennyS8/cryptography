import string

def modular_inverse(n, m):
    """
    Calculate the modular multiplicative inverse of n modulo m.
    """
    for i in range(m):
        if (n*i) % m == 1:
            return i
    raise ValueError("Modular inverse does not exist.")

def num_list_to_string(number_list, mode):
    # Validate input
    if not mode == 0 and not mode == 1:
        raise ValueError('Invalid mode. Mode must be 0 or 1.')

    string = ''
    for num in number_list:
        ascii = num + 96 + mode
        if ascii == 96:
            ascii += 26
        string += chr(ascii)
    
    return string

def string_to_num_list(string, mode):
    if not mode == 0 and not mode == 1:
        raise ValueError('Invalid mode. Mode must be 0 or 1.')

    number_list = []
    for char in string:
        letter = char.lower()
        number_list.append((ord(letter) - 96 - mode) % 26)
    
    return number_list

def clean_text(text):
    cleaned_text = ''
    punctuation_list = []

    for char in text:
        if char.isalpha():
            cleaned_text += char
            punctuation_list.append(None)
        elif char in string.punctuation:
            punctuation_list.append(char)

    return cleaned_text, punctuation_list

def print_plaintext(text, punctuation_list):
    modified_text = ''

    for i, char in enumerate(text):
        if not punctuation_list[i] == None:
            modified_text += punctuation_list[i]
        else:
            modified_text += char

    plaintext = modified_text.lower()
    print(plaintext)

def print_monographs(ciphertext):
    # Count occurrences of each letter in the plaintext
    plaintext_counts = {chr(letter): 0 for letter in range(ord('A'), ord('Z') + 1)}
    for char in ciphertext:
        if char.isalpha():
            plaintext_counts[char] += 1

    # Sort plaintext counts by frequency
    sorted_counts = sorted(plaintext_counts.items(), key=lambda x: x[1], reverse=True)

    # Print occurrences of each letter in the specified order
    print("\nOccurrences of each letter in the plaintext:")
    count = 0
    for letter, freq in sorted_counts:
        if len(str(freq)) == 1:  # Check if the frequency is a single digit
            freq = f" {freq}"  # Add a leading space before the frequency
        print(f"{letter}: {freq}", end="  ")
        count += 1
        if count % 5 == 0:  # Start a new line after every 5th frequency
            print()

def print_digraphs(ciphertext):
    # Calculate the digraphs in the ciphertext
    digraphs = {}
    for i in range(len(ciphertext) - 1):
        digraph = ciphertext[i:i+2]
        if digraph.isalpha():
            if digraph in digraphs:
                digraphs[digraph] += 1
            else:
                digraphs[digraph] = 1

    # Filter out digraphs with only one occurrence
    filtered_digraphs = {digraph: freq for digraph, freq in digraphs.items() if freq > 1}

    # Sort digraphs by frequency
    sorted_digraphs = sorted(filtered_digraphs.items(), key=lambda x: x[1], reverse=True)

    # Print occurrences of each digraph in the ciphertext
    print("\nOccurrences of each digraph in the ciphertext :")
    count = 0
    for digraph, freq in sorted_digraphs:
        print(f"{digraph}: {freq}", end="  ")
        count += 1
        if count % 5 == 0:  # Start a new line after every 5th digraph
            print()

def print_trigraphs(ciphertext):
    # Calculate the trigraphs in the ciphertext
    trigraphs = {}
    for i in range(len(ciphertext) - 2):
        trigraph = ciphertext[i:i+3]
        if trigraph.isalpha():
            if trigraph in trigraphs:
                trigraphs[trigraph] += 1
            else:
                trigraphs[trigraph] = 1

    # Filter out trigraphs with only one occurrence
    filtered_trigraphs = {trigraph: freq for trigraph, freq in trigraphs.items() if freq > 1}

    # Sort trigraphs by frequency
    sorted_trigraphs = sorted(filtered_trigraphs.items(), key=lambda x: x[1], reverse=True)

    # Print occurrences of each trigraph in the ciphertext
    print("\nOccurrences of each trigraph in the ciphertext:")
    count = 0
    for trigraph, freq in sorted_trigraphs:
        print(f"{trigraph}: {freq}", end="  ")
        count += 1
        if count % 5 == 0:  # Start a new line after every 5th trigraph
            print()
