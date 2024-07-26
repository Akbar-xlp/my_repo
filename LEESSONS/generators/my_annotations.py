# a: int = 5
# a = "barskoon"
# print(a)


def get_info(name:str, age:int) -> str:
    print(name)
    print(age)
    return f"{name} is {age} years old"

# print(get_info.__annotations__)
#
#
#
# def get_sum(nums: dict[int, str]) -> int:
#     return sum(nums)
#
#
# get_sum({1: "one", 2: "two"})
#
# get_info("Akbar",4 )
#

# import random
# a, b = map(int, input().split())
# if a > b:
#     print("b > a")
#
# else:
#     print(random)
# print(random.randint(a,b))

import random
cities = [i for i in input().split()]
s = int(input())
print(random.sample(cities, s))







