for i in range(1, 101):
  if i % 3 and i % 5:
    print(i)
  elif not i % 3 and not i % 5:
    print("FizzBuzz")
  elif i % 3 and not i % 5:
    print("Buzz")
  elif not i % 3 and i % 5:
    print("Fizz")
    