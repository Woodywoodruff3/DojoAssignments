times = 1
grade = ""
while times <= 10:
	import random
	random_num = random.randint(60,100)
	if random_num < 70:
		grade = "D"
		print "Score:", str(random_num)+"; Your grade is",grade
	elif random_num < 80:
		grade = "C"
		print "Score:", str(random_num)+"; Your grade is",grade
	elif random_num < 90:
		grade = "B"
		print "Score:", str(random_num)+"; Your grade is",grade
	else:
		grade = "A"
		print "Score:", str(random_num)+"; Your grade is",grade
	times += 1
print "End of the program, Bye!"
