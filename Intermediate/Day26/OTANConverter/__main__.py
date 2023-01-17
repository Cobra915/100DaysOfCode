if __name__ == '__main__':

    import pandas

    data = pandas.read_csv('./OTANConverter/nato_phonetic_alphabet.csv')

    otan = {row.letter:row.code for (index, row) in data.iterrows()}

    user_input = input('Input a string to convert: ').upper()

    conversion = [otan[l] for l in user_input]

    print(conversion)

