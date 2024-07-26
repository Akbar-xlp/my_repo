def check_password(password, special_chars="$%!?@#"):
    return len(password) > 8 and any(char in special_chars for char in password)

print(check_password("Akbarakbar#"))





def get_rect_value(a,b ,tp=True):
    if tp == True:
        print((a+b)*2)
    else:
        print(a*b)

get_rect_value(2,3)
get_rect_value(3,4, tp=False)