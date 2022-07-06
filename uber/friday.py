import builtins
from functools import reduce

# d = dict(a=1, b=2, c=3)
#
# print({}.fromkeys('abcde', list(range(5))))
#
# d.setdefault('d', 8)
# print(d)


def sum_num(a: int, b: int) -> int:
  """Adds two numbers"""
  return a + b


def subtract(m, n):
  return m - n


# Higher-order function 👇
# A function that either returns, takes it in or deals with it.
def operate(fn, x, y):
  return fn(x, y)


# print(operate(sum_num, 2, 3))
# print(operate(subtract, 5, 2))
# print(operate(lambda x, y: x * y, 3, 4))

# Anonymous functions 👇
# Syntax.: lambda ...params: executable
division = lambda p, q: p / q
print(division(3, 5))

# print(division.__name__)

# print(sum_num(3, 6))
# print(sum_num.__name__)
# print(sum_num.__doc__)
# print(sum_num.__annotations__)
# Regular Function 👆
# Your normal function. Bleh!


# list_of_string = "i LOVey ".split()

# print(min(list_of_string, key=lambda x: x[-1]))

ages = [{"name": "Adedayo", "age": 6}, {"name": "Titi", "age": 16}]

print(sorted(ages, key=lambda x: len(x["name"]), reverse=True))
# Same thing would happen to `min`


# print(list(map(lambda x: x**2, [2, 3, 4, 5])))

# print(list(filter(lambda x: x % 2 == 0, [3, 4, 2, 0])))

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 10))
# print(sum([1, 2, 3, 4], 10))
# print(reduce(lambda a, b: a * b, [2, 4, 6]))


# filter & reduce (Next Class)

# You are going to make a list of tweets, dicts really
# e.g
# twitter_users: [
#   {
#     name: str,
#     username: str,
#     age: int,
#     tweets: [list[stats]],
#     followers: int,
#     following: int,
#     verified: bool
#   }
# ]


# Way of arranging params in a function. ==> (compulsory args, *args, optional args, **kwargs)

