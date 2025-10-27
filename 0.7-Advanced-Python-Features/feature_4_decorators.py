# why we use decorators
# --> Decorator helps to adding extra behavior of the functions.
# --> Debug a Functions

def func(string):
    def wrapper():
        print('Started')
        print(string)
        print("End")
    
    return wrapper

def func2():
    print("I'm Function 2...")

x = func("Test line")
x()