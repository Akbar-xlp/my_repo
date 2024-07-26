def get_elements(numbers, n):
    return [i for i in numbers if i % n == 0]
numbers = input("Enter numbers: ")
n = int(input("Enter n: "))
print(get_elements([int(i) for i in numbers.split()], n))
