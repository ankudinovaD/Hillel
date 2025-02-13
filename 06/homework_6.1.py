import string
input_string = input('Input your first number: ')

first_letter, last_letter = input_string.split('-')
first_code, last_code = ord(first_letter), ord(last_letter)
letters = string.ascii_letters

dictionary = {ord(char): char for char in letters}

if first_code <= last_code:
    print(''.join([values for key, values in dictionary.items() if first_code <= key <= last_code]))
else:
    print(''.join([values for key, values in dictionary.items() if first_code <= key or last_code >= key]))
