def play_with_computer():
    result = ""
    play_again = "yes"  # Initialize play_again variable
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input.lower() != "yes":
            return render_template('play_with_computer.html', result="It's fine if you don't want to play")
        
        result += "Welcome to this wonderful adventure of Rock Paper Scissors!<br>Starting..."
        difficulty = request.form.get('difficulty')
        if difficulty not in ["easy","medium","hard"]:
            return render_template('play_with_computer.html', result="Invalid difficulty level. Please select one of the levels above.")
        
        num_rounds = int(request.form.get('num_rounds'))
        for round in range(1, num_rounds + 1):
            result += f"<br><br>Round {round}:<br>"
            player_choice = request.form.get('player_choice')
            computer_choice = game.get_computer_choice(difficulty)
            result += f"You chose: {player_choice}<br>Computer chose: {computer_choice}<br>"
            result += game.determine_winner(player_choice, computer_choice) + "<br>"
        
        game.save_scores()
        result += "<br>---------------- SCORES -------------------<br>"
        with open("score.txt", "r") as file:
            scores = file.read()
            result += scores + "<br>"
        result += f"<br>Rounds: {num_rounds}, Wins: {game.wins}, Loses: {game.losses}, Draws: {game.draws}<br>"
        if game.wins > game.losses:
            result += "You are on a winning streak! Keep it up 😄<br>"
        elif game.losses > game.wins:
            result += "The computer seems to have your number. Can you turn the tide? 😪<br>"
        else:
            result += "It's neck and neck! Keep playing to see who comes out on top. 😄😪<br>"
        result += "<br>---------------------------------------------<br>"
        play_again = request.form.get('play_again')  # Get user's choice to play again
    
    return render_template('play_with_computer.html', result=result, play_again=play_again)

if __name__ == "__main__":
    app.run(debug=True)