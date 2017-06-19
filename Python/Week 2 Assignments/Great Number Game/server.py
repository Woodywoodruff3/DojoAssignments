from flask import Flask, flash, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisisSecret"

session={}
session['random']=None

def random():
	import random
	session['random'] = random.randrange(1, 101) # random number between 0-100
	print session['random']
	
@app.route('/')
def index():
	if session['random']==None:
    		random()
    	else:
        	pass
    	return render_template('index.html', number = session['random'])

@app.route('/submit', methods=['POST'])
def submit():
	guess=request.form.get('guess')
	if len(guess)<1:
		flash('Please Enter a Number')
	else:
		submit = int(guess)
		if (submit==session['random']):
			flash('1')
		elif (submit < session['random']):
			flash('2')
		elif (submit > session['random']):
			flash('3')
	return redirect('/')

@app.route('/new', methods=['GET', 'POST'])
def newGame():
	random()
	return redirect('/')	


app.run(debug=True)