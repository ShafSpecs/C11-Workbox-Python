def is_prime(num: int) -> bool:
  if num == 1:
    return False
  
  for i in range(2, num):
    if num % i == 0:
      return False
  
  return True


user_input = is_prime(int(input("Enter a number to test if it's prime or not: ")))
print(user_input)
