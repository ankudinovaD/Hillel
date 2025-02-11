import string

input_string = input('Input your first number: ')

print('#' + ''.join([str(char) for char in input_string.title() if char != " " and char not in string.punctuation])[0:140])
