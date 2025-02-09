my_list = []
new_list = []

for index, element in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(element)

if not my_list:
    result = 0
else:
    result = (sum(new_list)) * my_list[-1]

print(result)
