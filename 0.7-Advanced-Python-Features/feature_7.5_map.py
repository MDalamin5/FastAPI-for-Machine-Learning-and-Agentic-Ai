## Introductions of map functions
num = [1, 2, 3, 4, 5, 6, 7]

def func(x: int) -> int:
    """
    Func functions square integer number

    :param x: this is a integer number.
    :return: another integer number.
    
    """
    return x**2

print(list(map(func, num)))

## same things doing by list compression
[func(x) for x in num]