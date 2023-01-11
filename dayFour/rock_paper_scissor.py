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

#Write your code below this line 👇
import random

comp = random.randint(0, 2)
player = int(input("What do you choose?:\n 0: Rock\n 1: Paper\n 2:Scissors : \n"))
choices = [rock, paper, scissors]

comp_win = "You lose"
you_win = "You win"


if player > 2 or player < 0:
    print("You typed an invalid number. You lose!")
else:
    print(choices[player])
    print(f"Computer chose: \n {choices[comp]}")

    if player == comp:
        print("Draw!")
    elif player == 0:  # Rock
        if comp == 1:
            print(comp_win)
        elif comp == 2:
            print(you_win)
    elif player == 1:  # Paper
        if comp == 0:
            print(you_win)
        elif comp == 2:
            print(comp_win)
    elif player == 2:  # Scissors
        if comp == 0:
            print(comp_win)
        elif comp == 1:
            print(you_win)


