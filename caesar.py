def alphabet_position(letter):
    letter = letter.lower()
    return list(string.ascii_lowercase).index(letter)

def rotate_character(letter, rot):
    shift = 97 if letter.islower() else 65
    if not letter.isalpha():
        return(letter)
    return chr((ord(letter) + rot - shift) % 26 + shift)

def encrypt(text, rot):
    newText = ""
    for letter in text:
        newChar = rotate_character(letter, rot)
        newText += newChar
    return newText
