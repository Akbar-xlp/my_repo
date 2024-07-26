# A, E, I, O, U, L, N, S, T, R – 1 очко;
#     D, G – 2 очка;
#     B, C, M, P – 3 очка;
#     F, H, V, W, Y – 4 очка;
#     K – 5 очков;
#     J, X – 8 очков;
#     Q, Z – 10 очков.

# score = {
#     1: 'AEIOULNSTR',
#     2: 'DG',
#     3: 'BCMP',
#     4: 'FHVWY',
#     5: 'K',
#     8: 'JX',
#     10: 'QZ'
# }
# word = input()
# word = word.upper()


# total_score = 0
# for letter in word:
#    for key, value in score.items():
#       if letter in value:
#          total_score += key
#          break
# print(total_score)


# cats = [
#     ('Мартин', 5, 'Алексей', 'Егоров'),
#     ('Фродо', 3, 'Анна', 'Самохина'),
#     ('Вася', 4, 'Андрей', 'Белов'),
#     ('Муся', 7, 'Игорь', 'Бероев'),  
#     ('Изольда', 2, 'Игорь', 'Бероев'),
#     ('Снейп', 1, 'Марина', 'Апраксина'),
#     ('Лютик', 4, 'Виталий', 'Соломин'),
#     ('Снежок', 3, 'Марина', 'Апраксина'),
#     ('Марта', 5, 'Сергей', 'Колесников'),
#     ('Буся', 12, 'Алена', 'Федорова'),
#     ('Джонни', 10, 'Игорь', 'Андропов'),
#     ('Мурзик', 1,'Даниил', 'Невзоров'),
#     ('Барсик', 2, 'Виталий', 'Соломин'),
#     ('Рыжик', 7, 'Владимир', 'Медведев'),
#     ('Матильда', 8, 'Андрей', 'Белов'),
#     ('Гарфилд', 3, 'Александр', 'Березуев')]

# result = {}
# for cat in cats:
#     value = cat[0]+", "+str(cat[1])
#     result.setdefault(cat[2:], []).append(value)


# for key, value in result.items():
#     print(f'{key}:{value}')    

# text = input()
# {
#     'o':2,
#     'k':2,
#     'u':2,
#     'r':2,
#     'm':1,
#     'e':1,
#     'n':1,
# }
# word ={}
# for i in text:
#     word[i] = text.count(i)

# print(i)

# names = ["Arsen","Bakbol","erbol"]
# surnames = ["Kengegulov","Shiregeliev","Kudakeev"]


# lenght = len(names)
# people = dict()
# for i in range(lenght):
#     people[names[i]]=surnames[i]
# print(people)
# for key,value in people.items():
#     print(key,value)


# name = "Okurmen"
# age = 1
# if age > 2 or not name == "Okurmen" and age != 1: # False + False * True
#     print("if ishtedi")
# else:
#     print("else ishtedi")


num_1 = int(input("Enter number one: ")) 
num_2 = int(input("Enter number two: "))
num_3 = int(input("Enter number three: "))

big_number = (num_1 + num_2) ** num_3
# big_number = (12 + 21) ** 1

print(big_number)
tak_sandar = 0

if big_number % 2 == 1:
    tak_sandar = big_number // 2 + 1
else:
    tak_sandar = big_number // 2

print(tak_sandar)

def get_tak_sandar(numbers):
    result = []
    for number in numbers:
        if number % 2 == 1:
            result.append(number)
    return result

tak_sandar = get_tak_sandar([1,2,3,4,5,6,7,8,9])
tak_sandar_2 = get_tak_sandar([8, 12, 23, 54, 78])
print(tak_sandar)
print(tak_sandar_2)

def info(name, surname, age):
    print()
    print(f'Name: {name}')
    print(f'Surname: {surname}')
    print(f'Age: ', {age})
    print()

person = input("Name Surname Age: ")
p = person.split()
