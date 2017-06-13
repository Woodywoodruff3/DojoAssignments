word_list = ['hello','world','my','name','is','Anna']
char = 'o'
letter = set(char)
new_list = []

for word in word_list:
 if letter & set(word):
  new_list.append(word)
print "newList =",new_list