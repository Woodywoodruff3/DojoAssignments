#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
#Multiples
for i in range (1, 1000, 2): # varable i starts at 1 until 1000, 2 equals how much variable i will go up each for loop pass
	print i

#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for i in range (5, 1000001, 5): # variable i starts at 5, and goes up every 5 numbers until it reaches 1,000,000
	print i

#Sum list
a = [1, 2, 5, 10, 255, 3]
b = len(a)
number = 0
for i in range (0, b):	#for loop variable i start at index 0, through a length(variable b)
	number = number + a[i] #add the previous number count to value of a[i].  becomes new number value

print number # prints final sum - 276

#Average list
a = [1, 2, 5, 10, 255, 3]
b = len(a)
avg = 0

for i in range (0, b):	#for loop variable i start at index 0, through a length(variable b)
	number = number + a[i] #add the previous number count to value of a[i].  becomes new number value

avg = number / b  # variable avg equals var number divided by variable b 

print avg #prints avg - 46