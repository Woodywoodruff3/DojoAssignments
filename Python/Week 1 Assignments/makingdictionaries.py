def makingdict(list1, list2):
	if len(list1)>=len(list2):
		new_dict = zip(list1, list2)
		print new_dict
	else:
		new_dict = zip(list2, list1)
		print new_dict


makingdict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas",])