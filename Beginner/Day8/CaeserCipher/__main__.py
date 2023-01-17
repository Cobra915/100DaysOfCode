if __name__ == "__main__":
    import Functions as f
    import ascii_art as art

    print(art.logo)
    print('Welcome to my Ceaser Cipher! This tool will take any message alogn with a shift value and encrypt or decrypt it using that value. ')

    direction = input("Please input a directive, encrypt or decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encrypt':
        cipher_text = f.encrypt(text, shift)
        print(cipher_text)
    elif direction == 'decrypt':
        cipher_text = f.decrypt(text, shift)
        print(cipher_text)