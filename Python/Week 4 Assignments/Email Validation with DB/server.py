from flask import Flask, render_template, redirect, flash, request, session
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'week4')
app.secret_key = "secretkey"
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def add_to_db():
	query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:em, NOW(), NOW())"
	data = {'em': request.form['email']}
	mysql.query_db(query, data)

def success():
	query = "SELECT * FROM emails"
	total = mysql.query_db(query)
	return render_template('success.html', all_emails = total, just_email = request.form['email'])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/validate', methods=["POST"])
def validate():
	
	if len(request.form['email']) < 1:
		flash("Email cannot be left blank")
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
        	flash("Email not is correct format")
        	return redirect('/')
   	else:
   			flash ("is a VALID emal address! Thank You!")
    			add_to_db()
    			return success()

app.run(debug=True)