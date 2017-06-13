words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day") #18

print words.replace('day', 'month') #It's thanksgiving month. It's my birthmonth,too!

x = [2,54,-2,7,12,98]
print min(x) #-2
print max(x) #98

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0] #hello

print y[len(y)-1] #world

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort() #[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
n = len(z)
zz = []
for i in range(0, n/2):
	zz.append(z.pop(0))

z.insert(0, zz)
print z

 