input_number = int(input('Input your number: '))

while input_number > 9:

    numbers = [int(number) for number in str(input_number)]

    output_number = 1

    for number in numbers:
        output_number *= number

    input_number = output_number

print(input_number)
