from flask import Flask, render_template, redirect, flash, request, session
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friends')
app.secret_key = "secretkey"
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	
	return render_template('index.html', all_friends = friends)

@app.route('/submit', methods=['POST'])
def process():
	query = 'INSERT INTO friends(first_name, last_name, email, created_at, updated_at) VALUES (:fname, :lname, :email, NOW(), NOW()'
	data = {
		'fname': request.form['first_name'],
		'lname': request.form['last_name'],
		'email': request.form['email']
	}

	mysql.query_db(query,data)
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id = '{}'".format(id)
	individual = mysql.query_db(query)
	return render_template('edit.html', edituser = individual)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	fname= request.form['first_name']
	lname= request.form['last_name']
	email= request.form['email']
	#query = "UPDATE friends SET first_name={}, last_name={}, email={}, updated_at = NOW() WHERE id = {}".format(request.form['first_name'], request.form['last_name'], request.form['email'], int(id))
	query = "UPDATE friends SET first_name='%s', last_name='%s', email='%s' WHERE friends.id=%s"%(fname,lname,email,id)
	mysql.query_db(query)
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = '{}'".format(id)
    mysql.query_db(query)
    return redirect('/')

app.run(debug=True)