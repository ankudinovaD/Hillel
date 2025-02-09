import random
random_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]

print(random_list)
result_list = ([random_list[0], random_list[2], random_list[-2]])

print(result_list)
