def odd_even(start, end):
	for x in range(start,end):
		if x%2 == 1:
			print "Number is " + str(x) +". This is an odd number"
		else:
			print "Number is " + str(x) + ". This is an even number"

odd_even(1,1000)

