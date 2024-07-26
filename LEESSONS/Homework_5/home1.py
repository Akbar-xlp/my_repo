def is_triangle(side1, side2, side3):

    if (side1 + side2 > side3):
        (side1 + side3 > side2) 
        (side2 + side3 > side1)
        return True
    return False

print(is_triangle(3, 6, 10))  
print(is_triangle(3, 6, 8))  


'''
Функция жазыныздар, анын аты is_triangle болсун
жана ал озуно 3 параметр алсын(уч бурчтуктун уч жагы),
текшериш керек ошол берилген уч сан менен уч бурчтук
тузууго болобу. Эгер болос функция True деген болбосо False
деген жооп кайтарыш керек

Мисалы:
is_triangle(3, 6, 10) бизге кайтарыш керек False
is_triangle(3, 6, 8) бизге кайтарыш керек True

'''