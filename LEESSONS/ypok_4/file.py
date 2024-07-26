# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result




# def sum_a_b(c,b):
#     return c + b




# a = factorial(5)
# print(sum_a_b(5,8))
# print(a)

def get_tak_sandar(numbers):
    result = []
    for number in numbers:
        if number % 2 ==1:
            result.append(number)
    return result

tak_sandar = get_tak_sandar([1,2,3,4,5,6,7,8,9])
tak_sandar_2 = get_tak_sandar([8,12,23,54,78])
print(tak_sandar)
print(tak_sandar_2)        

# def info(name, surname, age):
#     print(f'Name:',{name})
#     print(f'Surname:',{surname})
#     print(f'Age:',{age})
#     print()
# person = input("Name Surname Age:")
# p = person.split()
# info (p[0],p[1],int(p[2]))


# def max_a_b(a,b):
#     if a > b:
#         return a
#     else:
#         return b


# print(max_a_b(2,3))
# print(max_a_b(58,35))
# print(max_a_b(15668754368264576,1234567362))


# def f():
#     print("siz f chykyrdynyz")



# def get_max_element(numbers):
#      max = 0

#      for number in numbers:
#           if number >max:
#                max = number
#      print(max)           
          
# get_max_element([56,46 ,346,45 ,-1])


# def get_min_element(numbers):
#      min = 100

#      for number in numbers:
#           if number <min:
#                min = number
#      print(min)          

# get_min_element([56,46 ,346,45 ,-1])

# numbers = [56,46 ,346,45 ,-1]
# max = 0
# min = 100
# for number in numbers:
#     if number > max:
#         max = number
#     if number < min:
#             min = number
# print(max)       
# print(min)

