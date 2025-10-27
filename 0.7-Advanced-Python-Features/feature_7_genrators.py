# yield --> pase the execution of the functions value and execute a little bit of the code, return a value and then pause and wait until you're ask for the next value to generate.

# ---> use space efficient executions or calculations to be done.
import time
def count_up_to(max_value):
    current = 1

    while current <= max_value:
        yield current
        time.sleep(0.5)
        current += 1


if __name__ == "__main__":
    counter = count_up_to(10)

    # print(next(counter))
    ## iterate over the generator
    for number in counter:
        print(number)