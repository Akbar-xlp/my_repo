def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fib(n-1) + fib(n-2)

# print(fib(1))

def rec(x):
    if (x < 4):
        print(x)
        rec(x +1)
        print(x)

# rec(3)

def pal(s):
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return pal(s[1:-1])

# print(pal("заказ"))

s = "заказ"


def get_filter(lst,filter=None):
    if filter is None:
        return lst
    res =[]
    for x in lst:
        if filter(x):
            res.append(x)

    return res
        
# print(s == s[::-1])
# a = [1,2,3,4,5]
# b =get_filter(lst=a)
# c = get_filter(lst=a, filter=lambda x: x % 2 == 0)
# print(b)
# print(c)


def say_name(name):
    def say_goodbay():
        print(f"Don't say my name,{name}!")

    return say_goodbay
    
# a = say_name("Akbar")
# a()


def get_book(name):
    def get_author(author):
        print(f"The book {name} - author {author}")

#     return get_author
# a = get_book("Harry Potter")
# a("J.K.Rowling")


def make_counter(n = 0):
    def next():
        nonlocal n
        n += 1
        return n
    return next

# t_1 = make_counter()
# t_2 = make_counter(9)
# print(t_1(), t_2())
# print(t_1(), t_2())
# print(t_1(), t_2())
# print(t_1(), t_2())


def limited_calls(func,n):
    def limit():
        nonlocal n
        n -= 1
        if n <= 0:
            print("Limit reached")
        else:
            func()
    return limit
def func():
    print("Function was called")


a = limited_calls(func=func,n = 5)
a()
a()
a()
a()
