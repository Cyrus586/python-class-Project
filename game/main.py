import random

print("WELCOME TO THE GAME OF ROCK PAPER AND SCISSORS!!!")

print("")

game_options=("rock", "paper", "scissor")

player_points, computer_points = 0,0

running = True

while running:

    x = 1
    game_rounds=int(input("Enter the number of rounds you would like to play: "))

    print("")

    while x <= game_rounds:
            
        player_choice= None
        computer_choice = random.choice(game_options)

        player_choice=input("Enter your choice from (Rock, Paper or Scissor): ")

        print(f"Your choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")

        if player_choice == computer_choice:
            print("This round is a Tie!")
            player_points += 1
            computer_points += 1
                
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print("You Win this round!")
                player_points += 2
                
            else:
                print("The Computer wins!")
                computer_points += 2

        elif player_choice == "paper":
            if computer_choice == "rock":
                print("You Win this round!")
                player_points += 2
                
            else:
                print("The Computer wins!")
                computer_points += 2


        elif player_choice == "scissors":
            if computer_choice == "paper":
                print("You Win this round!")
                player_points += 2
                
            else:
                print("The Computer wins!")
                computer_points += 2

        else:
            print(f"Invalid choice: {player_choice}")
            
        print(f"You currently have {player_points} points and the Computer has {computer_points} points.")
        print("--------------------")

        x += 1

    if player_points > computer_points:
        print("YOU WON THE MATCH!!!")

    elif player_points == computer_points:
        print("THIS MATCH WAS A DRAW!!!")

    else:
        print("THE COMPUTER WON THE MATCH!!!")

    print("--------------------")

    if input("Do you want to play again? (yes/no): ") == "no":
        running = False

print("--------------------")

print("THANK YOU FOR PLAYING!")  

        