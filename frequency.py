# Define expected letter frequencies in English

# The following, or ending in '_FREQ', dictionaries have the character
# indexing the frequency that it is seen in strings.

CHAR_FREQ = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
    'Z': 0.07
}

DIGRAPH_FREQ = {
    'TH': 1.52, 'HE': 1.28, 'IN': 0.94, 'ER': 0.94, 'AN': 0.82,
    'RE': 0.68, 'ND': 0.63, 'AT': 0.59, 'ON': 0.57, 'NT': 0.56,
    'HA': 0.56, 'ES': 0.56, 'ST': 0.55, 'EN': 0.55, 'ED': 0.53,
    'TO': 0.52, 'IT': 0.50, 'OU': 0.50, 'EA': 0.47, 'HI': 0.46,
    'IS': 0.46, 'OR': 0.43, 'TI': 0.34, 'AS': 0.33, 'TE': 0.27,
    'ET': 0.19
}

# The following, or ending in '_COMMON', lists
# are in no particular order.

TRIGRAPH_COMMON = [
    'THE', 'AND', 'THA', 'ENT', 'ION',
    'TIO', 'FOR', 'NDE', 'HAS', 'NCE'
]

STARTING_CHAR_COMMON = [
    'T', 'O', 'A', 'W', 'B',
    'C', 'D', 'S', 'F', 'M'
]

ENDING_CHAR_COMMON =[
    'E', 'T', 'D', 'S'
]