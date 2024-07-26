def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    return a % b

def div(a, b):
    return a // b

def main():
    while True:
        print("1) + ")
        print("2) - ")
        print("3) * ")
        print("4) / ")
        print("5) // ")
        print("6) ** ")
        print("7) % ")
        print("q (exit)")

        choice = input("Enter your choice: ")
        if choice == "q":
            break

        if choice == "1":
            n, m = map(int, input("Enter two numbers: ").split())
            print(add(n, m))
        elif choice == "2":
            n, m = map(int, input("Enter two numbers: ").split())
            print(subtract(n, m))
        elif choice == "3":
            n, m = map(int, input("Enter two numbers: ").split())
            print(multiply(n, m))
        elif choice == "4":
            n, m = map(int, input("Enter two numbers: ").split())
            print(divide(n, m))
        elif choice == "5":
            n, m = map(int, input("Enter two numbers: ").split())
            print(div(n, m))
        elif choice == "6":
            n, m = map(int, input("Enter two numbers: ").split())
            print(power(n, m))
        elif choice == "7":
            n, m = map(int, input("Enter two numbers: ").split())
            print(mod(n, m))


if name == "__main__":
    main()