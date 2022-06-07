number = int(input("Enter a number: "))

a, b = divmod(number, 2)

if b == 0:
  print("Even number")
else:
  print("Odd number")