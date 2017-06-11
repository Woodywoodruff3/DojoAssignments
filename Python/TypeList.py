l = ['magical unicorns',19,'hello',98.98,'world']

sumInt= 0
string = ""
num=len(l)
for x in l:
  check1=isinstance(x, int)
  if check1 == False:
    for y in l:
      check2=isinstance(y, str)
      if check2 == False:
        break
    if check2 == True:
     print "The array you entered is of string type"
     for count in range(0,num):
      string+=l[count]
     print "String:",allString

    elif check2 == False:
     print "The array you entered is of mixed type"
     break

if check1 == True:
 print "The array you entered is of integer type"

 for count in range(0,num):
  sumInt+=l[count]
 print sumInt

 	