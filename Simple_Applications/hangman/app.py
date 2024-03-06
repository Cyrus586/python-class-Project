import random
from words import words_list_func


class Hangman:
    def __init__(self, word_list) -> None:
        self.word_list = word_list
        self.secret_word = self.get_secret_word()
        self.guesses_left = 6
        self.guessed_letters = set()
        self.hidden_word = ["_" for _ in self.secret_word]
    
    def get_secret_word(self):
        return random.choice(self.word_list).lower()
    
    def display_hidden_word(self):
        return " ".join(self.hidden_word)
    
    def display_guessed_letters(self):
        return ", ".join(sorted(self.guessed_letters))
    
    def guess_letter(self):
        letter = ""
        if letter in self.guessed_letters:
            print("You have already guessed that letter.")
            return
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.hidden_word[i] = letter
                print("Correct guess!")
        else:
            self.guesses_left -= 1
            print("Incorrect guess!")
        print(f"Guesses left: {self.guesses_left}")
        print(f"Guessed letters: {self.display_guessed_letters()}")
        print(f"Word: {self.display_hidden_word()}")
        
    def is_game_over(self):
        if "_" not in self.hidden_word:
            print(f"Congratulations! You guessed the word: {self.secret_word}")
            return True
        elif self.guesses_left == 0:
            print(f"Game over! The word was: {self.secret_word}")
            return True
        return False
    






if __name__ == "__main__":
    word_list = ["hello", "world"]  
    game = Hangman(word_list)
    print("Welcome to Hangman!")
    print("Guess the word: ", game.display_hidden_word())
    
    while not game.is_game_over():
        game = input("Please enter a letter: ").lower()
        Hangman.guess_letter()

    




