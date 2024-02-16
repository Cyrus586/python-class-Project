import random

print("WELCOME TO THE GAME OF ROCK PAPER AND SCISSORS!!!")

x = 1
game_rounds=int(input("Enter the number of rounds you would like to play: "))

game_options=("rock", "paper", "scissor")


while x <= game_rounds:

    player_choice= None
    computer_choice = random.choice(game_options)

    player_choice=input("Enter your choice from (Rock, Paper or Scissor): ")

    print(f"Your choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a Tie!")

    elif player_choice == "rock" and computer_choice == "scissor":
        print("You Win!")

    elif player_choice == "paper" and computer_choice == "rock":
        print("You Win!")

    elif player_choice == "scissor" and computer_choice == "paper":
        print("You Win!")

    else:
        print("You lost")
    x += 1

    
    