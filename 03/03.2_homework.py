first_list = [12, 3, 4, 10]
if len(first_list) != 0:
    second_list = [first_list[-1]]
    del first_list[-1]
    result_list = second_list + first_list
else:
    result_list = first_list
print(result_list)


first_list = [1]
if len(first_list) != 0:
    second_list = [first_list[-1]]
    del first_list[-1]
    result_list = second_list + first_list
else:
    result_list = first_list
print(result_list)


first_list = []
if len(first_list) != 0:
    second_list = [first_list[-1]]
    del first_list[-1]
    result_list = second_list + first_list
else:
    result_list = first_list
print(result_list)


first_list = [12, 3, 4, 10, 8]
if len(first_list) != 0:
    second_list = [first_list[-1]]
    del first_list[-1]
    result_list = second_list + first_list
else:
    result_list = first_list
print(result_list)
