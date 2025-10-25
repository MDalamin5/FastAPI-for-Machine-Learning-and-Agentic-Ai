# Unpacking: is refers to splitting up an iterable object and grabbing its individual elements

# Basics Unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}" )

# extended Iterable Unpacking with *
a, b, *c = [1, 2, 3, 4, 5, 6]
print(f"a: {a}, b: {b}, c: {c}")
print(type(a))
print(type(c))

a, *b, c = [1, 2, 3, 4, 5, 6]
print(f"a: {a}, b: {b}, c: {c}")

# Ignoring Values by using '_'
a, _, c = [1, 2, 3]


## Unpacking Nested Structures
data = ("Alamin", (26, "Engineer"))
name, (age, profession) = data

print(f"Name: {name}, Age: {age}, Profession: {profession}")


## Unpacking Functions Arguments
def print_name(*names):
    for name in names:
        print("-"*7)
        print(name)
    print("-"*7)


print_name("Alamin", "Aminul", "niloy")

# Combing Lists with Unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]

list3 = list1+list2 # approach 1
print(list3)
combined = [*list1, *list2] # its spread out like [1, 2, 3, and 4, 5, ..]
print(combined)

# Swapping Variables Using Unpacking
x = 10
y = 20

print(f"x: {x}, y: {y}")
x, y = y, x
print(f"x: {x}, y: {y}")
