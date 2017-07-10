def fun_with_functions():
	for x in range(1, 2001):
		if x % 2 == 0:
			print "Number is ", x, "This is an even number."
		else:
			print "Number is ", x, "This is an odd number."


fun_with_functions()

def multiply(arr, num):
	# print numList, multiplier
	for x in range(len(arr)):
		# print x
		arr[x] = arr[x]*num
	return arr
a=[1,2,3,4]
print multiply(a, 2)

def layered_multiples(arr):
	two_dim_list=[]
	for idx in range(len(arr)):
		inner_list=[]
		for num in range (arr[idx]):
			inner_list.append(1)
		two_dim_list.append(inner_list)
	print two_dim_list

layered_multiples(multiply(a,2))

	