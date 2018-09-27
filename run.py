import os
from flask import Flask, render_template, redirect, request, url_for
from flask.json import jsonify

app = Flask(__name__)
    
def get_questions_and_answers():
    
    questions = []
    answers =[]
    
    #take data from .txt file. Read and store data in lists
    with open('data/riddles.txt','r') as riddle_list:
       riddles = riddle_list.readlines()
        
    for i, text in enumerate(riddles):
       if i % 2 == 0:
           questions.append(text)
       else:
            answers.append(text)
    
    questions_and_answers = zip(questions, answers)
    return questions_and_answers

# def ask_riddle():
    
#     riddle_questions = get_questions_and_answers()
#     qa_dict = dict(riddle_questions)
#     number_of_riddles= len(qa_dict)
    
#     for (q, a) in riddle_questions:
#         quest = q
#         question = quest.splitlines()
#         return question

# score function to build below
# def score_count(answer):
#     count = 0
  
#     for a in answer:
#         if a.correct_answer():
#             count += 1
#         return count

# def show_answer():
#      print ('Your score is {0} / {1}'.format(score, number_of_questions))

def game_motivators(questions_and_answers, score):
    #print statements to validate player success on high score
    for answer in score:
        if score > 3:
            print('So far, so good.')
        if score > 5:
            print('You\'re pretty good at this.')

@app.route('/', methods=['GET', 'POST'])
def index():
    #store playerID in a txt file. Then redirect to user view
    if request.method == ('POST'):
        with open('data/players.txt', 'a') as player_list:
            player_list.writelines(request.form['username'] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')
    
@app.route('/<username>')
def user(username):
    riddle_list = []
    
    questions_and_answers = get_questions_and_answers()
    
    for q,a in questions_and_answers:
        riddle_list.append(q)
        
    return render_template('game.html', username=username, riddle_list=riddle_list)
    
@app.route('/check-answer', methods=['POST'])
def check_answer():
    score = 0 
    score_plus = score + 1
    
    riddle_questions = get_questions_and_answers()
    qa_dict = dict(riddle_questions)
    
    checked_answer = qa_dict['I stay in the corner but I travel around the world. What am I?\n']
    guess = request.form['answer'].lower()
    
    return render_template('score.html', guess=guess, checked_answer=checked_answer, score=score, score_plus=score_plus)  

@app.route('/result')
def result():
    return render_template('confirmation.html')
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)