import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    users_choices = input("enter your choice in Rock/Paper/Scissors or Q to quit").lower()
    computers_choice = random.choice(choices)
    print("computers choice", computers_choice)
    if users_choices == 'q':
       break
    if users_choices not in choices:
       print("enter valid choice")
       continue
    else:
        if (users_choices == "rock" and computers_choice == "scissors") or (users_choices == "scissors" and computers_choice == "paper") or (users_choices == "paper" and computers_choice == "rock"):
            print("you won")
            user_wins += 1
           
        else:
            print("computer won")
            computer_wins += 1
