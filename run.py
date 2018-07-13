import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Riddle Me This</h1>'
    
    
@app.route('/<username>')
def player(username):
    return 'Welcome ' + username
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

