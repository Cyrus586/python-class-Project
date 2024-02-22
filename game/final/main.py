
from main import *
from game_start import *
from getpass import getpass
import time


class Game_Setup(Main):
    def Play_game_setup(self):
        while True:
            print("\n")
            print("===========================================================")
            print("=                                                         =")
            print("=      WELCOME TO ROCK, PAPER AND SCISSORS GAME           =")
            print("=                                                         =")
            print("===========================================================")
            print("SELECT ONE OPTION")
            print("-------------------------------")
            print("\n")
            print("A. Play against the computer")
            print("B. Play with a friend")
            print("C. Exit the game")
            print("\n")
            choice = input("Enter your Choice (A, B, C): ")
            
            if choice == "A" or choice == "a":
                self.play_with_computer()
            elif choice == "B" or choice == "b":
                self.play_with_friend()
            elif choice == "C" or choice == "c":
                print("-------------------------------")
                print("Thanks for visiting our developing game")
                break
            else:
                print("Invalid Choice, pick from (A, B, C)")







class Game_options(Game_Setup):
    def play_with_computer(self):
        while True:
            
            print(" ☆☆☆☆☆☆☆☆☆☆☆ L E T 'S P L A Y ! ☆☆☆☆☆☆☆☆☆☆☆ ")
            print("---------------------------------------------")
            user_input = input("Would you like to play rock paper scissors (yes/no): ").lower()
            
            if user_input != "yes":
                print("Its fine if you dont want to play")
                print("------------------------------------------")
                break
            
            print("\n")
            print("Welcome to this wonderful adventure of Rock Paper Scissors! \n")
            print("Starting...\n")
            time.sleep(1)  # Adding delays for extra effects
            print("Please wait!")
            time.sleep(1)
            difficulty = input("Choose difficult level (easy, medium, hard): ").lower()
            if difficulty not in ["easy","medium","hard"]:
                print("Invalid difficulty level. Please select on the levels above.")
                continue
            
            num_rounds = int(input("How many rounds do you want to play? "))
            
            for round in range(1, num_rounds + 1):
                print(f"\nRound {round}:")
                player_choice = self.get_payer_choice()
                computer_choice = self.get_computer_choice(difficulty)
                print(f"\nYou chose: {player_choice}")
                print(f"Computer chose: {computer_choice}")
                print(self.determine_winner(player_choice, computer_choice))
                
            
            
            
            print("\nGame Over!")
            print(f"Rounds: {num_rounds}, Wins: {self.wins}, Loses: {self.losses}, Draws: {self.draws}")
            
            if self.wins > self.losses:
                # emojis 
                emoji = "\U0001F600"
                print("You are on a wining streak! keep it up", emoji)
            elif self.losses > self.wins:
                # emojis 
                emoji = "\U0001F62A"
                print("The computer seems to have your number. Can you turn the tide?", emoji)
            else:
                # emojis 
                emoji = "\U0001F923"
                print("Its neck and neck! Keep playing to see who comes out on top.", emoji)
            
            print("---------------------------------------------")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing, COME BACK AGAIN")
                print("------------------------------------------")

                break
           
    
    def play_with_friend(self):
        player1_wins, player2_wins, draws= 0,0,0
        
        player1_name = input("Enter the name of the first player: ")

        player2_name = input("Enter the name of the second player")

        print(f"{player1_name} and {player2_name}, lets's start the game!")

        players_choice= {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "spock"}

        print("PLAYERS SHOULD ENTER AN OPTION FROM BELOW: ")
        print("------------------------------------------")
        print("\n")

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
            return "It is a tie"
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

        print(f"{player1_name}'s_Wins: {player1_wins}, {player1_name}'s_Wins: {player2_wins}, Draws: {draws}")

        if player1_wins > player2_wins:
            print(f"{player1_name} Wins!!! :)")

        elif player1_wins < player2_wins:
            print(f"{player1_name} Wins!!! :)")

        else:
            print("This Game's a Tie!")
        
            

if __name__ == "__main__":
    game = Game_options()
    game.Play_game_setup()
