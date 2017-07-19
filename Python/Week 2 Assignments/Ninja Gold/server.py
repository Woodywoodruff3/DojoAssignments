from flask import Flask, session, redirect, request, render_template
import random
import datetime

app=Flask(__name__)
app.secret_key="thisissecret"

session={}
session['gold']=None
session['activity']=None

def activity(num, action, location):
    timestamp = datetime.datetime.now()
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, timestamp)
            session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %d gold... Ouch %s' % (num, timestamp)
            session['activity'].append(['lost', lost])
        else:
            print "error"
    elif location == 'farm':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    else:
        print "error"

@app.route('/')
def index():
	if session['gold']==None:
    		session['gold']=0
    	if session['activity']==None:
    		session['activity']=[]
    	return render_template("index.html", total_gold = session['gold'], activities = session['activity'])

@app.route('/process_money', methods=['POST'])
def process():
	selection = request.form['hidden']

	if selection == 'farm':
		farmnum = random.randrange(10, 22)
		session['gold'] += farmnum
		activity(farmnum, 'earned', 'farm')
	elif selection == 'cave':
		cavenum = random.randrange(5, 11)
		session['gold'] += cavenum
		activity(cavenum, 'earned', 'cave')
	elif selection == 'house':
		housenum = random.randrange(2, 6)
		session['gold'] += housenum
		activity(housenum, 'earned', 'house')
	elif selection == 'casino':
		winloss = random.randrange(1,3)
		if winloss == 1:
			casinonum = random.randrange(0, 51)
			session['gold'] -= casinonum
			activity(casinonum, 'lost', 'casino')
		else:
			casinonum = random.randrange(0, 51)
			session['gold'] += casinonum
			activity(casinonum, 'earned', 'casino')
	else:
		print "error"
	return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['gold'] = 0
    session['activity'] = []
    return redirect('/')

app.run(debug=True)
