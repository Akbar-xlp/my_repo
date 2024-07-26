# def show_func(func):
#     def wrapper(*argc,**kwargs):
#         result = func(*argc,**kwargs)
#         print(f"Ploshad primiygolnika: {result}")

#     return wrapper

# @show_func
# def get_sq(width,hight):
#     return width *hight

# get_sq = show_func(func=get_sq)
# get_sq(11,8)

# n , m = map(int,input().split())
# get_sq(n,m)
def show_menu(func):
    def wrapper(*args,**kwargs):
        result =func(*args, **kwargs)
        for i in range(len(result)):
            print(f"{i + 1}. {result[i]}")
    return wrapper
@show_menu
def get_menu(menus):
    return menus.split()

text = input("Введите меню через пробел: ")
get_menu(text)

