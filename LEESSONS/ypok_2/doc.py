# lang_X = {'C++','python','Java'}
# lang_Y = {'PHP','python','PHP','C#'}

# lang_Z = set(lang_X) & (lang_Y)

# print(lang_Z)
# cats = [('Мартин', 5, 'Алексей', 'Егоров'),
#       ('Фродо', 3, 'Анна', 'Самохина'),
#       ('Вася', 4, 'Андрей', 'Белов'),
#       ('Муся', 7, 'Игорь', 'Бероев'),
#       ('Изольда', 2, 'Игорь', 'Бероев'),
#       ('Снейп', 1, 'Марина', 'Апраксина'),
#       ('Лютик', 4, 'Виталий', 'Соломин'),
#       ('Снежок', 3, 'Марина', 'Апраксина'),
#       ('Марта', 5, 'Сергей', 'Колесников'),
#       ('Буся', 12, 'Алена', 'Федорова'),
#       ('Джонни', 10, 'Игорь', 'Андропов'),
#       ('Мурзик', 1,'Даниил', 'Невзоров'),
#       ('Барсик', 2, 'Виталий', 'Соломин'),
#       ('Рыжик', 7, 'Владимир', 'Медведев'),
#         ('Матильда', 8, 'Андрей', 'Белов'),
#       ('Гарфилд', 3, 'Александр', 'Березуев')]

# cat = set(cats)

# print(cat)


# numbers = map(int,input("Enter numbers:").split())
# # num = set(numbers)
# # sum = 0 
# # for number in num:
# #     sum+=number
# # print(sum)
# a = list(numbers)
# b = set(a)

# dic = dict()

# for i in b:
#     s = 0
#     for j in a:
#         if i ==j:
#             s=s+1
#     dic[i]=s
# print(dic)            

numbers_1 = map(int, input().split())
numbers_2 = map(int, input().split())

n = set(numbers_1) & set(numbers_2)
print(n)

