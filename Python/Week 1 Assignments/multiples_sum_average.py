
for num in range(1,1001, 2):
	print num

for times5 in range (5, 1000001, 5):
	print times5


a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in range(len(a)):
	sum += a[num]

print sum

b = [1, 2, 5, 10, 255, 3]
avg = 0
for numbers in range(len(b)):
	avg += b[numbers]

print avg / len(b)
