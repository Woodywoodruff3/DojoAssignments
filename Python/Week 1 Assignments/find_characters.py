def find_characters(word_list, char):
	new_list=[]
	for item in word_list:
		if char in item:
			new_list.append(item)
	print new_list

find_characters(['Hello',"world",'my',"name","is","Anna"], 'a')