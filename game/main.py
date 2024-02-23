
from main import *
from functions import *
import time



# Game_options inherited All other classes from Game_setup
class Game_options(Game_Setup):
    def play_with_computer(self):
        while True:
            print("\n")
            print(" ☆☆☆☆☆☆☆☆☆☆☆ L E T 'S P L A Y ! ☆☆☆☆☆☆☆☆☆☆☆ ")
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
            print(" ☆☆☆☆☆☆☆☆☆☆☆ L E T 'S   P L A Y   T O G E T H E R ! ☆☆☆☆☆☆☆☆☆☆☆ ")
            player_1_name = input("Please enter your username player 1: ").lower()
            player_2_name = input("Please enter your username player 2: ").lower()
            
            player_1_choice = self.get_payer_choice()
            print(f"\n{player_2_name}, Please look away...!")
            print("Press Enter when ready to continue....")
            player_2_choice = self.get_payer_choice()
            print(f"\n{player_2_choice} has made their choice. {player_1_name}, you can Look now.")
            print(f"\n{player_1_name} choice: {player_1_choice}")
            print(f"{player_2_name}`s choice is hidden")
            
            time.sleep(1)
            print("\nCalculating results.....")
            print("================================")
            time.sleep(1)
            
            result = self.determine_winner(player_1_choice, player_2_choice)
            print(result)
            
            if result == "You win!":
                self.wins += 1
                print(f"{player_1_name} wins!")
            elif result == "Computer wins!":
                self.losses += 1
                print(f"{player_2_name} wins")
            else:
                self.draws += 1
                print("It`s a tie!")
            
            print(f"Wins: {self.wins}, Loses: {self.losses}, Draws: {self.draws}")
            
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
        
            

if __name__ == "__main__":
    game = Game_options()
    game.Play_game_setup()

