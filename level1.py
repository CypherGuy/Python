str = 'l3ar0b3_i0_iw3_4g3c4'
key = -8

text = ''

#a3_2o
#
for char in str:
    if char == '_':
        text += '_'
    elif char.isnumeric():
        text += char
    else:
        text += chr((ord(char) - 97 + key) % 26 + 97)

print(text)

# l3ar0b3_i0_iw3_4g3c4 was encrypted using this script with the numbers in the flag format as the key.
# Inverse the encrption and retrive the flag.
# Answer Format: d0cum4t1c{decryptedtext}


