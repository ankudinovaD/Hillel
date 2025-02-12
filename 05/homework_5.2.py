while True:
    first_number = int(input('Input your first number: '))
    second_number = int(input('Input your second number: '))
    arithmetic_operation = input('Input your arithmetic operation: ')

    if arithmetic_operation == '*':
        print(first_number * second_number)
    elif arithmetic_operation == '/':
        if second_number == 0:
            print('Error: Division by zero.')
        else:
            print(first_number / second_number)
    elif arithmetic_operation == '+':
        print(first_number + second_number)
    elif arithmetic_operation == '-':
        print(first_number - second_number)
    else:
        print('Arithmetic operation not recognized.')

    choice_client = input('Do you want to continue? (y/n): ').lower()
    if choice_client not in ['y', 'yes']:
        break
