# ---> Calculate the execution time of the functions use as the decorators

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Execution time is: {end - start}")
        
    
    return wrapper

@timer
def production_func():
    time.sleep(2)
    for _ in range(100000):
        pass


production_func()