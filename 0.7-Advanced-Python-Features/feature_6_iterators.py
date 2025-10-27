r = range(10)
itr = iter(r)
# print(next(itr))
# print(next(itr))

## own loop

while True:
    try:
        value = next(itr)
        print(value)

    except StopIteration:
        break