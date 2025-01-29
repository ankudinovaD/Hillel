input_number = int(input('Input your number: '))
# a = int

div_first, mode_first_number = divmod(input_number, 10000)
div_second, mode_second_number = divmod(mode_first_number, 1000)
div_third, mode_third_number = divmod(mode_second_number, 100)
div_fourth, mode_fourth_number = divmod(mode_third_number, 10)
div_fifth, mode_fifth_number = divmod(mode_fourth_number, 1)
# print (input_number)
print(div_fifth, div_fourth, div_third, div_second, div_first)

# або можна просто прописати print (mode_third_number) і не викон. зайву дію
