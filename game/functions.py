import random


# MAIN FUNCTIONS AND THE CLASS FOR THE USER AND THE COMP INPUTS
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
            player_choice = input("> Enter your choice (rock, paper, scissors, lizard, spock) >: ").lower()
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
            choice_with_bias = self.choices + ["rock", "paper", "scissors"]
            return random.choice(choice_with_bias)
        elif difficulty == "hard":
            # making the computer to always win more often 80%
            print(f"You chose difficulty level: {difficulty}")
            
            if self.wins > self.losses:
                return random.choice(["paper", "scissors"])
            else:
                return random.choice(["rock", "paper", "scissors", "lizard"]) 
        
        else:
            raise ValueError("Invalid difficulty level. please choose (easy, medium, hard).")
        # ---------------------------------------------------
            


# CLASS TO CHECK THE WINING INPUT FROM BOTH THE USER AND THE COMPUTER
class Main(Game_Rock_Paper_Scissors):
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
        


# Game_setup inherited All other classes from main

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






