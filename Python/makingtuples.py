my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
tupleout = ()
i = 0
for key,data in my_dict.iteritems():
	tupleout = tupleout + (key,data)

print tupleout