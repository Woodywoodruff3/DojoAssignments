def odd_even(start, end):
	for x in range(start,end):
		if x%2 == 1:
			print "Number is " + str(x) +". This is an odd number"
		else:
			print "Number is " + str(x) + ". This is an even number"

odd_even(1,1000)

def multiply(arr,num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr

a = [2,4,10,16]
b = multiply(a,5)
print b

def layered_multiples(arr):
	new_array = []
	for x in arr:
		val_arr=[]
		for i in range(0,x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array
x = layered_multiples(multiply([2,4,5], 3)
print x

