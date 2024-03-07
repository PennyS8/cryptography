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
    # Store punctuation and list all indexes of each mark in the text
    punct_index_map = {}
    punct_index_tracker = 0
    for char in text:
        if char.isalpha():
            cleaned_text += char
        elif char in string.punctuation:
            if char not in punct_index_map.keys():
                punct_index_map[char] = [punct_index_tracker]
            else:
                punct_index_map[char].append(punct_index_tracker)
        else: # Spaces or other non-valid symbols
            continue

        punct_index_tracker += 1

    return cleaned_text, punct_index_map

def print_plaintext(text, punct_index_map):
    modified_text = text

    # Insert preserved punctuation
    for char in punct_index_map:
        for i in range(len(char)):
            # insert the punctuation into the text
            modified_text[:i] + char + modified_text[i:]

    plaintext = modified_text.lower()
    print(plaintext)
'''
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
'''
def print_frequency_graph_n(ciphertext, n):
    n = int(n)
    # Calculate the trigraphs in the ciphertext
    trigraphs = {}
    for i in range(len(ciphertext) - (n-1)):
        trigraph = ciphertext[i:i+n]
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
