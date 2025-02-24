def difference(*args):
    rounded_args = [round(num, 2) for num in args]

    if rounded_args:
        return round(max(rounded_args) - min(rounded_args), 2)
    else:
        return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
