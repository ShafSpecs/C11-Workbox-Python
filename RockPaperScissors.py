import random

possible_wins = ["Paper", "Rock", "Scissors"]

number_of_rounds = int(input("How many rounds do you want to play? "))

current_round = 0


def computer_win():
  print("Computer WON! Try better next time, Earthling!")


def player_win():
  print("You won! You're awesome!")


while current_round < number_of_rounds:
  computer_choice = possible_wins[random.randint(0, 2)]
  print("""
  What do you want to play?
  1. Paper
  2. Rock
  3. Scissors
  
  """)
  
  player_choice = input("Enter your choice: ")
  player_choice = possible_wins[int(player_choice) - 1]
  
  if player_choice == computer_choice:
    print("DRAW ROUND!")
  elif player_choice == "Rock" and computer_choice == "Paper":
    computer_win()
  elif player_choice == "Paper" and computer_choice == "Rock":
    player_win()
  elif player_choice == "Paper" and computer_choice == "Scissors":
    computer_win()
  elif player_choice == "Scissors" and computer_choice == "Paper":
    player_win()
  elif player_choice == "Rock" and computer_choice == "Scissors":
    player_win()
  elif player_choice == "Scissors" and computer_choice == "Rock":
    computer_win()
  
  current_round += 1
