for num in range(2, 101):
	for divider in range (2, num/2):
		if num % divider == 0:
			break
		else:
			print num, "FooBar"
			break

