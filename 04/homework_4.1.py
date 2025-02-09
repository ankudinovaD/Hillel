my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result_list = []
index = 0
while index < len(my_list):
    if my_list[index] == 0:
        my_list.pop(index)
        result_list.append(0)
    else:
        # result_list.append(my_list[index])
        index += 1
my_list += result_list
print(my_list)
