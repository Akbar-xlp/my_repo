import time 

def get_time(func):
    def wrapper(*argc,**kwargs):
        start_time = time.time()
        result = func(*argc, **kwargs)
        end_time = time.time()
        print(result)
        print(f"Time: {end_time - start_time}")
    return wrapper

@get_time
def get_fast_gcd(a, b):
    a = 0
    for i in range(1,100000):
        a += i
    
@get_time
def get_gcd(a ,b):
    a = 0
    for i in range(1,100000):
        a += i
 

# get_gcd = get_time(func=get_gcd)
# get_fast_gcd = get_time(func=get_fast_gcd)
get_gcd(10, 15)
get_fast_gcd(10,2)
