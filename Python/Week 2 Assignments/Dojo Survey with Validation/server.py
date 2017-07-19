from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key="Thisissecret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	if len(request.form['name'])< 1 and len(request.form['comments'])>120:
		flash("Name cannot be empty!")
		flash('Comments are too long!')
		return redirect('/')

	if len(request.form['name'])< 1 and len(request.form['comments'])<1:
		flash("Name cannot be empty!")
		flash('Comments cannot be empty!')
		return redirect('/')

	if len(request.form['name']) < 1:
		flash("Name cannot be empty")
		return redirect('/')

	if len(request.form['comments']) < 1:
		flash('Comments cannot be empty!')
		return redirect('/')

	if len(request.form['comments']) > 120:
		flash('Comments are too long!')
		return redirect('/')

	return render_template('results.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comments'])

app.run(debug=True)