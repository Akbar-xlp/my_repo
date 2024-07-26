n = int(input("Enter your number: "))

fibonacci_1 = 0
fibonacci_2 = 1

for i in range(2, n):
        fibonacci_n = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = fibonacci_n

print(fibonacci_n)




