# print(bool(0))
#
# print(bool(-1))
#
# print(bool(None))

# a = 100
# ...
# # c = None
# if a == 0:
#     c = 0
#     print('a = 0')
#     ...
# else:
#     c = -1
#     ...
#
# print('c= ', c)

a = -10
b = 2.5
c = 0
d = None

print(type(a))
print(type(b))
# print(type(c))
# print(type(d))


if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
    print('d')
else:
    print('failed')

