message = 'FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV C'
ciphertext = message.replace(' ', '')
split_text = ''
for i, char in enumerate(ciphertext):
    split_text += char
    if i % 7 == 6:
        split_text += ' '

print(split_text)

mode = 1
number_list = []
for char in split_text:
    if char.isalpha():
        letter = char.lower()
        number_list.append((ord(letter) - 96 - mode) % 26)

num_string = ''
for i, num in enumerate(number_list):
    num_string += (str(num) + ' ')
    if i % 7 == 6:
        num_string += '\n'

print(num_string)

col = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
for i, num in enumerate(number_list):
    mod = i % 7
    col[mod].append(num)

print(col)




