def makingdict(list1, list2):
	if len(list1)>len(list2):
		zipped = zip(list1, list2)
		print dict(zipped)

	else:
		zipped = zip(list2, list1)
		print dict(zipped)
		


makingdict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar",], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "dog"])