# import random
#
# random.shuffle([1, 2, 3, 4])
#
# rng = list(range(1, 100, 5))
#
# # rng.remove(16)
#
# # for i in range(1, 3):
# #   rng.append(3)
#
# # fruits = ['🥭', '🍎', '🍍', '🥒']
# # fruits.sort()
# # print(fruits)

# sortText = input("Enter the expression to play with: ")

def sort(train: str) -> bool:
  open_list = ['(', '{', '[']
  close_list = [')', '}', ']']
  
  if len(train) % 2 != 0:
    return False


print(sort("{{{}}}"))
