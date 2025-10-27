# why we use decorators
# --> Decorator helps to adding extra behavior of the functions.
# --> Debug a Functions

def func(fan):
    def wrapper(*args, **kwargs):
        print('Started')
        fan(*args, **kwargs)
        print("End")
    
    return wrapper

def func2():
    print("I'm Function 2...")

def func3():
    print("I'm func 3...")


# x = func(func2)
# print(x)
# x()
# y = func(func3)
# y()

@func
def func3():
    print("Hello test line...")

@func
def func4(p, q, r):
    print(p)


func4(5, 4, 2)
func3()