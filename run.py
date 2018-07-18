import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #store playerID in a txt file and redirect to user view
    if request.method == ('POST'):
        with open('data/players.txt', 'a') as player_list:
            player_list.writelines(request.form['username'] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')
    
@app.route('/<username>')
def user(username):
    riddles = ask_all_riddles()
    return render_template('game.html', username=username, riddle_list=riddles)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

