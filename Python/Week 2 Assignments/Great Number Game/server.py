from flask import Flask, render_template, session, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'thisissecret'
import random

session={}
session['number'] = None

def setnumber():
	session['number'] = random.randrange(0,101)
	print session['number']

@app.route('/')
def index():
	if session['number']==None:
		setnumber();
	else:
		pass
	return render_template('index.html', number = session['number'])

@app.route('/guessed', methods=["POST"])
def guessed():
	print request.form['guess_number']
	guessed = request.form['guess_number']
	
	if len(guessed)<1:
		flash('Please Enter a Number')
	else:
		submit = int(guessed)
		if (submit==session['number']):
			flash('1')
		elif (submit < session['number']):
			flash('2')
		elif (submit > session['number']):
			flash('3')
	return redirect('/')
	
@app.route('/new', methods=['POST'])
def newGame():
	session['number'] = None
	return redirect('/')

app.run(debug=True)