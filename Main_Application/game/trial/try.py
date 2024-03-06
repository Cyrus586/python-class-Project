from getpass import getpass
player1_wins, player2_wins, draws= 0,0,0
        
player1_name = input("Enter the name of the first player: ")

player2_name = input("Enter the name of the second player: ")

print(f"{player1_name} and {player2_name}, lets's start the game!")

players_choice= {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "spock"}

print("PLAYERS SHOULD ENTER AN OPTION FROM BELOW: ")
print("------------------------------------------")

print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Lizard")
print("5. Spock")

player1_choice= getpass(f"{player1_name}, Enter your option: ")
player2_choice= getpass(f"{player2_name}, Enter your option: ")

print(f"{player1_name} chose: {player1_choice}")
print(f"{player2_name} chose: {player2_choice}")

if player1_choice == player2_choice:
    draws += 1
    print("It is a tie")
elif (player1_choice == "rock" and player2_choice == "scissors" or player2_choice == "lizard"):
    player1_wins += 1
    print(f"{player1_name} wins!")
elif (player1_choice == "paper" and player2_choice == "rock" or player2_choice == "spock"):
    player1_wins += 1
    print(f"{player1_name} wins!")
elif (player1_choice == "scissors" and player2_choice == "paper" or player2_choice == "lizard"):
    player1_wins += 1
    print(f"{player1_name} wins!")

elif (player1_choice == "lizard" and player2_choice == "spock" or player2_choice == "paper"):
    player1_wins += 1
    print(f"{player1_name} wins!")
elif (player1_choice == "spock" and player2_choice == "scissors" or player2_choice == "rock"):
    player1_wins += 1
    print(f"{player1_name} wins!")
else:
    player2_wins += 1
    print(f"{player2_name} wins!")

print("--------------------------------------------------------------------------")
print(f"{player1_name}'s_Wins: {player1_wins}, {player2_name}'s_Wins: {player2_wins}, Draws: {draws}")
print("--------------------------------------------------------------------------")

if player1_wins > player2_wins:
    print(f"{player1_name} Wins!!! :)")

elif player1_wins < player2_wins:
    print(f"{player2_name} Wins!!! :)")

else:
    print("This Game's a Tie!")
