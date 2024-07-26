names = input("Enter names: ")

names_list = names.split()


result = []

for i in range(len(names_list)):
    if len(names_list[i]) > 5:
        result.append(names_list[i])

print(*result)

print(*(name for name in input("Enter names: ").split() if len(name) >= 5))
