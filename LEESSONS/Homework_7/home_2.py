def numbers(number):
    num = [num for num in number if num % 2 == 0]
    if num:
        return num
    else:
        return "list is empty"

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = numbers(number)
print()
print(result)
print()
# number = [1, 3, 5, 7]
# res = numbers(number)
# print()
# print(res)
# print()
