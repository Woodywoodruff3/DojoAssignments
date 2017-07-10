def coin_toss(howmany):
	heads = 0
	tails = 0
	for attempt in range (1, howmany):
		import random
		random_number = random.random()
		if random_number < 0.5:
			heads += 1
			print "Attempt #",str(attempt)+": Throwing a coin...It's heads! ... Got ",str(heads),"head(s) so far and ",str(tails), "tail(s)  so far"
		else:
			tails += 1
			print "Attempt #",str(attempt)+": Throwing a coin...It's tails! ... Got ",str(heads),"head(s) so far and ",str(tails), "tail(s)  so far"

	print "Ending the Program, thank you!"

coin_toss(5001)