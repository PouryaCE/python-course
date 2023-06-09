from time import time, sleep


# def f():
#     sleep(.3)

# def g():
#     sleep(.5)

# t = time()    
# f()           
# print("time after f function: ", time() - t)  


# t = time()
# g()
# print("time after g function: ", time() - t)


#_____________________________________________________________________________
# def f():
#     sleep(.3)

# def g():
#     sleep(.5)


# def measure(func):
#     t = time()
#     func()
#     print("name of function is ",func.__name__ ,"and time after measure: ", time() - t)

# measure(f)
# measure(g)


#________________________________________________________________________
# def my_sleep(sleep_time):
#     sleep(sleep_time)

# def measure(f, *args, **kwargs):
#     t = time()
#     f(*args, **kwargs)
#     print(f.__name__, "time after measure: ", time() - t)

# measure(my_sleep, 0.3)
# measure(my_sleep, 0.5)
# measure(my_sleep ,0.7)
#________________________________________________________________________




def my_decorator(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "time after decorator :", time() - t)
    return wrapper

# my_sleep = my_decorator(my_sleep)   # decorator point

@my_decorator # decorator point
def my_sleep(sleep_time):
    sleep(sleep_time)
my_sleep(.2)
my_sleep(.5)


#________________________________________________________________________

def dec(func):
    def wrapper(*args):
        print("*****************************************")
        func(*args)
        print("*****************************************")
    return wrapper



@dec
def hello(name):
    print("hello ", name)

hello("pourya")

