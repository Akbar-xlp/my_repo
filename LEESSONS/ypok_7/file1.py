# def get_list(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
    

    
# get_list(1,2,3,4,5)


# def get_all(a ,b,c, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(kwargs)

# get_all(name ="Akbar",surname="Nurbekov",age = 17)
# # get_all(a=1,b=2,c=3,d=4,e=5)


# def list1(*args,**kwargs):
#     print(*args)
#     print(kwargs['a'])
#     print(kwargs['b'])
#     print(kwargs['c'])

# list1(1,2,3,4, a =3,b=4,e=5,c=True)



# def get_info(a,b,d,e,*c):
#     print(f'a = {a}')
#     print(f'b = {b}')
#     print(f'c = {c}')
#     print(f'd = {d}')
#     print(f'e = {e}')
# a, b, *c ,d, e =[i for i in input().split()]
# get_info(a, b, d, e, *c)
def get_info(**kwargs):
    print(kwargs)
    print(f'Name: {name}')
    print(f'Surname: {surname}')
    print(f'Age: {age}')
    print()
name ,surname,age = [i for i in input().split()]
print()
get_info(name=name,surname=surname,age=age)
# print()