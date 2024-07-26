def aynt(widht, height):
    return widht * height

# print(aynt(4,3))

def get_qart(n):
    return n ** (1/2)

# number = int(input("Enter a number:"))
# print(get_qart(number))

def get_max_element(nums):
     max = int(nums[0])

     for number in nums:
          if int (number) >max:
               max = int(number)
num = [i for i in input().split()]
print(num)
element = get_max_element(num)
print(element)



