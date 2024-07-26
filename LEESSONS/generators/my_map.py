def get_tak(number):
    return number % 2 == 1

numbers_bool = map(get_tak,range(10))
print(numbers_bool)
print(list(numbers_bool))

cities = ["Bishkek","Talas","Naryn","Jalal-Abad"]
cit_up = list(map(lambda x: x.upper(),cities))
print(cit_up)
