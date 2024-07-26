# a = [1, 2, 3]
# b = [4, 5, 6, 7, 8, 9]
# c = [11, 12]
# print(list(zip(a, b, c)))
#
# names = ["Akbar", "Jantoro"]
# sur_names = ["Nurbekov", "Sultanov"]
#
# print(tuple(zip(names, sur_names)))
# print(dict(zip(names, sur_names)))

a, b = map(int, input().split())
print(tuple(map(lambda x: x ** 2, [i for i in range(a, b + 1)])))

