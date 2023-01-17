alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(free_text, shift):
    text_list = [*free_text]
    cipher_text = ''
    for letter in text_list:
        if letter.isspace():
            cipher_text += letter
            continue
        pos = alphabet.index(letter)
        new_pos = pos + shift
        if new_pos >= len(alphabet):
            new_pos =  (new_pos % len(alphabet))
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    return cipher_text

def decrypt(free_text, shift):
    text_list = [*free_text]
    cipher_text = ''
    for letter in text_list:
        if letter.isspace():
            cipher_text += letter
            continue
        pos = alphabet.index(letter)
        new_pos = pos - shift
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    return cipher_text