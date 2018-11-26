import os
import json
import math
from flask import Flask, session, render_template, redirect, request, url_for, flash
from flask.json import jsonify

app = Flask(__name__)
app.secret_key = 'ffb8574786f724d0ca95698772955a65'

# def leaderboard():
#     with open('data/online_players.json', 'w') as outfile:
#         json.dump(data, outfile)
    
    
# score function to build below
# def score_count(answer):
#     count = 0
  
#     for a in answer:
#         if a.correct_answer():
#             count += 1
#         return count

# def show_score():
    
#      print ('Your score is {0} / {1}'.format(score, number_of_questions))

# def game_motivators(questions_and_answers, score):
#     #print statements to validate player success on high score
#     for answer in score:
#         if score > 3:
#             print('So far, so good.')
#         if score > 5:
#             print('You\'re pretty good at this.')

@app.route('/', methods = ['GET','POST'])
def index():
    #store playerID in a txt file. Then redirect to user view
    if request.method == ('POST'):
        with open('data/players.txt', 'a') as player_list:
            player_list.writelines(request.form['username'] + '\n'),
        ("data/online_players.json", request.form["username"] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')
    
@app.route('/<username>', methods = ['GET','POST'])
def user(username):
    #get json data and store in variable 'riddles'
    data = []
    
    with open('data/riddles.json','r') as riddle_data:
        riddles = json.load(riddle_data)
    
    #set the riddle_index to its starting position
    riddle_index = 0 
    
    #initialize correct_answer before assignment
    correct_answer = ''
    
    #set score to beginning position 0
    score = 0
    
    #get length of riddles
    number_of_riddles = len(riddles)
    game_length = int(number_of_riddles)
    
    if request.method == "POST":
        
        #get riddle_index & score from form's hidden input field 
        riddle_index = int(request.form["riddle_index"])
        score = int(request.form['score'])
        
        #obtain the user's guess
        guess = request.form['answer'].lower() 
        
        #obtain the correct answer
        correct_answer = riddles[riddle_index]['answer'].strip()
      
        #compare user guess and correct answer
        if correct_answer == guess:
            flash('Correct Answer')
            riddle_index += 1
            score += 1
        #next work out how to add score to online users file
        else:
            flash('Wrong Answer. Try Again')
    
    # write username & score to leaderboard file at game-over
    # redirect to gameover.html
    # currently this function overwrites past writes: FIX NEEDED
    
    if request.method == 'POST':
        # amend this for a more dynamic game
        if correct_answer == 'a bookkeeper':
            with open('data/leaderboard.txt', 'a') as leaderboard:
                leaderboard.writelines('%s : %d' %(username, score) + '\n')
                
                leaderboard_file = open('data/leaderboard.txt', 'r') 
                leaderboard = leaderboard_file.readlines()
                
            return render_template('gameover.html', username=username, score=score, game_length=game_length, leaderboard=leaderboard)

    return render_template('game.html', username=username, score=score, riddles=riddles, riddle_index=riddle_index, number_of_riddles=number_of_riddles, game_length=game_length)


if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)