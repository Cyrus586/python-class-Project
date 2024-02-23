import random
import time
from main import *
from functions import *

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
            
            print("Lets play rock paper scissors game! ")
            print("---------------------------------------------")
            user_input = input("Would you like to play rock paper scissors (yes/no): ").lower()
            
            if user_input != "yes":
                print("Its fine if you dont want to play")
                print("------------------------------------------")
                break
            
            print("\n")
            print("Welcome to this wonderful adventure of Rock Paper Scissors! 🏕️🏝️🏖️🏕 \n")
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
        while True:
            player_1_choice = self.get_player_choice()
            print("\nPlayer 2, Please look away...!")
            print("Press Enter when ready to continue....")
            player_2_choice = self.get_player_choice()
            print("\nPlayer 2 has made their choice. Player 1, you can Look now.")
            print(f"\nPlayer 1 choice: {player_1_choice}")
            print("Player 2`s choice is hidden")
            time.sleep(1)
            print("\nCalculating results.....")
            time.sleep(1)
            
            result = self.determine_winner(player_1_choice, player_2_choice)
            print(result)
            
            if result == "You win!":
                self.wins += 1
                print("Player 1 wins!")
            elif result == "Computer wins!":
                self.losses += 1
                print("Player 2 wins")
            else:
                self.draws += 1
                print("It`s a draw!")
            
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing, COME BACK AGAIN")
                print("------------------------------------------")

                break
        
            

if __name__ == "__main__":
    game = Game_options()
    game.Play_game_setup()

