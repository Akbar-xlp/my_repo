def recursive(n):
    if n == 1:
        return 1
    else:
        return n + recursive(n - 1)

n = int(input("Enter a number: "))
result = recursive(n)
print(result)  
