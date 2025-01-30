first_num = input('Input your first number: ')
second_num = input('Input your second number: ')
arithmetic_operation = input('Input your arithmetic operation: ')

if (not first_num.isdigit() or int(first_num) < 0) and (not second_num.isdigit() or int(second_num) < 0):
    if arithmetic_operation == '*':
        print(int(first_num) * int(second_num))
    elif arithmetic_operation == '/':
        if int(second_num) == 0:
            print('Error: Division by zero.')
        else:
            print(int(first_num) / int(second_num))
    elif arithmetic_operation == '+':
        print(int(first_num) + int(second_num))
    elif arithmetic_operation == '-':
        print(int(first_num) - int(second_num))
    else:
        print('Arithmetic operation not recognized.')
else:
    print('Error! Expected a number, but received something else.')
