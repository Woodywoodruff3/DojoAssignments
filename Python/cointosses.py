heads = 0
tails = 0
for x in range (1,5001):
	import random
	toss = random.randint(0,1)
	if toss == 0:
		heads += 1
		print "Attempt #"+str(x)+" Throwing a coin... It is Heads!!! ... Got " +str(heads)+" head(s) so far and "+ str(tails) + " (s) so far"
		
	else:
		tails += 1
		print "Attempt #"+str(x)+" Throwing a coin... It is Tails!!! ... Got " +str(heads)+" tail(s) so far and "+ str(tails) + " (s) so far"
		
print "Ending the program, thank you"