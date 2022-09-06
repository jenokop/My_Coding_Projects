import random

def game2():
    list2 = ["rock", "paper", "scissor"]
    count = 0
    while True:
        random_AI_choice = random.choice(list2)
        user_choice = input("Rock, Paper or Scissor? ")
        if user_choice.lower() not in list2:
            print("Invalid input. Please try again.")
        elif user_choice.lower() == random_AI_choice:
            print("My choice: " + random_AI_choice.capitalize())
            print("Your choice: " + user_choice.capitalize())
            print("It's a tie. Please try again")
        elif (user_choice.lower() == "rock" and random_AI_choice == "scissor")\ or (user_choice.lower() == "paper" and random_AI_choice == "rock") or (user_choice.lower() == "scissor" and random_AI_choice == "paper"):
            print("My choice: " + random_AI_choice.capitalize())
            print("Your choice: " + user_choice.capitalize())
            print("You win! :D")
            break
        else:
            print("My choice: " + random_AI_choice.capitalize())
            print("Your choice: " + user_choice.capitalize())
            print("You lose :(")
            break
