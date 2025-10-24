# Basics Unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}" )

# extended Iterable Unpacking with *
a, b, *c = [1, 2, 3, 4, 5, 6]
print(f"a: {a}, b: {b}, c: {c}")
print(type(a))
print(type(c))

# Ignoring Values by using '_'
a, _, c = [1, 2, 3]
