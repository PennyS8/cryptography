#!/usr/bin/env python

def convert_to_char(num, a):
    """
    Convert a number to a character in the English alphabet based on the specified mode.

    Args:
        num (int): The number to be converted.
        a (int): The mode.
                If 0: a/A maps to 0, and z/Z maps to 25
                if 1: a/A maps to 1, and z/Z maps to 0

    Returns:
        str: The corresponding character.
    """
    # Validate input
    if not a == 0 or not a == 1:
        raise ValueError('Invalid "a" in helper.py: convert_to_char(), a must be 0 or 1.')
    if num < 0:
        raise ValueError('Invalid "num" in helper.py: convert_to_char(), num must be >= 0.')

    # Define alphabet mappings
    a_is_zero_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a_is_one_alph = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'

    # Return corresponding character based on mode
    if a == 1:
        return a_is_one_alph[num]
    else:
        return a_is_zero_alph[num]
        
def decrypt_with_shifts(shifts):
    """
    Decrypt the text using a given set of shift values and print the result.

    Args:
        shifts (list): A list of lists containing guesses for the Caesar cipher shifts.

    Returns:
        None
    """
    for sequence in shifts:
        for index, shift in enumerate(sequence):
            sequence[index] = calculate_shift('e', shift)

    num_sequences = len(shifts)
    positions = [0] * num_sequences  

    loop = True

    while loop:
        for i in range(num_sequences):
            print(convert_to_char(shifts[i][positions[i]], 0), end="")
        print()
        for i in range(num_sequences):
            print(convert_to_char(shifts[i][positions[i]], 1), end="")
        print()

        # Check if all positions have been iterated through
        if all(positions[i] >= len(shifts[i]) - 1 for i in range(num_sequences)):
            loop = False
        else:
            # Increment the current position or reset if at the end
            for i in range(num_sequences):
                if positions[i] < len(shifts[i]) - 1:
                    positions[i] += 1
                    break
                else:
                    positions[i] = 0

def calculate_shift(char_a, char_b):
    """
    Calculate the shift between two characters in the English alphabet.

    Args:
        char_a (str): The first character.
        char_b (str): The second character.

    Returns:
        int: The shift value.
    """
    return (convert_to_index(char_b, 1) - convert_to_index(char_a, 1)) % 26

def convert_to_index(character, mode):
    """
    Convert a character to a number representing its position in the English alphabet.

    Args:
        character (str): The character to be converted.
        mode (int): The mode. If 0, assumes 'a' is 1, if 1, assumes 'a' is 0.

    Returns:
        int: The corresponding number.
        
    Raises:
        ValueError: If the mode is not 0 or 1.
    """
    character = character.lower()
    if mode == 0:
        if character == 'a':
            return 1
        return ord(character) - 96
    elif mode == 1:
        if character == 'z':
            return 1
        return ord(character) - 96
    else:
        raise ValueError("Invalid mode. Mode must be 0 or 1.")

if __name__ == '__main__':
    # Example usage
    shifts = [['x'], ['b'], ['b'], ['b'], ['b'], ['b'], ['b']]  # Guesses for the Caesar cipher key
    print("Decryption with guessed key:")
    decrypt_with_shifts(shifts)
