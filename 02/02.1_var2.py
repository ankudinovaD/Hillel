input_number = int(input('Input your number: '))


first_number = input_number // 1000
second_number = (input_number // 100) % 10
third_number = (input_number // 10) % 10
fourth_number = (input_number // 1) % 10

# print (input_number)
print(first_number)
print(second_number)
print(third_number)
print(fourth_number)
