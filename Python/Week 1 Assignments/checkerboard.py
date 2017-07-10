def checkerboard(size):
	space = 1
	while space <= size:
		if space % 2 == 0:
			print "* * * * "
			space += 1
		else:
			print " * * * *"
			space += 1

checkerboard(20)