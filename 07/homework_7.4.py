def common_elements():
    range_of_3 = {x for x in range(100) if x % 3 == 0}
    range_of_5 = {x for x in range(100) if x % 5 == 0}

    result = range_of_3.intersection(range_of_5)
    print(result)
    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
