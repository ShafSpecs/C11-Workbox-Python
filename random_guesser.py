import random

guess_number = random.randint(0, 50)

user_lives = 3

while user_lives > 0:
  user_guess = int(input("Guess the number: "))
  
  if user_guess > guess_number:
    print("Too High! Try again.")
    user_lives -= 1
  elif user_guess < guess_number:
    print("Too Low! Try again.")
    user_lives -= 1
  else:
    print("Awesome! You are correct!")
    break
else:
  print("Game Over! The correct number was", guess_number)
  