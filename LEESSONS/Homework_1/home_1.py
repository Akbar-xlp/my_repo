n = int(input("Your number: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print((i * n +j) ** 2, end=" ")
    print()  
