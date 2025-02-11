import keyword
import string

input_string = input("Введіть ім'я змінної: ")

if input_string[0].isdigit():
    print(False)
elif " " in input_string:
    print(False)
elif input_string == "_":
    print(True)
elif input_string.count('_')  == len(input_string):
    print(False)
elif any(char in string.punctuation and char != "_" for char in input_string):
    print(False)
elif keyword.iskeyword(input_string):
    print(False)
elif not input_string.islower():
    print(False)
else:
    print(True)
