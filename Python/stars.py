def draw_stars(x):
	
	for y in range(0, len(x)):
		if isinstance(x[y], int) == True:
			print ("*" * (x[y]))
		else:
			print x[y][:1].lower()*len(x[y])

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]))