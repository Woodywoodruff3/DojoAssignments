from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	name = request.form.get('name')
	location = request.form.get('location')
	language = request.form.get('language')
	comment = request.form.get('comments')
	return render_template('results.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)