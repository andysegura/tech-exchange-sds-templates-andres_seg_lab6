# Andres Segura and Munir Adeyola
# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import capital_check


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "you must fill out the quiz to see your answers"
    else:
        answers = { "new york": request.form['New York'], 
                    "california": request.form['California'],
                    "new mexico": request.form['New Mexico'],
                    "colorado": request.form['Colorado'],
                    "texas": request.form['Texas'],
                    "arizona": request.form['Arizona'],
                }
        
        graded_answers = capital_check(answers)
        new_york_answer = graded_answers['new york']
        california_answer = graded_answers['california']
        new_mexico_answer = graded_answers['new mexico']
        colorado_answer = graded_answers['colorado']
        texas_answer = graded_answers['texas']
        arizona_answer = graded_answers['arizona']
        score = graded_answers['score']

        return render_template('results.html', new_york_answer = new_york_answer,
        california_answer = california_answer, new_mexico_answer = new_mexico_answer,
        colorado_answer = colorado_answer, texas_answer = texas_answer, 
        arizona_answer = arizona_answer, score = score)

