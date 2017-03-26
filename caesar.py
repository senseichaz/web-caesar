def alphabet_position(letter):
    # returns zero-based numerical position of letter
    return (ord(letter.lower())-97)

def rotate_character(char, rot):
    # rotates character by given index
    if char.isalpha():
        if char.isupper(): #separate capital vs lowercase
            return chr((alphabet_position(char) + rot) % 26 + 97).upper() # ord(a) = 97
        elif char.islower():
            return chr((alphabet_position(char) + rot) % 26 + 97)
    else:
        return char

def encrypt(text, rot):
    txtcrypted = ''
    for char in text:
        txtcrypted += rotate_character(char,rot) # add each rotated character to output string
    return txtcrypted
