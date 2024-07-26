# numbers = list(map(int, input().split()))
#
# print(list(map(lambda x: x if x > 0 else -x, numbers)))
# print(list(map(lambda x: abs(x),numbers)))
#


# 2 тапшырма
#
# text = list(map(str, input().split()))
# print(tuple(map(lambda x: tuple(x.split("=")), text)))


# 3 тапшырма

numbers = list(map(int, input().split()))
print(list(filter(lambda x: 10 <= x < 100, numbers)))