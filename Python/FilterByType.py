def whatsTheType(x):
	xtype = type(x)
	if xtype == int:
		if x < 100:
			#If the integer is less than 100, print "That's a small number"
			print "Thats a small number"
		else:
			#If the integer is greater than or equal to 100, print "That's a big number!" 
			print "Thats a big number!"

	elif xtype == str:
		if  len(x) < 50:
			#If the string is shorter than 50 characters print "Short sentence."
			print "Short Sentance"
		else:
			#If the string is greater than or equal to 50 characters print "Long sentence."
			print "Long Sentance"

	elif xtype == list:
		if len(x) < 10:
			#If the list has fewer than 10 values print "Short list."
			print "Short List"
		else:
			#If the length of the list is greater than or equal to 10 print "Big list!"
			print "Big list!"
	else:
		print "I dont know about this:", xtype._name_


sI = 45
mI = 100
bI = 455
eI = 0
spI = -23

sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""

aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

whatsTheType(sI)
whatsTheType(mI)
whatsTheType(bI)
whatsTheType(eI)
whatsTheType(spI)

whatsTheType(sS)
whatsTheType(mS)
whatsTheType(bS)
whatsTheType(eS)

whatsTheType(aL)
whatsTheType(mL)
whatsTheType(lL)
whatsTheType(eL)
whatsTheType(spL)

