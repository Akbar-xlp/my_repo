def sum_a_b(a ,b):
    result = a +b
    return result


def get_info():
    name = "Arsen"
    surname = "Kengegulov"
    people = ["Akbar","Asan","Kairat"]
    return name, surname, people


def set_name(name):
    name_1 = name
    return name_1

a, b,c = get_info()
print(a)
print(b)
print(c)
res = sum_a_b(1,999)
print(res)
a_b_sum = sum_a_b
print( a_b_sum(3,4))

def max_a_b(a,b):
    return a if a > b else b


def max_a_b_c(a,b,c):
    k = max_a_b(a,b)
    return k if c < k else c

print(max_a_b(10,11))
print(max_a_b_c(10,11,12))
print(max_a_b(15,max_a_b (18,17)))
