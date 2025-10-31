# Normal Functions
"""
def val(x, y):
    return x**y
"""

# Normal functions convert into the Lambda functions.
val = lambda x, y: x**y
print(val(4,0))


## Check expression


check = lambda i: i in "hello"
print(check('h'))


## Integrate lambda functions as map functions function parameter.

# task: prices are stored as messy strings and need cleaning to float



## remove '$' sign before the number
## brainstorming
p = "$32.33"
val = p.replace("$", "")
print(type(float(val)))

## brainstorming end <---

cleaning = lambda x: float(x.replace("$", ""))

cleaning("$33.3")

## now whole things apply on the list
prices = ["$12.33", "$33.32", "$23.44"]
list(map(lambda p: float(p.replace("$", "")), prices))


## Lambda with filter functions

get_even = lambda x: x % 2 == 0

print(get_even(4))

num = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter((lambda x: x % 2 == 0), num)))

## keep only student with names starting with 'M'

students = [
    ["Aminul", 23],
    ["Alamin", 27],
    ["Mohimen", 25]
]


list(filter((lambda row: row[0].startswith("A") if True else False), students))

number = [32, 24, 5,6,2]
sorted(number, reverse=True)
