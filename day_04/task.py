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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
options = [rock, paper, scissors]
print(f"You chose{options[user_choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose {options[computer_choice]}")

if user_choice == 0 and computer_choice == 0:
    print("You chose rock. Computer chose rock. Its a tie")
elif user_choice == 0 and computer_choice == 1:
    print("You chose rock. Computer chose paper. You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You chose rock. Computer chose scissors. You win")

if user_choice == 1 and computer_choice == 1:
    print("You chose paper. Computer chose paper. Its a tie")
elif user_choice == 1 and computer_choice == 0:
    print("You chose paper. Computer chose rock. You win")
elif user_choice == 1 and computer_choice == 2:
    print("You chose paper. Computer chose scissors. You lose")

if user_choice == 2 and computer_choice == 1:
    print("You chose scissors. Computer chose paper. You win")
elif user_choice == 2 and computer_choice == 0:
    print("You chose scissors. Computer chose rock. You lose")
elif user_choice == 2 and computer_choice == 2:
    print("You chose scissors. Computer chose scissors. Uts a tie")

