import random
rock='''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors='''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_images=[rock,paper,scissors]

user_choice=int(input("what do you choose? type 0 for rock 1 for paper and 2 for scissors."))
computer_choice=random.randint(0,2)
print(f"computer choice:{computer_choice}")
print(game_images[computer_choice])

if user_choice >=3 or user_choice<0:
    print("it's a invalid number .Go ahead")
elif user_choice > computer_choice:
    print("yoiu win!\N{smiling face with smiling eyes}")
elif user_choice == computer_choice:
    print("it's tie.\N{thinking face}")

else:
    print("you lose.😢")

