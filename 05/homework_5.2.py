choice_client = 'y'

while choice_client == 'y':
    if choice_client == 'y':
        first_number = int(input('Input your first number: '))
        second_number = int(input('Input your second number: '))
        arithmetic_operation = input('Input your arithmetic operation: ')
        if arithmetic_operation == '*':
            print(first_number * second_number)
            choice_client = input('Do you want to continue?(y/n): ')
        elif arithmetic_operation == '/':
            if second_number == 0:
                print('Error: Division by zero.')
                choice_client = input('Do you want to continue?(y/n): ')
            else:
                print(first_number / second_number)
                choice_client = input('Do you want to continue?(y/n): ')
        elif arithmetic_operation == '+':
            print(first_number + second_number)
            choice_client = input('Do you want to continue?(y/n): ')
        elif arithmetic_operation == '-':
            print(first_number - second_number)
            choice_client = input('Do you want to continue?(y/n): ')
        else:
            print('Arithmetic operation not recognized.')
            choice_client = input('Do you want to continue?(y/n): ')
