def grades():
	import random
	print "Scores and Grades"
	for x in range(10):
		score = random.randint(60,100)

		if score < 70:
			print "Score: " + str(score)+"; Your grade is D"
		elif score < 80:
			print "Score: " + str(score)+"; Your grade is C"
		elif score < 90:
			print "Score: " + str(score)+"; Your grade is B"
		else:
			print "Score: " + str(score)+"; Your grade is A"
	print "End of the Program. Bye!"

grades()