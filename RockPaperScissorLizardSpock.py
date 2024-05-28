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

lizard = '''
             _                  
            / )                 
          .' /                      
      ---'  (__________                
                _______)             
                __)               
               __)              
      ---.______)
'''

spock = '''
   _
  ( \       _
 ( \ \     / )
  \ \ \   / / 
 _ \ \ \ / / )
( \ \_\_V_/ /
 \ \      `-|  
  \ \  `--  |  
  |      || |  
   \     '  /  
    |      |   
    |      |
'''


game_images = [rock, paper, scissors, lizard, spock]

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, or 4 for Spock.\n"
    ))

if user_choice >= 5 or user_choice < 0:
    print("You typed an invalid number, you lose.")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 4)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif user_choice == 1 and computer_choice == 0:
        print("You win.")
    elif computer_choice == 1 and user_choice == 0:
        print("You lose.")
    elif user_choice == 3 and computer_choice == 1:
        print("You win.")
    elif computer_choice == 3 and user_choice == 1:
        print("You lose.")
    elif user_choice == 2 and computer_choice == 1:
        print("You win.")
    elif computer_choice == 2 and user_choice == 1:
        print("You lose.")
    elif user_choice == 3 and computer_choice == 2:
        print("You lose.")
    elif computer_choice == 3 and user_choice == 2:
        print("You win.")
    elif user_choice == 0 and computer_choice == 3:
        print("You win.")
    elif computer_choice == 0 and user_choice == 3:
        print("You lose.")
    elif user_choice == 4 and computer_choice == 0:
        print("You win.")
    elif computer_choice == 4 and user_choice == 0:
        print("You lose.")
    elif user_choice == 4 and computer_choice == 1:
        print("You lose.")
    elif computer_choice == 4 and user_choice == 1:
        print("You win.")
    elif user_choice == 4 and computer_choice == 2:
        print("You win.")
    elif computer_choice == 4 and user_choice == 2:
        print("You lose.")
    elif user_choice == 4 and computer_choice == 3:
        print("You lose.")
    elif computer_choice == 4 and user_choice == 3:
        print("You win.")
    elif computer_choice == user_choice:
        print("It is a draw.")
