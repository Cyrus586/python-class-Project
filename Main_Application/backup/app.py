from flask import Flask, render_template, request, redirect, url_for
from main import Game_Play
import time

app = Flask(__name__)

# Instantiate the Game_Play class
game = Game_Play()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_with_computer', methods=['GET', 'POST'])


def play_with_computer():
    result = ""
    num_rounds = 0 
    play_again = "yes"  # Initialize play_again variable
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input != "yes":
            return render_template('play_with_computer.html', result="The game has been reset")
        
        time.sleep(2)
        result += "Welcome to this wonderful adventure of Rock Paper Scissors!<br><br>"
        time.sleep(2)
        result += "Starting the game please wait......."
        difficulty = request.form.get('difficulty')
        if difficulty not in ["easy","medium","hard"]:
            return render_template('play_with_computer.html', result="Invalid difficulty level. Please select one of the levels above.")
        
        
        result += f"<br><br>"
        player_choice = request.form.get('player_choice')
        computer_choice = game.get_computer_choice(difficulty)
        result += f"You chose: {player_choice}<br>Computer chose: {computer_choice}<br>"
        result += game.determine_winner(player_choice, computer_choice) + "<br>"
    
        game.save_scores()
        result += "<br>---------------- SCORES -------------------<br>"
        with open("score.txt", "r") as file:
            scores = file.read()
            result += scores + "<br>"
        # result += f"<br>Wins: {game.wins}, Loses: {game.losses}, Draws: {game.draws}<br>"
        if game.wins > game.losses:
            result += "<h4>You are on a winning streak! Keep it up 😄</h4>"
        elif game.losses > game.wins:
            result += "<h4>The computer seems to have your number. Can you turn the tide? 😪</h4>"
        else:
            result += "<h4>It's neck and neck! Keep playing to see who comes out on top. 😄😪</h4>"
        
        play_again = request.form.get('play_again')  # Get user's choice to play again
        

        
    
    return render_template('play_with_computer.html', result=result, play_again=True, num_rounds=num_rounds)


@app.route('/play_with_friend', methods=['GET', 'POST'])


def play_with_friend():
    if request.method == 'POST':
             
        player_1_name = request.form['player_1_name']
        player_2_name = request.form['player_2_name']
        player_1_choice = request.form['player_1_choice']
        player_2_choice = request.form['player_2_choice']
        
        
           
        
        
        class SelectWinner(Game_Play):
            def __init__(self):
                self.wins = 0
                self.losses = 0
                self.draws = 0
            def determine_winners(self, player_1_choice, player_2_choice):
                    if player_1_choice == player_2_choice:
                        self.draws += 1
                        return "It is a tie"
                    elif (player_1_choice == "rock" and player_2_choice == "scissors"):
                        self.wins += 1
                        return f"{player_1_name} win!, Rock crushes scissors!"
                    elif (player_1_choice == "paper" and player_2_choice == "rock"):
                        self.wins += 1
                        return f"{player_1_name} win!, Paper covers rock!"
                    elif (player_1_choice == "scissors" and player_2_choice == "paper"):
                        self.wins += 1
                        return f"{player_1_name} win!, Scissors cuts paper!"
                    else:
                        self.losses += 1
                        return f"{player_2_name} wins, {player_1_name} lose"
                    
        game = SelectWinner()
        result = game.determine_winners(player_1_choice, player_2_choice)
        
        return render_template('play_with_friend_result.html', 
                               player_1_name=player_1_name,
                               player_2_name=player_2_name,
                               player_1_choice=player_1_choice,
                               player_2_choice=player_2_choice,
                               result=result)
        
    else:
        return render_template('play_with_friend.html')

if __name__ == "__main__":
    app.run(debug=True)
