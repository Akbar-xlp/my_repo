cities = ["Bishkek","Talas","Naryn","Jalal-Abad"]
cit_filter = list(filter(lambda x: len(x) > 2,cities))
print([i for i in cities if len(i) > 5])
print(cit_filter)

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
print(list(filter(is_prime, numbers)))