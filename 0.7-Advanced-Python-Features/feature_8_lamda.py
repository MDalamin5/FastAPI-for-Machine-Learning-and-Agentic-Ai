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