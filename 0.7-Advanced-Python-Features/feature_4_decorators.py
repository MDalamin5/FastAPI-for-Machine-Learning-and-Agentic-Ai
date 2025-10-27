# why we use decorators
# --> Decorator helps to adding extra behavior of the functions.
# --> Debug a Functions

def func(fan):
    def wrapper():
        print('Started')
        fan()
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
def func4():
    print("i'm hello sir...")


func4()