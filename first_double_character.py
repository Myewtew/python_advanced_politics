
def first_double_string(mot):

    dict_char = dict()

    for letter in mot:

        if letter in dict_char:
            dict_char[letter]+=1
            print(letter)
            return letter

        else:
            dict_char[letter]=1

    return dict_char

first_double_string('abcdefa')
first_double_string('jfslsfjdl')
