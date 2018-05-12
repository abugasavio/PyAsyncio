# one nice simple explanation
# https://stackoverflow.com/questions/15331726/how-does-the-functools-partial-work-in-python

from functools import partial


def foo(a, b, c, d):
    return a + b + c + d


bar = partial(foo, a=2, b=4)

r = bar(c=5, d=6)

print(r)

# ===========


def add_numbers(x, y):
    return x + y


add_to_five = partial(add_numbers, x=5)


print(add_to_five(y=10))
