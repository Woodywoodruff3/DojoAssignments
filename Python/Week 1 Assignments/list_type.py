l = ['magical unicorns',19,'hello',98.98,'world']

sumInt = 0
sumStr = ""
num = len(l)
for x in l:
	check1 = isinstance(x, int)
	if check1 == False:
		for y in l:
			check2 = isinstance(y, str)
			if check2 == False:
				print 'The array you entered is of mixed type'
				for sum in range(0, num):
					if type(l[sum]) == int:
						sumInt += l[sum]
					else:
						sumStr += str(l[sum])

				print "String:",sumStr 
				print "Sum:", sumInt
				break
			if check2 == True:
				print "The array you entered is of string type"
				for count in range(0, num):
					sumStr += str(l[count])
				
				print "String:",sumStr

	else:
		for sum in range(0,num):
			sumInt = sumInt + l[sum]

		print "The array you entered is of integer type"
		print "Sum:", sumInt



