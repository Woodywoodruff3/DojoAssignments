from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ninja")
def ninja():
	all=True
	return render_template('ninja.html', all=all)

@app.route("/ninja/<color>")
def indColor(color):
	all=False
	return render_template('ninja.html', all=all, color=color)

app.run(debug=True)