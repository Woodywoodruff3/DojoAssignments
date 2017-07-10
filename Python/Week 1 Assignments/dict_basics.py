myself = {
	"name":"Ross",
	"age":34,
	"birth":"USA",
	"language":"Python"
}

def calling_myself(what):
	if what == "name":
		print "My name is", myself[what]
	elif what == "age":
		print "My age is", myself[what]
	elif what == "birth":
		print "My country of birth is", myself[what]
	elif what == "language":
		print "My favorite language is", myself[what]
	elif what == "all":
		print "My name is", myself["name"]
		print "My age is", myself["age"]
		print "My country of birth is", myself["birth"]
		print "My favorite language is", myself["language"]
	else:
		print "Either select name, age, birth, language or all"

calling_myself()