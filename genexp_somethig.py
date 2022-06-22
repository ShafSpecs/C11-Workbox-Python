def is_prime_genX(num: int) -> bool:
  if num < 2:
    return False
  
  for i in range(2, 8):
    if num % i == 0:
      return False
    
  return True


print(is_prime_genX(43))

# Set Comp
# primes_set = {i for i in range(1, 10_000_000) if is_prime_genX(i)}

# GenX (Generator Expression)
# primes_gen = (i for i in range(1, 10_000_000) if is_prime_genX(i))

# print(type(primes_set))

dict_play: dict = {
  "a": 1,
  "b": 2,
  "c": 3
}

print(type(dict_play.values()))
