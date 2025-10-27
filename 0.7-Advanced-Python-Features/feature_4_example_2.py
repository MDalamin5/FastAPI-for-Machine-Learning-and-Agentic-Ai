def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function executions...")
        result = func(*args, **kwargs)
        print("After execution the functions...")

        return result
    
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello {name}.")

@my_decorator
def add(x, y):
    return x + y



if __name__ == "__main__":
    d = say_hello("Alamin")
    print(d)

    p = add(3, 4)
    print(p)
