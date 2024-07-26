def get_biggest_city(*args):
    long_city = args[0]  
    max_length = len(long_city)

    for city in args[1:]:
        if len(city) > max_length:
            long_city = city
            max_length = len(city)

    return long_city

cities = ["Bishkek", "Osh", "Talas", "Batken", "Stambul","Barskoon"]
print()
print(get_biggest_city(*cities))  
print()