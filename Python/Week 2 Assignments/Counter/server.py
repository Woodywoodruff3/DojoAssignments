from flask import Flask, render_template, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def numsessions():
	try:
		session['count'] += 1
	except:
		session['count'] = 1

@app.route('/')
def index():
	numsessions()
	return render_template('index.html')

@app.route('/addtwo', methods=['POST'])
def addtwo():
	session['count'] += 1
	return redirect('/')
@app.route('/clear', methods=['POST'])
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)