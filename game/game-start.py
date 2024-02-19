
import random


class Game_Rock_Paper_Scissors:
    def __init__(self) :
        self.choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.difficulty = "easy"
        
    # Player choice to pick from the list self.choices
    def get_payer_choice(self):
        while True:
            player_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
            if player_choice in self.choices:
                return player_choice
            else:
                print("Invalid choice. Please enter (rock, paper, scissors, lizard, spock). ")
    
    # Computer choice to pick from the list self.choices but on random
    def get_computer_choice(self, difficulty):
        # difficulty level --------------------------------
        if difficulty == "easy":
            print(f"You chose difficulty level: {difficulty}")
            return random.choice(self.choices)
            
        elif difficulty == "medium":
            # making the computer to win more often 50%
            print(f"You chose difficulty level: {difficulty}")
            choice_with_bias = self.choices + ["rock", "paper", "scissors", "lizard", "spock"]
            return random.choice(choice_with_bias)
        elif difficulty == "hard":
            # making the computer to always win more often 80%
            print(f"You chose difficulty level: {difficulty}")
            
            if self.wins > self.losses:
                return random.choice(["paper", "scissors", "lizard", "spock"])
            else:
                return random.choice(["rock", "paper", "scissors", "lizard"]) 
        
        else:
            raise ValueError("Invalid difficulty level. please choose (easy, medium, hard).")
        # ---------------------------------------------------
            
        

    
    
    
    # a function which will determine the winner if the choices are the same or different
    def determine_winner(self, player_choice, computer_choice): 
        if player_choice == computer_choice:
            self.draws += 1
            return "It is a tie"
        elif (player_choice == "rock" and computer_choice == "scissors" or computer_choice == "lizard"):
            self.wins += 1
            return "You win!, Rock crushes scissors or lizard!"
        elif (player_choice == "paper" and computer_choice == "rock" or computer_choice == "spock"):
            self.wins += 1
            return "You win!, Paper covers rock or disproves spock!"
        elif (player_choice == "scissors" and computer_choice == "paper" or computer_choice == "lizard"):
            self.wins += 1
            return "You win!, Scissors cuts paper or decapitates lizard!"
        
        elif (player_choice == "lizard" and computer_choice == "spock" or computer_choice == "paper"):
            self.wins += 1
            return "You win!, Lizard poisons spock or eats paper!"
        elif (player_choice == "spock" and computer_choice == "scissors" or computer_choice == "rock"):
            self.wins += 1
            return "You win!, spock smashes scissors or vaporizes rock!"
        else:
            self.losses += 1
            return "Computer wins, you lose"
        
    
    # the function to run all the other function in a loop 
    def play_game(self):
        while True:
            print("\nLets play Rock, Paper, Scissors!")
            print("---------------------------------------------")
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
                print("Thanks for playing")
                break
            

if __name__ == "__main__":
    game = Game_Rock_Paper_Scissors()
    game.play_game()
            