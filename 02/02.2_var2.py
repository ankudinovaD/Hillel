input_number = int(input('Input your number: '))


first = input_number // 10000
second = (input_number // 1000) % 10
third = (input_number // 100) % 10
fourth = (input_number // 10) % 10
fifth = (input_number // 1) % 10

# print (input_number)
result = fifth * 10000 + fourth * 1000 + third * 100 + second * 10 + first

print(result)
