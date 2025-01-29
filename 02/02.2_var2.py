input_number = int(input('Input your number: '))


first_number    = input_number // 10000
second_number   = (input_number // 1000) % 10
third_number    = (input_number // 100) % 10
fourth_number   = (input_number // 10) % 10
fifth_number   = (input_number // 1) % 10

# print (input_number)
print (fifth_number, fourth_number,third_number,second_number,first_number)