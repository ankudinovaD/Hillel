input_number = int(input('Input your number: '))
# a = int

div_first_number, mode_first_number = divmod(input_number,10000)
div_second_number, mode_second_number = divmod(mode_first_number, 1000)
div_third_number, mode_third_number =  divmod(mode_second_number, 100)
div_fourth_number, mode_fourth_number   = divmod(mode_third_number, 10)
div_fifth_number, mode_fifth_number   = divmod(mode_fourth_number, 1)
# print (input_number)
print (div_fifth_number, div_fourth_number,div_third_number,div_second_number,div_first_number)

# або можна просто прописати print (mode_third_number) і не виконувати зайву дію