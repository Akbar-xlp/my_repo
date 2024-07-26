def get_even(*numbers):
    result = []
    for number in numbers:
        if number % 2 ==0:
            result.append(number)
    return result
num = [int(i) for i in input().split()]
# jup_sandar = get_even([1,2,3,4,5,6,7,8,9])
print(get_even(*num))









'''
 Напишите функцию, которая принимает один *args в качестве параметра.
 Функция должна возвращать нам только четные числа.
 Вводим цифры с консоли!
 Пусть имя функции будет get_even!
'''