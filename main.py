import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
player_choice = int(input("Please pick one. 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number.")
else:
  #Images print first, then logic is run below
  print("You chose:")
  print(images[player_choice])
  computer_choice = random.randint(0, 2)
  print("The computer chose:")
  print(images[computer_choice])


  #player picks rock (0), computer picks scissors (2)
  if player_choice == 0 and computer_choice == 2:
    print("You win!") 
  #player picks scissors (2), computer picks rock (0)
  elif computer_choice == 0 and player_choice == 2:
    print("You lose.")
  #player picks rock or paper but computer picks paper or scissors 
  elif computer_choice > player_choice:
    print("You lose.")
  #computer picks rock or paper but player picks paper or scissors
  elif player_choice > computer_choice:
    print("You win!")
  #both pick the same number  
  elif computer_choice == player_choice:
    print("It's a draw!")

