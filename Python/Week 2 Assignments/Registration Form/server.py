from flask import Flask, render_template, redirect, request, session, flash
import re
app=Flask(__name__)
app.secret_key="Thisissecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if len(request.form['email']) < 1 and len(request.form['email']) < 1 and len(request.form['first_name']) < 1 and len(request.form['last_name']) < 1 and len(request.form['password']) <1 and len(request.form['confirm_password']) < 1:
		flash("Make sure to fill out all boxes")
		return redirect('/')
	elif len(request.form['email']) < 1:
		flash('Email cannot be blank!')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address!')

	
	if len(request.form['first_name']) < 1:
		flash("First Name cannot be blank!")

	if request.form['first_name'].isalpha() == False:
		flash("First Name must be all alphabetic charaters")

	if len(request.form['last_name']) < 1:
		flash('Last Name cannot be blank!')

	if request.form['last_name'].isalpha() == False:
		flash("Last Name must be all alphabetic charaters")
	
	if len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
		flash('Password needs to be 8 charaters!')
	
	if request.form['password'] != request.form['confirm_password']:
		flash('Passwords do not match!')
	
	if len(request.form['email']) > 1 and len(request.form['email']) > 1 and len(request.form['first_name']) > 1 and request.form['first_name'].isalpha() == True and len(request.form['last_name']) > 1 and len(request.form['password']) > 1 and len(request.form['confirm_password']) > 1 and EMAIL_REGEX.match(request.form['email']) and len(request.form['password']) > 7 and len(request.form['confirm_password']) > 7 and request.form['password'] == request.form['confirm_password']:
		flash("Thanks for submitting!")
		return redirect('/')

	return redirect('/')


app.run(debug=True)