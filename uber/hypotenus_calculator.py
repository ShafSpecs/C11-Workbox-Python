import math

print("Welcome to Hypotenuse calculator!", end="\n\n")

side1: float = float(input("Enter the value of the first side: "))
side2: float = float(input("Enter the value of the second side: "))


def hypotenus_calculation(first_side: float, second_side: float) -> float:
  hyp_squared: float = math.pow(float(first_side), 2) + math.pow(float(second_side), 2)
  hyp: float = math.sqrt(hyp_squared)
  return hyp


hypotenus = hypotenus_calculation(side1, side2)

print("The hypotenus of the triangle is", hypotenus)
