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

#Write your code below this line 👇

options = [rock,paper,scissors]

choice_user= options[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))]
choice_computer = random.choice(options)
print("The computer chose: \n"+ choice_computer)

print("You chose:\n"+ choice_user)

if choice_computer ==rock:
    
    if choice_user == rock:
        print("Draw")
    elif choice_user== scissors:
        print("You Lose")
    else:
        print("You Win")
elif choice_computer == paper:
    
    if choice_user == paper:
        print("Draw")
    elif choice_user== scissors:
        print("You Win")
    else:
        print("You Lose")
elif choice_computer == scissors:
   
    if choice_user == scissors:
        print("Draw")
    elif choice_user== rock:
        print("You Win")
    else:
        print("You Lose")
