if __name__ == '__main__':

    import pandas

    data = pandas.read_csv('./NATOConverterRevisted/nato_phonetic_alphabet.csv')

    nato = {row.letter:row.code for (index, row) in data.iterrows()}

    is_correct = False

    # You can use a while loop like this
    # while not is_correct:
    #     user_input = input('Input a string to convert: ').upper()
    #     try:
    #         conversion = [nato[l] for l in user_input]
    #         is_correct = True
    #     except KeyError:
    #         print('sorry, only letters in the alphabet please.')
    #     else:
    #         print(conversion)

    #Or a recursive function like this
    def generate_phonetic():
        user_input = input('Input a string to convert: ').upper()
        try:
            conversion = [nato[l] for l in user_input]
        except KeyError:
            print('sorry, only letters in the alphabet please.')
            generate_phonetic()
        else:
            print(conversion)
    
    generate_phonetic()

